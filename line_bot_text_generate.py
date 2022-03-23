# coding: utf-8




import random




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_msg_anlyz_rslt, lsttm_intnt):
    flw_of_uttrnc = line_msg_anlyz_rslt + "→" + lsttm_intnt
    if   flw_of_uttrnc == "(称賛＆礼賛)→":
         rply_msg_lst = ["ありがとうございます", "嬉しいです", "あなたが好きです"]
         txt_gnrt_from_anlyz_rslt = random.choice(rply_msg_lst)
         cmpltn_flg = True
    elif flw_of_uttrnc == "(称賛＆礼賛)→(称賛＆礼賛)":
         rply_msg_lst = ["またまた～ お上手ですね", "そう言われても何も出ませんよ 笑"]
         txt_gnrt_from_anlyz_rslt = random.choice(rply_msg_lst)
         cmpltn_flg = True
    elif flw_of_uttrnc == "(モノマネ＆ギャグ＆一発芸)(人物・キャラクターに基づいて)→":
         rply_msg_lst = ["それはギャグですか？", "面白いです", "楽しませてくれてありがとう"]
         txt_gnrt_from_anlyz_rslt = random.choice(rply_msg_lst)
         cmpltn_flg = True
    else:
       txt_gnrt_from_anlyz_rslt = "既存フロウに該当しない"
       cmpltn_flg = False
    return txt_gnrt_from_anlyz_rslt, cmpltn_flg


#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result2(line_msg_anlyz_rslt):
    if   line_msg_anlyz_rslt == "(称賛＆礼賛)":
         rply_msg_lst = ["ありがとうございます", "嬉しいです", "あなたが好きです"]
         txt_gnrt_from_anlyz_rslt = random.choice(rply_msg_lst)
    elif line_msg_anlyz_rslt == "(モノマネ＆ギャグ＆一発芸)(人物・キャラクターに基づいて)":
         rply_msg_lst = ["それはギャグですか？", "面白いです", "楽しませてくれてありがとう"]
         txt_gnrt_from_anlyz_rslt = random.choice(rply_msg_lst)
    else:
       txt_gnrt_from_anlyz_rslt = line_msg_anlyz_rslt
    return txt_gnrt_from_anlyz_rslt