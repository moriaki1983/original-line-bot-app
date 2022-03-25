# coding: utf-8




import random




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_msg_txt, line_msg_intnt, prv_msgrcd_lst):
    #
    flw_of_uttrnc = prv_msgrcd_lst[0][2] + prv_msgrcd_lst[1][2] + \
                    prv_msgrcd_lst[2][2] + prv_msgrcd_lst[3][2] + line_msg_intnt
    #
    if flw_of_uttrnc == "称賛＆礼賛":
       rply_msg_cnddt = ["ありがとうございます", "嬉しいです", "あなたが好きです"]
       rply_msg = random.choice(rply_msg_cnddt)
       cmpltn_flg = False
       return rply_msg, cmpltn_flg
    if flw_of_uttrnc == "称賛＆礼賛":
       rply_msg_cnddt = ["ありがとうございます", "嬉しいです", "あなたが好きです"]
       rply_msg = random.choice(rply_msg_cnddt)
       cmpltn_flg = False
       return rply_msg, cmpltn_flg
    if flw_of_uttrnc == "称賛＆礼賛称賛＆礼賛":
       rply_msg_cnddt = ["またまた～ お上手ですね", "そう言われても何も出ませんよ"]
       rply_msg = random.choice(rply_msg_cnddt)
       cmpltn_flg = True
       return rply_msg, cmpltn_flg
    if flw_of_uttrnc == "辱め 卑猥な言動":
       rply_msg_cnddt = ["やめてください", "/ω＼)ｲﾔﾝ"]
       rply_msg = random.choice(rply_msg_cnddt)
       cmpltn_flg = False
       return rply_msg, cmpltn_flg
    if flw_of_uttrnc == "辱め 卑猥な言動辱め 卑猥な言動":
       rply_msg_cnddt = ["もうええわ", "そんなこと言ってると 女性に嫌われますよ"]
       rply_msg = random.choice(rply_msg_cnddt)
       cmpltn_flg = True
       return rply_msg, cmpltn_flg

    rply_msg = "また おしゃべりしましょう♪"
    cmpltn_flg = True
    return rply_msg, cmpltn_flg