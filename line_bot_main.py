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
line_bot_api              = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler                   = WebhookHandler(YOUR_CHANNEL_SECRET)

#Herokuの環境に設定されている、postgresにアクセスするためのキーを取得する
DATABASE_URL = os.environ["DATABASE_URL"]

#Postgresデータベース上のテーブルの有無を示すフラグを宣言する
has_db_tbl = False

#Postgresデータベースに登録・格納するLINEレコードのID(＝レコードカウンター)を示す変数を宣言する
rcd_id = -1




#Postgresデータベース上のテーブル内のレコードを取得して、ブラウザーに引渡しをする
@app.route("/")
def show_db_record():
    #データベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #データベースからLINEレコードを過去１件分取得してブラウザーに引渡しをする(なければ、代わりにメッセージの引渡しをする)
    global has_db_tbl
    global rcd_id
    app.logger.info(has_db_tbl)
    app.logger.info(rcd_id)
    if has_db_tbl == True:
       if rcd_id == -1:
          cur.close()
          conn.close()
          return "table record not exist..."
       if rcd_id == 0:
          rcd_id_tmp = 0
          cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id_tmp})
          rcd = cur.fetchone()
          cur.close()
          conn.close()
          return jsonify(rcd), 200
       if rcd_id >= 1:
          rcd_id_tmp = rcd_id - 1
          cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id_tmp})
          rcd = cur.fetchone()
          cur.close()
          conn.close()
          return jsonify(rcd), 200
       if rcd_id == 100:
          cur.close()
          conn.close()
          return "reached the end of the table..."
    else:
       cur.close()
       conn.close()
       return "table not exist..."


