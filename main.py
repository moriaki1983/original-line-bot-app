#モジュールの読み込み
import os
import psycopg2
from flask import Flask, jsonify, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from janome.tokenizer import Tokenizer




#Flaskのアプリモジュールを作成する
app = Flask(__name__)

#herokuの環境変数に設定されている、LINE-Developersのアクセストークンとチャンネルシークレットを取得する
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET       = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler      = WebhookHandler(YOUR_CHANNEL_SECRET)

#herokuの環境に設定されている、Postgresにアクセスするためのキーを取得する
DATABASE_URL = os.environ["DATABASE_URL"]

#herokuの環境に設定されている、Postgres上のテーブルの有無を示す変数を取得する
HAS_DB_TABLE = os.environ["HAS_DB_TABLE"]

rcd_id = "0"




#herokuへのデプロイが成功したかどうかを確認する
@app.route("/")
def now_online():
    #データベースへの接続を確立して、カーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    cur  = conn.cursor()

    # データベースからLINEメッセージを取得して、ブラウザーに引渡しする
    rcd_id = os.environ["DB_RCD_NUM"]
    cur.execute("""SELECT * FROM items WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id})
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    #
    #return jsonify(row), 200
    return rcd_id


#LINE DevelopersのWebhookにURLを指定してWebhookからURLにイベントが送られるようにする
@app.route("/callback", methods=['POST'])
def callback():
    # HTTPリクエストヘッダーから署名検証のためのシグネチャーを取得する
    #signature = request.META['HTTP_X_LINE_SIGNATURE']
    signature = request.headers['X-Line-Signature']

    # HTTPリクエストボディを取得する
    #body = request.body.decode('utf-8')
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 署名を検証して、問題がなければhandleに定義されている関数の呼出しをする
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        # 署名検証に失敗したら例外を送出する
        #return HttpResponseForbidden()
        abort(400)
    #呼出し元にステータスコードを送出する
    #return HttpResponse('OK')
    return 'OK'


#以下でWebhookから送られてきたイベントをどのように処理するかを記述する
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #JanomeでユーザーからのLINEメッセージを解析する
    tknzr = Tokenizer()
    tkns = tknzr.tokenize(event.message.text)
    rslt = []
    for tkn in tkns:
        rslt.append(tkn.surface)

    #ユーザーへの返信メッセージを生成する
    if rslt[0] == "わたし":
       rslt[0] = "LINE-Client"

    #ユーザーにLINEメッセージを送信する
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="/".join(rslt)))
    
    #
    main.db_process(event)

    global rcd_id
    rcd_id = str(int(rcd_id) + 1)
    
    #
    #main.env_set()

    #
    #main.env_count()


def db_process(event):
    #データベースに接続して、カーソルを用意する
    #conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn = psycopg2.connect(DATABASE_URL)
    conn.set_client_encoding('utf-8') 
    cur  = conn.cursor()

    #テーブルを作成する
    if os.environ["HAS_DB_TABLE"] == 'True':
       cur.execute("DROP TABLE items")
       cur.execute("CREATE TABLE items(rcd_id text, date text, speaker text, msg text)")
    else:
       cur.execute("CREATE TABLE items(rcd_id text, date text, speaker text, msg text)")
       os.environ["HAS_DB_TABLE"] = 'True'
    
    #ユーザーからのLINEメッセージをデータベースに登録・格納する
    global rcd_id    
    #rcd_id  = os.environ["DB_RCD_NUM"]
    date    = "2022-02-22-22:22"
    #speaker = event.source.userId
    speaker = "LINE-Client"
    msg     = event.message.text

    #
    cur.execute("""SELECT * FROM items WHERE rcd_id = %(rcd_id)s;""", {'rcd_id': rcd_id})
    row = cur.fetchone()
    cur.execute("SELECT * FROM items")
    row_num = len(cur.fetchall())

    #
    if row is None:
       cur.execute("""INSERT INTO items (rcd_id, date, speaker, msg) VALUES (%(rcd_id)s, %(date)s, %(speaker)s, %(msg)s);""", {'rcd_id': rcd_id, 'date' : date, 'speaker': speaker, 'msg': msg})
    elif int(os.environ["DB_RCD_NUM"]) < 99:
       cur.execute("""UPDATE items SET (rcd_id, date, speaker, msg) VALUES (%(rcd_id)s, %(date)s, %(speaker)s, %(msg)s) WHERE = %(rcd_id)s;""", {'rcd_id': rcd_id, 'date' : date, 'speaker': speaker, 'msg': msg, 'rcd_id': rcd_id})
    elif int(os.environ["DB_RCD_NUM"]) == 99:
       cur.execute("""UPDATE items SET (rcd_id, date, speaker, msg) VALUES (%(rcd_id)s, %(date)s, %(speaker)s, %(msg)s) WHERE = '0';""", {'rcd_id': "0", 'date' : date, 'speaker': speaker, 'msg': msg})

    #データベースへコミットし、カーソルを破棄して、接続を解除する。
    conn.commit()
    cur.close()
    conn.close()


#
def env_set():
    if int(os.environ["DB_RCD_NUM"]) > 99:
       os.environ["DB_RCD_NUM"] = "-1"


#
def env_count():
    os.environ["DB_RCD_NUM"] = str(int(os.environ["DB_RCD_NUM"]) + 1)




# ポート番号の設定
if __name__ == "__main__":
    #FlaskのアプリモジュールをWebアプリケーションサーバー上で実行する
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
