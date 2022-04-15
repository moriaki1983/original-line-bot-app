# coding: utf-8




import random
from line_bot_character import BotCharacter




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_nwrcd, line_oldrcds):
    #を示す変数を宣言・定義する
    flw_of_uttrnc = line_nwrcd[0][3]
    cntnt         = line_nwrcd[0][4]
    mind          = BotCharacter.calc_mind(flw_of_uttrnc, cntnt)

    #ユーザーの発話の流れに沿った返信メッセージを生成する
    if mind == "<挨拶>":
       gnrtd_msg_cnddt = ["こんにちは", "どうも"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if mind == "<聞出し>":
       gnrtd_msg_cnddt = ["どうされましたか？", "伺います"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if mind == "<依頼＆要求への返答>":
       gnrtd_msg_cnddt = ["どうぞお話しください", "いいですよ"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg

    #ユーザーの発話の流れがどのパターンにも該当しない場合の処理をする
    gnrtd_msg = "また おしゃべりしましょう♪"
    return gnrtd_msg