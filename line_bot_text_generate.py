# coding: utf-8




import random
from line_bot_character import BotCharacter




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_rcds):
    #ユーザーの発話の流れを示す変数を宣言・定義する
    flw_of_uttrnc = line_rcds[0][3] + line_rcds[1][3] + line_rcds[2][3] + line_rcds[3][3] + line_rcds[4][3]

    #ユーザーの発話の流れに沿った返信メッセージを生成する
    if flw_of_uttrnc == "<称賛＆礼賛>":
       if  BotCharacter.get_mind() >= 0:
           gnrtd_msg_cnddt = ["ありがとうございます", "嬉しいです"]
           gnrtd_msg = random.choice(gnrtd_msg_cnddt)
           BotCharacter.add_mind(50)
       if (BotCharacter.get_mind() >= 100):
           gnrtd_msg_cnddt = ["大好きです", "スキ"]
           gnrtd_msg = random.choice(gnrtd_msg_cnddt)
           BotCharacter.set_mind(0)
        return gnrtd_msg
    if flw_of_uttrnc == "<卑猥な言動 辱め>":
       if BotCharacter.get_mind() < 0:
          gnrtd_msg_cnddt = ["やめてください", "/ω＼)ｲﾔﾝ", "いやらしいですよね"]
          gnrtd_msg = random.choice(gnrtd_msg_cnddt)
          BotCharacter.sub_mind(50)
       if BotCharacter.get_mind() <= -50:
          gnrtd_msg_cnddt = ["もうエエわ", "そんなこと言ってると 女性に嫌われますよ"]
          gnrtd_msg = random.choice(gnrtd_msg_cnddt)
          BotCharacter.set_mind(0)
        return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまた～ お上手ですね", "褒められるとテレます 照"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまたまた～", "そう言われても何も出ませんよ 笑"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまたまた～", "もういいですって 笑"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまたまた～", "もうしょうがないな～ 付き合ってあげますよ 笑"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg

    gnrtd_msg = "また おしゃべりしましょう♪"
    return gnrtd_msg