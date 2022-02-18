#各モジュールの読み込み
from flask import Flask, request, abort
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
import sqlite3
import os
import re
import random


#
app = Flask(__name__)
#db_init_flg = False

#データベースへの接続を確立すると供にデータベースファイルを作成する
db_nm = 'line_msg.db'
conn = sqlite3.connect(db_nm)
cur = conn.cursor()

# テーブルの作成
cur.execute("CREATE TABLE items(date, speaker, msg)")
 
#herokuの環境変数に設定された、LINE DevelopersのアクセストークンとChannelSecretを取得するコード
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


#herokuへのデプロイが成功したかどうかを確認するためのコード
@app.route("/")
def now_online():
    # データ検索
    return cur.execute("SELECT * FROM items")


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
    #データベースへの接続を確立すると供にデータベースファイルを作成する
    #db_nm = 'line_msg.db'
    #conn = sqlite3.connect(db_nm)
    #cur = conn.cursor()

    #
    #if db_init_flg == False
    #   # テーブルの作成
    #   cur.execute('CREATE TABLE items(id INTEGER PRIMARY KEY AUTOINCREMENT, date STRING, speaker STRING, msg STRING)')
    #   db_init_flg = True

    #
    tknzr = Tokenizer()
    tkns = tknzr.tokenize(event.message.text)
    rslt = []
    for tkn in tkns:
        rslt.append(tkn.surface)

    if rslt[0] == "わたし":
       rslt[0] = "LINE-Client"

    #
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text="/".join(rslt)))

    # 登録するデータ
    inserts = ["test", "test", "test"]
    cur.execute("INSERT INTO items VALUES(?, ?, ?)", inserts)
    conn.commit()


# ポート番号の設定
if __name__ == "__main__":
    #
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    cur.close()
    conn.close()
    #db_init_flg = False
