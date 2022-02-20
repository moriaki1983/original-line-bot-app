#モジュールの読み込み
import os
#import gunicorn
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
#HAS_DB_TABLE = os.environ["HAS_DB_TABLE"]

#herokuの環境に設定されている、Postgres上のLINEメッセージの登録・格納件数を示す変数を取得する
DB_RCD_NUM = os.environ["DB_RCD_NUM"]




#herokuへのデプロイが成功したかどうかを確認する
@app.route("/")
def now_online():
    #データベースへの接続を確立して、カーソルを用意する
    conn = psycopg2.connect(DATABASE_URL)
    cur  = conn.cursor()

    # データベースからLINEメッセージを取得して、ブラウザーに引渡しする
    rcd_id = int(os.environ['DB_RCD_NUM'])
    cur.execute("SELECT * FROM items WHERE id=%s", [rcd_id])
    row = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(row), 200
    #return os.environ['DB_RCD_NUM']

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
    
    
    #データベースに接続して、カーソルを用意する
    #conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn = psycopg2.connect(DATABASE_URL)
    cur  = conn.cursor()

    #テーブルを作成する
    if cos.environ["HAS_DB_TABLE"] == 'True':
        cur.execute("DROP TABLE items")
        cur.execute("CREATE TABLE items(id int, date, speaker text, msg text)")
    else:
        cur.execute("CREATE TABLE items(id int, date, speaker text, msg text)")
        cos.environ["HAS_DB_TABLE"] = 'True'
 
    #ユーザーからのLINEメッセージをデータベースに登録・格納する
    rcd_id  = int(os.environ["DB_RCD_NUM"])
    date    = "2022-02-22-22:22"
    speaker = event.source.userId
    msg     = event.message.text
    cur.execute("SELECT * FROM items WHERE id=%s", [rcd_id])
    row = cur.fetchone()
    cur.execute("SELECT * FROM items")
    row_num = len(cur.fetchall())

    if row == null:
        cur.execute("INSERT INTO items (id, date, speaker, msg) VALUES (%s, %s, %s, %s)", [rcd_id, date, speaker, msg])
    elif row_num >= 100:
        os.environ["DB_RCD_NUM"] = '-1'
        cur.execute("UPDATE items SET id=%s, date=%s, speaker=%s, msg=%s, WHERE id=%s", [rcd_id, date, speaker, msg, rcd_id])
    cur.execute("INSERT INTO items (id, date, speaker, msg) VALUES (%s, %s, %s, %s)", [rcd_id, date, speaker, msg])
    
    #
    env_count()
    
    #データベースへコミットし、カーソルを破棄して、接続を解除する。
    conn.commit()
    cur.close()
    conn.close()

#
def env_count():
    os.environ["DB_RCD_NUM"] = str(int(os.environ["DB_RCD_NUM"]) + 1)


# ポート番号の設定
if __name__ == "__main__":
    #FlaskのアプリモジュールをWebアプリケーションサーバー上で実行する
    #app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
