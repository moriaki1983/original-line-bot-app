# coding: utf-8




import random
from line_bot_character import BotCharacter




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_nwrcd, line_oldrcds, line_tpc):
    #会話の流れ等を示す変数を宣言・定義する
    flw_of_cnvrstn = line_nwrcd[0][4]
    msg            = line_nwrcd[0][3]
    cntnt          = line_nwrcd[0][5]
    tpc            = line_tpc

    #会話の流れ等からボットのマインドを計算する
    mind = BotCharacter.calc_mind(flw_of_cnvrstn, msg, cntnt, tpc)

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