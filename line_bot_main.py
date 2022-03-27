# coding: utf-8




#各モジュールの読み込み
import os
import datetime
import psycopg2
import line_bot_text_analyze
import line_bot_text_generate
from flask import Flask, jsonify, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, FollowEvent, TextMessage, TextSendMessage)




#Flaskのアプリケーションモジュールを作成する
app = Flask(__name__)

#Herokuの環境変数に設定されている、LINE-Developersのアクセストークンとチャンネルシークレットを取得する
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET       = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler      = WebhookHandler(YOUR_CHANNEL_SECRET)

#Herokuの環境に設定されている、postgresにアクセスするためのキーを取得する
DATABASE_URL = os.environ["DATABASE_URL"]

#Postgresデータベース上のテーブル「line_entries」の有無を示すフラグを宣言する
has_db_table = False

#Postgresデータベースに登録・格納するLINEメッセージ(＝レコード)のID(＝レコードカウンター)を宣言する
rcd_id = "-1"

#ユーザーの発話の流れ(＝複数回のLINEメッセージの送信)を区切るためのフラグを宣言する
cmpltn_flg = False




#Postgresデータベース上のテーブル内のレコードを取得して、ブラウザーに引渡しをする
@app.route("/")
def show_db_record():
    #データベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    # データベースから該当IDのメッセージ(＝レコード)を取得し、jsonifyで整形して呼出し元に引き渡しをする
    global has_db_table
    global rcd_id
    if has_db_table == True:
       if int(rcd_id) == -1:
          return "table-record not exist..."
       if int(rcd_id) >= 1:
          cur.execute("""SELECT * FROM line_entries WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': str(int(rcd_id)-1)})
       rcd = cur.fetchone()
       cur.close()
       conn.close()
       return jsonify(rcd), 200
    else:
       cur.close()
       conn.close()
       return "db-table not exist..."


#Postgresデータベース上のテーブルを破棄する
@app.route("/table_drop")
def db_table_drop():
    #データベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #既にテーブルが作成・用意されていれば、それを破棄する
    cur.execute("DROP TABLE line_entries")
    global has_db_table
    has_db_table = False

    #データベースに登録・格納するLINEメッセージ(＝レコード)のID(＝レコードカウンタ)を示す変数を初期化する
    global rcd_id
    rcd_id = "-1"

    #データベースへコミットし、テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    cur.close()
    conn.close()
    return "table droped!"


#LINE-DevelopersのWebhookからURLにイベントが送出されるようにする(内部でイベントハンドラーを呼び出す)
@app.route("/callback", methods=["POST"])
def callback():
    #HTTPリクエストヘッダーから署名検証のためのシグネチャーを取得する
    signature = request.headers["X-Line-Signature"]

    #HTTPリクエストボディを取得して、ログに記録する
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    #署名を検証して問題がなければ、最終的に「handle_message(＝イベントハンドラー)」の呼出しをする
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


#LINE-DevelopersのWebhookを介して送られてくるイベントを処理する(＝メッセージイベントを処理する)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #ユーザーから送られるLINEメッセージをJanomeで形態素解析する
    line_msg_intnt, prv_msgrcd_lst = line_msg_analyze(event.message.text)

    #ユーザーから送られるLINEメッセージの解析結果から返信メッセージを生成する
    line_msg_gnrt_rslt = line_msg_generate(event.source.user_id, event.message.text, line_msg_intnt, prv_msgrcd_lst)

    #LINEBotAPIを使って生成されるLINEメッセージをユーザーに対して送信する
    line_msg_send(event, line_msg_gnrt_rslt)

    #ユーザーから送られるLINEメッセージをpostgresのデータベースに登録・格納する
    postgres_insert_and_update(event, line_msg_intnt)


#LINE-DevelopersのWebhookを介して送られてくるイベントを処理する(＝フォローイベントを処理する)
@handler.add(FollowEvent)
def handle_follow(event):
    fllw_msg = "友達追加 ありがとう！"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=fllw_msg))


#ユーザーから送られるLINEメッセージを解析する
def line_msg_analyze(line_msg_txt):
    #過去５件分のユーザーからのLINEメッセージ(＝レコード)をデータベースから取得する
    global rcd_id
    prv_msgrcd_lst = []
    if int(rcd_id) == -1:
       prv_msgrcd_lst.append(["", "", ""])
       prv_msgrcd_lst.append(["", "", ""])
       prv_msgrcd_lst.append(["", "", ""])
       prv_msgrcd_lst.append(["", "", ""])
    if int(rcd_id) == 1:
       prv_msgrcd_tmp  = postgres_select("0")
       prv_msgrcd_lst.append([prv_msgrcd_tmp[1],  prv_msgrcd_tmp[3],  prv_msgrcd_tmp[4]])
       prv_msgrcd_lst.append(["", "", ""])
       prv_msgrcd_lst.append(["", "", ""])
       prv_msgrcd_lst.append(["", "", ""])
    if int(rcd_id) == 2:
       prv_msgrcd_tmp  = postgres_select("0")
       prv_msgrcd_tmp2 = postgres_select("1")
       prv_msgrcd_lst.append([prv_msgrcd_tmp[1],  prv_msgrcd_tmp[3],  prv_msgrcd_tmp[4]])
       prv_msgrcd_lst.append([prv_msgrcd_tmp2[1], prv_msgrcd_tmp2[3], prv_msgrcd_tmp2[4]])
       prv_msgrcd_lst.append(["", "", ""])
       prv_msgrcd_lst.append(["", "", ""])
    if int(rcd_id) == 3:
       prv_msgrcd_tmp  = postgres_select("0")
       prv_msgrcd_tmp2 = postgres_select("1")
       prv_msgrcd_tmp3 = postgres_select("2")
       prv_msgrcd_lst.append([prv_msgrcd_tmp[1],  prv_msgrcd_tmp[3],  prv_msgrcd_tmp[4]])
       prv_msgrcd_lst.append([prv_msgrcd_tmp2[1], prv_msgrcd_tmp2[3], prv_msgrcd_tmp2[4]])
       prv_msgrcd_lst.append([prv_msgrcd_tmp3[1], prv_msgrcd_tmp3[3], prv_msgrcd_tmp3[4]])
       prv_msgrcd_lst.append(["", "", ""])
    if int(rcd_id) >= 4:
       idx = int(rcd_id) - 4
       prv_msgrcd_tmp = postgres_select(str(idx))
       prv_msgrcd_lst.append([prv_msgrcd_tmp[1], prv_msgrcd_tmp[3], prv_msgrcd_tmp[4]])
       idx = int(rcd_id) - 3
       prv_msgrcd_tmp = postgres_select(str(idx))
       prv_msgrcd_lst.append([prv_msgrcd_tmp[1], prv_msgrcd_tmp[3], prv_msgrcd_tmp[4]])
       idx = int(rcd_id) - 2
       prv_msgrcd_tmp = postgres_select(str(idx))
       prv_msgrcd_lst.append([prv_msgrcd_tmp[1], prv_msgrcd_tmp[3], prv_msgrcd_tmp[4]])
       idx = int(rcd_id) - 1
       prv_msgrcd_tmp = postgres_select(str(idx))
       prv_msgrcd_lst.append([prv_msgrcd_tmp[1], prv_msgrcd_tmp[3], prv_msgrcd_tmp[4]])

    #ユーザーから送られるLINEメッセージの中に含まれるインテントを抽出する
    rmv_etc      = line_bot_text_analyze.remove_etc(line_msg_txt)
    extrct_intnt = line_bot_text_analyze.extract_intent_from_gag_and_vocalcordcopy(rmv_etc)
    if extrct_intnt != "<その他・不明>":
       line_msg_intnt = extrct_intnt
       return line_msg_intnt, prv_msgrcd_lst
    rmv_etc       = line_bot_text_analyze.remove_etc(line_msg_txt)
    rmv_symbl     = line_bot_text_analyze.remove_symbol(rmv_etc)
    extrct_intnt2 = line_bot_text_analyze.extract_intent_from_gag_and_vocalcordcopy(rmv_symbl)
    if extrct_intnt2 != "<その他・不明>":
       line_msg_intnt = extrct_intnt2
       return line_msg_intnt, prv_msgrcd_lst
    rmv_etc       = line_bot_text_analyze.remove_etc(line_msg_txt)
    rmv_symbl     = line_bot_text_analyze.remove_symbol(rmv_etc)
    extrct_intnt3 = line_bot_text_analyze.extract_intent_from_short_and_boilerplate(rmv_symbl)
    if extrct_intnt3 != "<その他・不明>":
       line_msg_intnt = extrct_intnt3
       return line_msg_intnt, prv_msgrcd_lst
    rmv_etc          = line_bot_text_analyze.remove_etc(line_msg_txt)
    rmv_symbl        = line_bot_text_analyze.remove_symbol(rmv_etc)
    rmv_edprtcl      = line_bot_text_analyze.remove_endparticle(rmv_symbl)
    extrct_intnt4 = line_bot_text_analyze.extract_intent_from_short_and_boilerplate(rmv_edprtcl)
    if extrct_intnt4 != "<その他・不明>":
       line_msg_intnt = extrct_intnt4
       return line_msg_intnt, prv_msgrcd_lst
    rmv_etc          = line_bot_text_analyze.remove_etc(line_msg_txt)
    rmv_symbl        = line_bot_text_analyze.remove_symbol(rmv_etc)
    rmv_edprtcl      = line_bot_text_analyze.remove_endparticle(rmv_symbl)
    extrct_intnt_end = line_bot_text_analyze.extract_intent(rmv_edprtcl)
    line_msg_intnt = extrct_intnt_end
    return line_msg_intnt, prv_msgrcd_lst


#ユーザーから送られるLINEメッセージの解析結果から返信メッセージを生成する
def line_msg_generate(line_spkr_id, line_msg_txt, line_msg_intnt, prv_msgrcd_lst):
    #ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
    line_prfl    = line_bot_api.get_profile(line_spkr_id)
    line_spkr_nm = line_prfl.display_name
    gnrtd_msg    = line_bot_text_generate.text_generate_from_analyze_result(line_spkr_nm, line_msg_txt, line_msg_intnt, prv_msgrcd_lst)
    return gnrtd_msg


#LINEBotAPIを使って生成されるLINEメッセージをユーザーに対して送信する
def line_msg_send(event, line_msg_gnrt_rslt):
    #LINEの返信用トークンと生成されたメッセージをセットにしてLINEBotAPIの呼出しをする
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=line_msg_gnrt_rslt))


#ユーザーから送られるLINEメッセージをpostgresのデータベースに登録・格納する
def postgres_insert_and_update(event, line_msg_intnt):
    #データベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #既にテーブルが用意・作成されていれば、それを破棄して新たにテーブルを用意・作成する
    global has_db_table
    if has_db_table == False:
       cur.execute("DROP TABLE line_entries")
       cur.execute("CREATE TABLE line_entries(rcd_id text, dt_tm text, spkr text, msg text, intnt text)")
       has_db_table = True

    #データベースに登録・格納するLINEメッセージ(＝レコード)を構成する情報をまとめて用意する
    global rcd_id
    jst       = datetime.timezone(datetime.timedelta(hours=+9), "JST")
    dt_tm_tmp = datetime.datetime.now(jst)
    dt_tm     = dt_tm_tmp.strftime("%Y/%m/%d %H:%M:%S")
    prfl      = line_bot_api.get_profile(event.source.user_id)
    spkr      = prfl.display_name
    msg       = event.message.text
    intnt     = line_msg_intnt

    #該当IDのメッセージ(＝レコード)がなかったら、データベースにインサート(＝新規に登録・格納)し、既にメッセージがあったらアップデート(＝上書き)する
    if int(rcd_id) == -1:
       rcd_id = "0"
    if int(rcd_id) != 100:
       cur.execute("""SELECT * FROM line_entries WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id})
       rcd = cur.fetchone()
       if  rcd is None:
           cur.execute("""INSERT INTO line_entries (rcd_id, dt_tm, spkr, msg, intnt) VALUES (%(rcd_id)s, %(dt_tm)s, %(spkr)s, %(msg)s, %(intnt)s);""", {'rcd_id': rcd_id, 'dt_tm' : dt_tm, 'spkr': spkr, 'msg': msg, 'intnt': intnt})
           rcd_id = str(int(rcd_id) + 1)
       if (rcd is not None and int(rcd_id) >= 0 and int(rcd_id) <= 99):
           cur.execute("""UPDATE line_entries SET (rcd_id, dt_tm, spkr, msg, intnt) VALUES (%(rcd_id)s, %(dt_tm)s, %(spkr)s, %(msg)s, %(intnt)s) WHERE = %(rcd_id)s;""", {'rcd_id': rcd_id, 'dt_tm' : dt_tm, 'spkr': spkr, 'msg': msg, 'intnt': intnt, 'rcd_id': rcd_id})
           rcd_id = str(int(rcd_id) + 1)
    else:
       rcd_id = "-1"

    #データベースへコミットし、テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    conn.commit()
    cur.close()
    conn.close()


