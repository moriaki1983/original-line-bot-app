import re
from janome.tokenizer import Tokenizer




#ユーザーから送られるLINEメッセージの中に含まれる記号を除去する
def remove_symbol(line_msg_txt):
    #メッセージの中に含まれる日本語固有の記号を除去する
    rmv_symbl_rslt = re.sub("(「)", "", line_msg_txt)
    rmv_symbl_rslt = re.sub("(」)", "", rmv_symbl_rslt)
    rmv_symbl_rslt = re.sub("(、)", "", rmv_symbl_rslt)
    rmv_symbl_rslt = re.sub("(。)", "", rmv_symbl_rslt)
    rmv_symbl_rslt = re.sub("(？)", "", rmv_symbl_rslt)
    rmv_symbl_rslt = re.sub("(！)", "", rmv_symbl_rslt)

    #メッセージの中に含まれる英語固有の記号を除去する
    rmv_symbl_rslt = re.sub("(,)", "", rmv_symbl_rslt)
    rmv_symbl_rslt = re.sub("(.)", "", rmv_symbl_rslt)
    #rmv_symbl_rslt = re.sub("(?)", "", rmv_symbl_rslt)
    #rmv_symbl_rslt = re.sub("(!)", "", rmv_symbl_rslt)

    #メッセージの中に含まれる先頭と末尾の空白と改行を除去する
    #rmv_symbl_rslt = rmv_symbl_rslt.strip()
    return rmv_symbl_rslt


