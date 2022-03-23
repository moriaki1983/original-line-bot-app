# coding: utf-8




#ユーザーから送られるLINEメッセージの解析結果を基に、自然でかつ適切な返信メッセージを生成する
def text_generate_from_analyze_result(line_msg_anlyz_rslt):
    if   line_msg_anlyz_rslt == "(称賛＆礼賛)":
         txt_gnrt_from_anlyz_rslt = "ありがとうございます"
    elif line_msg_anlyz_rslt == "(モノマネ＆ギャグ＆一発芸)(人物・キャラクターに基づいて)":
         txt_gnrt_from_anlyz_rslt = "それはギャグですか？"
    else:
       txt_gnrt_from_anlyz_rslt = line_msg_anlyz_rslt
    return txt_gnrt_from_anlyz_rslt