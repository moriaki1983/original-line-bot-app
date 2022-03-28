# coding: utf-8




import random




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(crrnt_msgrcd_lst, prv_msgrcd_lst):
    #ユーザーの発話の流れを示す変数を宣言・定義する
    flw_of_uttrnc = prv_msgrcd_lst[0][2] + prv_msgrcd_lst[1][2] + \
                    prv_msgrcd_lst[2][2] + prv_msgrcd_lst[3][2] + crrnt_msgrcd_lst[2]

    #ユーザーの発話の流れに沿った返信メッセージを生成する
    if flw_of_uttrnc == "<称賛＆礼賛>":
       gnrtd_msg_cnddt = [crrnt_msgrcd_lst[0] + "さん" + " " + "ありがとうございます", "嬉しいです"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = [crrnt_msgrcd_lst[0] + "さん" + " " + "またまた～ お上手ですね", "褒められるとテレます"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = [crrnt_msgrcd_lst[0] + "さん" + " " + "またまたまた～", "そう言われても何も出ませんよ 笑"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまたまた～", crrnt_msgrcd_lst[0] + "さん" + " " + "そう言われても何も出ませんよ 笑"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       gnrtd_msg_cnddt = ["またまたまた～", crrnt_msgrcd_lst[0] + "さん" + " " + "もうしょうがないな～ 付き合ってあげますよ 笑"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<卑猥な言動 辱め>":
       gnrtd_msg_cnddt = ["やめてください", "/ω＼)ｲﾔﾝ", crrnt_msgrcd_lst[0] + "さん" + " " + "いやらしいですよね"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg
    if flw_of_uttrnc == "<卑猥な言動 辱め><卑猥な言動 辱め>":
       gnrtd_msg_cnddt = ["もうええわ", crrnt_msgrcd_lst[0] + "さん" + " " + "そんなこと言ってると 女性に嫌われますよ"]
       gnrtd_msg = random.choice(gnrtd_msg_cnddt)
       return gnrtd_msg

    gnrtd_msg = "また おしゃべりしましょう♪"
    return gnrtd_msg