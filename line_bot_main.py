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

#herokuの環境変数に設定されている、LINE-Developersのアクセストークンとチャンネルシークレットを取得する
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET       = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler      = WebhookHandler(YOUR_CHANNEL_SECRET)

#herokuの環境に設定されている、postgresにアクセスするためのキーを取得する
DATABASE_URL = os.environ["DATABASE_URL"]

#Postgresデータベースに登録・格納するLINEメッセージ(＝レコード)のID(＝レコードカウンター)を示す変数を宣言する
rcd_id = -1




#Postgresデータベース上のテーブル内のレコードを取得して、ブラウザーに引渡しをする
@app.route("/")
def show_db_record():
    #データベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #データベースからLINEメッセージ(＝レコード)を過去１件分取得してブラウザーに引渡しをする
    global rcd_id
    app.logger.info(rcd_id)
    if rcd_id == -1:
       cur.close()
       conn.close()
       return "table record not exist..."
    if rcd_id == 0:
       rcd_id_tmp = 0
       cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id_tmp})
       rcd = cur.fetchone()
       cur.close()
       conn.close()
       return jsonify(rcd), 200
    if rcd_id >= 1:
       rcd_id_tmp = rcd_id - 1
       cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id_tmp})
       rcd = cur.fetchone()
       cur.close()
       conn.close()
       return jsonify(rcd), 200
    if rcd_id == 100:
       return "reached the end of the table..."
       cur.close()
       conn.close()


