# coding: utf-8




import random




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(crrnt_line_rcd_lst, prv_line_rcd_lst):
    #ユーザーの発話の流れを示す変数を宣言・定義する
    flw_of_uttrnc = prv_line_rcd_lst[0][3] + prv_line_rcd_lst[1][3] + \
                    prv_line_rcd_lst[2][3] + prv_line_rcd_lst[3][3] + crrnt_line_rcd_lst[3]

    #ユーザーの発話の流れに沿った返信メッセージを生成する
    if flw_of_uttrnc == "<称賛＆礼賛>":
       gnrtd_msg_cnddt = ["ありがとうございます", "嬉しいです"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまた～ お上手ですね", "褒められるとテレます"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまたまた～", "そう言われても何も出ませんよ 笑"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまたまた～", "そう言われても何も出ませんよ 笑"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまたまた～", "もうしょうがないな～ 付き合ってあげますよ 笑"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<卑猥な言動 辱め>":
       gnrtd_msg_cnddt = ["やめてください", "/ω＼)ｲﾔﾝ", "いやらしいですよね"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<卑猥な言動 辱め><卑猥な言動 辱め>":
       gnrtd_msg_cnddt = ["もうええわ", "そんなこと言ってると 女性に嫌われますよ"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg

    gnrtd_msg = "また おしゃべりしましょう♪"
    return gnrtd_msg