# coding: utf-8




import random




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_msg_anlyz_rslt, lsttm_intnt):
    flw_of_uttrnc = line_msg_anlyz_rslt + "→" + lsttm_intnt
    if   flw_of_uttrnc == "(称賛＆礼賛)→":
         rply_msg_lst = ["ありがとうございます", "嬉しいです", "あなたが好きです"]
         txt_gnrt_from_anlyz_rslt = random.choice(rply_msg_lst)
         cmpltn_flg = False
    elif flw_of_uttrnc == "(称賛＆礼賛)→(称賛＆礼賛)":
         rply_msg_lst = ["またまた～ お上手ですね", "そう言われても何も出ませんよ"]
         txt_gnrt_from_anlyz_rslt = random.choice(rply_msg_lst)
         cmpltn_flg = True
    elif flw_of_uttrnc == "(辱め)(卑猥な言動)→":
         rply_msg_lst = ["やめてください", "(/ω＼)ｲﾔﾝ"]
         txt_gnrt_from_anlyz_rslt = random.choice(rply_msg_lst)
         cmpltn_flg = False
    elif flw_of_uttrnc == "(辱め)(卑猥な言動)→(辱め)(卑猥な言動)":
         rply_msg_lst = ["もうええわ", "そんなこと言ってると 女性に嫌われますよ"]
         txt_gnrt_from_anlyz_rslt = random.choice(rply_msg_lst)
         cmpltn_flg = True
    else:
         txt_gnrt_from_anlyz_rslt = "また おしゃべりしましょう♪"
         cmpltn_flg = True
    return txt_gnrt_from_anlyz_rslt, cmpltn_flg