#Postgresデータベース上に新たにテーブルを用意・作成する
@app.route("/create_db_table")
def create_db_table():
    #データベースに接続して、テーブル操作のためのカーソルを用意・作成する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #データベース上に新たにテーブルを用意・作成する
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS line_test_entry2(rcd_id integer PRIMARY KEY, dttm text, usr_nm text, msg text, intnt text);""")
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
    global rcd_id
    try:
        cur.execute("DROP TABLE IF EXISTS line_test_entry2;")
    except Exception:
        pass

    #各種のプログラムの実行状態を示す変数を初期化する
    rcd_id       = -1

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
    line_msg_intnt, prv_line_rcd_lst = line_msg_analyze(event.message.text)

    #ユーザーから送られるLINEメッセージの解析結果から返信メッセージを生成する
    gnrtd_msg = line_msg_generate(event.source.user_id, event.message.text, line_msg_intnt, prv_line_rcd_lst)

    #LINEBotAPIを使って生成されるLINEメッセージをユーザーに対して送信する
    line_msg_send(event, gnrtd_msg)

    #ユーザーから送られるLINEメッセージをPostgresのデータベースに登録・格納する
    postgres_insert_and_update(event, line_msg_intnt)


#LINE-DevelopersのWebhookを介して送られてくるイベントを処理する(＝フォローイベントを処理する)
@handler.add(FollowEvent)
def handle_follow(event):
    fllw_msg = "友達追加 ありがとう！"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=fllw_msg))


#ユーザーから送られるLINEメッセージを解析する
def line_msg_analyze(line_msg_txt):
    #データベースに接続して、テーブル操作のためのカーソルを用意・作成する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #過去４件分のユーザーからのLINEメッセージ(＝レコード)をデータベースから取得する
    global rcd_id
    prv_line_rcd_lst = []
    if rcd_id == -1:
       prv_line_rcd_lst.append(["", "", "", ""])
       prv_line_rcd_lst.append(["", "", "", ""])
       prv_line_rcd_lst.append(["", "", "", ""])
       prv_line_rcd_lst.append(["", "", "", ""])
    if rcd_id == 0:
       prv_line_rcd_lst.append(["", "", "", ""])
       prv_line_rcd_lst.append(["", "", "", ""])
       prv_line_rcd_lst.append(["", "", "", ""])
       prv_line_rcd_lst.append(["", "", "", ""])
    if rcd_id == 1:
       cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = 0;""")
       prv_line_rcd = cur.fetchone()
       prv_line_rcd_lst.append([prv_line_rcd[1], prv_line_rcd[2], prv_line_rcd[3], prv_line_rcd[4]])
       prv_line_rcd_lst.append(["", "", "", ""])
       prv_line_rcd_lst.append(["", "", "", ""])
       prv_line_rcd_lst.append(["", "", "", ""])
    if rcd_id == 2:
       cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = 0;""")
       prv_line_rcd = cur.fetchone()
       cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = 1;""")
       prv_line_rcd2 = cur.fetchone()
       prv_line_rcd_lst.append([prv_line_rcd[1], prv_line_rcd[2], prv_line_rcd[3], prv_line_rcd[4]])
       prv_line_rcd_lst.append([prv_line_rcd2[1], prv_line_rcd[2], prv_line_rcd2[3], prv_line_rcd2[4]])
       prv_line_rcd_lst.append(["", "", "", ""])
       prv_line_rcd_lst.append(["", "", "", ""])
    if rcd_id == 3:
       cur.execute("SELECT * FROM line_test_entry2 WHERE rcd_id = 0;""")
       prv_line_rcd = cur.fetchone()
       cur.execute("SELECT * FROM line_test_entry2 WHERE rcd_id = 1;""")
       prv_line_rcd2 = cur.fetchone()
       cur.execute("SELECT * FROM line_test_entry2 WHERE rcd_id = 2;""")
       prv_line_rcd3 = cur.fetchone()
       prv_line_rcd_lst.append([prv_line_rcd[1], prv_line_rcd[2], prv_line_rcd[3], prv_line_rcd[4]])
       prv_line_rcd_lst.append([prv_line_rcd2[1], prv_line_rcd[2], prv_line_rcd2[3], prv_line_rcd2[4]])
       prv_line_rcd_lst.append([prv_line_rcd3[1], prv_line_rcd[2], prv_line_rcd3[3], prv_line_rcd3[4]])
       prv_line_rcd_lst.append(["", "", "", ""])
    if rcd_id >= 4:
       idx = rcd_id - 4
       cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': idx})
       prv_line_rcd = cur.fetchone()
       prv_line_rcd_lst.append([prv_line_rcd[1], prv_line_rcd[2], prv_line_rcd[3], prv_line_rcd[4]])
       idx = rcd_id - 3
       cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': idx})
       prv_line_rcd = cur.fetchone()
       prv_line_rcd_lst.append([prv_line_rcd[1], prv_line_rcd[2], prv_line_rcd[3], prv_line_rcd[4]])
       idx = rcd_id - 2
       cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': idx})
       prv_line_rcd = cur.fetchone()
       prv_line_rcd_lst.append([prv_line_rcd[1], prv_line_rcd[2], prv_line_rcd[3], prv_line_rcd[4]])
       idx = rcd_id - 1
       cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': idx})
       prv_line_rcd = cur.fetchone()
       prv_line_rcd_lst.append([prv_line_rcd[1], prv_line_rcd[2], prv_line_rcd[3], prv_line_rcd[4]])

    #データベースへコミットし、テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    conn.commit()
    cur.close()
    conn.close()

    #ユーザーから送られるLINEメッセージの中に含まれるインテントを抽出する
    rmv_etc      = line_bot_text_analyze.remove_etc(line_msg_txt)
    extrct_intnt = line_bot_text_analyze.extract_intent_from_gag_and_vocalcordcopy(rmv_etc)
    if extrct_intnt != "<その他・不明>":
       line_msg_intnt = extrct_intnt
       return line_msg_intnt, prv_line_rcd_lst
    rmv_etc       = line_bot_text_analyze.remove_etc(line_msg_txt)
    rmv_symbl     = line_bot_text_analyze.remove_symbol(rmv_etc)
    extrct_intnt2 = line_bot_text_analyze.extract_intent_from_gag_and_vocalcordcopy(rmv_symbl)
    if extrct_intnt2 != "<その他・不明>":
       line_msg_intnt = extrct_intnt2
       return line_msg_intnt, prv_line_rcd_lst
    rmv_etc       = line_bot_text_analyze.remove_etc(line_msg_txt)
    rmv_symbl     = line_bot_text_analyze.remove_symbol(rmv_etc)
    extrct_intnt3 = line_bot_text_analyze.extract_intent_from_short_and_boilerplate(rmv_symbl)
    if extrct_intnt3 != "<その他・不明>":
       line_msg_intnt = extrct_intnt3
       return line_msg_intnt, prv_line_rcd_lst
    rmv_etc          = line_bot_text_analyze.remove_etc(line_msg_txt)
    rmv_symbl        = line_bot_text_analyze.remove_symbol(rmv_etc)
    rmv_edprtcl      = line_bot_text_analyze.remove_endparticle(rmv_symbl)
    extrct_intnt4 = line_bot_text_analyze.extract_intent_from_short_and_boilerplate(rmv_edprtcl)
    if extrct_intnt4 != "<その他・不明>":
       line_msg_intnt = extrct_intnt4
       return line_msg_intnt, prv_line_rcd_lst
    rmv_etc          = line_bot_text_analyze.remove_etc(line_msg_txt)
    rmv_symbl        = line_bot_text_analyze.remove_symbol(rmv_etc)
    rmv_edprtcl      = line_bot_text_analyze.remove_endparticle(rmv_symbl)
    extrct_intnt_end = line_bot_text_analyze.extract_intent(rmv_edprtcl)
    line_msg_intnt = extrct_intnt_end
    return line_msg_intnt, prv_line_rcd_lst