#Postgresデータベース上に新たにテーブルを用意・作成する
@app.route("/create_db_table")
def create_db_table():
    #データベースに接続して、テーブル操作のためのカーソルを用意・作成する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #データベース上に新たにテーブルを用意・作成する
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS line_tbl(rcd_id integer PRIMARY KEY, dttm text, text, msg text, intnt text, cntnt text, ontrgy text);""")
    except Exception:
        pass

    #データベースへコミットし、テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    cur.close()
    conn.close()
    return "table created!"


#Postgresデータベース上のテーブルを破棄する
@app.route("/drop_db_table")
def drop_db_table():
    #データベースに接続して、テーブル操作のためのカーソルを用意・作成する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #データベース上の既に用意・作成されているテーブルを破棄する
    global has_db_tbl
    global usr_id
    global rcd_id
    try:
        cur.execute("""DROP TABLE IF EXISTS line_tbl;""")
    except Exception:
        pass

    #各種のプログラムの実行状態を示す変数を初期化する
    has_db_tbl = False
    rcd_id     = -1

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

    #署名を検証して問題がなければ、「handle_message(＝イベントハンドラー)」の呼出しをする
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


#LINE-DevelopersのWebhookを介して送られてくるイベントを処理する(＝メッセージイベントを処理する)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #ユーザーから送られるLINEメッセージをJanomeで形態素解析する
    line_intnt, line_cntnt, line_ontrgy = line_msg_analyze(event.message.text)

    #ユーザーから送られるLINEメッセージをPostgresのデータベースに登録・格納する
    postgres_insert_and_update(event, line_intnt, line_cntnt, line_ontrgy)

    #ユーザーから送られるLINEメッセージの解析結果から返信メッセージを生成する
    gnrtd_msg = line_msg_generate()

    #プログラムが生成するLINEメッセージをLINEBotAPIを使ってユーザーに対して送信する
    line_msg_send(event, gnrtd_msg)


#LINE-DevelopersのWebhookを介して送られてくるイベントを処理する(＝フォローイベントを処理する)
@handler.add(FollowEvent)
def handle_follow(event):
    fllw_msg = "友達追加 ありがとう！"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=fllw_msg))


#ユーザーから送られるLINEメッセージを解析する
def line_msg_analyze(line_msg):
    #ユーザーから送られるメッセージの中に含まれるコンテント・オントロジーを抽出する
    line_cntnt  = line_bot_text_analyze.extract_content(line_msg)
    line_ontrgy = line_bot_text_analyze.extract_ontrgy(line_msg)

    #ユーザーから送られるメッセージの中に含まれるインテントを抽出する
    rmvd_etc_msg = line_bot_text_analyze.remove_etc(line_msg)
    extrctd_intnt = line_bot_text_analyze.extract_intent_from_gag_and_vocalcordcopy(rmvd_etc_msg)
    if extrctd_intnt != "<その他・不明>":
       line_intnt = extrctd_intnt
       return line_intnt, line_cntnt, line_ontrgy
    rmvd_etc_msg   = line_bot_text_analyze.remove_etc(line_msg)
    rmvd_symbl_msg = line_bot_text_analyze.remove_symbol(rmvd_etc_msg)
    extrctd_intnt2 = line_bot_text_analyze.extract_intent_from_gag_and_vocalcordcopy(rmvd_symbl_msg)
    if extrctd_intnt2 != "<その他・不明>":
       line_intnt = extrctd_intnt2
       return line_intnt, line_cntnt, line_ontrgy
    rmvd_etc_msg   = line_bot_text_analyze.remove_etc(line_msg)
    rmvd_symbl_msg = line_bot_text_analyze.remove_symbol(rmvd_etc_msg)
    extrctd_intnt3 = line_bot_text_analyze.extract_intent_from_short_and_boilerplate(rmvd_symbl_msg)
    if extrctd_intnt3 != "<その他・不明>":
       line_intnt = extrctd_intnt3
       return line_intnt, line_cntnt, line_ontrgy
    rmvd_etc_msg     = line_bot_text_analyze.remove_etc(line_msg)
    rmvd_symbl_msg   = line_bot_text_analyze.remove_symbol(rmvd_etc_msg)
    rmvd_edprtcl_msg = line_bot_text_analyze.remove_endparticle(rmvd_symbl_msg)
    extrctd_intnt4 = line_bot_text_analyze.extract_intent_from_short_and_boilerplate(rmvd_edprtcl_msg)
    if extrctd_intnt4 != "<その他・不明>":
       line_intnt = extrctd_intnt4
       return line_intnt, line_cntnt, line_ontrgy
    rmvd_etc_msg     = line_bot_text_analyze.remove_etc(line_msg)
    rmvd_symbl_msg   = line_bot_text_analyze.remove_symbol(rmvd_etc_msg)
    rmvd_edprtcl_msg = line_bot_text_analyze.remove_endparticle(rmvd_symbl_msg)
    line_intnt       = line_bot_text_analyze.extract_intent(rmvd_edprtcl_msg)
    return line_intnt, line_cntnt, line_ontrgy


#ユーザーから送られるLINEメッセージの解析結果から返信メッセージを生成する
def line_msg_generate():
    #データベースに接続して、テーブル操作のためのカーソルを用意・作成する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8")
    cur  = conn.cursor()

    #現在と過去の分を合わせた５件のLINEレコードをデータベースから取得する
    global usr_id
    global rcd_id
    line_rcds = []
    if rcd_id == -1:
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
    if rcd_id == 0:
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
    if rcd_id == 1:
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 0;""")
       line_rcd = cur.fetchone()
       line_rcds.append([line_rcd[1], line_rcd[2], line_rcd[3], line_rcd[4], line_rcd[5], line_rcd[6], line_rcd[7]])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
    if rcd_id == 2:
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 0;""")
       line_rcd = cur.fetchone()
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 1;""")
       line_rcd2 = cur.fetchone()
       line_rcds.append([line_rcd[1], line_rcd[2], line_rcd[3], line_rcd[4], line_rcd[5], line_rcd[6], line_rcd[7]])
       line_rcds.append([line_rcd2[1], line_rcd2[2], line_rcd2[3], line_rcd2[4], line_rcd2[5], line_rcd2[6], line_rcd2[7]])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
    if rcd_id == 3:
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 0;""")
       line_rcd = cur.fetchone()
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 1;""")
       line_rcd2 = cur.fetchone()
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 2;""")
       line_rcd3 = cur.fetchone()
       line_rcds.append([line_rcd[1], line_rcd[2], line_rcd[3], line_rcd[4], line_rcd[5], line_rcd[6], line_rcd[7]])
       line_rcds.append([line_rcd2[1], line_rcd2[2], line_rcd2[3], line_rcd2[4], line_rcd2[5], line_rcd2[6], line_rcd2[7]])
       line_rcds.append([line_rcd3[1], line_rcd3[2], line_rcd3[3], line_rcd3[4], line_rcd3[5], line_rcd3[6], line_rcd3[7]])
       line_rcds.append(["", "", "", "", "", "", ""])
       line_rcds.append(["", "", "", "", "", "", ""])
    if rcd_id == 4:
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 0;""")
       line_rcd = cur.fetchone()
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 1;""")
       line_rcd2 = cur.fetchone()
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 2;""")
       line_rcd3 = cur.fetchone()
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = 3;""")
       line_rcd4 = cur.fetchone()
       line_rcds.append([line_rcd[1], line_rcd[2], line_rcd[3], line_rcd[4], line_rcd[5], line_rcd[6], line_rcd[7]])
       line_rcds.append([line_rcd2[1], line_rcd2[2], line_rcd2[3], line_rcd2[4], line_rcd2[5], line_rcd2[6], line_rcd2[7]])
       line_rcds.append([line_rcd3[1], line_rcd3[2], line_rcd3[3], line_rcd3[4], line_rcd3[5], line_rcd3[6], line_rcd3[7]])
       line_rcds.append([line_rcd4[1], line_rcd4[2], line_rcd4[3], line_rcd4[4], line_rcd4[5], line_rcd4[6], line_rcd4[7]])
       line_rcds.append(["", "", "", "", "", "", ""])
    if rcd_id >= 5:
       idx = rcd_id - 5
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': idx})
       line_rcd = cur.fetchone()
       line_rcds.append([line_rcd[1], line_rcd[2], line_rcd[3], line_rcd[4], line_rcd[5], line_rcd[6], line_rcd[7]])
       idx = rcd_id - 4
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': idx})
       line_rcd = cur.fetchone()
       line_rcds.append([line_rcd[1], line_rcd[2], line_rcd[3], line_rcd[4], line_rcd[5], line_rcd[6], line_rcd[7]])
       idx = rcd_id - 3
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': idx})
       line_rcd = cur.fetchone()
       line_rcds.append([line_rcd[1], line_rcd[2], line_rcd[3], line_rcd[4], line_rcd[5], line_rcd[6], line_rcd[7]])
       idx = rcd_id - 2
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': idx})
       line_rcd = cur.fetchone()
       line_rcds.append([line_rcd[1], line_rcd[2], line_rcd[3], line_rcd[4], line_rcd[5], line_rcd[6], line_rcd[7]])
       idx = rcd_id - 1
       cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': idx})
       line_rcd = cur.fetchone()
       line_rcds.append([line_rcd[1], line_rcd[2], line_rcd[3], line_rcd[4], line_rcd[5], line_rcd[6], line_rcd[7]])

    #データベースへコミットし、テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    conn.commit()
    cur.close()
    conn.close()

    #LINEレコードリストを基にユーザーに返信するLINEメッセージを生成する
    gnrtd_msg = line_bot_text_generate.text_generate_from_analyze_result(line_rcds)
    return gnrtd_msg


#LINEBotAPIを使って生成されるLINEメッセージをユーザーに対して送信する
def line_msg_send(event, line_gnrtd_msg):
    #LINEの返信用トークンと生成されたメッセージをセットにしてLINEBotAPIの呼出しをする
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=line_gnrtd_msg))


#ユーザーから送られるLINEメッセージをPostgresのデータベースに登録・格納する
def postgres_insert_and_update(event, line_intnt, line_cntnt, line_ontrgy):
    #データベースに接続して、テーブル操作のためのカーソルを用意・作成する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #データベースに登録・格納するLINEレコードを構成する情報をまとめて用意・作成する
    global has_db_tbl
    global usr_nm
    global usr_id
    global rcd_id
    jst        = datetime.timezone(datetime.timedelta(hours=+9), "JST")
    dttm_tmp   = datetime.datetime.now(jst)
    dttm       = dttm_tmp.strftime("%Y/%m/%d %H:%M:%S")
    prfl       = line_bot_api.get_profile(event.source.user_id)
    usr_nm_tmp = prfl.display_name
    msg        = event.message.text
    intnt      = line_intnt
    cntnt      = line_cntnt
    ontrgy     = line_ontrgy

    #プログラム実行中にLINEユーザーが入れ変わったら、ユーザーIDとユーザー名を変更する(テーブルフラグを倒しておく)
    if usr_id != event.source.user_id:
       has_db_tbl = False
       usr_id     = event.source.user_id
       usr_nm     = usr_nm_tmp

    #テーブルフラグが倒れていたら、データベース上に新たにテーブルを用意・作成する(ユーザーIDとユーザー名の設定もしておく)
    if has_db_tbl == False:
       usr_id = event.source.user_id
       usr_nm = usr_nm_tmp
       try:
        cur.execute("""CREATE TABLE IF NOT EXISTS line_tbl(rcd_id integer PRIMARY KEY, dttm text, text, msg text, intnt text, cntnt text, ontrgy text);""")
       except Exception:
           pass

    #該当IDのメッセージ(＝レコード)がなかったら、データベースにインサート(＝新規に登録・格納)し、既にメッセージがあったらアップデート(＝上書き)する
    if rcd_id == -1:
       rcd_id = 0
    cur.execute("""SELECT * FROM line_tbl WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id})
    line_rcd = cur.fetchone()
    if (rcd_id >= 0 and rcd_id <= 99):
        if line_rcd is None:
           cur.execute("""INSERT INTO line_tbl (rcd_id, dttm, usr_nm, msg, intnt, cntnt, ontrgy) VALUES (%(rcd_id)s, %(dttm)s, %(msg)s, %(intnt)s, %(cntnt)s, %(ontrgy)s);""", {'rcd_id': rcd_id, 'dttm': dttm, 'usr_nm': usr_nm, 'msg': msg, 'intnt': intnt, 'cntnt': cntnt, 'ontrgy': ontrgy})
        if line_rcd is not None:
           cur.execute("""UPDATE line_tbl SET rcd_id=%(rcd_id)s, dttm=%(dttm)s, msg=%(msg)s, intnt=%(intnt)s, cntnt=%(mncntnt)s, ontrgy=%(ontrgy)s WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id, 'dttm': dttm, 'msg': msg, 'intnt': intnt, 'cntnt': cntnt, 'ontrgy': ontrgy, 'rcd_id': rcd_id})
        rcd_id +=  1
    if rcd_id == 100:
       rcd_id = -1

    #データベースへコミットし、テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    conn.commit()
    cur.close()
    conn.close()


#Postgresのデータベースからレコードを全件取得する
def postgres_select_all():
    #データベースに接続して、テーブル操作のためのカーソルを用意・作成する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8")
    cur  = conn.cursor()

    #データベースに登録・格納されている全てのレコードをセレクトして取得する
    rcds = []
    cur.execute("""SELECT * FROM line_tbl;""")
    rcds = cur.fetchall()

    #テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    cur.close()
    conn.close()
    return rcds




#FlaskのアプリケーションモジュールをWebアプリケーションサーバー上で実行する
if __name__ == "__main__":
    # デバッグモードをオンにし、ポート番号の設定をしてアプリケーションモジュールを実行する
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))