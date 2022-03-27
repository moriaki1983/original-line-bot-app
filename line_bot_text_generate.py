# coding: utf-8




import random




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_usr_nm, crrnt_msgrcd_lst, prv_msgrcd_lst):
    #ユーザーの発話の流れを示す変数を宣言・定義する
    flw_of_uttrnc = prv_msgrcd_lst[0][2] + prv_msgrcd_lst[1][2] + \
                    prv_msgrcd_lst[2][2] + prv_msgrcd_lst[3][2] + crrnt_msgrcd_lst[2]

    #ユーザーの発話の流れに沿った返信メッセージを生成する
    if flw_of_uttrnc == "<称賛＆礼賛>":
       rply_msg_cnddt = [line_usr_nm + "さん" + " " + "ありがとうございます", "嬉しいです"]
       rply_msg = random.choice(rply_msg_cnddt)
       return rply_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛>":
       rply_msg_cnddt = [line_usr_nm + "さん" + " " + "またまた～ お上手ですね", "褒められるとテレます"]
       rply_msg = random.choice(rply_msg_cnddt)
       return rply_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       rply_msg_cnddt = [line_usr_nm + "さん" + " " + "またまたまた～", "そう言われても何も出ませんよ 笑"]
       rply_msg = random.choice(rply_msg_cnddt)
       return rply_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       rply_msg_cnddt = ["またまたまた～", line_usr_nm + "さん" + " " + "そう言われても何も出ませんよ 笑"]
       rply_msg = random.choice(rply_msg_cnddt)
       return rply_msg
    if flw_of_uttrnc == "<称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛><称賛＆礼賛>":
       rply_msg_cnddt = ["またまたまた～", line_usr_nm + "さん" + " " + "もうしょうがないな～ 付き合ってあげますよ 笑"]
       rply_msg = random.choice(rply_msg_cnddt)
       return rply_msg
    if flw_of_uttrnc == "<卑猥な言動 辱め>":
       rply_msg_cnddt = ["やめてください", "/ω＼)ｲﾔﾝ", line_usr_nm + "さん" + " " + "いやらしいですよね"]
       rply_msg = random.choice(rply_msg_cnddt)
       return rply_msg
    if flw_of_uttrnc == "<卑猥な言動 辱め><卑猥な言動 辱め>":
       rply_msg_cnddt = ["もうええわ", line_usr_nm + "さん" + " " + "そんなこと言ってると 女性に嫌われますよ"]
       rply_msg = random.choice(rply_msg_cnddt)
       return rply_msg

    rply_msg = "また おしゃべりしましょう♪"
    return rply_msg