#ユーザーから送られるLINEメッセージが指定された文字列で開始するかを判定する
def check_text_start_string(line_msg_txt, str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で開始するかを判定する
    rmv_symbl_rslt = remove_symbol(line_msg_txt)
    if str in rmv_symbl_rslt:
       chk_txt_strt_str_rslt = rmv_symbl_rslt.startswith(str)
    else:
       chk_txt_strt_str = False
    return chk_txt_strt_str_rslt


#ユーザーから送られるLINEメッセージが指定された文字列で終結するかを判定する
def check_text_terminated_string(line_msg_txt, str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で終結するかを判定する
    rmv_symbl_rslt          = remove_symbol(line_msg_txt)
    chk_txt_trmntd_str_rslt = rmv_symbl_rslt.endswith(str)
    return chk_txt_trmntd_str_rslt


#ユーザーから送られるLINEメッセージをJanomeで形態素解析する(見出しのみをリストにして出力する)
def line_msg_morpho_analyze(line_msg_txt):
    #メッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr   = Tokenizer()
    tkns    = tknzr.tokenize(line_msg_txt)

    #分解後のメッセージをリストに格納して呼出し元に引渡しをする
    anlyz_rslt = []
    for tkn in tkns:
        anlyz_rslt.append(tkn.surface)
    return anlyz_rslt


#ユーザーから送られるLINEメッセージをJanomeで形態素解析する(見出しと品詞のセットをリストにして出力する)
def line_msg_morpho_analyze2(line_msg_txt):
    #メッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr = Tokenizer()
    tkns  = tknzr.tokenize(line_msg_txt)

    #分解後のメッセージをリストに格納して呼出し元に引渡しをする
    anlyz2_rslt = []
    for tkn in tkns:
        anlyz2_rslt.append([tkn.surface, tkn.part_of_speech])
    return (anlyz2_rslt)


#LINEメッセージが短文＆定型文だったとして、これからインテント(＝意図するもの)を抽出する
def extract_intent_from_short_and_boilerplate(line_msg_txt):
    #メッセージの中に含まれる記号を除去して、短文＆定型文となっているメッセージからインテントを抽出して、これを呼出し元に引渡しをする
    rmv_symbl_rslt = remove_symbol(line_msg_txt)
    #rmv_symbl_rslt = line_msg_txt
    if   (rmv_symbl_rslt == "おはよう" or
          rmv_symbl_rslt == "こんにちは" or
          rmv_symbl_rslt == "こんばんは" or
          rmv_symbl_rslt == "やあ" or
          rmv_symbl_rslt == "どうも"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "挨拶"
    elif (rmv_symbl_rslt == "さすがですね" or
          rmv_symbl_rslt == "さすが" or
          rmv_symbl_rslt == "素晴らしい" or
          rmv_symbl_rslt == "すばらしい"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "称賛"
    elif (rmv_symbl_rslt == "最低" or
          rmv_symbl_rslt == "バカ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "罵倒"
    elif (rmv_symbl_rslt == "天才ですか" or
          rmv_symbl_rslt == "秀才ですか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "称賛(半疑問)"
    elif (rmv_symbl_rslt == "バカですか" or
          rmv_symbl_rslt == "アホですか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "罵倒(半疑問)"
    elif (rmv_symbl_rslt == "何をしますか" or
          rmv_symbl_rslt == "どうしますか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(意図＆目的)(現在)"
    elif (rmv_symbl_rslt == "何をしていますか" or
          rmv_symbl_rslt == "どうしていますか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(意図＆目的)(現在進行)"
    elif (rmv_symbl_rslt == "何をしてきましたか" or
          rmv_symbl_rslt == "どうしてきましたか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(意図＆目的)(過去)"
    elif (rmv_symbl_rslt == "何をしていきたいですか" or
          rmv_symbl_rslt == "どうしていきたいですか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(意図＆目的)(未来)"
    elif (rmv_symbl_rslt == "いいですよ" or
          rmv_symbl_rslt == "いいよ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "許可"
    elif (rmv_symbl_rslt == "おい" or
          rmv_symbl_rslt == "ねぇ" or
          rmv_symbl_rslt == "なぁ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "呼掛け"
    elif rmv_symbl_rslt == "海":
            extrct_intnt_frm_shrt_and_blrplt_rslt = "掛合い"
    else:
         extrct_intnt_frm_shrt_and_blrplt_rslt = "その他・不明"
    return extrct_intnt_frm_shrt_and_blrplt_rslt


#LINEメッセージの末尾部分からインテント(＝意図するもの)を抽出する
def extract_intent_from_endnotes(line_msg_txt):
    #メッセージの中に含まれる記号を除去して、メッセージの末尾部分からインテントを抽出して、これを呼出し元に引渡しをする
    rmv_symbl_rslt = remove_symbol(line_msg_txt)
    if   check_text_terminated_string(rmv_symbl_rslt, "する"):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在＆肯定)"
    elif check_text_terminated_string(rmv_symbl_rslt, "しない"):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在＆否定)"
    elif check_text_terminated_string(rmv_symbl_rslt, "している"):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在進行＆肯定)"
    elif check_text_terminated_string(rmv_symbl_rslt, "してる"):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在進行＆肯定)"
    elif check_text_terminated_string(rmv_symbl_rslt, "しています"):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在進行＆肯定)"
    elif check_text_terminated_string(rmv_symbl_rslt, "してます"):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在進行＆肯定)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "していない") or
          check_text_terminated_string(rmv_symbl_rslt, "してない") or
          check_text_terminated_string(rmv_symbl_rslt, "していません") or
          check_text_terminated_string(rmv_symbl_rslt, "してません")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在進行＆否定)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "できている") or
          check_text_terminated_string(rmv_symbl_rslt, "できてる")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在進行＆可能＆肯定)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "できていない") or
          check_text_terminated_string(rmv_symbl_rslt, "できてない") or
          check_text_terminated_string(rmv_symbl_rslt, "できていません") or
          check_text_terminated_string(rmv_symbl_rslt, "できてません")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在進行＆可能＆否定)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "できました") or
          check_text_terminated_string(rmv_symbl_rslt, "できた")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(過去＆可能＝完了)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "できていません") or
          check_text_terminated_string(rmv_symbl_rslt, "できてません") or
          check_text_terminated_string(rmv_symbl_rslt, "できてない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(過去＆不可能＝未完了)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "できます") or
          check_text_terminated_string(rmv_symbl_rslt, "できると思います") or
          check_text_terminated_string(rmv_symbl_rslt, "できると思う")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在＆可能)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "できません") or
          check_text_terminated_string(rmv_symbl_rslt, "できない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在＆不可能)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "しよう") or
          check_text_terminated_string(rmv_symbl_rslt, "しようと思います") or
          check_text_terminated_string(rmv_symbl_rslt, "しようと思う")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(未来＆肯定)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "しない") or
          check_text_terminated_string(rmv_symbl_rslt, "しないと思う")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(未来＆否定)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "しました") or
          check_text_terminated_string(rmv_symbl_rslt, "した")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(過去＆肯定)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "していません") or
          check_text_terminated_string(rmv_symbl_rslt, "してません") or
          check_text_terminated_string(rmv_symbl_rslt, "してない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(過去＆否定)"
    elif (check_text_terminated_string(rmv_symbl_rslt, "です") or
          check_text_terminated_string(rmv_symbl_rslt, "でした")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "紹介＆説明＆提示"
    elif (check_text_terminated_string(rmv_symbl_rslt, "でしょうか") or
          check_text_terminated_string(rmv_symbl_rslt, "ですか")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "疑義＆質問"
    elif (check_text_terminated_string(rmv_symbl_rslt, "しませんか") or
          check_text_terminated_string(rmv_symbl_rslt, "しません")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "誘導＆勧誘"
    elif (check_text_terminated_string(rmv_symbl_rslt, "したいな") or
          check_text_terminated_string(rmv_symbl_rslt, "したい") or
          check_text_terminated_string(rmv_symbl_rslt, "やりたいな") or
          check_text_terminated_string(rmv_symbl_rslt, "やりたい")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "欲求＆欲動"
    elif (check_text_terminated_string(rmv_symbl_rslt, "いいですよ") or
          check_text_terminated_string(rmv_symbl_rslt, "いいよ")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "許可＆認可" 
    elif (check_text_terminated_string(rmv_symbl_rslt, "しないように") or
          check_text_terminated_string(rmv_symbl_rslt, "しないよう") or
          check_text_terminated_string(rmv_symbl_rslt, "するなよ") or
          check_text_terminated_string(rmv_symbl_rslt, "するな")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "制止＆禁止"
    elif (check_text_terminated_string(rmv_symbl_rslt, "してください") or
          check_text_terminated_string(rmv_symbl_rslt, "して")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "依頼"
    elif (check_text_terminated_string(rmv_symbl_rslt, "しなさい") or
          check_text_terminated_string(rmv_symbl_rslt, "しろ")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "命令"
    else:
           extrct_intnt_frm_shrt_and_blrplt_rslt = "その他・不明"
    return extrct_intnt_frm_shrt_and_blrplt_rslt


#LINEメッセージの先頭・中間部分からコンテント(＝意図されるもの)を抽出する
def extract_content_from_top_and_middle(line_msg_txt):
    #メッセージの中に含まれる記号を除去して、メッセージの先頭・中間部分部分からコンテントを抽出して、これを呼出し元に引渡しをする
    rmv_symbl_rslt = remove_symbol(line_msg_txt)
    if   check_text_terminated_string(rmv_symbl_rslt, "する"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(する)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しない)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "している"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(している)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "してる"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(してる)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しています"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しています)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "してます"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(してます)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "していない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(していない)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "してない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(してない)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "していません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(していません)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "してません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(してません)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できている"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できている)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できてる"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できてる)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できていない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できていない)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できてない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できてない)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できていません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できていません)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できてません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できてません)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できました"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できました)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できた"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できた)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できていません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できていません)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できてません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(してます)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できてない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できてない)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できます"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できます)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できると思います"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できると思います)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できると思う"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できると思う)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できません)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "できない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(できない)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しよう"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しよう)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しようと思います"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しようと思います)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しようと思う"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しようと思う)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しない)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しないと思う"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しないと思う)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しました"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しました)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "した"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(した)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "していません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(していません)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "してません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(してません)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "してない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(してない)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "です"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(です)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "でした"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(でした)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "でしょうか"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(でしょうか)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "ですか"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(ですか)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しませんか"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しませんか)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しません"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しません)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "したいな"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(したいな)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "したい"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(したい)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "やりたいな"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(やりたいな)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "やりたい"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(やりたい)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しないように"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しないように)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しないよう"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しないよう)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "するなよ"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(するなよ)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "するな"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(するな)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "してください"):
          extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(してください)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "して"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(して)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しなさい"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しなさい)", "", rmv_symbl_rslt)
    elif check_text_terminated_string(rmv_symbl_rslt, "しろ"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しろ)", "", rmv_symbl_rslt)
    else:
           extrct_cntnt_frm_tp_and_mddl_rslt = rmv_symbl_rslt
    return extrct_cntnt_frm_tp_and_mddl_rslt


#LINEの返信メッセージをインテントとコンテントから生成する
def line_msg_generate_from_intent_and_content(intnt, cntnt):
    #返信メッセージをインテントとコンテントから生成して、これを呼出し元に引渡しをする
    line_msg_gnrt_frm_intnt_and_cntnt_rslt = "test"
    return line_msg_gnrt_frm_intnt_and_cntnt_rslt
