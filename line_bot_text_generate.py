# coding: utf-8




#各モジュールの読み込み
import random
import wikipedia
from line_bot_character import BotCharacter




#Wikipediaサイト内のページを検索する
def wikipedia_search(srch_txt):
    wikipedia.set_lang("ja")
    rsps_str  = ""
    srch_rsps = wikipedia.search(srch_txt)
    if not srch_rsps:
       rsps_str = "その単語は 登録されていません"
       return rsps_str
    try:
        wk_pg = wikipedia.page(srch_rsps[0])
    except Exception:
        rsps_str = "エラーが発生しました"
        return rsps_str
    wk_cntnt = wk_pg.content
    rsps_str = wk_cntnt[0:wk_cntnt.find("。")] + "。\n"
    rsps_str += "リンクはこちら：" + wk_pg.url
    return rsps_str


#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_rcd, line_tpc):
    #会話の流れ等を示す変数を宣言・定義する
    msg   = line_rcd[0][3]
    intnt = line_rcd[0][4]
    cntnt = line_rcd[0][5]
    tpc   = line_tpc

    #会話の流れ等からボットのマインドを計算する
    mind = BotCharacter.calc_mind(msg, intnt, cntnt, tpc)

    #ボットのマインドに沿った返信メッセージを生成する
    if mind == "<挨拶 朝>":
       gnrtd_msg_cnddt = ["おはよう", "どうも"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if mind == "<挨拶 昼>":
       gnrtd_msg_cnddt = ["こんにちは", "どうも"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if mind == "<挨拶 夜>":
       gnrtd_msg_cnddt = ["こんばんは", "どうも"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if mind == "<挨拶 その他>":
       gnrtd_msg = "どうも"
       return gnrtd_msg

    #ユーザーの発話の流れがどのパターンにも該当しない場合の処理をする
    gnrtd_msg = "また おしゃべりしましょう♪"
    return gnrtd_msg