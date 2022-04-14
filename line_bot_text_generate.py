# coding: utf-8




import random
from line_bot_character import BotCharacter




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_nwrcd, line_oldrcds):
    #ユーザーの発話の流れを示す変数を宣言・定義する
    flw_of_uttrnc   = line_nwrcd[0][3]
    cntnt_of_uttrnc = line_nwrcd[0][4]

    #ユーザーの発話の流れに沿った返信メッセージを生成する
    if flw_of_uttrnc == "<称賛＆礼賛>":
       if BotCharacter.calc_mind(flw_of_uttrnc) == "<謝意＆感謝>":
          gnrtd_msg_cnddt = ["ありがとうございます", "嬉しいです"]
          gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       gnrtd_msg = gnrtd_msg + " cntnt:" + cntnt_of_uttrnc
       return gnrtd_msg

    #ユーザーの発話の流れがどのパターンにも該当しない場合の処理をする
    gnrtd_msg = "また おしゃべりしましょう♪"
    gnrtd_msg = gnrtd_msg + " cntnt:" + cntnt_of_uttrnc
    return gnrtd_msg