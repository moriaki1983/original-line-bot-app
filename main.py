#各モジュールの読み込み
import os
import datetime
import psycopg2
from flask import Flask, jsonify, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, FollowEvent, TextMessage, TextSendMessage)
from janome.tokenizer import Tokenizer




#Flaskのアプリケーションモジュールを作成する
app = Flask(__name__)

#herokuの環境変数に設定されている、LINE-Developersのアクセストークンとチャンネルシークレットを取得する
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET       = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler      = WebhookHandler(YOUR_CHANNEL_SECRET)

#herokuの環境に設定されている、postgresにアクセスするためのキーを取得する
DATABASE_URL = os.environ["DATABASE_URL"]

#postgresデータベース上のテーブル「line_entries」の有無を示す変数を宣言する
has_db_table = False

#postgresデータベースに登録・格納するLINEメッセージ(＝レコード)のID(＝レコードカウンタ)を示す変数を宣言する
rcd_id = "0"




#postgresデータベース上のテーブル内のレコードを取得して、ブラウザーに引渡しをする
@app.route("/")
def show_db_record():
    #postgresデータベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()

    # データベースから該当IDのLINEメッセージ(＝レコード)を取得し、jsonifyで整形して呼出し元に引き渡しをする
    global has_db_table
    global rcd_id
    if has_db_table == True:
       if rcd_id == "0":
         cur.execute("""SELECT * FROM line_entries WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id})
       elif int(rcd_id) > int("0"):
         cur.execute("""SELECT * FROM line_entries WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': str(int(rcd_id) - 1)})
       rcd = cur.fetchone()
       cur.close()
       conn.close()
       return jsonify(rcd), 200
    else:
       cur.close()
       conn.close()
       return "db-table not exist..."


#postgresデータベース上のテーブルを破棄する
@app.route("/table_drop")
def db_table_drop():
    #postgresデータベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding("utf-8") 
    cur  = conn.cursor()
    tbl_oprtn_rslt = ""

    #既にテーブルが作成・用意されていれば、それを破棄する
    cur.execute("DROP TABLE line_entries")
    global has_db_table
    has_db_table = False

    #データベースに登録・格納するLINEメッセージ(＝レコード)のID(＝レコードカウンタ)を示す変数を初期化する
    global rcd_id
    rcd_id = "0"

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
    tknz_rslt = tokenize(event.message.text)

    #janomeで解析されたユーザーのメッセージを基に返信メッセージを生成する
    msg_gnrt_rslt = generate(tknz_rslt)
    
    #LINEBotAPIを使って、ユーザーに生成されたLINEメッセージを送信する
    send(event, msg_gnrt_rslt)

    #ユーザーから送られるLINEメッセージをpostgresのデータベースに登録・格納する
    db_insert_and_update(event)


#LINE-DevelopersのWebhookを介して送られてくるイベントを処理する(＝フォローイベントを処理する)
@handler.add(FollowEvent)
def handle_follow(event):
    follow_msg = "友達追加 ありがとう！"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=follow_msg))


#ユーザーから送られるLINEメッセージをJanomeで形態素解析する
def tokenize(line_msg_text):
    #LINEメッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr = Tokenizer()
    tkns  = tknzr.tokenize(line_msg_text)
    
    #分解後のLINEメッセージをリストに格納して呼出し元に引渡しをする
    tknz_rslt = []
    for tkn in tkns:
        tknz_rslt.append(tkn.surface)
    tknz_rslt
    return tknz_rslt


#janomeで解析されたユーザーのメッセージを基に返信メッセージを生成する
def generate(tknz_rslt):
    #解析後のLINEメッセージの主語を置き換え、「/」で文節に分けて、呼出し元に引渡しをする
    msg_gnrt_rslt = []
    if tknz_rslt[0] == "わたし":
         tknz_rslt[0] = "LINE-Client"
    msg_gnrt_rslt = "/".join(tknz_rslt)
    return msg_gnrt_rslt


#LINEBotAPIを使って、ユーザーに生成されたLINEメッセージを送信する
def send(event, msg_gnrt_rslt):
    #LINEの返信用トークンと生成されたメッセージをセットにしてLINEBotAPIの呼出しをする
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg_gnrt_rslt))


#ユーザーから送られるLINEメッセージをpostgresのデータベースに登録・格納する
def db_insert_and_update(event):
    #postgresデータベースに接続して、テーブル操作のためのカーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding('utf-8') 
    cur  = conn.cursor()

    #既にテーブルが作成・用意されていれば、それを破棄して新たにテーブルを作成・用意する
    global has_db_table
    if has_db_table == False:
       cur.execute("DROP TABLE line_entries")
       cur.execute("CREATE TABLE line_entries(rcd_id text, date text, speaker text, msg text)")
       has_db_table = True

    #データベースに登録・格納するLINEメッセージ(＝レコード)を構成する情報をまとめて用意する
    global rcd_id
    jst = datetime.timezone(datetime.timedelta(hours=+9), "JST")
    dt_tm   = datetime.datetime.now(jst)
    date    = dt_tm.strftime("%Y/%m/%d %H:%M:%S")
    profile = line_bot_api.get_profile(event.source.user_id)
    speaker = profile.display_name
    msg     = event.message.text

    #該当IDのLINEメッセージ(＝レコード)がないか調べる、また、データベースに登録・格納されているメッセージの数も調べる
    cur.execute("""SELECT * FROM line_entries WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id})
    rcd = cur.fetchone()
    cur.execute("SELECT * FROM line_entries")
    rcd_num = len(cur.fetchall())

    #該当IDのLINEメッセージ(＝レコード)がなかったら、データベースにインサート(＝挿入)(＝新規に登録・格納)し、既にメッセージがあったらアップデート(＝上書き)する
    if rcd is None:
       cur.execute("""INSERT INTO line_entries (rcd_id, date, speaker, msg) VALUES (%(rcd_id)s, %(date)s, %(speaker)s, %(msg)s);""", {'rcd_id': rcd_id, 'date' : date, 'speaker': speaker, 'msg': msg})
       rcd_id = str(int(rcd_id) + 1)
    elif rcd_num < 99:
       cur.execute("""UPDATE line_entries SET (rcd_id, date, speaker, msg) VALUES (%(rcd_id)s, %(date)s, %(speaker)s, %(msg)s) WHERE = %(rcd_id)s;""", {'rcd_id': rcd_id, 'date' : date, 'speaker': speaker, 'msg': msg, 'rcd_id': rcd_id})
       rcd_id = str(int(rcd_id) + 1)
    elif rcd_num == 99:
       cur.execute("""UPDATE line_entries SET (rcd_id, date, speaker, msg) VALUES (%(rcd_id)s, %(date)s, %(speaker)s, %(msg)s) WHERE = '0';""", {'rcd_id': "0", 'date' : date, 'speaker': speaker, 'msg': msg})
       rcd_id = str(0)

    #データベースへコミットし、テーブル操作のためのカーソルを破棄して、データベースとの接続を解除する
    conn.commit()
    cur.close()
    conn.close()




#FlaskのアプリケーションモジュールをWebアプリケーションサーバー上で実行する
if __name__ == "__main__":
    # デバッグモードをオンにし、ポート番号の設定をしてアプリケーションモジュールを実行する
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