#ユーザーから送られるLINEメッセージの解析結果から返信メッセージを生成する
def line_msg_generate(line_usr_id, line_msg_txt, line_msg_intnt, prv_line_rcd_lst):
    #ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
    line_prfl          = line_bot_api.get_profile(line_usr_id)
    line_usr_nm        = line_prfl.display_name
    jst                = datetime.timezone(datetime.timedelta(hours=+9), "JST")
    dttm_tmp           = datetime.datetime.now(jst)
    line_msg_dttm      = dttm_tmp.strftime("%Y/%m/%d %H:%M:%S")
    crrnt_line_rcd_lst = [line_msg_dttm, line_usr_nm, line_msg_txt, line_msg_intnt]
    gnrtd_msg          = line_bot_text_generate.text_generate_from_analyze_result(crrnt_line_rcd_lst, prv_line_rcd_lst)
    return gnrtd_msg


#LINEBotAPIを使って生成されるLINEメッセージをユーザーに対して送信する
def line_msg_send(event, line_gnrtd_msg):
    #LINEの返信用トークンと生成されたメッセージをセットにしてLINEBotAPIの呼出しをする
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=line_gnrtd_msg))


#ユーザーから送られるLINEメッセージをPostgresのデータベースに登録・格納する
def postgres_insert_and_update(event, line_msg_intnt):
    #データベースに接続して、テーブル操作のためのカーソルを用意・作成する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    #データベースに登録・格納するLINEメッセージ(＝レコード)を構成する情報をまとめて用意・作成する
    global rcd_id
    jst      = datetime.timezone(datetime.timedelta(hours=+9), "JST")
    dttm_tmp = datetime.datetime.now(jst)
    dttm     = dttm_tmp.strftime("%Y/%m/%d %H:%M:%S")
    prfl     = line_bot_api.get_profile(event.source.user_id)
    usr_nm   = prfl.display_name
    msg      = event.message.text
    intnt    = line_msg_intnt

    #該当IDのメッセージ(＝レコード)がなかったら、データベースにインサート(＝新規に登録・格納)し、既にメッセージがあったらアップデート(＝上書き)する
    if rcd_id == -1:
       rcd_id = 0
    cur.execute("""SELECT * FROM line_test_entry2 WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id})
    line_rcd = cur.fetchone()
    if (rcd_id >= 0 and rcd_id <= 99):
        if line_rcd is None:
           cur.execute("""INSERT INTO line_test_entry2 (rcd_id, dttm, usr_nm, msg, intnt) VALUES (%(rcd_id)s, %(dttm)s, %(usr_nm)s, %(msg)s, %(intnt)s);""", {'rcd_id': rcd_id, 'dttm': dttm, 'usr_nm': usr_nm, 'msg': msg, 'intnt': intnt})
        if line_rcd is not None:
           rcd_id_tmp = rcd_id
           cur.execute("""UPDATE line_test_entry2 SET (rcd_id, dttm, usr_nm, msg, intnt) VALUES (%(rcd_id)s, %(dttm)s, %(usr_nm)s, %(msg)s, %(intnt)s) WHERE = %(rcd_id_tmp)s;""", {'rcd_id': rcd_id, 'dttm': dttm, 'usr_nm': usr_nm, 'msg': msg, 'intnt': intnt, 'rcd_id_tmp': rcd_id_tmp})
        rcd_id = rcd_id + 1
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
    rcd_list = []
    cur.execute("""SELECT * FROM line_test_entry2;""")
    rcd_list = cur.fetchall()

    #テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    cur.close()
    conn.close()
    return rcd_list




#FlaskのアプリケーションモジュールをWebアプリケーションサーバー上で実行する
if __name__ == "__main__":
    # デバッグモードをオンにし、ポート番号の設定をしてアプリケーションモジュールを実行する
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))