#Postgresのデータベースからレコードを1件取得する
def postgres_select(rcd_id):
    #データベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8")
    cur  = conn.cursor()

    #指定されたIDのメッセージ(＝レコード)をデータベースから個別にセレクトして取得する
    if (int(rcd_id) <= -1 or int(rcd_id) == 0):
        cur.execute("""SELECT * FROM line_entries WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': "0"})
    if (int(rcd_id) >= 1 and int(rcd_id) <= 99):
        cur.execute("""SELECT * FROM line_entries WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id})
    if  int(rcd_id) >= 100:
        cur.execute("""SELECT * FROM line_entries WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': "99"})
    rcd = cur.fetchone()

    #テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    cur.close()
    conn.close()
    return rcd


#Postgresのデータベースからレコードを全件取得する
def postgres_select_all():
    #データベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8")
    cur  = conn.cursor()

    #データベースに登録・格納されている全てのレコードをセレクトして取得する
    rcd_list = []
    cur.execute("SELECT * FROM line_entries")
    rcd_list = cur.fetchall()

    #テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    cur.close()
    conn.close()
    return rcd_list




#FlaskのアプリケーションモジュールをWebアプリケーションサーバー上で実行する
if __name__ == "__main__":
    # デバッグモードをオンにし、ポート番号の設定をしてアプリケーションモジュールを実行する
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))