#モジュールの読み込み
from flask import Flask,jsonify,request,abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from janome.tokenizer import Tokenizer
import psycopg2
import os
import re
import random




#Flaskのアプリモジュールを作成する
app = Flask(__name__)

#herokuの環境変数に設定された、LINE DevelopersのアクセストークンとChannelSecretを取得するコード
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET       = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler      = WebhookHandler(YOUR_CHANNEL_SECRET)

#herokuの環境に設定されているPostgresの変数を取得する
DATABASE_URL = os.environ["DATABASE_URL"]

#データベースの初期化フラグと、LINEメッセージをデータベースに登録・格納する際のIDを宣言する
#is_db_init = False
id = 0




#herokuへのデプロイが成功したかどうかを確認する
@app.route("/")
def now_online():
    #データベースへの接続を確立して、カーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    cur  = conn.cursor()

    # データベースからLINEメッセージを取得す
    cur.execute("SELECT * FROM items WHERE id=%s", [id])
    row = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(row), 500

#LINE DevelopersのWebhookにURLを指定してWebhookからURLにイベントが送られるようにする
@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得
    signature = request.headers['X-Line-Signature']

    # リクエストボディを取得
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 署名を検証し、問題なければhandleに定義されている関数を呼ぶ
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
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

    #データベースへの接続を確立して、カーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    cur  = conn.cursor()

    #テーブルを作成する
    #if is_db_init == False:
    #   cur.execute("CREATE TABLE items(id int, date text, speaker text, msg text)")
    #   is_db_init = True
 
    #ユーザーからのLINEメッセージをデータベースに登録・格納する
    #date    = "test"
    #speaker = event.source.userId
    #msg     = event.message.text
    #cur.execute("SELECT * FROM items WHERE id=%s", [id])
    #row = cur.fetchone()
    #if row == null:
    #   cur.execute("INSERT INTO items VALUES(%s, %s, %s, %s)", [id, date, speaker, msg])
    #   id += 1
    #elif len(cur.fetchall()) >= 100:
    #   id = 0
    #   cur.execute("UPDATE items SET date=%s, speaker=%s, msg=%s, WHERE id=%s", [date, speaker, msg, id])
    #   id += 1
    cur.execute("UPDATE items SET date='Test', speaker='LINE-Client', msg='こんにちは！' WHERE id=0")

    #
    conn.commit()
    cur.close()
    conn.close()




# ポート番号の設定
if __name__ == "__main__":
    #Flaskのアプリモジュールを実行する
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))