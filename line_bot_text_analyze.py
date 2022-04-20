# coding: utf-8




import re
from janome.tokenizer import Tokenizer




#ユーザーから送られるLINEメッセージが指定された文字列で開始するかを判定する
def check_text_start_string(line_msg, pttrn_str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で開始するかを判定する
    rmvd_symbl_msg = remove_symbol(line_msg)
    is_strt        = rmvd_symbl_msg.startswith(pttrn_str)
    return is_strt


#ユーザーから送られるLINEメッセージが指定された文字列で終結するかを判定する
def check_text_terminate_string(line_msg, pttrn_str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で終結するかを判定する
    rmvd_symbl_msg = remove_symbol(line_msg)
    is_trmnt       = rmvd_symbl_msg.endswith(pttrn_str)
    return is_trmnt


#ユーザーから送られるLINEメッセージをJanomeで形態素解析する(見出しのみをリストにして出力する)
def line_msg_morpho_analyze(line_msg):
    #メッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr = Tokenizer()
    tkns  = tknzr.tokenize(line_msg)

    #分解後のメッセージをリストに格納して、これを呼出し元に引渡しをする
    anlyzd_msg = []
    for tkn in tkns:
        anlyzd_msg.append(tkn.surface)
    return anlyzd_msg


#ユーザーから送られるLINEメッセージをJanomeで形態素解析する(見出しと品詞のセットをリストにして出力する)
def line_msg_morpho_analyze2(line_msg):
    #メッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr = Tokenizer()
    tkns  = tknzr.tokenize(line_msg)

    #分解後のメッセージをリストに格納して、これを呼出し元に引渡しをする
    anlyzd_msg = []
    for tkn in tkns:
        anlyzd_msg.append([tkn.surface, tkn.part_of_speech])
    return anlyzd_msg


#ユーザーから送られるLINEメッセージの中に含まれるその他のもの(＝感情表現のためのもの)を除去する
def remove_etc(line_msg):
    #メッセージの中に含まれるその他のものを除去する
    if   bool(re.search(r"怒$",      line_msg)) == True:
         rmvd_etc = re.sub(r"怒$",      "", line_msg)
    elif bool(re.search(r"泣$",      line_msg)) == True:
         rmvd_etc = re.sub(r"泣$",      "", line_msg)
    elif bool(re.search(r"汗$",      line_msg)) == True:
         rmvd_etc = re.sub(r"汗$",      "", line_msg)
    elif bool(re.search(r"爆$",      line_msg)) == True:
         rmvd_etc = re.sub(r"爆$",     "", line_msg)
    elif bool(re.search(r"(爆笑)$",  line_msg)) == True:
         rmvd_etc = re.sub(r"(爆笑)$", "", line_msg)
    elif bool(re.search(r"笑+$",     line_msg)) == True:
         rmvd_etc = re.sub(r"笑+$",     "", line_msg)
    elif bool(re.search(r"(わら)+$", line_msg)) == True:
         rmvd_etc = re.sub(r"(わら)+$", "", line_msg)
    elif bool(re.search(r"(ワラ)+$", line_msg)) == True:
         rmvd_etc = re.sub(r"(ワラ)+$", "", line_msg)
    elif bool(re.search(r"草+$",     line_msg)) == True:
         rmvd_etc = re.sub(r"草+$",     "", line_msg)
    elif bool(re.search(r"(くさ)+$", line_msg)) == True:
         rmvd_etc = re.sub(r"(くさ)+$", "", line_msg)
    elif bool(re.search(r"(クサ)+$", line_msg)) == True:
         rmvd_etc = re.sub(r"(クサ)+$", "", line_msg)
    elif bool(re.search(r"w+$",      line_msg)) == True:
         rmvd_etc = re.sub(r"w+$",      "", line_msg)
    elif bool(re.search(r"W+$",      line_msg)) == True:
         rmvd_etc = re.sub(r"W+$",      "", line_msg)
    else:
         rmvd_etc = line_msg
    return rmvd_etc


#ユーザーから送られるLINEメッセージの中に含まれる記号を除去する
def remove_symbol(line_msg):
    #メッセージの中に含まれる各種の記号・空白を除去する
    rmvd_symbl_msg   = re.sub("(’)", "", line_msg)
    rmvd_symbl_msg2  = re.sub("(”)", "", rmvd_symbl_msg)
    rmvd_symbl_msg3  = re.sub("(「)", "", rmvd_symbl_msg2)
    rmvd_symbl_msg4  = re.sub("(」)", "", rmvd_symbl_msg3)
    rmvd_symbl_msg5  = re.sub("(、)", "", rmvd_symbl_msg4)
    rmvd_symbl_msg6  = re.sub("(。)", "", rmvd_symbl_msg5)
    rmvd_symbl_msg7  = re.sub("(！)", "", rmvd_symbl_msg6)
    rmvd_symbl_msg8  = re.sub("(？)", "", rmvd_symbl_msg7)
    rmvd_symbl_msg9  = re.sub("(♪)", "", rmvd_symbl_msg8)
    rmvd_symbl_msg10 = re.sub("(ー)", "", rmvd_symbl_msg9)
    rmvd_symbl_msg11 = re.sub("(～)", "", rmvd_symbl_msg10)
    rmvd_symbl_msg12 = re.sub("(・)", "", rmvd_symbl_msg11)
    rmvd_symbl_msg13 = re.sub("(＝)", "", rmvd_symbl_msg12)
    rmvd_symbl_msg14 = re.sub("(＆)", "", rmvd_symbl_msg13)
    rmvd_symbl_msg15 = re.sub("(＋)", "", rmvd_symbl_msg14)
    rmvd_symbl_msg16 = re.sub("(　)", "", rmvd_symbl_msg15)
    rmvd_symbl_msg17 = re.sub("(\')", "", rmvd_symbl_msg16)
    rmvd_symbl_msg18 = re.sub("(\")", "", rmvd_symbl_msg17)
    rmvd_symbl_msg19 = re.sub("(\[)", "", rmvd_symbl_msg18)
    rmvd_symbl_msg20 = re.sub("(\])", "", rmvd_symbl_msg19)
    rmvd_symbl_msg21 = re.sub("(\,)", "", rmvd_symbl_msg20)
    rmvd_symbl_msg22 = re.sub("(\.)", "", rmvd_symbl_msg21)
    rmvd_symbl_msg23 = re.sub("(\!)", "", rmvd_symbl_msg22)
    rmvd_symbl_msg24 = re.sub("(\?)", "", rmvd_symbl_msg23)
    rmvd_symbl_msg25 = re.sub("(\=)", "", rmvd_symbl_msg24)
    rmvd_symbl_msg26 = re.sub("(\&)", "", rmvd_symbl_msg25)
    rmvd_symbl_msg27 = re.sub("(\+)", "", rmvd_symbl_msg26)
    rmvd_symbl_msg28 = re.sub("( )",  "", rmvd_symbl_msg27)
    return rmvd_symbl_msg28


#ユーザーから送られるLINEメッセージの中に含まれる終助詞を除去する
def remove_endparticle(line_msg):
    #メッセージの中に含まれる終助詞を除去する
    if   bool(re.search(r"よお$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"よお$", "", line_msg)
    elif bool(re.search(r"よぉ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"よぉ$", "", line_msg)
    elif bool(re.search(r"よっ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"よっ$", "", line_msg)
    elif bool(re.search(r"よ$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"よ$",   "", line_msg)
    elif bool(re.search(r"ねえ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"ねえ$", "", line_msg)
    elif bool(re.search(r"ねぇ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"ねぇ$", "", line_msg)
    elif bool(re.search(r"ねっ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"ねっ$", "", line_msg)
    elif bool(re.search(r"ね$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"ね$",   "", line_msg)
    elif bool(re.search(r"なあ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"なあ$", "", line_msg)
    elif bool(re.search(r"なぁ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"なぁ$", "", line_msg)
    elif bool(re.search(r"なっ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"なっ$", "", line_msg)
    elif bool(re.search(r"な$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"な$",   "", line_msg)
    elif bool(re.search(r"わあ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"わあ$", "", line_msg)
    elif bool(re.search(r"わぁ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"わぁ$",   "", line_msg)
    elif bool(re.search(r"わっ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"わっ$",   "", line_msg)
    elif bool(re.search(r"わ$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"わ$",     "", line_msg)
    elif bool(re.search(r"ぜえ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"ぜえ$",   "", line_msg)
    elif bool(re.search(r"ぜぇ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"ぜぇ$",   "", line_msg)
    elif bool(re.search(r"ぜっ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"ぜっ$",   "", line_msg)
    elif bool(re.search(r"ぜ$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"ぜ$",       "", line_msg)
    elif bool(re.search(r"っすよ$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"っすよ$",   "", line_msg)
    elif bool(re.search(r"っすね$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"っすね$",   "", line_msg)
    elif bool(re.search(r"でっす$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"でっす$",   "", line_msg)
    elif bool(re.search(r"っす$", line_msg))     == True:
         rmvd_edprtcl_msg = re.sub(r"っす$",     "", line_msg)
    elif bool(re.search(r"わよ$", line_msg))     == True:
         rmvd_edprtcl_msg = re.sub(r"わよ$",     "", line_msg)
    elif bool(re.search(r"わよっ$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"わよっ$",   "", line_msg)
    elif bool(re.search(r"わね$", line_msg))     ==   True:
         rmvd_edprtcl_msg = re.sub(r"わね$",     "", line_msg)
    elif bool(re.search(r"わねっ$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"わねっ$",   "", line_msg)
    elif bool(re.search(r"ってね$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"ってね$",   "", line_msg)
    elif bool(re.search(r"ってば$", line_msg))   == True:
         rmvd_edprtcl_msg = re.sub(r"ってば$",   "", line_msg)
    elif bool(re.search(r"ってばよ$", line_msg)) == True:
         rmvd_edprtcl_msg = re.sub(r"ってばよ$", "", line_msg)
    elif bool(re.search(r"っ$", line_msg))       == True:
         rmvd_edprtcl_msg = re.sub(r"っ$",       "", line_msg)
    elif bool(re.search(r"から$", line_msg))     == True:
         rmvd_edprtcl_msg = re.sub(r"から$",     "", line_msg)
    else:
         rmvd_edprtcl_msg = line_msg
    return rmvd_edprtcl_msg


#ユーザーから送られるLINEメッセージの中に含まれるインテント(＝意図するもの)を除去する
def remove_intent(line_msg):
    #メッセージの中に含まれる日本語固有のインテントの削除候補をリストアップする
    intnt_rmv_cnddts = []
    if   check_text_terminate_string(line_msg, "を行います"):
         intnt_rmv_cnddts.append("を行います")
    elif check_text_terminate_string(line_msg, "を行う"):
         intnt_rmv_cnddts.append("を行う")
    elif check_text_terminate_string(line_msg, "をします"):
         intnt_rmv_cnddts.append("をします")
    elif check_text_terminate_string(line_msg, "をする"):
         intnt_rmv_cnddts.append("をする")
    elif check_text_terminate_string(line_msg, "はします"):
         intnt_rmv_cnddts.append("はします")
    elif check_text_terminate_string(line_msg, "はする"):
         intnt_rmv_cnddts.append("はする")
    elif check_text_terminate_string(line_msg, "します"):
         intnt_rmv_cnddts.append("します")
    elif check_text_terminate_string(line_msg, "する"):
         intnt_rmv_cnddts.append("する")
    elif check_text_terminate_string(line_msg, "を行いません"):
         intnt_rmv_cnddts.append("を行いません")
    elif check_text_terminate_string(line_msg, "を行わない"):
         intnt_rmv_cnddts.append("を行わない")
    elif check_text_terminate_string(line_msg, "をしません"):
         intnt_rmv_cnddts.append("をしません")
    elif check_text_terminate_string(line_msg, "をしない"):
         intnt_rmv_cnddts.append("をしない")
    elif check_text_terminate_string(line_msg, "はしません"):
         intnt_rmv_cnddts.append("はしません")
    elif check_text_terminate_string(line_msg, "はしない"):
         intnt_rmv_cnddts.append("はしない")
    elif check_text_terminate_string(line_msg, "しません"):
         intnt_rmv_cnddts.append("しません")
    elif check_text_terminate_string(line_msg, "しない"):
         intnt_rmv_cnddts.append("しない")
    elif check_text_terminate_string(line_msg, "を行っています"):
         intnt_rmv_cnddts.append("を行っています")
    elif check_text_terminate_string(line_msg, "を行っている"):
         intnt_rmv_cnddts.append("を行っている")
    elif check_text_terminate_string(line_msg, "をしています"):
         intnt_rmv_cnddts.append("をしています")
    elif check_text_terminate_string(line_msg, "をしてます"):
         intnt_rmv_cnddts.append("をしてます")
    elif check_text_terminate_string(line_msg, "をしている"):
         intnt_rmv_cnddts.append("をしている")
    elif check_text_terminate_string(line_msg, "をしてる"):
         intnt_rmv_cnddts.append("をしてる")
    elif check_text_terminate_string(line_msg, "しています"):
         intnt_rmv_cnddts.append("しています")
    elif check_text_terminate_string(line_msg, "してます"):
         intnt_rmv_cnddts.append("してます")
    elif check_text_terminate_string(line_msg, "している"):
         intnt_rmv_cnddts.append("している")
    elif check_text_terminate_string(line_msg, "してる"):
         intnt_rmv_cnddts.append("してる")
    elif check_text_terminate_string(line_msg, "を行っていません"):
         intnt_rmv_cnddts.append("を行っていません")
    elif check_text_terminate_string(line_msg, "を行ってません"):
         intnt_rmv_cnddts.append("を行ってません")
    elif check_text_terminate_string(line_msg, "をしていません"):
         intnt_rmv_cnddts.append("をしていません")
    elif check_text_terminate_string(line_msg, "をしてません"):
         intnt_rmv_cnddts.append("をしてません")
    elif check_text_terminate_string(line_msg, "をしていない"):
         intnt_rmv_cnddts.append("をしていない")
    elif check_text_terminate_string(line_msg, "をしてない"):
         intnt_rmv_cnddts.append("をしてない")
    elif check_text_terminate_string(line_msg, "していません"):
         intnt_rmv_cnddts.append("していません")
    elif check_text_terminate_string(line_msg, "してません"):
         intnt_rmv_cnddts.append("してません")
    elif check_text_terminate_string(line_msg, "していない"):
         intnt_rmv_cnddts.append("していない")
    elif check_text_terminate_string(line_msg, "してない"):
         intnt_rmv_cnddts.append("してない")
    elif check_text_terminate_string(line_msg, "ができています"):
         intnt_rmv_cnddts.append("ができています")
    elif check_text_terminate_string(line_msg, "ができている"):
         intnt_rmv_cnddts.append("ができている")
    elif check_text_terminate_string(line_msg, "ができてる"):
         intnt_rmv_cnddts.append("ができてる")
    elif check_text_terminate_string(line_msg, "できています"):
         intnt_rmv_cnddts.append("できています")
    elif check_text_terminate_string(line_msg, "できている"):
         intnt_rmv_cnddts.append("できている")
    elif check_text_terminate_string(line_msg, "できてる"):
         intnt_rmv_cnddts.append("できてる")
    elif check_text_terminate_string(line_msg, "ができていません"):
         intnt_rmv_cnddts.append("ができていません")
    elif check_text_terminate_string(line_msg, "ができてません"):
         intnt_rmv_cnddts.append("ができてません")
    elif check_text_terminate_string(line_msg, "ができていない"):
         intnt_rmv_cnddts.append("ができていない")
    elif check_text_terminate_string(line_msg, "ができてない"):
         intnt_rmv_cnddts.append("ができてない")
    elif check_text_terminate_string(line_msg, "できていません"):
         intnt_rmv_cnddts.append("できていません")
    elif check_text_terminate_string(line_msg, "できてません"):
         intnt_rmv_cnddts.append("できてません")
    elif check_text_terminate_string(line_msg, "できていない"):
         intnt_rmv_cnddts.append("できていない")
    elif check_text_terminate_string(line_msg, "できてない"):
         intnt_rmv_cnddts.append("できてない")
    elif check_text_terminate_string(line_msg, "ができます"):
         intnt_rmv_cnddts.append("ができます")
    elif check_text_terminate_string(line_msg, "ができる"):
         intnt_rmv_cnddts.append("ができる")
    elif check_text_terminate_string(line_msg, "できます"):
         intnt_rmv_cnddts.append("できます")
    elif check_text_terminate_string(line_msg, "できる"):
         intnt_rmv_cnddts.append("できる")
    elif check_text_terminate_string(line_msg, "ができません"):
         intnt_rmv_cnddts.append("ができません")
    elif check_text_terminate_string(line_msg, "ができない"):
         intnt_rmv_cnddts.append("ができない")
    elif check_text_terminate_string(line_msg, "できません"):
         intnt_rmv_cnddts.append("できません")
    elif check_text_terminate_string(line_msg, "できない"):
         intnt_rmv_cnddts.append("できない")
    elif check_text_terminate_string(line_msg, "をしました"):
         intnt_rmv_cnddts.append("をしました")
    elif check_text_terminate_string(line_msg, "をした"):
         intnt_rmv_cnddts.append("をした")
    elif check_text_terminate_string(line_msg, "はしました"):
         intnt_rmv_cnddts.append("はしました")
    elif check_text_terminate_string(line_msg, "はした"):
         intnt_rmv_cnddts.append("はした")
    elif check_text_terminate_string(line_msg, "しました"):
         intnt_rmv_cnddts.append("しました")
    elif check_text_terminate_string(line_msg, "した"):
         intnt_rmv_cnddts.append("した")
    elif check_text_terminate_string(line_msg, "をやりました"):
         intnt_rmv_cnddts.append("をやりました")
    elif check_text_terminate_string(line_msg, "をやった"):
         intnt_rmv_cnddts.append("をやった")
    elif check_text_terminate_string(line_msg, "はやりました"):
         intnt_rmv_cnddts.append("はやりました")
    elif check_text_terminate_string(line_msg, "はやった"):
         intnt_rmv_cnddts.append("はやった")
    elif check_text_terminate_string(line_msg, "をしていません"):
         intnt_rmv_cnddts.append("をしていません")
    elif check_text_terminate_string(line_msg, "をしてません"):
         intnt_rmv_cnddts.append("をしてません")
    elif check_text_terminate_string(line_msg, "をしてない"):
         intnt_rmv_cnddts.append("をしてない")
    elif check_text_terminate_string(line_msg, "はしていません"):
         intnt_rmv_cnddts.append("はしていません")
    elif check_text_terminate_string(line_msg, "はしてません"):
         intnt_rmv_cnddts.append("はしてません")
    elif check_text_terminate_string(line_msg, "はしてない"):
         intnt_rmv_cnddts.append("はしてない")
    elif check_text_terminate_string(line_msg, "していません"):
         intnt_rmv_cnddts.append("していません")
    elif check_text_terminate_string(line_msg, "してません"):
         intnt_rmv_cnddts.append("してません")
    elif check_text_terminate_string(line_msg, "してない"):
         intnt_rmv_cnddts.append("してない")
    elif check_text_terminate_string(line_msg, "をやってません"):
         intnt_rmv_cnddts.append("をやってません")
    elif check_text_terminate_string(line_msg, "をやってない"):
         intnt_rmv_cnddts.append("をやってない")
    elif check_text_terminate_string(line_msg, "はやってません"):
         intnt_rmv_cnddts.append("はやってません")
    elif check_text_terminate_string(line_msg, "はやってない"):
         intnt_rmv_cnddts.append("はやってない")
    elif check_text_terminate_string(line_msg, "をするのですか"):
         intnt_rmv_cnddts.append("をするのですか")
    elif check_text_terminate_string(line_msg, "をするんですか"):
         intnt_rmv_cnddts.append("をするんですか")
    elif check_text_terminate_string(line_msg, "をしますか"):
         intnt_rmv_cnddts.append("をしますか")
    elif check_text_terminate_string(line_msg, "はするのですか"):
         intnt_rmv_cnddts.append("はするのですか")
    elif check_text_terminate_string(line_msg, "はするんですか"):
         intnt_rmv_cnddts.append("はするんですか")
    elif check_text_terminate_string(line_msg, "はしますか"):
         intnt_rmv_cnddts.append("はしますか")
    elif check_text_terminate_string(line_msg, "するのですか"):
         intnt_rmv_cnddts.append("するのですか")
    elif check_text_terminate_string(line_msg, "するんですか"):
         intnt_rmv_cnddts.append("するんですか")
    elif check_text_terminate_string(line_msg, "しますか"):
         intnt_rmv_cnddts.append("しますか")
    elif check_text_terminate_string(line_msg, "するのか"):
         intnt_rmv_cnddts.append("するのか")
    elif check_text_terminate_string(line_msg, "するか"):
         intnt_rmv_cnddts.append("するか")
    elif check_text_terminate_string(line_msg, "をしないのですか"):
         intnt_rmv_cnddts.append("をしないのですか")
    elif check_text_terminate_string(line_msg, "はしないのですか"):
         intnt_rmv_cnddts.append("はしないのですか")
    elif check_text_terminate_string(line_msg, "をしないんですか"):
         intnt_rmv_cnddts.append("をしないんですか")
    elif check_text_terminate_string(line_msg, "はしないんですか"):
         intnt_rmv_cnddts.append("はしないんですか")
    elif check_text_terminate_string(line_msg, "をしないのか"):
         intnt_rmv_cnddts.append("をしないのか")
    elif check_text_terminate_string(line_msg, "はしないのか"):
         intnt_rmv_cnddts.append("はしないのか")
    elif check_text_terminate_string(line_msg, "しないのですか"):
         intnt_rmv_cnddts.append("しないのですか")
    elif check_text_terminate_string(line_msg, "しないんですか"):
         intnt_rmv_cnddts.append("しないんですか")
    elif check_text_terminate_string(line_msg, "しないのか"):
         intnt_rmv_cnddts.append("しないのか")
    elif check_text_terminate_string(line_msg, "をしていますか"):
         intnt_rmv_cnddts.append("をしていますか")
    elif check_text_terminate_string(line_msg, "はしていますか"):
         intnt_rmv_cnddts.append("はしていますか")
    elif check_text_terminate_string(line_msg, "をしてますか"):
         intnt_rmv_cnddts.append("をしてますか")
    elif check_text_terminate_string(line_msg, "はしてますか"):
         intnt_rmv_cnddts.append("はしてますか")
    elif check_text_terminate_string(line_msg, "をしているか"):
         intnt_rmv_cnddts.append("をしているか")
    elif check_text_terminate_string(line_msg, "はしているか"):
         intnt_rmv_cnddts.append("はしているか")
    elif check_text_terminate_string(line_msg, "をしてるか"):
         intnt_rmv_cnddts.append("をしてるか")
    elif check_text_terminate_string(line_msg, "はしてるか"):
         intnt_rmv_cnddts.append("はしてるか")
    elif check_text_terminate_string(line_msg, "していますか"):
         intnt_rmv_cnddts.append("していますか")
    elif check_text_terminate_string(line_msg, "してますか"):
         intnt_rmv_cnddts.append("してますか")
    elif check_text_terminate_string(line_msg, "しているか"):
         intnt_rmv_cnddts.append("しているか")
    elif check_text_terminate_string(line_msg, "してるか"):
         intnt_rmv_cnddts.append("してるか")
    elif check_text_terminate_string(line_msg, "をしていませんか"):
         intnt_rmv_cnddts.append("をしていませんか")
    elif check_text_terminate_string(line_msg, "はしていませんか"):
         intnt_rmv_cnddts.append("はしていませんか")
    elif check_text_terminate_string(line_msg, "をしてませんか"):
         intnt_rmv_cnddts.append("をしてませんか")
    elif check_text_terminate_string(line_msg, "はしてませんか"):
         intnt_rmv_cnddts.append("はしてませんか")
    elif check_text_terminate_string(line_msg, "をしていないか"):
         intnt_rmv_cnddts.append("をしていないか")
    elif check_text_terminate_string(line_msg, "はしていないか"):
         intnt_rmv_cnddts.append("はしていないか")
    elif check_text_terminate_string(line_msg, "をしてないか"):
         intnt_rmv_cnddts.append("をしてないか")
    elif check_text_terminate_string(line_msg, "はしてないか"):
         intnt_rmv_cnddts.append("はしてないか")
    elif check_text_terminate_string(line_msg, "していませんか"):
         intnt_rmv_cnddts.append("していませんか")
    elif check_text_terminate_string(line_msg, "してませんか"):
         intnt_rmv_cnddts.append("してませんか")
    elif check_text_terminate_string(line_msg, "していないか"):
         intnt_rmv_cnddts.append("していないか")
    elif check_text_terminate_string(line_msg, "してないか"):
         intnt_rmv_cnddts.append("してないか")
    elif check_text_terminate_string(line_msg, "ができていますか"):
         intnt_rmv_cnddts.append("ができていますか")
    elif check_text_terminate_string(line_msg, "はできていますか"):
         intnt_rmv_cnddts.append("はできていますか")
    elif check_text_terminate_string(line_msg, "ができてますか"):
         intnt_rmv_cnddts.append("ができてますか")
    elif check_text_terminate_string(line_msg, "はできてますか"):
         intnt_rmv_cnddts.append("はできてますか")
    elif check_text_terminate_string(line_msg, "ができているか"):
         intnt_rmv_cnddts.append("ができているか")
    elif check_text_terminate_string(line_msg, "はできているか"):
         intnt_rmv_cnddts.append("はできているか")
    elif check_text_terminate_string(line_msg, "ができてるか"):
         intnt_rmv_cnddts.append("ができてるか")
    elif check_text_terminate_string(line_msg, "はできてるか"):
         intnt_rmv_cnddts.append("はできてるか")
    elif check_text_terminate_string(line_msg, "できていますか"):
         intnt_rmv_cnddts.append("できていますか")
    elif check_text_terminate_string(line_msg, "できてますか"):
         intnt_rmv_cnddts.append("できてますか")
    elif check_text_terminate_string(line_msg, "できているか"):
         intnt_rmv_cnddts.append("できているか")
    elif check_text_terminate_string(line_msg, "できてるか"):
         intnt_rmv_cnddts.append("できてるか")
    elif check_text_terminate_string(line_msg, "はできていませんか"):
         intnt_rmv_cnddts.append("はできていませんか")
    elif check_text_terminate_string(line_msg, "はできてませんか"):
         intnt_rmv_cnddts.append("はできてませんか")
    elif check_text_terminate_string(line_msg, "はできていないか"):
         intnt_rmv_cnddts.append("はできていないか")
    elif check_text_terminate_string(line_msg, "はできてないか"):
         intnt_rmv_cnddts.append("はできてないか")
    elif check_text_terminate_string(line_msg, "できていませんか"):
         intnt_rmv_cnddts.append("できていませんか")
    elif check_text_terminate_string(line_msg, "できてませんか"):
         intnt_rmv_cnddts.append("できてませんか")
    elif check_text_terminate_string(line_msg, "できていないか"):
         intnt_rmv_cnddts.append("できていないか")
    elif check_text_terminate_string(line_msg, "できてないか"):
         intnt_rmv_cnddts.append("できてないか")
    elif check_text_terminate_string(line_msg, "ができましたか"):
         intnt_rmv_cnddts.append("ができましたか")
    elif check_text_terminate_string(line_msg, "はできましたか"):
         intnt_rmv_cnddts.append("はできましたか")
    elif check_text_terminate_string(line_msg, "ができたか"):
         intnt_rmv_cnddts.append("ができたか")
    elif check_text_terminate_string(line_msg, "はできたか"):
         intnt_rmv_cnddts.append("はできたか")
    elif check_text_terminate_string(line_msg, "できましたか"):
         intnt_rmv_cnddts.append("できましたか")
    elif check_text_terminate_string(line_msg, "できたか"):
         intnt_rmv_cnddts.append("できたか")
    elif check_text_terminate_string(line_msg, "はできていませんか"):
         intnt_rmv_cnddts.append("はできていませんか")
    elif check_text_terminate_string(line_msg, "はできてませんか"):
         intnt_rmv_cnddts.append("はできてませんか")
    elif check_text_terminate_string(line_msg, "はできてないか"):
         intnt_rmv_cnddts.append("はできてないか")
    elif check_text_terminate_string(line_msg, "できていませんか"):
         intnt_rmv_cnddts.append("できていませんか")
    elif check_text_terminate_string(line_msg, "できてませんか"):
         intnt_rmv_cnddts.append("できてませんか")
    elif check_text_terminate_string(line_msg, "できてないか"):
         intnt_rmv_cnddts.append("できてないか")
    elif check_text_terminate_string(line_msg, "ができますか"):
         intnt_rmv_cnddts.append("ができますか")
    elif check_text_terminate_string(line_msg, "はできますか"):
         intnt_rmv_cnddts.append("はできますか")
    elif check_text_terminate_string(line_msg, "ができるか"):
         intnt_rmv_cnddts.append("ができるか")
    elif check_text_terminate_string(line_msg, "はできるか"):
         intnt_rmv_cnddts.append("はできるか")
    elif check_text_terminate_string(line_msg, "できますか"):
         intnt_rmv_cnddts.append("できますか")
    elif check_text_terminate_string(line_msg, "できるか"):
         intnt_rmv_cnddts.append("できるか")
    elif check_text_terminate_string(line_msg, "はできませんか"):
         intnt_rmv_cnddts.append("はできませんか")
    elif check_text_terminate_string(line_msg, "はできないか"):
         intnt_rmv_cnddts.append("はできないか")
    elif check_text_terminate_string(line_msg, "できませんか"):
         intnt_rmv_cnddts.append("できませんか")
    elif check_text_terminate_string(line_msg, "できないか"):
         intnt_rmv_cnddts.append("できないか")
    elif check_text_terminate_string(line_msg, "がされています"):
         intnt_rmv_cnddts.append("がされています")
    elif check_text_terminate_string(line_msg, "はされています"):
         intnt_rmv_cnddts.append("はされています")
    elif check_text_terminate_string(line_msg, "がされてます"):
         intnt_rmv_cnddts.append("がされてます")
    elif check_text_terminate_string(line_msg, "はされてます"):
         intnt_rmv_cnddts.append("はされてます")
    elif check_text_terminate_string(line_msg, "がされている"):
         intnt_rmv_cnddts.append("がされている")
    elif check_text_terminate_string(line_msg, "はされている"):
         intnt_rmv_cnddts.append("はされている")
    elif check_text_terminate_string(line_msg, "がされてる"):
         intnt_rmv_cnddts.append("がされてる")
    elif check_text_terminate_string(line_msg, "はされてる"):
         intnt_rmv_cnddts.append("はされてる")
    elif check_text_terminate_string(line_msg, "されています"):
         intnt_rmv_cnddts.append("されています")
    elif check_text_terminate_string(line_msg, "されてます"):
         intnt_rmv_cnddts.append("されてます")
    elif check_text_terminate_string(line_msg, "されている"):
         intnt_rmv_cnddts.append("されている")
    elif check_text_terminate_string(line_msg, "がやられています"):
         intnt_rmv_cnddts.append("がやられています")
    elif check_text_terminate_string(line_msg, "がやられてます"):
         intnt_rmv_cnddts.append("がやられてます")
    elif check_text_terminate_string(line_msg, "がやられてる"):
         intnt_rmv_cnddts.append("がやられてる")
    elif check_text_terminate_string(line_msg, "はやられています"):
         intnt_rmv_cnddts.append("はやられています")
    elif check_text_terminate_string(line_msg, "はやられてます"):
         intnt_rmv_cnddts.append("はやられてます")
    elif check_text_terminate_string(line_msg, "はやられてる"):
         intnt_rmv_cnddts.append("はやられてる")
    elif check_text_terminate_string(line_msg, "がされていません"):
         intnt_rmv_cnddts.append("がされていません")
    elif check_text_terminate_string(line_msg, "はされていません"):
         intnt_rmv_cnddts.append("はされていません")
    elif check_text_terminate_string(line_msg, "されていません"):
         intnt_rmv_cnddts.append("されていません")
    elif check_text_terminate_string(line_msg, "がされてません"):
         intnt_rmv_cnddts.append("がされてません")
    elif check_text_terminate_string(line_msg, "はされてません"):
         intnt_rmv_cnddts.append("はされてません")
    elif check_text_terminate_string(line_msg, "されてません"):
         intnt_rmv_cnddts.append("されてません")
    elif check_text_terminate_string(line_msg, "がされていない"):
         intnt_rmv_cnddts.append("がされていない")
    elif check_text_terminate_string(line_msg, "はされていない"):
         intnt_rmv_cnddts.append("はされていない")
    elif check_text_terminate_string(line_msg, "されていない"):
         intnt_rmv_cnddts.append("されていない")
    elif check_text_terminate_string(line_msg, "がされてない"):
         intnt_rmv_cnddts.append("がされてない")
    elif check_text_terminate_string(line_msg, "はされてない"):
         intnt_rmv_cnddts.append("はされてない")
    elif check_text_terminate_string(line_msg, "されてない"):
         intnt_rmv_cnddts.append("されてない")
    elif check_text_terminate_string(line_msg, "がされました"):
         intnt_rmv_cnddts.append("がされました")
    elif check_text_terminate_string(line_msg, "はされました"):
         intnt_rmv_cnddts.append("はされました")
    elif check_text_terminate_string(line_msg, "されました"):
         intnt_rmv_cnddts.append("されました")
    elif check_text_terminate_string(line_msg, "がされた"):
         intnt_rmv_cnddts.append("がされた")
    elif check_text_terminate_string(line_msg, "はされた"):
         intnt_rmv_cnddts.append("はされた")
    elif check_text_terminate_string(line_msg, "された"):
         intnt_rmv_cnddts.append("された")
    elif check_text_terminate_string(line_msg, "がされませんでした"):
         intnt_rmv_cnddts.append("がされませんでした")
    elif check_text_terminate_string(line_msg, "はされませんでした"):
         intnt_rmv_cnddts.append("はされませんでした")
    elif check_text_terminate_string(line_msg, "されませんでした"):
         intnt_rmv_cnddts.append("されませんでした")
    elif check_text_terminate_string(line_msg, "がされなかった"):
         intnt_rmv_cnddts.append("がされなかった")
    elif check_text_terminate_string(line_msg, "はされなかった"):
         intnt_rmv_cnddts.append("はされなかった")
    elif check_text_terminate_string(line_msg, "されなかった"):
         intnt_rmv_cnddts.append("されなかった")
    elif check_text_terminate_string(line_msg, "でした"):
         intnt_rmv_cnddts.append("でした")
    elif check_text_terminate_string(line_msg, "だった"):
         intnt_rmv_cnddts.append("だった")
    elif check_text_terminate_string(line_msg, "ではなかったです"):
         intnt_rmv_cnddts.append("ではなかったです")
    elif check_text_terminate_string(line_msg, "でなかったです"):
         intnt_rmv_cnddts.append("でなかったです")
    elif check_text_terminate_string(line_msg, "ではなかった"):
         intnt_rmv_cnddts.append("ではなかった")
    elif check_text_terminate_string(line_msg, "でなかった"):
         intnt_rmv_cnddts.append("でなかった")
    elif check_text_terminate_string(line_msg, "をしていきたい"):
         intnt_rmv_cnddts.append("をしていきたい")
    elif check_text_terminate_string(line_msg, "はしていきたい"):
         intnt_rmv_cnddts.append("はしていきたい")
    elif check_text_terminate_string(line_msg, "していきたい"):
         intnt_rmv_cnddts.append("していきたい")
    elif check_text_terminate_string(line_msg, "をやっていきたい"):
         intnt_rmv_cnddts.append("をやっていきたい")
    elif check_text_terminate_string(line_msg, "はやっていきたい"):
         intnt_rmv_cnddts.append("はやっていきたい")
    elif check_text_terminate_string(line_msg, "をしていきたくはない"):
         intnt_rmv_cnddts.append("をしていきたくはない")
    elif check_text_terminate_string(line_msg, "はしていきたくはない"):
         intnt_rmv_cnddts.append("はしていきたくはない")
    elif check_text_terminate_string(line_msg, "していきたくはない"):
         intnt_rmv_cnddts.append("していきたくはない")
    elif check_text_terminate_string(line_msg, "をしていきたくない"):
         intnt_rmv_cnddts.append("をしていきたくない")
    elif check_text_terminate_string(line_msg, "はしていきたくない"):
         intnt_rmv_cnddts.append("はしていきたくない")
    elif check_text_terminate_string(line_msg, "していきたくない"):
         intnt_rmv_cnddts.append("していきたくない")
    elif check_text_terminate_string(line_msg, "をやっていきたくはない"):
         intnt_rmv_cnddts.append("をやっていきたくはない")
    elif check_text_terminate_string(line_msg, "はやっていきたくはない"):
         intnt_rmv_cnddts.append("はやっていきたくはない")
    elif check_text_terminate_string(line_msg, "をやっていきたくない"):
         intnt_rmv_cnddts.append("をやっていきたくない")
    elif check_text_terminate_string(line_msg, "はやっていきたくない"):
         intnt_rmv_cnddts.append("はやっていきたくない")
    elif check_text_terminate_string(line_msg, "ではありました"):
         intnt_rmv_cnddts.append("ではありました")
    elif check_text_terminate_string(line_msg, "ではあった"):
         intnt_rmv_cnddts.append("ではあった")
    elif check_text_terminate_string(line_msg, "であった"):
         intnt_rmv_cnddts.append("であった")
    elif check_text_terminate_string(line_msg, "ではありませんでした"):
         intnt_rmv_cnddts.append("ではありませんでした")
    elif check_text_terminate_string(line_msg, "ではなかった"):
         intnt_rmv_cnddts.append("ではなかった")
    elif check_text_terminate_string(line_msg, "でなかった"):
         intnt_rmv_cnddts.append("でなかった")
    elif check_text_terminate_string(line_msg, "で御座います"):
         intnt_rmv_cnddts.append("で御座います")
    elif check_text_terminate_string(line_msg, "でございます"):
         intnt_rmv_cnddts.append("でございます")
    elif check_text_terminate_string(line_msg, "であります"):
         intnt_rmv_cnddts.append("であります")
    elif check_text_terminate_string(line_msg, "です"):
         intnt_rmv_cnddts.append("です")
    elif check_text_terminate_string(line_msg, "では御座いません"):
         intnt_rmv_cnddts.append("では御座いません")
    elif check_text_terminate_string(line_msg, "ではございません"):
         intnt_rmv_cnddts.append("ではございません")
    elif check_text_terminate_string(line_msg, "ではありません"):
         intnt_rmv_cnddts.append("ではありません")
    elif check_text_terminate_string(line_msg, "をやっていました"):
         intnt_rmv_cnddts.append("をやっていました")
    elif check_text_terminate_string(line_msg, "をやってました"):
         intnt_rmv_cnddts.append("をやってました")
    elif check_text_terminate_string(line_msg, "をやってた"):
         intnt_rmv_cnddts.append("をやってた")
    elif check_text_terminate_string(line_msg, "をやっていませんでした"):
         intnt_rmv_cnddts.append("をやっていませんでした")
    elif check_text_terminate_string(line_msg, "をやってませんでした"):
         intnt_rmv_cnddts.append("をやってませんでした")
    elif check_text_terminate_string(line_msg, "をやってなかった"):
         intnt_rmv_cnddts.append("をやってなかった")
    elif check_text_terminate_string(line_msg, "を致しませんか"):
         intnt_rmv_cnddts.append("を致しませんか")
    elif check_text_terminate_string(line_msg, "をいたしませんか"):
         intnt_rmv_cnddts.append("をいたしませんか")
    elif check_text_terminate_string(line_msg, "致しませんか"):
         intnt_rmv_cnddts.append("致しませんか")
    elif check_text_terminate_string(line_msg, "いたしませんか"):
         intnt_rmv_cnddts.append("いたしませんか")
    elif check_text_terminate_string(line_msg, "しませんか"):
         intnt_rmv_cnddts.append("しませんか")
    elif check_text_terminate_string(line_msg, "を行いたい"):
         intnt_rmv_cnddts.append("を行いたい")
    elif check_text_terminate_string(line_msg, "をしたい"):
         intnt_rmv_cnddts.append("をしたい")
    elif check_text_terminate_string(line_msg, "がしたい"):
         intnt_rmv_cnddts.append("がしたい")
    elif check_text_terminate_string(line_msg, "したい"):
         intnt_rmv_cnddts.append("したい")
    elif check_text_terminate_string(line_msg, "をやりたい"):
         intnt_rmv_cnddts.append("をやりたい")
    elif check_text_terminate_string(line_msg, "がやりたい"):
         intnt_rmv_cnddts.append("がやりたい")
    elif check_text_terminate_string(line_msg, "を行いたくない"):
         intnt_rmv_cnddts.append("を行いたくない")
    elif check_text_terminate_string(line_msg, "をしたくない"):
         intnt_rmv_cnddts.append("をしたくない")
    elif check_text_terminate_string(line_msg, "がしたくない"):
         intnt_rmv_cnddts.append("がしたくない")
    elif check_text_terminate_string(line_msg, "したくない"):
         intnt_rmv_cnddts.append("したくない")
    elif check_text_terminate_string(line_msg, "をやりたくない"):
         intnt_rmv_cnddts.append("をやりたくない")
    elif check_text_terminate_string(line_msg, "がやりたくない"):
         intnt_rmv_cnddts.append("がやりたくない")
    elif check_text_terminate_string(line_msg, "を行いたいのですか"):
         intnt_rmv_cnddts.append("を行いたいのですか")
    elif check_text_terminate_string(line_msg, "を行いたいんですか"):
         intnt_rmv_cnddts.append("を行いたいんですか")
    elif check_text_terminate_string(line_msg, "を行いたいですか"):
         intnt_rmv_cnddts.append("を行いたいですか")
    elif check_text_terminate_string(line_msg, "をしたいのですか"):
         intnt_rmv_cnddts.append("をしたいのですか")
    elif check_text_terminate_string(line_msg, "をしたいんですか"):
         intnt_rmv_cnddts.append("をしたいんですか")
    elif check_text_terminate_string(line_msg, "をしたいですか"):
         intnt_rmv_cnddts.append("をしたいですか")
    elif check_text_terminate_string(line_msg, "は行いたいのですか"):
         intnt_rmv_cnddts.append("は行いたいのですか")
    elif check_text_terminate_string(line_msg, "は行いたいんですか"):
         intnt_rmv_cnddts.append("は行いたいんですか")
    elif check_text_terminate_string(line_msg, "は行いたいですか"):
         intnt_rmv_cnddts.append("は行いたいですか")
    elif check_text_terminate_string(line_msg, "はしたいのですか"):
         intnt_rmv_cnddts.append("はしたいのですか")
    elif check_text_terminate_string(line_msg, "はしたいんですか"):
         intnt_rmv_cnddts.append("はしたいんですか")
    elif check_text_terminate_string(line_msg, "はしたいですか"):
         intnt_rmv_cnddts.append("はしたいですか")
    elif check_text_terminate_string(line_msg, "したいのですか"):
         intnt_rmv_cnddts.append("したいのですか")
    elif check_text_terminate_string(line_msg, "したいんですか"):
         intnt_rmv_cnddts.append("したいんですか")
    elif check_text_terminate_string(line_msg, "したいですか"):
         intnt_rmv_cnddts.append("したいですか")
    elif check_text_terminate_string(line_msg, "したいのか"):
         intnt_rmv_cnddts.append("したいのか")
    elif check_text_terminate_string(line_msg, "したいか"):
         intnt_rmv_cnddts.append("したいか")
    elif check_text_terminate_string(line_msg, "をやりたいのですか"):
         intnt_rmv_cnddts.append("をやりたいのですか")
    elif check_text_terminate_string(line_msg, "をやりたいんですか"):
         intnt_rmv_cnddts.append("をやりたいんですか")
    elif check_text_terminate_string(line_msg, "をやりたいですか"):
         intnt_rmv_cnddts.append("をやりたいですか")
    elif check_text_terminate_string(line_msg, "をやりたいのか"):
         intnt_rmv_cnddts.append("をやりたいのか")
    elif check_text_terminate_string(line_msg, "をやりたいか"):
         intnt_rmv_cnddts.append("をやりたいか")
    elif check_text_terminate_string(line_msg, "がやりたいのですか"):
         intnt_rmv_cnddts.append("がやりたいのですか")
    elif check_text_terminate_string(line_msg, "がやりたいんですか"):
         intnt_rmv_cnddts.append("がやりたいんですか")
    elif check_text_terminate_string(line_msg, "がやりたいですか"):
         intnt_rmv_cnddts.append("がやりたいですか")
    elif check_text_terminate_string(line_msg, "がやりたいのか"):
         intnt_rmv_cnddts.append("がやりたいのか")
    elif check_text_terminate_string(line_msg, "がやりたいか"):
         intnt_rmv_cnddts.append("がやりたいか")
    elif check_text_terminate_string(line_msg, "を行いたくないのですか"):
         intnt_rmv_cnddts.append("を行いたくないのですか")
    elif check_text_terminate_string(line_msg, "を行いたくないんですか"):
         intnt_rmv_cnddts.append("を行いたくないんですか")
    elif check_text_terminate_string(line_msg, "を行いたくないですか"):
         intnt_rmv_cnddts.append("を行いたくないですか")
    elif check_text_terminate_string(line_msg, "をしたくないのですか"):
         intnt_rmv_cnddts.append("をしたくないのですか")
    elif check_text_terminate_string(line_msg, "をしたくないんですか"):
         intnt_rmv_cnddts.append("をしたくないんですか")
    elif check_text_terminate_string(line_msg, "をしたくないですか"):
         intnt_rmv_cnddts.append("をしたくないですか")
    elif check_text_terminate_string(line_msg, "は行いたくないのですか"):
         intnt_rmv_cnddts.append("は行いたくないのですか")
    elif check_text_terminate_string(line_msg, "は行いたくないんですか"):
         intnt_rmv_cnddts.append("は行いたくないんですか")
    elif check_text_terminate_string(line_msg, "は行いたくないですか"):
         intnt_rmv_cnddts.append("は行いたくないですか")
    elif check_text_terminate_string(line_msg, "はしたくないのですか"):
         intnt_rmv_cnddts.append("はしたくないのですか")
    elif check_text_terminate_string(line_msg, "はしたくないんですか"):
         intnt_rmv_cnddts.append("はしたくないんですか")
    elif check_text_terminate_string(line_msg, "はしたくないですか"):
         intnt_rmv_cnddts.append("はしたくないですか")
    elif check_text_terminate_string(line_msg, "したくないのですか"):
         intnt_rmv_cnddts.append("したくないのですか")
    elif check_text_terminate_string(line_msg, "したくないんですか"):
         intnt_rmv_cnddts.append("したくないんですか")
    elif check_text_terminate_string(line_msg, "したくないですか"):
         intnt_rmv_cnddts.append("したくないですか")
    elif check_text_terminate_string(line_msg, "したくないか"):
         intnt_rmv_cnddts.append("したくないか")
    elif check_text_terminate_string(line_msg, "をやりたくないのですか"):
         intnt_rmv_cnddts.append("をやりたくないのですか")
    elif check_text_terminate_string(line_msg, "をやりたくないんですか"):
         intnt_rmv_cnddts.append("をやりたくないんですか")
    elif check_text_terminate_string(line_msg, "をやりたくないですか"):
         intnt_rmv_cnddts.append("をやりたくないですか")
    elif check_text_terminate_string(line_msg, "をやりたくないか"):
         intnt_rmv_cnddts.append("をやりたくないか")
    elif check_text_terminate_string(line_msg, "がやりたくないのですか"):
         intnt_rmv_cnddts.append("がやりたくないのですか")
    elif check_text_terminate_string(line_msg, "がやりたくないんですか"):
         intnt_rmv_cnddts.append("がやりたくないんですか")
    elif check_text_terminate_string(line_msg, "がやりたくないですか"):
         intnt_rmv_cnddts.append("がやりたくないですか")
    elif check_text_terminate_string(line_msg, "がやりたくないのか"):
         intnt_rmv_cnddts.append("がやりたくないのか")
    elif check_text_terminate_string(line_msg, "がやりたくないか"):
         intnt_rmv_cnddts.append("がやりたくないか")
    elif check_text_terminate_string(line_msg, "をしていきたいですか"):
         intnt_rmv_cnddts.append("をしていきたいですか")
    elif check_text_terminate_string(line_msg, "をしていきたいか"):
         intnt_rmv_cnddts.append("をしていきたいか")
    elif check_text_terminate_string(line_msg, "していきたいか"):
         intnt_rmv_cnddts.append("していきたいか")
    elif check_text_terminate_string(line_msg, "をやっていきたいですか"):
         intnt_rmv_cnddts.append("をやっていきたいですか")
    elif check_text_terminate_string(line_msg, "をやっていきたいか"):
         intnt_rmv_cnddts.append("をやっていきたいか")
    elif check_text_terminate_string(line_msg, "をしていきたくないですか"):
         intnt_rmv_cnddts.append("をしていきたくないですか")
    elif check_text_terminate_string(line_msg, "はしていきたくないですか"):
         intnt_rmv_cnddts.append("はしていきたくないですか")
    elif check_text_terminate_string(line_msg, "していきたくないですか"):
         intnt_rmv_cnddts.append("していきたくないですか")
    elif check_text_terminate_string(line_msg, "をしていきたくないか"):
         intnt_rmv_cnddts.append("をしていきたくないか")
    elif check_text_terminate_string(line_msg, "はしていきたくないか"):
         intnt_rmv_cnddts.append("はしていきたくないか")
    elif check_text_terminate_string(line_msg, "していきたくないか"):
         intnt_rmv_cnddts.append("していきたくないか")
    elif check_text_terminate_string(line_msg, "はやっていきたくないか"):
         intnt_rmv_cnddts.append("はやっていきたくないか")
    elif check_text_terminate_string(line_msg, "をやっていきたくないか"):
         intnt_rmv_cnddts.append("をやっていきたくないか")
    elif check_text_terminate_string(line_msg, "をやり続けたいですか"):
         intnt_rmv_cnddts.append("をやり続けたいですか")
    elif check_text_terminate_string(line_msg, "をやり続けたいか"):
         intnt_rmv_cnddts.append("をやり続けたいか")
    elif check_text_terminate_string(line_msg, "をやってたいですか"):
         intnt_rmv_cnddts.append("をやってたいですか")
    elif check_text_terminate_string(line_msg, "をやってたいか"):
         intnt_rmv_cnddts.append("をやってたいか")
    elif check_text_terminate_string(line_msg, "をし続けたいですか"):
         intnt_rmv_cnddts.append("をし続けたいですか")
    elif check_text_terminate_string(line_msg, "をし続けたいか"):
         intnt_rmv_cnddts.append("をし続けたいか")
    elif check_text_terminate_string(line_msg, "をしてたいですか"):
         intnt_rmv_cnddts.append("をしてたいですか")
    elif check_text_terminate_string(line_msg, "をしてたいか"):
         intnt_rmv_cnddts.append("をしてたいか")
    elif check_text_terminate_string(line_msg, "をやり続けたくないですか"):
         intnt_rmv_cnddts.append("をやり続けたくないですか")
    elif check_text_terminate_string(line_msg, "をやり続けたくないか"):
         intnt_rmv_cnddts.append("をやり続けたくないか")
    elif check_text_terminate_string(line_msg, "をやってたくないですか"):
         intnt_rmv_cnddts.append("をやってたくないですか")
    elif check_text_terminate_string(line_msg, "をやってたくないか"):
         intnt_rmv_cnddts.append("をやってたくないか")
    elif check_text_terminate_string(line_msg, "をし続けたくないですか"):
         intnt_rmv_cnddts.append("をし続けたくないですか")
    elif check_text_terminate_string(line_msg, "をし続けたくないか"):
         intnt_rmv_cnddts.append("をし続けたくないか")
    elif check_text_terminate_string(line_msg, "をしてたくないですか"):
         intnt_rmv_cnddts.append("をしてたくないですか")
    elif check_text_terminate_string(line_msg, "をしてたくないか"):
         intnt_rmv_cnddts.append("をしてたくないか")
    elif check_text_terminate_string(line_msg, "をしましたか"):
         intnt_rmv_cnddts.append("をしましたか")
    elif check_text_terminate_string(line_msg, "をしたか"):
         intnt_rmv_cnddts.append("をしたか")
    elif check_text_terminate_string(line_msg, "はしましたか"):
         intnt_rmv_cnddts.append("はしましたか")
    elif check_text_terminate_string(line_msg, "はしたか"):
         intnt_rmv_cnddts.append("はしたか")
    elif check_text_terminate_string(line_msg, "しましたか"):
         intnt_rmv_cnddts.append("しましたか")
    elif check_text_terminate_string(line_msg, "したか"):
         intnt_rmv_cnddts.append("したか")
    elif check_text_terminate_string(line_msg, "をやりましたか"):
         intnt_rmv_cnddts.append("をやりましたか")
    elif check_text_terminate_string(line_msg, "をやったか"):
         intnt_rmv_cnddts.append("をやったか")
    elif check_text_terminate_string(line_msg, "はやりましたか"):
         intnt_rmv_cnddts.append("はやりましたか")
    elif check_text_terminate_string(line_msg, "はやったか"):
         intnt_rmv_cnddts.append("はやったか")
    elif check_text_terminate_string(line_msg, "をしていませんか"):
         intnt_rmv_cnddts.append("をしていませんか")
    elif check_text_terminate_string(line_msg, "をしてませんか"):
         intnt_rmv_cnddts.append("をしてませんか")
    elif check_text_terminate_string(line_msg, "をしてないか"):
         intnt_rmv_cnddts.append("をしてないか")
    elif check_text_terminate_string(line_msg, "はしていませんか"):
         intnt_rmv_cnddts.append("はしていませんか")
    elif check_text_terminate_string(line_msg, "はしてませんか"):
         intnt_rmv_cnddts.append("はしてませんか")
    elif check_text_terminate_string(line_msg, "はしてないか"):
         intnt_rmv_cnddts.append("はしてないか")
    elif check_text_terminate_string(line_msg, "していませんか"):
         intnt_rmv_cnddts.append("していませんか")
    elif check_text_terminate_string(line_msg, "してませんか"):
         intnt_rmv_cnddts.append("してませんか")
    elif check_text_terminate_string(line_msg, "してないか"):
         intnt_rmv_cnddts.append("してないか")
    elif check_text_terminate_string(line_msg, "はされていますか"):
         intnt_rmv_cnddts.append("はされていますか")
    elif check_text_terminate_string(line_msg, "されていますか"):
         intnt_rmv_cnddts.append("されていますか")
    elif check_text_terminate_string(line_msg, "されてますか"):
         intnt_rmv_cnddts.append("されてますか")
    elif check_text_terminate_string(line_msg, "されてますか"):
         intnt_rmv_cnddts.append("されてますか")
    elif check_text_terminate_string(line_msg, "はされていませんか"):
         intnt_rmv_cnddts.append("はされていませんか")
    elif check_text_terminate_string(line_msg, "されていませんか"):
         intnt_rmv_cnddts.append("されていませんか")
    elif check_text_terminate_string(line_msg, "されてませんか"):
         intnt_rmv_cnddts.append("されてませんか")
    elif check_text_terminate_string(line_msg, "されていないか"):
         intnt_rmv_cnddts.append("されていないか")
    elif check_text_terminate_string(line_msg, "されてないか"):
         intnt_rmv_cnddts.append("されてないか")
    elif check_text_terminate_string(line_msg, "はされていましたか"):
         intnt_rmv_cnddts.append("はされていましたか")
    elif check_text_terminate_string(line_msg, "はされてましたか"):
         intnt_rmv_cnddts.append("はされてましたか")
    elif check_text_terminate_string(line_msg, "されてましたか"):
         intnt_rmv_cnddts.append("されてましたか")
    elif check_text_terminate_string(line_msg, "されてたか"):
         intnt_rmv_cnddts.append("されてたか")
    elif check_text_terminate_string(line_msg, "はされていませんでしたか"):
         intnt_rmv_cnddts.append("はされていませんでしたか")
    elif check_text_terminate_string(line_msg, "はされていなかったか"):
         intnt_rmv_cnddts.append("はされていなかったか")
    elif check_text_terminate_string(line_msg, "されていませんでしたか"):
         intnt_rmv_cnddts.append("されていませんでしたか")
    elif check_text_terminate_string(line_msg, "されていなかったか"):
         intnt_rmv_cnddts.append("されていなかったか")
    elif check_text_terminate_string(line_msg, "だったですか"):
         intnt_rmv_cnddts.append("だったですか")
    elif check_text_terminate_string(line_msg, "だったか"):
         intnt_rmv_cnddts.append("だったか")
    elif check_text_terminate_string(line_msg, "でしたか"):
         intnt_rmv_cnddts.append("でしたか")
    elif check_text_terminate_string(line_msg, "ではなかったですか"):
         intnt_rmv_cnddts.append("ではなかったですか")
    elif check_text_terminate_string(line_msg, "ではなかったか"):
         intnt_rmv_cnddts.append("ではなかったか")
    elif check_text_terminate_string(line_msg, "でなかったか"):
         intnt_rmv_cnddts.append("でなかったか")
    elif check_text_terminate_string(line_msg, "をしなさい"):
         intnt_rmv_cnddts.append("をしなさい")
    elif check_text_terminate_string(line_msg, "をしろ"):
         intnt_rmv_cnddts.append("をしろ")
    elif check_text_terminate_string(line_msg, "はしなさい"):
         intnt_rmv_cnddts.append("はしなさい")
    elif check_text_terminate_string(line_msg, "はしろ"):
         intnt_rmv_cnddts.append("はしろ")
    elif check_text_terminate_string(line_msg, "しなさい"):
         intnt_rmv_cnddts.append("しなさい")
    elif check_text_terminate_string(line_msg, "しろ"):
         intnt_rmv_cnddts.append("しろ")
    elif check_text_terminate_string(line_msg, "をしなければならない"):
         intnt_rmv_cnddts.append("をしなければならない")
    elif check_text_terminate_string(line_msg, "をしなければ"):
         intnt_rmv_cnddts.append("をしなければ")
    elif check_text_terminate_string(line_msg, "をしないといけないです"):
         intnt_rmv_cnddts.append("をしないといけないです")
    elif check_text_terminate_string(line_msg, "をしないといけない"):
         intnt_rmv_cnddts.append("をしないといけない")
    elif check_text_terminate_string(line_msg, "をしなきゃいけないです"):
         intnt_rmv_cnddts.append("をしなきゃいけないです")
    elif check_text_terminate_string(line_msg, "をしなきゃいけない"):
         intnt_rmv_cnddts.append("をしなきゃいけない")
    elif check_text_terminate_string(line_msg, "をしなきゃならない"):
         intnt_rmv_cnddts.append("をしなきゃならない")
    elif check_text_terminate_string(line_msg, "をしなきゃ"):
         intnt_rmv_cnddts.append("をしなきゃ")
    elif check_text_terminate_string(line_msg, "はしなければならない"):
         intnt_rmv_cnddts.append("はしなければならない")
    elif check_text_terminate_string(line_msg, "はしなければ"):
         intnt_rmv_cnddts.append("はしなければ")
    elif check_text_terminate_string(line_msg, "はしないといけないです"):
         intnt_rmv_cnddts.append("はしないといけないです")
    elif check_text_terminate_string(line_msg, "はしないといけない"):
         intnt_rmv_cnddts.append("はしないといけない")
    elif check_text_terminate_string(line_msg, "はしなきゃいけないです"):
         intnt_rmv_cnddts.append("はしなきゃいけないです")
    elif check_text_terminate_string(line_msg, "はしなきゃいけない"):
         intnt_rmv_cnddts.append("はしなきゃいけない")
    elif check_text_terminate_string(line_msg, "はしなきゃならない"):
         intnt_rmv_cnddts.append("はしなきゃならない")
    elif check_text_terminate_string(line_msg, "はしなきゃ"):
         intnt_rmv_cnddts.append("はしなきゃ")
    elif check_text_terminate_string(line_msg, "しなければならない"):
         intnt_rmv_cnddts.append("しなければならない")
    elif check_text_terminate_string(line_msg, "しなければ"):
         intnt_rmv_cnddts.append("しなければ")
    elif check_text_terminate_string(line_msg, "しないといけないです"):
         intnt_rmv_cnddts.append("しないといけないです")
    elif check_text_terminate_string(line_msg, "しないといけない"):
         intnt_rmv_cnddts.append("しないといけない")
    elif check_text_terminate_string(line_msg, "しなきゃいけないです"):
         intnt_rmv_cnddts.append("しなきゃいけないです")
    elif check_text_terminate_string(line_msg, "しなきゃいけない"):
         intnt_rmv_cnddts.append("しなきゃいけない")
    elif check_text_terminate_string(line_msg, "しなきゃならない"):
         intnt_rmv_cnddts.append("しなきゃならない")
    elif check_text_terminate_string(line_msg, "しなきゃ"):
         intnt_rmv_cnddts.append("しなきゃ")
    elif check_text_terminate_string(line_msg, "がしなければならない"):
         intnt_rmv_cnddts.append("がしなければならない")
    elif check_text_terminate_string(line_msg, "がしなければ"):
         intnt_rmv_cnddts.append("がしなければ")
    elif check_text_terminate_string(line_msg, "がしないといけないです"):
         intnt_rmv_cnddts.append("がしないといけないです")
    elif check_text_terminate_string(line_msg, "がしないといけない"):
         intnt_rmv_cnddts.append("がしないといけない")
    elif check_text_terminate_string(line_msg, "がしなきゃいけないです"):
         intnt_rmv_cnddts.append("がしなきゃいけないです")
    elif check_text_terminate_string(line_msg, "がしなきゃいけない"):
         intnt_rmv_cnddts.append("がしなきゃいけない")
    elif check_text_terminate_string(line_msg, "がしなきゃならない"):
         intnt_rmv_cnddts.append("がしなきゃならない")
    elif check_text_terminate_string(line_msg, "がしなきゃ"):
         intnt_rmv_cnddts.append("がしなきゃ")
    elif check_text_terminate_string(line_msg, "はしてはならない"):
         intnt_rmv_cnddts.append("はしてはならない")
    elif check_text_terminate_string(line_msg, "はしてはいけない"):
         intnt_rmv_cnddts.append("はしてはいけない")
    elif check_text_terminate_string(line_msg, "はしたらいけない"):
         intnt_rmv_cnddts.append("はしたらいけない")
    elif check_text_terminate_string(line_msg, "はしちゃいけない"):
         intnt_rmv_cnddts.append("はしちゃいけない")
    elif check_text_terminate_string(line_msg, "をしてはならない"):
         intnt_rmv_cnddts.append("をしてはならない")
    elif check_text_terminate_string(line_msg, "をしてはいけない"):
         intnt_rmv_cnddts.append("をしてはいけない")
    elif check_text_terminate_string(line_msg, "をしたらいけない"):
         intnt_rmv_cnddts.append("をしたらいけない")
    elif check_text_terminate_string(line_msg, "をしちゃいけない"):
         intnt_rmv_cnddts.append("をしちゃいけない")
    elif check_text_terminate_string(line_msg, "してはならない"):
         intnt_rmv_cnddts.append("してはならない")
    elif check_text_terminate_string(line_msg, "してはいけない"):
         intnt_rmv_cnddts.append("してはいけない")
    elif check_text_terminate_string(line_msg, "したらいけない"):
         intnt_rmv_cnddts.append("したらいけない")
    elif check_text_terminate_string(line_msg, "しちゃいけない"):
         intnt_rmv_cnddts.append("しちゃいけない")
    elif check_text_terminate_string(line_msg, "がしてはならない"):
         intnt_rmv_cnddts.append("がしてはならない")
    elif check_text_terminate_string(line_msg, "がしてはいけない"):
         intnt_rmv_cnddts.append("がしてはいけない")
    elif check_text_terminate_string(line_msg, "がしたらいけない"):
         intnt_rmv_cnddts.append("がしたらいけない")
    elif check_text_terminate_string(line_msg, "がしちゃいけない"):
         intnt_rmv_cnddts.append("がしちゃいけない")
    elif check_text_terminate_string(line_msg, "はしなければならないのですか"):
         intnt_rmv_cnddts.append("はしなければならないのですか")
    elif check_text_terminate_string(line_msg, "はしなければならないんですか"):
         intnt_rmv_cnddts.append("はしなければならないんですか")
    elif check_text_terminate_string(line_msg, "はしなければならないですか"):
         intnt_rmv_cnddts.append("はしなければならないですか")
    elif check_text_terminate_string(line_msg, "はしなければいけないですか"):
         intnt_rmv_cnddts.append("はしなければいけないですか")
    elif check_text_terminate_string(line_msg, "はしないといけないですか"):
         intnt_rmv_cnddts.append("はしないといけないですか")
    elif check_text_terminate_string(line_msg, "はしなきゃいけないですか"):
         intnt_rmv_cnddts.append("はしなきゃいけないですか")
    elif check_text_terminate_string(line_msg, "はしなきゃいけないか"):
         intnt_rmv_cnddts.append("はしなきゃいけないか")
    elif check_text_terminate_string(line_msg, "はしなきゃならないか"):
         intnt_rmv_cnddts.append("はしなきゃならないか")
    elif check_text_terminate_string(line_msg, "をしなければならないのですか"):
         intnt_rmv_cnddts.append("をしなければならないのですか")
    elif check_text_terminate_string(line_msg, "をしなければならないんですか"):
         intnt_rmv_cnddts.append("をしなければならないんですか")
    elif check_text_terminate_string(line_msg, "をしなければならないですか"):
         intnt_rmv_cnddts.append("をしなければならないですか")
    elif check_text_terminate_string(line_msg, "をしなければいけないですか"):
         intnt_rmv_cnddts.append("をしなければいけないですか")
    elif check_text_terminate_string(line_msg, "をしないといけないですか"):
         intnt_rmv_cnddts.append("をしないといけないですか")
    elif check_text_terminate_string(line_msg, "をしなきゃいけないですか"):
         intnt_rmv_cnddts.append("をしなきゃいけないですか")
    elif check_text_terminate_string(line_msg, "をしなきゃいけないか"):
         intnt_rmv_cnddts.append("をしなきゃいけないか")
    elif check_text_terminate_string(line_msg, "をしなきゃならないか"):
         intnt_rmv_cnddts.append("をしなきゃならないか")
    elif check_text_terminate_string(line_msg, "しなければならないのですか"):
         intnt_rmv_cnddts.append("しなければならないのですか")
    elif check_text_terminate_string(line_msg, "しなければならないんですか"):
         intnt_rmv_cnddts.append("しなければならないんですか")
    elif check_text_terminate_string(line_msg, "しなければならないですか"):
         intnt_rmv_cnddts.append("しなければならないですか")
    elif check_text_terminate_string(line_msg, "しなければいけないですか"):
         intnt_rmv_cnddts.append("しなければいけないですか")
    elif check_text_terminate_string(line_msg, "しないといけないですか"):
         intnt_rmv_cnddts.append("しないといけないですか")
    elif check_text_terminate_string(line_msg, "しなきゃいけないですか"):
         intnt_rmv_cnddts.append("しなきゃいけないですか")
    elif check_text_terminate_string(line_msg, "しなきゃいけないか"):
         intnt_rmv_cnddts.append("しなきゃいけないか")
    elif check_text_terminate_string(line_msg, "しなきゃならないか"):
         intnt_rmv_cnddts.append("しなきゃならないか")
    elif check_text_terminate_string(line_msg, "がしなければならないのですか"):
         intnt_rmv_cnddts.append("がしなければならないのですか")
    elif check_text_terminate_string(line_msg, "がしなければならないんですか"):
         intnt_rmv_cnddts.append("がしなければならないんですか")
    elif check_text_terminate_string(line_msg, "がしなければならないのか"):
         intnt_rmv_cnddts.append("がしなければならないのか")
    elif check_text_terminate_string(line_msg, "がしなければならないか"):
         intnt_rmv_cnddts.append("がしなければならないか")
    elif check_text_terminate_string(line_msg, "がしないといけないですか"):
         intnt_rmv_cnddts.append("がしないといけないですか")
    elif check_text_terminate_string(line_msg, "がしないといけないか"):
         intnt_rmv_cnddts.append("がしないといけないか")
    elif check_text_terminate_string(line_msg, "がしなきゃいけないですか"):
         intnt_rmv_cnddts.append("がしなきゃいけないですか")
    elif check_text_terminate_string(line_msg, "がしなきゃいけないのか"):
         intnt_rmv_cnddts.append("がしなきゃいけないのか")
    elif check_text_terminate_string(line_msg, "がしなきゃいけないか"):
         intnt_rmv_cnddts.append("がしなきゃいけないか")
    elif check_text_terminate_string(line_msg, "はしてはならないのか"):
         intnt_rmv_cnddts.append("はしてはならないのか")
    elif check_text_terminate_string(line_msg, "はしてはならないか"):
         intnt_rmv_cnddts.append("はしてはならないか")
    elif check_text_terminate_string(line_msg, "はしてはいけないか"):
         intnt_rmv_cnddts.append("はしてはいけないか")
    elif check_text_terminate_string(line_msg, "はしたらいけないか"):
         intnt_rmv_cnddts.append("はしたらいけないか")
    elif check_text_terminate_string(line_msg, "はしちゃいけないか"):
         intnt_rmv_cnddts.append("はしちゃいけないか")
    elif check_text_terminate_string(line_msg, "をしてはならないのか"):
         intnt_rmv_cnddts.append("をしてはならないのか")
    elif check_text_terminate_string(line_msg, "をしてはならないか"):
         intnt_rmv_cnddts.append("をしてはならないか")
    elif check_text_terminate_string(line_msg, "をしてはいけないか"):
         intnt_rmv_cnddts.append("をしてはいけないか")
    elif check_text_terminate_string(line_msg, "をしたらいけないか"):
         intnt_rmv_cnddts.append("をしたらいけないか")
    elif check_text_terminate_string(line_msg, "をしちゃいけないか"):
         intnt_rmv_cnddts.append("をしちゃいけないか")
    elif check_text_terminate_string(line_msg, "してはならないのか"):
         intnt_rmv_cnddts.append("してはならないのか")
    elif check_text_terminate_string(line_msg, "してはならないか"):
         intnt_rmv_cnddts.append("してはならないか")
    elif check_text_terminate_string(line_msg, "してはいけないか"):
         intnt_rmv_cnddts.append("してはいけないか")
    elif check_text_terminate_string(line_msg, "したらいけないか"):
         intnt_rmv_cnddts.append("したらいけないか")
    elif check_text_terminate_string(line_msg, "しちゃいけないか"):
         intnt_rmv_cnddts.append("しちゃいけないか")
    elif check_text_terminate_string(line_msg, "がしてはならないのか"):
         intnt_rmv_cnddts.append("がしてはならないのか")
    elif check_text_terminate_string(line_msg, "がしてはならないか"):
         intnt_rmv_cnddts.append("がしてはならないか")
    elif check_text_terminate_string(line_msg, "がしてはいけないか"):
         intnt_rmv_cnddts.append("がしてはいけないか")
    elif check_text_terminate_string(line_msg, "がしたらいけないか"):
         intnt_rmv_cnddts.append("がしたらいけないか")
    elif check_text_terminate_string(line_msg, "がしちゃいけないか"):
         intnt_rmv_cnddts.append("がしちゃいけないか")
    elif check_text_terminate_string(line_msg, "はするべきです"):
         intnt_rmv_cnddts.append("はするべきです")
    elif check_text_terminate_string(line_msg, "をするべきです"):
         intnt_rmv_cnddts.append("をするべきです")
    elif check_text_terminate_string(line_msg, "はすべきです"):
         intnt_rmv_cnddts.append("はすべきです")
    elif check_text_terminate_string(line_msg, "をすべきです"):
         intnt_rmv_cnddts.append("をすべきです")
    elif check_text_terminate_string(line_msg, "するべきです"):
         intnt_rmv_cnddts.append("するべきです")
    elif check_text_terminate_string(line_msg, "すべきです"):
         intnt_rmv_cnddts.append("すべきです")
    elif check_text_terminate_string(line_msg, "はするべきではないです"):
         intnt_rmv_cnddts.append("はするべきではないです")
    elif check_text_terminate_string(line_msg, "をするべきではないです"):
         intnt_rmv_cnddts.append("をするべきではないです")
    elif check_text_terminate_string(line_msg, "はすべきではないです"):
         intnt_rmv_cnddts.append("はすべきではないです")
    elif check_text_terminate_string(line_msg, "をすべきではないです"):
         intnt_rmv_cnddts.append("をすべきではないです")
    elif check_text_terminate_string(line_msg, "はすべきではないです"):
         intnt_rmv_cnddts.append("はすべきではないです")
    elif check_text_terminate_string(line_msg, "をすべきではないです"):
         intnt_rmv_cnddts.append("をすべきではないです")
    elif check_text_terminate_string(line_msg, "するべきではないです"):
         intnt_rmv_cnddts.append("するべきではないです")
    elif check_text_terminate_string(line_msg, "するべきでない"):
         intnt_rmv_cnddts.append("するべきでない")
    elif check_text_terminate_string(line_msg, "すべきでない"):
         intnt_rmv_cnddts.append("すべきでない")
    elif check_text_terminate_string(line_msg, "をするべきでしょうか"):
         intnt_rmv_cnddts.append("をするべきでしょうか")
    elif check_text_terminate_string(line_msg, "はするべきでしょうか"):
         intnt_rmv_cnddts.append("はするべきでしょうか")
    elif check_text_terminate_string(line_msg, "をすべきでしょうか"):
         intnt_rmv_cnddts.append("をすべきでしょうか")
    elif check_text_terminate_string(line_msg, "はすべきでしょうか"):
         intnt_rmv_cnddts.append("はすべきでしょうか")
    elif check_text_terminate_string(line_msg, "するべきでしょうか"):
         intnt_rmv_cnddts.append("するべきでしょうか")
    elif check_text_terminate_string(line_msg, "すべきでしょうか"):
         intnt_rmv_cnddts.append("すべきでしょうか")
    elif check_text_terminate_string(line_msg, "をするべきではないのでしょうか"):
         intnt_rmv_cnddts.append("をするべきではないのでしょうか")
    elif check_text_terminate_string(line_msg, "はするべきではないのでしょうか"):
         intnt_rmv_cnddts.append("はするべきではないのでしょうか")
    elif check_text_terminate_string(line_msg, "をすべきではないのでしょうか"):
         intnt_rmv_cnddts.append("をすべきではないのでしょうか")
    elif check_text_terminate_string(line_msg, "はすべきではないのでしょうか"):
         intnt_rmv_cnddts.append("はすべきではないのでしょうか")
    elif check_text_terminate_string(line_msg, "するべきではないのでしょうか"):
         intnt_rmv_cnddts.append("するべきではないのでしょうか")
    elif check_text_terminate_string(line_msg, "すべきではないのでしょうか"):
         intnt_rmv_cnddts.append("すべきではないのでしょうか")
    elif check_text_terminate_string(line_msg, "すべきでないのでしょうか"):
         intnt_rmv_cnddts.append("すべきでないのでしょうか")
    elif check_text_terminate_string(line_msg, "をしても良いです"):
         intnt_rmv_cnddts.append("をしても良いです")
    elif check_text_terminate_string(line_msg, "をしてもいいです"):
         intnt_rmv_cnddts.append("をしてもいいです")
    elif check_text_terminate_string(line_msg, "をして良いです"):
         intnt_rmv_cnddts.append("をして良いです")
    elif check_text_terminate_string(line_msg, "をしていいです"):
         intnt_rmv_cnddts.append("をしていいです")
    elif check_text_terminate_string(line_msg, "をしても良い"):
         intnt_rmv_cnddts.append("をしても良い")
    elif check_text_terminate_string(line_msg, "をしてもいい"):
         intnt_rmv_cnddts.append("をしてもいい")
    elif check_text_terminate_string(line_msg, "をして良い"):
         intnt_rmv_cnddts.append("をして良い")
    elif check_text_terminate_string(line_msg, "をしていい"):
         intnt_rmv_cnddts.append("をしていい")
    elif check_text_terminate_string(line_msg, "はしても良いです"):
         intnt_rmv_cnddts.append("はしても良いです")
    elif check_text_terminate_string(line_msg, "はしてもいいです"):
         intnt_rmv_cnddts.append("はしてもいいです")
    elif check_text_terminate_string(line_msg, "はして良いです"):
         intnt_rmv_cnddts.append("はして良いです")
    elif check_text_terminate_string(line_msg, "はしていいです"):
         intnt_rmv_cnddts.append("はしていいです")
    elif check_text_terminate_string(line_msg, "はしても良い"):
         intnt_rmv_cnddts.append("はしても良い")
    elif check_text_terminate_string(line_msg, "はしてもいい"):
         intnt_rmv_cnddts.append("はしてもいい")
    elif check_text_terminate_string(line_msg, "はして良い"):
         intnt_rmv_cnddts.append("はして良い")
    elif check_text_terminate_string(line_msg, "はしていい"):
         intnt_rmv_cnddts.append("はしていい")
    elif check_text_terminate_string(line_msg, "をやっても良いです"):
         intnt_rmv_cnddts.append("をやっても良いです")
    elif check_text_terminate_string(line_msg, "をやってもいいです"):
         intnt_rmv_cnddts.append("をやってもいいです")
    elif check_text_terminate_string(line_msg, "はやっても良いです"):
         intnt_rmv_cnddts.append("はやっても良いです")
    elif check_text_terminate_string(line_msg, "はやってもいいです"):
         intnt_rmv_cnddts.append("はやってもいいです")
    elif check_text_terminate_string(line_msg, "しても良いです"):
         intnt_rmv_cnddts.append("しても良いです")
    elif check_text_terminate_string(line_msg, "してもいいです"):
         intnt_rmv_cnddts.append("してもいいです")
    elif check_text_terminate_string(line_msg, "して良いです"):
         intnt_rmv_cnddts.append("して良いです")
    elif check_text_terminate_string(line_msg, "していいです"):
         intnt_rmv_cnddts.append("していいです")
    elif check_text_terminate_string(line_msg, "しても良い"):
         intnt_rmv_cnddts.append("しても良い")
    elif check_text_terminate_string(line_msg, "してもいい"):
         intnt_rmv_cnddts.append("してもいい")
    elif check_text_terminate_string(line_msg, "して良い"):
         intnt_rmv_cnddts.append("して良い")
    elif check_text_terminate_string(line_msg, "していい"):
         intnt_rmv_cnddts.append("していい")
    elif check_text_terminate_string(line_msg, "をしないように"):
         intnt_rmv_cnddts.append("をしないように")
    elif check_text_terminate_string(line_msg, "をしないよう"):
         intnt_rmv_cnddts.append("をしないよう")
    elif check_text_terminate_string(line_msg, "をするな"):
         intnt_rmv_cnddts.append("をするな")
    elif check_text_terminate_string(line_msg, "をしてはいけない"):
         intnt_rmv_cnddts.append("をしてはいけない")
    elif check_text_terminate_string(line_msg, "をしちゃいけない"):
         intnt_rmv_cnddts.append("をしちゃいけない")
    elif check_text_terminate_string(line_msg, "はしないように"):
         intnt_rmv_cnddts.append("はしないように")
    elif check_text_terminate_string(line_msg, "はしないよう"):
         intnt_rmv_cnddts.append("はしないよう")
    elif check_text_terminate_string(line_msg, "はするな"):
         intnt_rmv_cnddts.append("はするな")
    elif check_text_terminate_string(line_msg, "はしてはいけない"):
         intnt_rmv_cnddts.append("はしてはいけない")
    elif check_text_terminate_string(line_msg, "はしちゃいけない"):
         intnt_rmv_cnddts.append("はしちゃいけない")
    elif check_text_terminate_string(line_msg, "をやってはいけない"):
         intnt_rmv_cnddts.append("をやってはいけない")
    elif check_text_terminate_string(line_msg, "をやっちゃいけない"):
         intnt_rmv_cnddts.append("をやっちゃいけない")
    elif check_text_terminate_string(line_msg, "はやってはいけない"):
         intnt_rmv_cnddts.append("はやってはいけない")
    elif check_text_terminate_string(line_msg, "はやっちゃいけない"):
         intnt_rmv_cnddts.append("はやっちゃいけない")
    elif check_text_terminate_string(line_msg, "をしちゃ駄目だ"):
         intnt_rmv_cnddts.append("をしちゃ駄目だ")
    elif check_text_terminate_string(line_msg, "をしちゃだめだ"):
         intnt_rmv_cnddts.append("をしちゃだめだ")
    elif check_text_terminate_string(line_msg, "をしちゃダメだ"):
         intnt_rmv_cnddts.append("をしちゃダメだ")
    elif check_text_terminate_string(line_msg, "はしちゃ駄目だ"):
         intnt_rmv_cnddts.append("はしちゃ駄目だ")
    elif check_text_terminate_string(line_msg, "はしちゃだめだ"):
         intnt_rmv_cnddts.append("はしちゃだめだ")
    elif check_text_terminate_string(line_msg, "をしちゃ駄目"):
         intnt_rmv_cnddts.append("をしちゃ駄目")
    elif check_text_terminate_string(line_msg, "をしちゃだめ"):
         intnt_rmv_cnddts.append("をしちゃだめ")
    elif check_text_terminate_string(line_msg, "をしちゃダメ"):
         intnt_rmv_cnddts.append("をしちゃダメ")
    elif check_text_terminate_string(line_msg, "はしちゃ駄目"):
         intnt_rmv_cnddts.append("はしちゃ駄目")
    elif check_text_terminate_string(line_msg, "はしちゃだめ"):
         intnt_rmv_cnddts.append("はしちゃだめ")
    elif check_text_terminate_string(line_msg, "しないように"):
         intnt_rmv_cnddts.append("しないように")
    elif check_text_terminate_string(line_msg, "しないよう"):
         intnt_rmv_cnddts.append("しないよう")
    elif check_text_terminate_string(line_msg, "するな"):
         intnt_rmv_cnddts.append("するな")
    elif check_text_terminate_string(line_msg, "してはいけない"):
         intnt_rmv_cnddts.append("してはいけない")
    elif check_text_terminate_string(line_msg, "しちゃいけない"):
         intnt_rmv_cnddts.append("しちゃいけない")
    elif check_text_terminate_string(line_msg, "はいけない"):
         intnt_rmv_cnddts.append("はいけない")
    elif check_text_terminate_string(line_msg, "しちゃ駄目だ"):
         intnt_rmv_cnddts.append("しちゃ駄目だ")
    elif check_text_terminate_string(line_msg, "しちゃだめだ"):
         intnt_rmv_cnddts.append("しちゃだめだ")
    elif check_text_terminate_string(line_msg, "しちゃダメだ"):
         intnt_rmv_cnddts.append("しちゃダメだ")
    elif check_text_terminate_string(line_msg, "しちゃ駄目"):
         intnt_rmv_cnddts.append("しちゃ駄目")
    elif check_text_terminate_string(line_msg, "しちゃだめ"):
         intnt_rmv_cnddts.append("しちゃだめ")
    elif check_text_terminate_string(line_msg, "しちゃダメ"):
         intnt_rmv_cnddts.append("しちゃダメ")
    elif check_text_terminate_string(line_msg, "がしないように"):
         intnt_rmv_cnddts.append("がしないように")
    elif check_text_terminate_string(line_msg, "がしないよう"):
         intnt_rmv_cnddts.append("がしないよう")
    elif check_text_terminate_string(line_msg, "がするな"):
         intnt_rmv_cnddts.append("がするな")
    elif check_text_terminate_string(line_msg, "がやってはいけない"):
         intnt_rmv_cnddts.append("がやってはいけない")
    elif check_text_terminate_string(line_msg, "がやっちゃいけない"):
         intnt_rmv_cnddts.append("がやっちゃいけない")
    elif check_text_terminate_string(line_msg, "がやっちゃ駄目だ"):
         intnt_rmv_cnddts.append("がやっちゃ駄目だ")
    elif check_text_terminate_string(line_msg, "がやっちゃだめだ"):
         intnt_rmv_cnddts.append("がやっちゃだめだ")
    elif check_text_terminate_string(line_msg, "がやっちゃダメだ"):
         intnt_rmv_cnddts.append("がやっちゃダメだ")
    elif check_text_terminate_string(line_msg, "がやっちゃ駄目"):
         intnt_rmv_cnddts.append("がやっちゃ駄目")
    elif check_text_terminate_string(line_msg, "がやっちゃだめ"):
         intnt_rmv_cnddts.append("がやっちゃだめ")
    elif check_text_terminate_string(line_msg, "がやっちゃダメ"):
         intnt_rmv_cnddts.append("がやっちゃダメ")
    elif check_text_terminate_string(line_msg, "がしちゃ駄目だ"):
         intnt_rmv_cnddts.append("がしちゃ駄目だ")
    elif check_text_terminate_string(line_msg, "がしちゃだめだ"):
         intnt_rmv_cnddts.append("がしちゃだめだ")
    elif check_text_terminate_string(line_msg, "がしちゃダメだ"):
         intnt_rmv_cnddts.append("がしちゃダメだ")
    elif check_text_terminate_string(line_msg, "がしちゃ駄目"):
         intnt_rmv_cnddts.append("がしちゃ駄目")
    elif check_text_terminate_string(line_msg, "がしちゃだめ"):
         intnt_rmv_cnddts.append("がしちゃだめ")
    elif check_text_terminate_string(line_msg, "がしちゃダメ"):
         intnt_rmv_cnddts.append("がしちゃダメ")
    elif check_text_terminate_string(line_msg, "をしてはいけませんか"):
         intnt_rmv_cnddts.append("をしてはいけませんか")
    elif check_text_terminate_string(line_msg, "をしてはいけないですか"):
         intnt_rmv_cnddts.append("をしてはいけないですか")
    elif check_text_terminate_string(line_msg, "をしてはいけないか"):
         intnt_rmv_cnddts.append("をしてはいけないか")
    elif check_text_terminate_string(line_msg, "はしてはいけませんか"):
         intnt_rmv_cnddts.append("はしてはいけませんか")
    elif check_text_terminate_string(line_msg, "はしてはいけないですか"):
         intnt_rmv_cnddts.append("はしてはいけないですか")
    elif check_text_terminate_string(line_msg, "はしてはいけないか"):
         intnt_rmv_cnddts.append("はしてはいけないか")
    elif check_text_terminate_string(line_msg, "をやってはいけませんか"):
         intnt_rmv_cnddts.append("をやってはいけませんか")
    elif check_text_terminate_string(line_msg, "をやってはいけないですか"):
         intnt_rmv_cnddts.append("をやってはいけないですか")
    elif check_text_terminate_string(line_msg, "をやってはいけないか"):
         intnt_rmv_cnddts.append("をやってはいけないか")
    elif check_text_terminate_string(line_msg, "をやっちゃ駄目か"):
         intnt_rmv_cnddts.append("をやっちゃ駄目か")
    elif check_text_terminate_string(line_msg, "をやっちゃだめか"):
         intnt_rmv_cnddts.append("をやっちゃだめか")
    elif check_text_terminate_string(line_msg, "をやっちゃダメか"):
         intnt_rmv_cnddts.append("をやっちゃダメか")
    elif check_text_terminate_string(line_msg, "をしちゃ駄目ですか"):
         intnt_rmv_cnddts.append("をしちゃ駄目ですか")
    elif check_text_terminate_string(line_msg, "をしちゃだめですか"):
         intnt_rmv_cnddts.append("をしちゃだめですか")
    elif check_text_terminate_string(line_msg, "をしちゃダメですか"):
         intnt_rmv_cnddts.append("をしちゃダメですか")
    elif check_text_terminate_string(line_msg, "はしちゃ駄目ですか"):
         intnt_rmv_cnddts.append("はしちゃ駄目ですか")
    elif check_text_terminate_string(line_msg, "はしちゃだめですか"):
         intnt_rmv_cnddts.append("はしちゃだめですか")
    elif check_text_terminate_string(line_msg, "はしちゃダメですか"):
         intnt_rmv_cnddts.append("はしちゃダメですか")
    elif check_text_terminate_string(line_msg, "をしちゃ駄目か"):
         intnt_rmv_cnddts.append("をしちゃ駄目か")
    elif check_text_terminate_string(line_msg, "をしちゃだめか"):
         intnt_rmv_cnddts.append("をしちゃだめか")
    elif check_text_terminate_string(line_msg, "をしちゃダメか"):
         intnt_rmv_cnddts.append("をしちゃダメか")
    elif check_text_terminate_string(line_msg, "はしちゃ駄目か"):
         intnt_rmv_cnddts.append("はしちゃ駄目か")
    elif check_text_terminate_string(line_msg, "はしちゃだめか"):
         intnt_rmv_cnddts.append("はしちゃだめか")
    elif check_text_terminate_string(line_msg, "はしちゃダメか"):
         intnt_rmv_cnddts.append("はしちゃダメか")
    elif check_text_terminate_string(line_msg, "しちゃ駄目か"):
         intnt_rmv_cnddts.append("しちゃ駄目か")
    elif check_text_terminate_string(line_msg, "しちゃだめか"):
         intnt_rmv_cnddts.append("しちゃだめか")
    elif check_text_terminate_string(line_msg, "しちゃダメか"):
         intnt_rmv_cnddts.append("しちゃダメか")
    elif check_text_terminate_string(line_msg, "がしてはいけませんか"):
         intnt_rmv_cnddts.append("がしてはいけませんか")
    elif check_text_terminate_string(line_msg, "がしてはいけないか"):
         intnt_rmv_cnddts.append("がしてはいけないか")
    elif check_text_terminate_string(line_msg, "がやってはいけないか"):
         intnt_rmv_cnddts.append("がやってはいけないか")
    elif check_text_terminate_string(line_msg, "がやっちゃ駄目か"):
         intnt_rmv_cnddts.append("がやっちゃ駄目か")
    elif check_text_terminate_string(line_msg, "がやっちゃだめか"):
         intnt_rmv_cnddts.append("がやっちゃだめか")
    elif check_text_terminate_string(line_msg, "がやっちゃダメか"):
         intnt_rmv_cnddts.append("がやっちゃダメか")
    elif check_text_terminate_string(line_msg, "がしちゃ駄目か"):
         intnt_rmv_cnddts.append("がしちゃ駄目か")
    elif check_text_terminate_string(line_msg, "がしちゃだめか"):
         intnt_rmv_cnddts.append("がしちゃだめか")
    elif check_text_terminate_string(line_msg, "がしちゃダメか"):
         intnt_rmv_cnddts.append("がしちゃダメか")
    elif check_text_terminate_string(line_msg, "をして下さい"):
         intnt_rmv_cnddts.append("をして下さい")
    elif check_text_terminate_string(line_msg, "をしてください"):
         intnt_rmv_cnddts.append("をしてください")
    elif check_text_terminate_string(line_msg, "をしてくれ"):
         intnt_rmv_cnddts.append("をしてくれ")
    elif check_text_terminate_string(line_msg, "をして"):
         intnt_rmv_cnddts.append("をして")
    elif check_text_terminate_string(line_msg, "はして下さい"):
         intnt_rmv_cnddts.append("はして下さい")
    elif check_text_terminate_string(line_msg, "はしてください"):
         intnt_rmv_cnddts.append("はしてください")
    elif check_text_terminate_string(line_msg, "して下さい"):
         intnt_rmv_cnddts.append("して下さい")
    elif check_text_terminate_string(line_msg, "してください"):
         intnt_rmv_cnddts.append("してください")
    elif check_text_terminate_string(line_msg, "下さい"):
         intnt_rmv_cnddts.append("下さい")
    elif check_text_terminate_string(line_msg, "ください"):
         intnt_rmv_cnddts.append("ください")
    elif check_text_terminate_string(line_msg, "はしてくれ"):
         intnt_rmv_cnddts.append("はしてくれ")
    elif check_text_terminate_string(line_msg, "はして"):
         intnt_rmv_cnddts.append("はして")
    elif check_text_terminate_string(line_msg, "してくれ"):
         intnt_rmv_cnddts.append("してくれ")
    elif check_text_terminate_string(line_msg, "くれ"):
         intnt_rmv_cnddts.append("くれ")
    elif check_text_terminate_string(line_msg, "がして下さい"):
         intnt_rmv_cnddts.append("がして下さい")
    elif check_text_terminate_string(line_msg, "がしてください"):
         intnt_rmv_cnddts.append("がしてください")
    elif check_text_terminate_string(line_msg, "がしてくれ"):
         intnt_rmv_cnddts.append("がしてくれ")
    elif check_text_terminate_string(line_msg, "がして"):
         intnt_rmv_cnddts.append("がして")
    elif check_text_terminate_string(line_msg, "をして下さいますか"):
         intnt_rmv_cnddts.append("をして下さいますか")
    elif check_text_terminate_string(line_msg, "をしてくださいますか"):
         intnt_rmv_cnddts.append("をしてくださいますか")
    elif check_text_terminate_string(line_msg, "して下さいますか"):
         intnt_rmv_cnddts.append("して下さいますか")
    elif check_text_terminate_string(line_msg, "してくださいますか"):
         intnt_rmv_cnddts.append("してくださいますか")
    elif check_text_terminate_string(line_msg, "下さいますか"):
         intnt_rmv_cnddts.append("下さいますか")
    elif check_text_terminate_string(line_msg, "くださいますか"):
         intnt_rmv_cnddts.append("くださいますか")
    elif check_text_terminate_string(line_msg, "をしてくれますか"):
         intnt_rmv_cnddts.append("をしてくれますか")
    elif check_text_terminate_string(line_msg, "をしてくれますか"):
         intnt_rmv_cnddts.append("をしてくれますか")
    elif check_text_terminate_string(line_msg, "はしてくれますか"):
         intnt_rmv_cnddts.append("はしてくれますか")
    elif check_text_terminate_string(line_msg, "くれますか"):
         intnt_rmv_cnddts.append("くれますか")
    elif check_text_terminate_string(line_msg, "してくれるか"):
         intnt_rmv_cnddts.append("してくれるか")
    elif check_text_terminate_string(line_msg, "くれるか"):
         intnt_rmv_cnddts.append("くれるか")
    elif check_text_terminate_string(line_msg, "をやって下さいますか"):
         intnt_rmv_cnddts.append("をやって下さいますか")
    elif check_text_terminate_string(line_msg, "をやってくださいますか"):
         intnt_rmv_cnddts.append("をやってくださいますか")
    elif check_text_terminate_string(line_msg, "をやってくれますか"):
         intnt_rmv_cnddts.append("をやってくれますか")
    elif check_text_terminate_string(line_msg, "をやってくれるか"):
         intnt_rmv_cnddts.append("をやってくれるか")
    elif check_text_terminate_string(line_msg, "はやって下さいますか"):
         intnt_rmv_cnddts.append("はやって下さいますか")
    elif check_text_terminate_string(line_msg, "はやってくださいますか"):
         intnt_rmv_cnddts.append("はやってくださいますか")
    elif check_text_terminate_string(line_msg, "はやってくれますか"):
         intnt_rmv_cnddts.append("はやってくれますか")
    elif check_text_terminate_string(line_msg, "はやってくれるか"):
         intnt_rmv_cnddts.append("はやってくれるか")
    elif check_text_terminate_string(line_msg, "をして下さいますか"):
         intnt_rmv_cnddts.append("をして下さいますか")
    elif check_text_terminate_string(line_msg, "をしてくださいますか"):
         intnt_rmv_cnddts.append("をしてくださいますか")
    elif check_text_terminate_string(line_msg, "して下さいますか"):
         intnt_rmv_cnddts.append("して下さいますか")
    elif check_text_terminate_string(line_msg, "してくださいますか"):
         intnt_rmv_cnddts.append("してくださいますか")
    elif check_text_terminate_string(line_msg, "をしてくれますか"):
         intnt_rmv_cnddts.append("をしてくれますか")
    elif check_text_terminate_string(line_msg, "をしてくれますか"):
         intnt_rmv_cnddts.append("をしてくれますか")
    elif check_text_terminate_string(line_msg, "はしてくれますか"):
         intnt_rmv_cnddts.append("はしてくれますか")
    elif check_text_terminate_string(line_msg, "してくれるか"):
         intnt_rmv_cnddts.append("してくれるか")
    elif check_text_terminate_string(line_msg, "をやって下さいますか"):
         intnt_rmv_cnddts.append("をやって下さいますか")
    elif check_text_terminate_string(line_msg, "をやってくださいますか"):
         intnt_rmv_cnddts.append("をやってくださいますか")
    elif check_text_terminate_string(line_msg, "をやってくれますか"):
         intnt_rmv_cnddts.append("をやってくれますか")
    elif check_text_terminate_string(line_msg, "をやってくれるか"):
         intnt_rmv_cnddts.append("をやってくれるか")
    elif check_text_terminate_string(line_msg, "はやって下さいますか"):
         intnt_rmv_cnddts.append("はやって下さいますか")
    elif check_text_terminate_string(line_msg, "はやってくださいますか"):
         intnt_rmv_cnddts.append("はやってくださいますか")
    elif check_text_terminate_string(line_msg, "はやってくれますか"):
         intnt_rmv_cnddts.append("はやってくれますか")
    elif check_text_terminate_string(line_msg, "はやってくれるか"):
         intnt_rmv_cnddts.append("はやってくれるか")
    elif check_text_terminate_string(line_msg, "がして下さいますか"):
         intnt_rmv_cnddts.append("がして下さいますか")
    elif check_text_terminate_string(line_msg, "がしてくださいますか"):
         intnt_rmv_cnddts.append("がしてくださいますか")
    elif check_text_terminate_string(line_msg, "がしてくれますか"):
         intnt_rmv_cnddts.append("がしてくれますか")
    elif check_text_terminate_string(line_msg, "がやってくれますか"):
         intnt_rmv_cnddts.append("がやってくれますか")
    elif check_text_terminate_string(line_msg, "がやってくれるか"):
         intnt_rmv_cnddts.append("がやってくれるか")
    elif check_text_terminate_string(line_msg, "がして下さいますか"):
         intnt_rmv_cnddts.append("がして下さいますか")
    elif check_text_terminate_string(line_msg, "がしてくださいますか"):
         intnt_rmv_cnddts.append("がしてくださいますか")
    elif check_text_terminate_string(line_msg, "がしてくれますか"):
         intnt_rmv_cnddts.append("がしてくれますか")
    elif check_text_terminate_string(line_msg, "がやってくれますか"):
         intnt_rmv_cnddts.append("がやってくれますか")
    elif check_text_terminate_string(line_msg, "がやってくれるか"):
         intnt_rmv_cnddts.append("がやってくれるか")
    elif check_text_terminate_string(line_msg, "をお願い致します"):
         intnt_rmv_cnddts.append("をお願い致します")
    elif check_text_terminate_string(line_msg, "をお願いいたします"):
         intnt_rmv_cnddts.append("をお願いいたします")
    elif check_text_terminate_string(line_msg, "をお願いします"):
         intnt_rmv_cnddts.append("をお願いします")
    elif check_text_terminate_string(line_msg, "をお願い"):
         intnt_rmv_cnddts.append("をお願い")
    elif check_text_terminate_string(line_msg, "しいです"):
         intnt_rmv_cnddts.append("しいです")
    elif check_text_terminate_string(line_msg, "だ"):
         intnt_rmv_cnddts.append("だ")
    elif check_text_terminate_string(line_msg, "でしょう"):
         intnt_rmv_cnddts.append("でしょう")
    elif check_text_terminate_string(line_msg, "だろう"):
         intnt_rmv_cnddts.append("だろう")
    elif check_text_terminate_string(line_msg, "だろ"):
         intnt_rmv_cnddts.append("だろ")
    elif check_text_terminate_string(line_msg, "ではないでしょう"):
         intnt_rmv_cnddts.append("ではないでしょう")
    elif check_text_terminate_string(line_msg, "ではないだろう"):
         intnt_rmv_cnddts.append("ではないだろう")
    elif check_text_terminate_string(line_msg, "ではないだろ"):
         intnt_rmv_cnddts.append("ではないだろ")
    elif check_text_terminate_string(line_msg, "でしょうか"):
         intnt_rmv_cnddts.append("でしょうか")
    elif check_text_terminate_string(line_msg, "だろうか"):
         intnt_rmv_cnddts.append("だろうか")
    elif check_text_terminate_string(line_msg, "だろか"):
         intnt_rmv_cnddts.append("だろか")
    elif check_text_terminate_string(line_msg, "ではないでしょうか"):
         intnt_rmv_cnddts.append("ではないでしょうか")
    elif check_text_terminate_string(line_msg, "ではないだろうか"):
         intnt_rmv_cnddts.append("ではないだろうか")
    elif check_text_terminate_string(line_msg, "ではないだろか"):
         intnt_rmv_cnddts.append("ではないだろか")
    elif check_text_terminate_string(line_msg, "だそうです"):
         intnt_rmv_cnddts.append("だそうです")
    elif check_text_terminate_string(line_msg, "だそう"):
         intnt_rmv_cnddts.append("だそう")
    elif check_text_terminate_string(line_msg, "ではないそうです"):
         intnt_rmv_cnddts.append("ではないそうです")
    elif check_text_terminate_string(line_msg, "ではないそう"):
         intnt_rmv_cnddts.append("ではないそう")
    elif check_text_terminate_string(line_msg, "はいます"):
         intnt_rmv_cnddts.append("はいます")
    elif check_text_terminate_string(line_msg, "はいる"):
         intnt_rmv_cnddts.append("はいる")
    elif check_text_terminate_string(line_msg, "がいます"):
         intnt_rmv_cnddts.append("がいます")
    elif check_text_terminate_string(line_msg, "がいる"):
         intnt_rmv_cnddts.append("がいる")
    elif check_text_terminate_string(line_msg, "はいません"):
         intnt_rmv_cnddts.append("はいません")
    elif check_text_terminate_string(line_msg, "はいない"):
         intnt_rmv_cnddts.append("はいない")
    elif check_text_terminate_string(line_msg, "がいません"):
         intnt_rmv_cnddts.append("がいません")
    elif check_text_terminate_string(line_msg, "がいない"):
         intnt_rmv_cnddts.append("がいない")
    elif check_text_terminate_string(line_msg, "はいますか"):
         intnt_rmv_cnddts.append("はいますか")
    elif check_text_terminate_string(line_msg, "はいるか"):
         intnt_rmv_cnddts.append("はいるか")
    elif check_text_terminate_string(line_msg, "がいますか"):
         intnt_rmv_cnddts.append("がいますか")
    elif check_text_terminate_string(line_msg, "がいるか"):
         intnt_rmv_cnddts.append("がいるか")
    elif check_text_terminate_string(line_msg, "はいませんか"):
         intnt_rmv_cnddts.append("はいませんか")
    elif check_text_terminate_string(line_msg, "はいないか"):
         intnt_rmv_cnddts.append("はいないか")
    elif check_text_terminate_string(line_msg, "がいませんか"):
         intnt_rmv_cnddts.append("がいませんか")
    elif check_text_terminate_string(line_msg, "がいないか"):
         intnt_rmv_cnddts.append("がいないか")
    elif check_text_terminate_string(line_msg, "にいます"):
         intnt_rmv_cnddts.append("にいます")
    elif check_text_terminate_string(line_msg, "にいる"):
         intnt_rmv_cnddts.append("にいる")
    elif check_text_terminate_string(line_msg, "にいません"):
         intnt_rmv_cnddts.append("にいません")
    elif check_text_terminate_string(line_msg, "にいない"):
         intnt_rmv_cnddts.append("にいない")
    elif check_text_terminate_string(line_msg, "はあります"):
         intnt_rmv_cnddts.append("はあります")
    elif check_text_terminate_string(line_msg, "はある"):
         intnt_rmv_cnddts.append("はある")
    elif check_text_terminate_string(line_msg, "があります"):
         intnt_rmv_cnddts.append("があります")
    elif check_text_terminate_string(line_msg, "がある"):
         intnt_rmv_cnddts.append("がある")
    elif check_text_terminate_string(line_msg, "はありません"):
         intnt_rmv_cnddts.append("はありません")
    elif check_text_terminate_string(line_msg, "はない"):
         intnt_rmv_cnddts.append("はない")
    elif check_text_terminate_string(line_msg, "がありません"):
         intnt_rmv_cnddts.append("がありません")
    elif check_text_terminate_string(line_msg, "がない"):
         intnt_rmv_cnddts.append("がない")
    elif check_text_terminate_string(line_msg, "にいますか"):
         intnt_rmv_cnddts.append("にいますか")
    elif check_text_terminate_string(line_msg, "にいるか"):
         intnt_rmv_cnddts.append("にいるか")
    elif check_text_terminate_string(line_msg, "にいませんか"):
         intnt_rmv_cnddts.append("にいませんか")
    elif check_text_terminate_string(line_msg, "にいないか"):
         intnt_rmv_cnddts.append("にいないか")
    elif check_text_terminate_string(line_msg, "はありますか"):
         intnt_rmv_cnddts.append("はありますか")
    elif check_text_terminate_string(line_msg, "はあるか"):
         intnt_rmv_cnddts.append("はあるか")
    elif check_text_terminate_string(line_msg, "がありますか"):
         intnt_rmv_cnddts.append("がありますか")
    elif check_text_terminate_string(line_msg, "があるか"):
         intnt_rmv_cnddts.append("があるか")
    elif check_text_terminate_string(line_msg, "はありませんか"):
         intnt_rmv_cnddts.append("はありませんか")
    elif check_text_terminate_string(line_msg, "はあるか"):
         intnt_rmv_cnddts.append("はあるか")
    elif check_text_terminate_string(line_msg, "がありませんか"):
         intnt_rmv_cnddts.append("がありませんか")
    elif check_text_terminate_string(line_msg, "がないか"):
         intnt_rmv_cnddts.append("がないか")
    elif check_text_terminate_string(line_msg, "っている"):
         intnt_rmv_cnddts.append("っている")
    elif check_text_terminate_string(line_msg, "ている"):
         intnt_rmv_cnddts.append("ている")
    elif check_text_terminate_string(line_msg, "ってある"):
         intnt_rmv_cnddts.append("ってある")
    elif check_text_terminate_string(line_msg, "ている"):
         intnt_rmv_cnddts.append("ている")
    elif check_text_terminate_string(line_msg, "ってない"):
         intnt_rmv_cnddts.append("ってない")
    elif check_text_terminate_string(line_msg, "てない"):
         intnt_rmv_cnddts.append("てない")
    elif check_text_terminate_string(line_msg, "で御座います"):
         intnt_rmv_cnddts.append("で御座います")
    elif check_text_terminate_string(line_msg, "でございます"):
         intnt_rmv_cnddts.append("でございます")
    elif check_text_terminate_string(line_msg, "であります"):
         intnt_rmv_cnddts.append("であります")
    elif check_text_terminate_string(line_msg, "です"):
         intnt_rmv_cnddts.append("です")
    elif check_text_terminate_string(line_msg, "では御座いません"):
         intnt_rmv_cnddts.append("では御座いません")
    elif check_text_terminate_string(line_msg, "ではございません"):
         intnt_rmv_cnddts.append("ではございません")
    elif check_text_terminate_string(line_msg, "ではありません"):
         intnt_rmv_cnddts.append("ではありません")
    elif check_text_terminate_string(line_msg, "ではないです"):
         intnt_rmv_cnddts.append("ではないです")
    elif check_text_terminate_string(line_msg, "で御座いますか"):
         intnt_rmv_cnddts.append("で御座いますか")
    elif check_text_terminate_string(line_msg, "でございますか"):
         intnt_rmv_cnddts.append("でございますか")
    elif check_text_terminate_string(line_msg, "でありますか"):
         intnt_rmv_cnddts.append("でありますか")
    elif check_text_terminate_string(line_msg, "ですか"):
         intnt_rmv_cnddts.append("ですか")
    elif check_text_terminate_string(line_msg, "では御座いませんか"):
         intnt_rmv_cnddts.append("では御座いませんか")
    elif check_text_terminate_string(line_msg, "ではございませんか"):
         intnt_rmv_cnddts.append("ではございませんか")
    elif check_text_terminate_string(line_msg, "ではありませんか"):
         intnt_rmv_cnddts.append("ではありませんか")
    elif check_text_terminate_string(line_msg, "ではないですか"):
         intnt_rmv_cnddts.append("ではないですか")
    elif check_text_terminate_string(line_msg, "で御座いましたか"):
         intnt_rmv_cnddts.append("で御座いましたか")
    elif check_text_terminate_string(line_msg, "でございましたか"):
         intnt_rmv_cnddts.append("でございましたか")
    elif check_text_terminate_string(line_msg, "でありましたか"):
         intnt_rmv_cnddts.append("でありましたか")
    elif check_text_terminate_string(line_msg, "でしたか"):
         intnt_rmv_cnddts.append("でしたか")
    elif check_text_terminate_string(line_msg, "だったか"):
         intnt_rmv_cnddts.append("だったか")
    elif check_text_terminate_string(line_msg, "という事で御座います"):
         intnt_rmv_cnddts.append("という事で御座います")
    elif check_text_terminate_string(line_msg, "という事でございます"):
         intnt_rmv_cnddts.append("という事でございます")
    elif check_text_terminate_string(line_msg, "ということで御座います"):
         intnt_rmv_cnddts.append("ということで御座います")
    elif check_text_terminate_string(line_msg, "ということでございます"):
         intnt_rmv_cnddts.append("ということでございます")
    elif check_text_terminate_string(line_msg, "という事であります"):
         intnt_rmv_cnddts.append("という事であります")
    elif check_text_terminate_string(line_msg, "ということであります"):
         intnt_rmv_cnddts.append("ということであります")
    elif check_text_terminate_string(line_msg, "という事です"):
         intnt_rmv_cnddts.append("という事です")
    elif check_text_terminate_string(line_msg, "ということです"):
         intnt_rmv_cnddts.append("ということです")
    elif check_text_terminate_string(line_msg, "って事です"):
         intnt_rmv_cnddts.append("って事です")
    elif check_text_terminate_string(line_msg, "ってことです"):
         intnt_rmv_cnddts.append("ってことです")
    elif check_text_terminate_string(line_msg, "という事では御座いません"):
         intnt_rmv_cnddts.append("という事では御座いません")
    elif check_text_terminate_string(line_msg, "という事ではございません"):
         intnt_rmv_cnddts.append("という事ではございません")
    elif check_text_terminate_string(line_msg, "ということでは御座いません"):
         intnt_rmv_cnddts.append("ということでは御座いません")
    elif check_text_terminate_string(line_msg, "ということではございません"):
         intnt_rmv_cnddts.append("ということではございません")
    elif check_text_terminate_string(line_msg, "という事ではありません"):
         intnt_rmv_cnddts.append("という事ではありません")
    elif check_text_terminate_string(line_msg, "ということではありません"):
         intnt_rmv_cnddts.append("ということではありません")
    elif check_text_terminate_string(line_msg, "って事ではないです"):
         intnt_rmv_cnddts.append("って事ではないです")
    elif check_text_terminate_string(line_msg, "ってことではないです"):
         intnt_rmv_cnddts.append("ってことではないです")
    elif check_text_terminate_string(line_msg, "という事で御座いますか"):
         intnt_rmv_cnddts.append("という事で御座いますか")
    elif check_text_terminate_string(line_msg, "という事でございますか"):
         intnt_rmv_cnddts.append("という事でございますか")
    elif check_text_terminate_string(line_msg, "ということで御座いますか"):
         intnt_rmv_cnddts.append("ということで御座いますか")
    elif check_text_terminate_string(line_msg, "ということでございますか"):
         intnt_rmv_cnddts.append("ということでございますか")
    elif check_text_terminate_string(line_msg, "という事でありますか"):
         intnt_rmv_cnddts.append("という事でありますか")
    elif check_text_terminate_string(line_msg, "ということでありますか"):
         intnt_rmv_cnddts.append("ということでありますか")
    elif check_text_terminate_string(line_msg, "という事ですか"):
         intnt_rmv_cnddts.append("という事ですか")
    elif check_text_terminate_string(line_msg, "ということですか"):
         intnt_rmv_cnddts.append("ということですか")
    elif check_text_terminate_string(line_msg, "って事ですか"):
         intnt_rmv_cnddts.append("って事ですか")
    elif check_text_terminate_string(line_msg, "ってことですか"):
         intnt_rmv_cnddts.append("ってことですか")
    elif check_text_terminate_string(line_msg, "という事では御座いませんか"):
         intnt_rmv_cnddts.append("という事では御座いませんか")
    elif check_text_terminate_string(line_msg, "という事ではございませんか"):
         intnt_rmv_cnddts.append("という事ではございませんか")
    elif check_text_terminate_string(line_msg, "ということでは御座いませんか"):
         intnt_rmv_cnddts.append("ということでは御座いませんか")
    elif check_text_terminate_string(line_msg, "ということではございませんか"):
         intnt_rmv_cnddts.append("ということではございませんか")
    elif check_text_terminate_string(line_msg, "という事ではありませんか"):
         intnt_rmv_cnddts.append("という事ではありませんか")
    elif check_text_terminate_string(line_msg, "ということではありませんか"):
         intnt_rmv_cnddts.append("ということではありませんか")
    elif check_text_terminate_string(line_msg, "って事ではないのですか"):
         intnt_rmv_cnddts.append("って事ではないのですか")
    elif check_text_terminate_string(line_msg, "ってことではなのですか"):
         intnt_rmv_cnddts.append("ってことではなのですか")
    elif check_text_terminate_string(line_msg, "って事ではないんですか"):
         intnt_rmv_cnddts.append("って事ではないんですか")
    elif check_text_terminate_string(line_msg, "ってことではないんですか"):
         intnt_rmv_cnddts.append("ってことではないんですか")
    elif check_text_terminate_string(line_msg, "は大丈夫です"):
         intnt_rmv_cnddts.append("は大丈夫です")
    elif check_text_terminate_string(line_msg, "は大丈夫だ"):
         intnt_rmv_cnddts.append("は大丈夫だ")
    elif check_text_terminate_string(line_msg, "は大丈夫"):
         intnt_rmv_cnddts.append("は大丈夫")
    elif check_text_terminate_string(line_msg, "は大丈夫ではない"):
         intnt_rmv_cnddts.append("は大丈夫ではない")
    elif check_text_terminate_string(line_msg, "は大丈夫でない"):
         intnt_rmv_cnddts.append("は大丈夫でない")
    elif check_text_terminate_string(line_msg, "は大丈夫じゃない"):
         intnt_rmv_cnddts.append("は大丈夫じゃない")
    elif check_text_terminate_string(line_msg, "は大丈夫でしょうか"):
         intnt_rmv_cnddts.append("は大丈夫でしょうか")
    elif check_text_terminate_string(line_msg, "は大丈夫ですか"):
         intnt_rmv_cnddts.append("は大丈夫ですか")
    elif check_text_terminate_string(line_msg, "は大丈夫か"):
         intnt_rmv_cnddts.append("は大丈夫か")
    elif check_text_terminate_string(line_msg, "は大丈夫ではないのでしょうか"):
         intnt_rmv_cnddts.append("は大丈夫ではないのでしょうか")
    elif check_text_terminate_string(line_msg, "は大丈夫ではないんですか"):
         intnt_rmv_cnddts.append("は大丈夫ではないんですか")
    elif check_text_terminate_string(line_msg, "は大丈夫じゃないんですか"):
         intnt_rmv_cnddts.append("は大丈夫じゃないんですか")
    elif check_text_terminate_string(line_msg, "が必要です"):
         intnt_rmv_cnddts.append("が必要です")
    elif check_text_terminate_string(line_msg, "は必要です"):
         intnt_rmv_cnddts.append("は必要です")
    elif check_text_terminate_string(line_msg, "が必要だ"):
         intnt_rmv_cnddts.append("が必要だ")
    elif check_text_terminate_string(line_msg, "は必要だ"):
         intnt_rmv_cnddts.append("は必要だ")
    elif check_text_terminate_string(line_msg, "が必要"):
         intnt_rmv_cnddts.append("が必要")
    elif check_text_terminate_string(line_msg, "は必要"):
         intnt_rmv_cnddts.append("は必要")
    elif check_text_terminate_string(line_msg, "が要ります"):
         intnt_rmv_cnddts.append("が要ります")
    elif check_text_terminate_string(line_msg, "は要ります"):
         intnt_rmv_cnddts.append("は要ります")
    elif check_text_terminate_string(line_msg, "が要る"):
         intnt_rmv_cnddts.append("が要る")
    elif check_text_terminate_string(line_msg, "は要る"):
         intnt_rmv_cnddts.append("は要る")
    elif check_text_terminate_string(line_msg, "が不要です"):
         intnt_rmv_cnddts.append("が不要です")
    elif check_text_terminate_string(line_msg, "は不要です"):
         intnt_rmv_cnddts.append("は不要です")
    elif check_text_terminate_string(line_msg, "が不要だ"):
         intnt_rmv_cnddts.append("が不要だ")
    elif check_text_terminate_string(line_msg, "は不要だ"):
         intnt_rmv_cnddts.append("は不要だ")
    elif check_text_terminate_string(line_msg, "が不要"):
         intnt_rmv_cnddts.append("が不要")
    elif check_text_terminate_string(line_msg, "は不要"):
         intnt_rmv_cnddts.append("は不要")
    elif check_text_terminate_string(line_msg, "が要りません"):
         intnt_rmv_cnddts.append("が要りません")
    elif check_text_terminate_string(line_msg, "は要りません"):
         intnt_rmv_cnddts.append("は要りません")
    elif check_text_terminate_string(line_msg, "が要らない"):
         intnt_rmv_cnddts.append("が要らない")
    elif check_text_terminate_string(line_msg, "は要らない"):
         intnt_rmv_cnddts.append("は要らない")
    elif check_text_terminate_string(line_msg, "が必要でしょうか"):
         intnt_rmv_cnddts.append("が必要でしょうか")
    elif check_text_terminate_string(line_msg, "は必要でしょうか"):
         intnt_rmv_cnddts.append("は必要でしょうか")
    elif check_text_terminate_string(line_msg, "が必要ですか"):
         intnt_rmv_cnddts.append("が必要ですか")
    elif check_text_terminate_string(line_msg, "は必要ですか"):
         intnt_rmv_cnddts.append("は必要ですか")
    elif check_text_terminate_string(line_msg, "が要りますでしょうか"):
         intnt_rmv_cnddts.append("が要りますでしょうか")
    elif check_text_terminate_string(line_msg, "は要りますでしょうか"):
         intnt_rmv_cnddts.append("は要りますでしょうか")
    elif check_text_terminate_string(line_msg, "が要りますか"):
         intnt_rmv_cnddts.append("が要りますか")
    elif check_text_terminate_string(line_msg, "は要りますか"):
         intnt_rmv_cnddts.append("は要りますか")
    elif check_text_terminate_string(line_msg, "が不要でしょうか"):
         intnt_rmv_cnddts.append("が不要でしょうか")
    elif check_text_terminate_string(line_msg, "は不要でしょうか"):
         intnt_rmv_cnddts.append("は不要でしょうか")
    elif check_text_terminate_string(line_msg, "が不要ですか"):
         intnt_rmv_cnddts.append("が不要ですか")
    elif check_text_terminate_string(line_msg, "は不要ですか"):
         intnt_rmv_cnddts.append("は不要ですか")
    elif check_text_terminate_string(line_msg, "が要りませんか"):
         intnt_rmv_cnddts.append("が要りませんか")
    elif check_text_terminate_string(line_msg, "は要りませんか"):
         intnt_rmv_cnddts.append("は要りませんか")
    elif check_text_terminate_string(line_msg, "が要らないのですか"):
         intnt_rmv_cnddts.append("が要らないのですか")
    elif check_text_terminate_string(line_msg, "は要らないのですか"):
         intnt_rmv_cnddts.append("は要らないのですか")
    elif check_text_terminate_string(line_msg, "が要らないのか"):
         intnt_rmv_cnddts.append("が要らないのか")
    elif check_text_terminate_string(line_msg, "は要らないのか"):
         intnt_rmv_cnddts.append("は要らないのか")
    elif check_text_terminate_string(line_msg, "が要らないか"):
         intnt_rmv_cnddts.append("が要らないか")
    elif check_text_terminate_string(line_msg, "は要らないか"):
         intnt_rmv_cnddts.append("は要らないか")
    elif check_text_terminate_string(line_msg, "という事でしょう"):
         intnt_rmv_cnddts.append("という事でしょう")
    elif check_text_terminate_string(line_msg, "ということでしょう"):
         intnt_rmv_cnddts.append("ということでしょう")
    elif check_text_terminate_string(line_msg, "という事ではないでしょう"):
         intnt_rmv_cnddts.append("という事ではないでしょう")
    elif check_text_terminate_string(line_msg, "ということではないでしょう"):
         intnt_rmv_cnddts.append("ということではないでしょう")
    elif check_text_terminate_string(line_msg, "かも知れないです"):
         intnt_rmv_cnddts.append("かも知れないです")
    elif check_text_terminate_string(line_msg, "かもしれないです"):
         intnt_rmv_cnddts.append("かもしれないです")
    elif check_text_terminate_string(line_msg, "かも知れない"):
         intnt_rmv_cnddts.append("かも知れない")
    elif check_text_terminate_string(line_msg, "かもしれない"):
         intnt_rmv_cnddts.append("かもしれない")
    elif check_text_terminate_string(line_msg, "ではないかも知れないです"):
         intnt_rmv_cnddts.append("ではないかも知れないです")
    elif check_text_terminate_string(line_msg, "ではないかもしれないです"):
         intnt_rmv_cnddts.append("ではないかもしれないです")
    elif check_text_terminate_string(line_msg, "ではないかも知れない"):
         intnt_rmv_cnddts.append("ではないかも知れない")
    elif check_text_terminate_string(line_msg, "ではないかもしれない"):
         intnt_rmv_cnddts.append("ではないかもしれない")
    elif check_text_terminate_string(line_msg, "かと存じ上げます"):
         intnt_rmv_cnddts.append("かと存じ上げます")
    elif check_text_terminate_string(line_msg, "と存じます"):
         intnt_rmv_cnddts.append("と存じます")
    elif check_text_terminate_string(line_msg, "かと思います"):
         intnt_rmv_cnddts.append("かと思います")
    elif check_text_terminate_string(line_msg, "と思います"):
         intnt_rmv_cnddts.append("と思います")
    elif check_text_terminate_string(line_msg, "と申します"):
         intnt_rmv_cnddts.append("と申します")
    elif check_text_terminate_string(line_msg, "と言います"):
         intnt_rmv_cnddts.append("と言います")
    elif check_text_terminate_string(line_msg, "とは思っています"):
         intnt_rmv_cnddts.append("とは思っています")
    elif check_text_terminate_string(line_msg, "とは思ってます"):
         intnt_rmv_cnddts.append("とは思ってます")
    elif check_text_terminate_string(line_msg, "とは思っている"):
         intnt_rmv_cnddts.append("とは思っている")
    elif check_text_terminate_string(line_msg, "とは思ってる"):
         intnt_rmv_cnddts.append("とは思ってる")
    elif check_text_terminate_string(line_msg, "とは思う"):
         intnt_rmv_cnddts.append("とは思う")
    elif check_text_terminate_string(line_msg, "と思っています"):
         intnt_rmv_cnddts.append("と思っています")
    elif check_text_terminate_string(line_msg, "と思ってます"):
         intnt_rmv_cnddts.append("と思ってます")
    elif check_text_terminate_string(line_msg, "と思っている"):
         intnt_rmv_cnddts.append("と思っている")
    elif check_text_terminate_string(line_msg, "と思ってる"):
         intnt_rmv_cnddts.append("と思ってる")
    elif check_text_terminate_string(line_msg, "と思う"):
         intnt_rmv_cnddts.append("と思う")
    elif check_text_terminate_string(line_msg, "とは思っていません"):
         intnt_rmv_cnddts.append("とは思っていません")
    elif check_text_terminate_string(line_msg, "とは思ってません"):
         intnt_rmv_cnddts.append("とは思ってません")
    elif check_text_terminate_string(line_msg, "とは思っていない"):
         intnt_rmv_cnddts.append("とは思っていない")
    elif check_text_terminate_string(line_msg, "とは思ってない"):
         intnt_rmv_cnddts.append("とは思ってない")
    elif check_text_terminate_string(line_msg, "とは思わない"):
         intnt_rmv_cnddts.append("とは思わない")
    elif check_text_terminate_string(line_msg, "と思っていません"):
         intnt_rmv_cnddts.append("と思っていません")
    elif check_text_terminate_string(line_msg, "と思ってません"):
         intnt_rmv_cnddts.append("と思ってません")
    elif check_text_terminate_string(line_msg, "と思っていない"):
         intnt_rmv_cnddts.append("と思っていない")
    elif check_text_terminate_string(line_msg, "と思ってない"):
         intnt_rmv_cnddts.append("と思ってない")
    elif check_text_terminate_string(line_msg, "と思わない"):
         intnt_rmv_cnddts.append("と思わない")
    elif check_text_terminate_string(line_msg, "とは思っていました"):
         intnt_rmv_cnddts.append("とは思っていました")
    elif check_text_terminate_string(line_msg, "とは思ってました"):
         intnt_rmv_cnddts.append("とは思ってました")
    elif check_text_terminate_string(line_msg, "とは思っていた"):
         intnt_rmv_cnddts.append("とは思っていた")
    elif check_text_terminate_string(line_msg, "とは思ってた"):
         intnt_rmv_cnddts.append("とは思ってた")
    elif check_text_terminate_string(line_msg, "と思っていました"):
         intnt_rmv_cnddts.append("と思っていました")
    elif check_text_terminate_string(line_msg, "と思ってました"):
         intnt_rmv_cnddts.append("と思ってました")
    elif check_text_terminate_string(line_msg, "と思っていた"):
         intnt_rmv_cnddts.append("と思っていた")
    elif check_text_terminate_string(line_msg, "と思ってた"):
         intnt_rmv_cnddts.append("と思ってた")
    elif check_text_terminate_string(line_msg, "とは思っていませんでした"):
         intnt_rmv_cnddts.append("とは思っていませんでした")
    elif check_text_terminate_string(line_msg, "とは思っていなかった"):
         intnt_rmv_cnddts.append("とは思っていなかった")
    elif check_text_terminate_string(line_msg, "とは思ってなかった"):
         intnt_rmv_cnddts.append("とは思ってなかった")
    elif check_text_terminate_string(line_msg, "と思っていませんでした"):
         intnt_rmv_cnddts.append("と思っていませんでした")
    elif check_text_terminate_string(line_msg, "と思っていなかった"):
         intnt_rmv_cnddts.append("と思っていなかった")
    elif check_text_terminate_string(line_msg, "と思ってなかった"):
         intnt_rmv_cnddts.append("と思ってなかった")
    elif check_text_terminate_string(line_msg, "らしいです"):
         intnt_rmv_cnddts.append("らしいです")
    elif check_text_terminate_string(line_msg, "らしい"):
         intnt_rmv_cnddts.append("らしい")
    elif check_text_terminate_string(line_msg, "らしくないです"):
         intnt_rmv_cnddts.append("らしくないです")
    elif check_text_terminate_string(line_msg, "らしくない"):
         intnt_rmv_cnddts.append("らしくない")
    elif check_text_terminate_string(line_msg, "とは何でしょうか"):
         intnt_rmv_cnddts.append("とは何でしょうか")
    elif check_text_terminate_string(line_msg, "とはなんでしょうか"):
         intnt_rmv_cnddts.append("とはなんでしょうか")
    elif check_text_terminate_string(line_msg, "とは何ですか"):
         intnt_rmv_cnddts.append("とは何ですか")
    elif check_text_terminate_string(line_msg, "とはなんですか"):
         intnt_rmv_cnddts.append("とはなんですか")
    elif check_text_terminate_string(line_msg, "とは何なのか"):
         intnt_rmv_cnddts.append("とは何なのか")
    elif check_text_terminate_string(line_msg, "とはなんなのか"):
         intnt_rmv_cnddts.append("とはなんなのか")
    elif check_text_terminate_string(line_msg, "とは何か"):
         intnt_rmv_cnddts.append("とは何か")
    elif check_text_terminate_string(line_msg, "とはなにか"):
         intnt_rmv_cnddts.append("とはなにか")
    elif check_text_terminate_string(line_msg, "とは何"):
         intnt_rmv_cnddts.append("とは何")
    elif check_text_terminate_string(line_msg, "とはなに"):
         intnt_rmv_cnddts.append("とはなに")
    elif check_text_terminate_string(line_msg, "とは"):
         intnt_rmv_cnddts.append("とは")
    elif check_text_terminate_string(line_msg, "でございます"):
         intnt_rmv_cnddts.append("でございます")
    elif check_text_terminate_string(line_msg, "にございます"):
         intnt_rmv_cnddts.append("にございます")
    elif check_text_terminate_string(line_msg, "となります"):
         intnt_rmv_cnddts.append("となります")
    elif check_text_terminate_string(line_msg, "になります"):
         intnt_rmv_cnddts.append("になります")
    elif check_text_terminate_string(line_msg, "にありまして"):
         intnt_rmv_cnddts.append("にありまして")
    elif check_text_terminate_string(line_msg, "におりまして"):
         intnt_rmv_cnddts.append("におりまして")
    elif check_text_terminate_string(line_msg, "がありまして"):
         intnt_rmv_cnddts.append("がありまして")
    elif check_text_terminate_string(line_msg, "がおりまして"):
         intnt_rmv_cnddts.append("がおりまして")
    elif check_text_terminate_string(line_msg, "ですので"):
         intnt_rmv_cnddts.append("ですので")
    elif check_text_terminate_string(line_msg, "なので"):
         intnt_rmv_cnddts.append("なので")
    elif check_text_terminate_string(line_msg, "ので"):
         intnt_rmv_cnddts.append("ので")
    elif check_text_terminate_string(line_msg, "なものでして"):
         intnt_rmv_cnddts.append("なものでして")
    elif check_text_terminate_string(line_msg, "なもので"):
         intnt_rmv_cnddts.append("なもので")
    elif check_text_terminate_string(line_msg, "でして"):
         intnt_rmv_cnddts.append("でして")

    #取得した削除候補の中から実際に削除するコンテントを決定して、これを呼出し元に引渡しをする
    intnt_rmv_cnddts_tmp = []
    for intnt in intnt_rmv_cnddts:
        intnt_rmv_cnddts_tmp.append([len(intnt), intnt])
    if  len(intnt_rmv_cnddts_tmp) == 0:
        rmvd_intnt_msg = line_msg
        return rmvd_intnt_msg
    if  len(intnt_rmv_cnddts_tmp) == 1:
        intnt_tmp      = intnt_rmv_cnddts_tmp[0][1]
        rmvd_intnt_msg = re.sub(intnt_tmp, "", line_msg)
        return rmvd_intnt_msg
    idx         = 0
    intnt_tmp = ""
    while len(intnt_rmv_cnddts_tmp) > (idx+1):
           if intnt_rmv_cnddts_tmp[idx+1][0] > intnt_rmv_cnddts_tmp[idx][0]:
              intnt_tmp = intnt_rmv_cnddts_tmp[idx+1][1]
              idx = idx + 1
           else:
              continue
    rmvd_intnt_msg = re.sub(intnt_tmp, "", line_msg)
    return rmvd_intnt_msg


#ユーザーから送られるLINEメッセージがギャグ＆声帯模写だったとして、これからインテント(＝発話の意図するもの)を抽出する
def extract_intent_from_gag_and_vocalcordcopy(line_msg):
    #ギャグ＆声帯模写＆その他となっているメッセージからインテントを抽出して、これを呼出し元に引渡しをする
    if   (line_msg == "はい ひょっこりはん" or
          line_msg == "はいひょっこりはん" or
          line_msg == "プレゼント フォー 肩幅" or
          line_msg == "プレゼントフォー肩幅" or
          line_msg == "うぃーん合唱団" or
          line_msg == "早く大人になれ 膝小僧" or
          line_msg == "早く大人になれ膝小僧" or
          line_msg == "おったまげ" or
          line_msg == "おったまげー" or
          line_msg == "おったまげ～" or
          line_msg == "しもしも" or
          line_msg == "しもしも？" or
          line_msg == "マンモスうれぴー" or
          line_msg == "マンモスうれぴ～" or
          line_msg == "湯飲みじゃなくて ホタルを守る" or
          line_msg == "湯飲みじゃなくてホタルを守る" or
          line_msg == "ウーパールーパー" or
          line_msg == "スフィンクス" or
          line_msg == "しゃか" or
          line_msg == "ホップステップ キャンプ" or
          line_msg == "ホップステップキャンプ" or
          line_msg == "落ち着いていきや" or
          line_msg == "落ち着いていきやー" or
          line_msg == "落ち着いていきや～" or
          line_msg == "PPAP" or
          line_msg == "PPAP!" or
          line_msg == "PPAP！" or
          line_msg == "パーフェクト ヒューマン" or
          line_msg == "パーフェクトヒューマン" or
          line_msg == "ボク ミッキーだよ" or
          line_msg == "ボクミッキーだよ" or
          line_msg == "あのね 芦田愛菜だよ" or
          line_msg == "あのね芦田愛菜だよ" or
          line_msg == "ピカピカ" or
          line_msg == "ピカチュウ" or
          line_msg == "ブンブン ハローYouTube" or
          line_msg == "ブンブンハローYouTube" or
          line_msg == "ブンブン ハロー" or
          line_msg == "ブンブンハロー" or
          line_msg == "ぶんぶん はろー" or
          line_msg == "ぶんぶんはろー" or
          line_msg == "ダンカン コノヤロ！" or
          line_msg == "ダンカンコノヤロ！" or
          line_msg == "大阪名物 パチパチパンチ" or
          line_msg == "大阪名物パチパチパンチ" or
          line_msg == "パチパチパンチ" or
          line_msg == "大阪名物 パチパチパンチ！" or
          line_msg == "大阪名物パチパチパンチ！" or
          line_msg == "パチパチパンチ！" or
          line_msg == "かいーの" or
          line_msg == "かい～の" or
          line_msg == "かいーのー" or
          line_msg == "かい～の～" or
          line_msg == "バカちゃいまんねん アホでんねん" or
          line_msg == "バカちゃいまんねんアホでんねん" or
          line_msg == "アホでんねん" or
          line_msg == "おっぱっぴー" or
          line_msg == "オッパッピー" or
          line_msg == "おっぱっぴ～" or
          line_msg == "オッパッピ～" or
          line_msg == "ぴぃやー" or
          line_msg == "ピィヤー" or
          line_msg == "ぴぃや～" or
          line_msg == "ピィヤ～" or
          line_msg == "俺の武勇伝" or
          line_msg == "おれの武勇伝" or
          line_msg == "オレの武勇伝" or
          line_msg == "武勇伝" or
          line_msg == "俺の武勇伝！" or
          line_msg == "おれの武勇伝！" or
          line_msg == "オレの武勇伝！" or
          line_msg == "武勇伝！" or
          line_msg == "俺の武勇伝を聞きたいか" or
          line_msg == "おれの武勇伝を聞きたいか" or
          line_msg == "オレの武勇伝を聞きたいか" or
          line_msg == "俺の武勇伝を聞きたいか？" or
          line_msg == "おれの武勇伝を聞きたいか？" or
          line_msg == "オレの武勇伝を聞きたいか？" or
          line_msg == "武勇伝 武勇伝" or
          line_msg == "武勇伝武勇伝" or
          line_msg == "武勇伝！ 武勇伝！" or
          line_msg == "武勇伝！武勇伝！" or
          line_msg == "キミ カワイーね" or
          line_msg == "キミカワイーね" or
          line_msg == "キミ カワイーね！" or
          line_msg == "キミカワイーね！" or
          line_msg == "空前絶後" or
          line_msg == "空 前 絶 後" or
          line_msg == "空！ 前！ 絶！ 後！" or
          line_msg == "空！前！絶！後！" or
          line_msg == "空前絶後！" or
          line_msg == "失礼 ぶっこきました" or
          line_msg == "失礼ぶっこきました"):
            extrctd_intnt = "<モノマネ＆ギャグ＆一発芸 人物・キャラクターに基づいて>"
    elif (line_msg == "にゃー にゃー" or
          line_msg == "にゃーにゃー" or
          line_msg == "ニャー ニャー" or
          line_msg == "ニャーニャー" or
          line_msg == "にゃ" or
          line_msg == "ニャ" or
          line_msg == "にゃー" or
          line_msg == "ニャー" or
          line_msg == "にゃ～" or
          line_msg == "ニャ～" or
          line_msg == "わんわん" or
          line_msg == "ワンワン" or
          line_msg == "わん" or
          line_msg == "ワン" or
          line_msg == "しゃー" or
          line_msg == "シャー" or
          line_msg == "ぎゃん ぎゃん" or
          line_msg == "ぎゃんぎゃん" or
          line_msg == "ギャン ギャン" or
          line_msg == "ギャンギャン" or
          line_msg == "ぎゃん" or
          line_msg == "ギャン" or
          line_msg == "うほ うほ" or         
          line_msg == "うほうほ" or
          line_msg == "ウホ ウホ" or
          line_msg == "ウホウホ" or
          line_msg == "うほ" or
          line_msg == "ウホ" or
          line_msg == "こけこっこー" or
          line_msg == "コケコッコー" or
          line_msg == "こけ" or
          line_msg == "コケ" or
          line_msg == "がお がおー" or
          line_msg == "がおがおー" or
          line_msg == "ガオ ガオー" or
          line_msg == "ガオガオー" or
          line_msg == "がおー" or
          line_msg == "ガオー" or
          line_msg == "ぶひ ぶひ" or
          line_msg == "ぶひぶひ" or
          line_msg == "ブヒ ブヒ" or
          line_msg == "ブヒブヒ" or
          line_msg == "ぶひ" or
          line_msg == "ブヒ" or
          line_msg == "ちゅん ちゅん" or
          line_msg == "ちゅんちゅん" or
          line_msg == "チュン チュン" or
          line_msg == "チュンチュン" or
          line_msg == "ちゅん" or
          line_msg == "チュン" or
          line_msg == "げろ げろ" or
          line_msg == "げろげろ" or
          line_msg == "ゲロ ゲロ" or
          line_msg == "ゲロゲロ" or
          line_msg == "げろ" or
          line_msg == "ゲロ" or
          line_msg == "げこ げこ" or
          line_msg == "げこげこ" or
          line_msg == "ゲコ ゲコ" or
          line_msg == "ゲコゲコ" or
          line_msg == "げこ" or
          line_msg == "ゲコ" or
          line_msg == "ぶー ぶー" or
          line_msg == "ぶーぶー" or
          line_msg == "ブー ブー" or
          line_msg == "ブーブー" or
          line_msg == "がったん ごっとん" or
          line_msg == "がったんごっとん" or
          line_msg == "ガッタン ゴットン" or
          line_msg == "ガッタンゴットン"):
            extrctd_intnt = "<モノマネ＆声帯模写 擬音・擬態>"
    elif (line_msg == "ぷー" or
          line_msg == "プー" or
          line_msg == "ぷ～" or
          line_msg == "プ～" or
          line_msg == "ぶりぶり" or
          line_msg == "ブリブリ" or
          line_msg == "ごほ ごほ" or
          line_msg == "ごほごほ" or
          line_msg == "ゴホ ゴホ" or
          line_msg == "ゴホゴホ" or
          line_msg == "ごほ" or
          line_msg == "ゴホ" or
          line_msg == "ごほっ ごほっ" or
          line_msg == "ごほっごほっ" or
          line_msg == "ゴホッ ゴホッ" or
          line_msg == "ゴホッゴホッ" or
          line_msg == "ごほっ" or
          line_msg == "ゴホッ" or
          line_msg == "へぶし" or
          line_msg == "ヘブシ" or
          line_msg == "へぶしっ" or
          line_msg == "ヘブシッ" or
          line_msg == "はっくしょん" or
          line_msg == "ハックション"):
            extrctd_intnt = "<生理現象 擬音・擬態>"
      elif (line_msg == "ブー ブー" or
            line_msg == "ブーブー" or
            line_msg == "ブー！ ブー！" or
            line_msg == "ブー！ブー！"):
            extrctd_intnt = "<ブーイング>"
    elif (line_msg == "あのー" or
          line_msg == "あの～" or
          line_msg == "あー" or
          line_msg == "あ～" or
          line_msg == "えーと" or
          line_msg == "え～と" or
          line_msg == "えー" or
          line_msg == "え～" or
          line_msg == "うーん" or
          line_msg == "う～ん" or
          line_msg == "うー" or
          line_msg == "う～"):
            extrctd_intnt = "<フィラー 間の引き延ばし>"
    elif (line_msg == "海" or
          line_msg == "海！" or
          line_msg == "うみ" or
          line_msg == "うみ！" or
          line_msg == "セイ イェーイ" or
          line_msg == "セイ イェーイ！" or
          line_msg == "セイイェーイ" or 
          line_msg == "セイイェーイ！"):
            extrctd_intnt = "<掛合い＝コールアンドレスポンス>"
    else:
            extrctd_intnt = "<その他・不明>"
    return extrctd_intnt


#LINEメッセージが短文＆定型文だったとして、これからインテント(＝発話の意図するもの)を抽出する
def extract_intent_from_short_and_boilerplate(line_msg):
    #短文＆定型文となっているメッセージからインテントを抽出して、これを呼出し元に引渡しをする
    if   (line_msg == "お初にお目にかかります" or
          line_msg == "初めまして" or
          line_msg == "はじめまして"):
            extrctd_intnt = "<挨拶 初対面>"
    elif (line_msg == "やあ" or
          line_msg == "どうも" or
          line_msg == "御免遊ばせ" or
          line_msg == "御免あそばせ" or
          line_msg == "ごめん遊ばせ" or
          line_msg == "ごめんあそばせ" or
          line_msg == "おはよう御座います" or
          line_msg == "おはようございます" or
          line_msg == "おはよう" or
          line_msg == "おはっす" or
          line_msg == "おは" or
          line_msg == "こんにちは" or
          line_msg == "こんにちわ" or
          line_msg == "ちはっす" or
          line_msg == "ちわっす" or
          line_msg == "こんばんは" or
          line_msg == "こんばんわ" or
          line_msg == "ばんわ" or
          line_msg == "ばんは" or
          line_msg == "ばんっす" or
          line_msg == "ばん"):
            extrctd_intnt = "<挨拶 時間帯によるもの>"
    elif (line_msg == "お先に失礼します" or
          line_msg == "それでは失礼します" or
          line_msg == "失礼します" or
          line_msg == "さようなら" or
          line_msg == "サヨウナラ" or
          line_msg == "サヨナラ" or
          line_msg == "また明日"):
            extrctd_intnt = "<挨拶 会社・学校などで>"
    elif (line_msg == "行って参ります" or
          line_msg == "行ってまいります" or
          line_msg == "行ってきます" or
          line_msg == "行きます" or
          line_msg == "行く"):
            extrctd_intnt = "<自宅・会社から出る時の決まり文句>"
    elif (line_msg == "只今戻りました" or
          line_msg == "ただいま戻りました" or
          line_msg == "只今" or
          line_msg == "ただいま" or
          line_msg == "お帰りなさいませ" or
          line_msg == "おかえりなさいませ" or
          line_msg == "お帰りなさい" or
          line_msg == "おかえりなさい"):
            extrctd_intnt = "<自宅・会社に戻る時の決まり文句>"
    elif (line_msg == "少々 お待ち下さい" or
          line_msg == "少々 お待ちください" or
          line_msg == "少々お待ち下さい" or
          line_msg == "少々お待ちください" or
          line_msg == "少し 待って下さい" or
          line_msg == "少し 待ってください" or
          line_msg == "少し待って下さい" or
          line_msg == "少し待ってください" or
          line_msg == "ちょっと待って" or
          line_msg == "チョット待って"):
            extrctd_intnt = "<相手を待たせる時の決まり文句>"
    elif (line_msg == "待っていました" or
          line_msg == "待ってました" or
          line_msg == "待ってた"):
            extrctd_intnt = "<相手に待たされた時の決まり文句>"
    elif (line_msg == "以後気を付けて下さい" or
          line_msg == "以後気を付けてください" or
          line_msg == "気を付けて下さい" or
          line_msg == "気を付けてください" or
          line_msg == "気をつけろ" or
          line_msg == "しっかりしろ" or
          line_msg == "しっかりやれ" or
          line_msg == "こら" or
          line_msg == "コラ"):
            extrctd_intnt = "<注意・叱責する時の決まり文句>"
    elif (line_msg == "以後気を付けます" or
          line_msg == "気を付けます" or
          line_msg == "気をつけます" or
          line_msg == "しっかりします" or
          line_msg == "しっかりやります"):
            extrctd_intnt = "<注意・叱責された時の決まり文句>"
    elif (line_msg == "失礼ですが" or
          line_msg == "失礼" or
          line_msg == "すみません" or
          line_msg == "すいません" or
          line_msg == "おい" or
          line_msg == "ねえ" or
          line_msg == "ねぇ" or
          line_msg == "なあ" or
          line_msg == "なぁ"):
            extrctd_intnt = "<呼掛け>"
    elif (line_msg == "流石ですね" or
          line_msg == "流石です" or
          line_msg == "流石ね" or
          line_msg == "流石" or
          line_msg == "さすがですね" or
          line_msg == "さすがです" or
          line_msg == "さすがね" or
          line_msg == "さすが" or
          line_msg == "凄いですね" or
          line_msg == "凄いです" or
          line_msg == "凄いね" or
          line_msg == "凄い" or
          line_msg == "すごいですね" or
          line_msg == "すごいです" or
          line_msg == "すごいね" or
          line_msg == "すごい" or
          line_msg == "素晴らしいですね" or
          line_msg == "すばらしいですね" or
          line_msg == "素晴らしいです" or
          line_msg == "すばらしいです" or
          line_msg == "素晴らしい" or
          line_msg == "すばらしい" or
          line_msg == "賢いですね" or
          line_msg == "賢いです" or
          line_msg == "賢いね" or
          line_msg == "賢い" or
          line_msg == "偉いですね" or
          line_msg == "偉いです" or
          line_msg == "偉いね" or
          line_msg == "偉い" or
          line_msg == "エラいですね" or
          line_msg == "エラいです" or
          line_msg == "エラいね" or
          line_msg == "エラい" or
          line_msg == "立派ですね" or
          line_msg == "立派です" or
          line_msg == "立派ね" or
          line_msg == "立派" or
          line_msg == "感服しました" or
          line_msg == "感服したわ" or
          line_msg == "感服した" or
          line_msg == "敬服いたします" or
          line_msg == "敬服しますわ" or
          line_msg == "敬服します" or
          line_msg == "感動しました" or
          line_msg == "感動したわ" or
          line_msg == "感動した" or
          line_msg == "かっこいいですね" or
          line_msg == "カッコいいですね" or
          line_msg == "カッコイイですね" or
          line_msg == "かっこいいです" or
          line_msg == "カッコいいです" or
          line_msg == "カッコイイです" or
          line_msg == "かっこいいわね" or
          line_msg == "カッコいいわね" or
          line_msg == "カッコイイわね" or
          line_msg == "かっこいい" or
          line_msg == "カッコいい" or
          line_msg == "カッコイイ" or
          line_msg == "可愛いですね" or
          line_msg == "かわいいですね" or
          line_msg == "カワイいですね" or
          line_msg == "カワイイですね" or
          line_msg == "可愛いです" or
          line_msg == "かわいいです" or
          line_msg == "カワイいです" or
          line_msg == "カワイイです" or
          line_msg == "可愛いわね" or
          line_msg == "かわいいわね" or
          line_msg == "カワイいわね" or
          line_msg == "カワイイわね" or
          line_msg == "可愛いね" or
          line_msg == "かわいいね" or
          line_msg == "カワイいね" or
          line_msg == "カワイイね" or
          line_msg == "可愛い" or
          line_msg == "かわいい" or
          line_msg == "カワイい" or
          line_msg == "カワイイ" or
          line_msg == "かわい" or
          line_msg == "カワイ" or
          line_msg == "かわゆす" or
          line_msg == "カワゆす" or
          line_msg == "カワユス" or
          line_msg == "美しいですね" or
          line_msg == "うつくしいですね" or
          line_msg == "美しいです" or
          line_msg == "うつくしいです" or
          line_msg == "美しいわね" or
          line_msg == "うつくしいわね" or
          line_msg == "美しいわ" or
          line_msg == "うつくしいわ" or
          line_msg == "美しい" or
          line_msg == "うつくしい" or
          line_msg == "綺麗ですね" or
          line_msg == "きれいですね" or
          line_msg == "キレいですね" or
          line_msg == "キレイですね" or
          line_msg == "綺麗だわ" or
          line_msg == "きれいだわ" or
          line_msg == "キレいだわ" or
          line_msg == "キレイだわ" or
          line_msg == "綺麗だ" or
          line_msg == "きれいだ" or
          line_msg == "キレいだ" or
          line_msg == "キレイだ" or
          line_msg == "綺麗ね" or
          line_msg == "きれいね" or
          line_msg == "キレいね" or
          line_msg == "キレイね" or
          line_msg == "綺麗" or
          line_msg == "きれい" or
          line_msg == "キレい" or
          line_msg == "キレイ" or
          line_msg == "いけてるよ" or
          line_msg == "イケてるよ" or
          line_msg == "イケテルよ" or
          line_msg == "いけてるね" or
          line_msg == "イケてるね" or
          line_msg == "イケテルね" or
          line_msg == "いけてるな" or
          line_msg == "イケてるな" or
          line_msg == "イケテルな" or
          line_msg == "いけてるわ" or
          line_msg == "イケてるわ" or
          line_msg == "イケテルわ" or
          line_msg == "いけてる" or
          line_msg == "イケてる" or
          line_msg == "イケテル" or
          line_msg == "素敵ですよ" or
          line_msg == "すてきですよ" or
          line_msg == "ステキですよ" or
          line_msg == "素敵ですね" or
          line_msg == "すてきですね" or
          line_msg == "ステキですね" or
          line_msg == "素敵です" or
          line_msg == "すてきです" or
          line_msg == "ステキです" or
          line_msg == "素敵だわ" or
          line_msg == "すてきだわ" or
          line_msg == "ステキだわ" or
          line_msg == "素敵よ" or
          line_msg == "すてきよ" or
          line_msg == "ステキよ" or
          line_msg == "素敵ね" or
          line_msg == "すてきね" or
          line_msg == "ステキね" or
          line_msg == "素敵" or
          line_msg == "すてき" or
          line_msg == "ステキ"):
            extrctd_intnt = "<称賛＆礼賛 お世辞に近い>"
    elif (line_msg == "この変態め" or
          line_msg == "このへんたいめ" or
          line_msg == "このヘンタイめ" or
          line_msg == "この変態が" or
          line_msg == "このへんたいが" or
          line_msg == "このヘンタイが" or
          line_msg == "変態め" or
          line_msg == "へんたいめ" or
          line_msg == "ヘンタイめ" or
          line_msg == "変態が" or
          line_msg == "へんたいが" or
          line_msg == "ヘンタイが" or
          line_msg == "変態ですね" or
          line_msg == "へんたいですね" or
          line_msg == "ヘンタイですね" or
          line_msg == "変態だわ" or
          line_msg == "へんたいだわ" or
          line_msg == "ヘンタイだわ" or
          line_msg == "変態ね" or
          line_msg == "へんたいね" or
          line_msg == "ヘンタイね" or
          line_msg == "変態" or
          line_msg == "へんたい" or
          line_msg == "ヘンタイ" or
          line_msg == "このぶすめ" or
          line_msg == "このブスめ" or
          line_msg == "この不細工め" or
          line_msg == "このぶさいくめ" or
          line_msg == "このブサイクめ" or
          line_msg == "このぶすが" or
          line_msg == "このブスが" or
          line_msg == "この不細工が" or
          line_msg == "このぶさいくが" or
          line_msg == "このブサイクが" or
          line_msg == "ぶすめ" or
          line_msg == "ブスめ" or
          line_msg == "不細工め" or
          line_msg == "ぶさいくめ" or
          line_msg == "ブサイクめ" or
          line_msg == "ぶすが" or
          line_msg == "ブスが" or
          line_msg == "不細工が" or
          line_msg == "ぶさいくが" or
          line_msg == "ブサイクが" or
          line_msg == "ぶすですね" or
          line_msg == "ブスですね" or
          line_msg == "不細工ですね" or
          line_msg == "ぶさいくですね" or
          line_msg == "ブサイクですね" or
          line_msg == "ぶすだわ" or
          line_msg == "ブスだわ" or
          line_msg == "不細工だわ" or
          line_msg == "ぶさいくだわ" or
          line_msg == "ブサイクだわ" or
          line_msg == "ぶすね" or
          line_msg == "ブスね" or
          line_msg == "不細工ね" or
          line_msg == "ぶさいくね" or
          line_msg == "ブサイクね" or
          line_msg == "ぶす" or
          line_msg == "ブス" or
          line_msg == "不細工" or
          line_msg == "ぶさいく" or
          line_msg == "ブサイク" or
          line_msg == "最低ですね" or
          line_msg == "さいていですね" or
          line_msg == "サイテーですね" or
          line_msg == "最低だね" or
          line_msg == "さいていだね" or
          line_msg == "サイテーだね" or
          line_msg == "最低だな" or
          line_msg == "さいていだな" or
          line_msg == "サイテーだな" or
          line_msg == "最低だわ" or
          line_msg == "さいていだわ" or
          line_msg == "サイテーだわ" or
          line_msg == "最低よ" or
          line_msg == "さいていよ" or
          line_msg == "サイテーよ" or
          line_msg == "最低ね" or
          line_msg == "さいていね" or
          line_msg == "サイテーね" or
          line_msg == "最低" or
          line_msg == "さいてい" or
          line_msg == "サイテー" or
          line_msg == "この無能野郎め" or
          line_msg == "この無能やろうめ" or
          line_msg == "この無能ヤロウめ" or
          line_msg == "この無能ヤローめ" or
          line_msg == "この無能め" or
          line_msg == "この無能野郎が" or
          line_msg == "この無能やろうが" or
          line_msg == "この無能ヤロウが" or
          line_msg == "この無能ヤローが" or
          line_msg == "無能野郎め" or
          line_msg == "無能やろうめ" or
          line_msg == "無能ヤロウめ" or
          line_msg == "無能ヤローめ" or
          line_msg == "無能め" or
          line_msg == "無能野郎が" or
          line_msg == "無能やろうが" or
          line_msg == "無能ヤロウが" or
          line_msg == "無能ヤローが" or
          line_msg == "無能ですね" or
          line_msg == "無能だね" or
          line_msg == "無能だわ" or
          line_msg == "無能よ" or
          line_msg == "無能ね" or
          line_msg == "無能" or
          line_msg == "この馬鹿野郎め" or
          line_msg == "このばか野郎め" or
          line_msg == "このバカ野郎め" or
          line_msg == "この馬鹿やろうめ" or
          line_msg == "このばかやろうめ" or
          line_msg == "このバカやろうめ" or
          line_msg == "この馬鹿ヤロウめ" or
          line_msg == "この馬鹿ヤローめ" or
          line_msg == "この馬鹿野郎が" or
          line_msg == "このばか野郎が" or
          line_msg == "このバカ野郎が" or
          line_msg == "この馬鹿やろうが" or
          line_msg == "このばかやろうが" or
          line_msg == "このバカやろうが" or
          line_msg == "この馬鹿ヤロウが" or
          line_msg == "この馬鹿ヤロが" or
          line_msg == "このばかヤロウが" or
          line_msg == "このばかヤローが" or
          line_msg == "この馬鹿野郎" or
          line_msg == "このばか野郎" or
          line_msg == "このバカ野郎" or
          line_msg == "この馬鹿やろう" or
          line_msg == "このばかやろう" or
          line_msg == "このバカやろう" or
          line_msg == "この馬鹿ヤロウ" or
          line_msg == "この馬鹿ヤロー" or
          line_msg == "このばかヤロウ" or
          line_msg == "このばかヤロー" or
          line_msg == "このバカヤロウ" or
          line_msg == "このバカヤロー" or
          line_msg == "馬鹿野郎ですね" or
          line_msg == "ばか野郎ですね" or
          line_msg == "バカ野郎ですね" or
          line_msg == "馬鹿やろうですね" or
          line_msg == "ばかやろうですね" or
          line_msg == "バカやろうですね" or
          line_msg == "馬鹿ヤロウですね" or
          line_msg == "馬鹿ヤローですね" or
          line_msg == "ばかヤロウですね" or
          line_msg == "ばかヤロですね" or
          line_msg == "バカヤロウですね" or
          line_msg == "バカヤローですね" or
          line_msg == "馬鹿野郎" or
          line_msg == "ばか野郎" or
          line_msg == "バカ野郎" or
          line_msg == "馬鹿やろう" or
          line_msg == "ばかやろう" or
          line_msg == "バカやろう" or
          line_msg == "馬鹿ヤロウ" or
          line_msg == "ばかヤロウ" or
          line_msg == "バカヤロウ" or
          line_msg == "バカヤロー" or
          line_msg == "馬鹿だわ" or
          line_msg == "ばかだわ" or
          line_msg == "バカだわ" or
          line_msg == "馬鹿ね" or
          line_msg == "ばかね" or
          line_msg == "バカね" or
          line_msg == "馬鹿め" or
          line_msg == "ばかめ" or
          line_msg == "バカめ" or
          line_msg == "馬鹿が" or
          line_msg == "ばかが" or
          line_msg == "バカが" or
          line_msg == "馬鹿" or
          line_msg == "ばか" or
          line_msg == "バカ" or
          line_msg == "あほですね" or
          line_msg == "アホですね" or
          line_msg == "あほだね" or
          line_msg == "アホだね" or
          line_msg == "あほだわ" or
          line_msg == "アホだわ" or
          line_msg == "あほね" or
          line_msg == "アホね" or
          line_msg == "あほ" or
          line_msg == "アホ" or
          line_msg == "このあほ垂れ" or
          line_msg == "このアホ垂れ" or
          line_msg == "あほ垂れ" or
          line_msg == "アホ垂れ" or
          line_msg == "このあほたれ" or
          line_msg == "このアホたれ" or
          line_msg == "あほたれ" or
          line_msg == "アホたれ" or
          line_msg == "このあほタレ" or
          line_msg == "このアホタレ" or
          line_msg == "あほタレ" or
          line_msg == "アホタレ" or
          line_msg == "このくず野郎め" or
          line_msg == "このくずやろうめ" or
          line_msg == "このくずヤロウめ" or
          line_msg == "このくずヤローめ" or
          line_msg == "このクズ野郎め" or
          line_msg == "このクズやろうめ" or
          line_msg == "このクズヤロウめ" or
          line_msg == "このクズヤローめ" or
          line_msg == "このくず野郎が" or
          line_msg == "このくずやろうが" or
          line_msg == "このくずヤロウが" or
          line_msg == "このくずヤローが" or
          line_msg == "このクズ野郎が" or
          line_msg == "このクズやろうが" or
          line_msg == "このクズヤロウが" or
          line_msg == "このクズヤローが" or
          line_msg == "くず野郎め" or
          line_msg == "くずやろうめ" or
          line_msg == "くずヤロウめ" or
          line_msg == "くずヤローめ" or
          line_msg == "クズ野郎め" or
          line_msg == "クズやろうめ" or
          line_msg == "クズヤロウめ" or
          line_msg == "クズヤローめ" or
          line_msg == "くず野郎が" or
          line_msg == "くずやろうが" or
          line_msg == "くずヤロウが" or
          line_msg == "くずヤロが" or
          line_msg == "クズ野郎が" or
          line_msg == "クズやろうが" or
          line_msg == "クズヤロウが" or
          line_msg == "クズヤローが" or
          line_msg == "このくず" or
          line_msg == "このクズ" or
          line_msg == "くず" or
          line_msg == "クズ" or
          line_msg == "このかす野郎め" or
          line_msg == "このかすやろうめ" or
          line_msg == "このかすヤロウめ" or
          line_msg == "このかすヤローめ" or
          line_msg == "このカス野郎め" or
          line_msg == "このカスやろうめ" or
          line_msg == "このカスヤロウめ" or
          line_msg == "このカスヤローめ" or
          line_msg == "このかす野郎が" or
          line_msg == "このかすやろうが" or
          line_msg == "このかすヤロウが" or
          line_msg == "このかすヤローが" or
          line_msg == "このカス野郎が" or
          line_msg == "このカスやろうが" or
          line_msg == "このカスヤロウが" or
          line_msg == "このカスヤローが" or
          line_msg == "かす野郎め" or
          line_msg == "かすやろうめ" or
          line_msg == "かすヤロウめ" or
          line_msg == "かすヤローめ" or
          line_msg == "カス野郎め" or
          line_msg == "カスやろうめ" or
          line_msg == "カスヤロウめ" or
          line_msg == "カスヤローめ" or
          line_msg == "かす野郎が" or
          line_msg == "かすやろうが" or
          line_msg == "かすヤロウが" or
          line_msg == "かすヤローが" or
          line_msg == "カス野郎が" or
          line_msg == "カスやろうが" or
          line_msg == "カスヤロウが" or
          line_msg == "カスヤローが" or
          line_msg == "このかす" or
          line_msg == "このカス" or
          line_msg == "かす" or
          line_msg == "カス" or
          line_msg == "このごみ野郎め" or
          line_msg == "このごみやろうめ" or
          line_msg == "このごみヤロウめ" or
          line_msg == "このごみヤローめ" or
          line_msg == "このゴミ野郎め" or
          line_msg == "このゴミやろうめ" or
          line_msg == "このゴミヤロウめ" or
          line_msg == "このゴミヤローめ" or
          line_msg == "このかす野郎が" or
          line_msg == "このかすやろうが" or
          line_msg == "このかすヤロウが" or
          line_msg == "このかすヤローが" or
          line_msg == "このゴミ野郎が" or
          line_msg == "このゴミやろうが" or
          line_msg == "このゴミヤロウが" or
          line_msg == "このゴミヤローが" or
          line_msg == "ごみ野郎め" or
          line_msg == "ごみやろうめ" or
          line_msg == "ごみヤロウめ" or
          line_msg == "ごみヤローめ" or
          line_msg == "ゴミ野郎め" or
          line_msg == "ゴミやろうめ" or
          line_msg == "ゴミヤロウめ" or
          line_msg == "ゴミヤローめ" or
          line_msg == "かす野郎が" or
          line_msg == "かすやろうが" or
          line_msg == "かすヤロウが" or
          line_msg == "かすヤローが" or
          line_msg == "ゴミ野郎が" or
          line_msg == "ゴミやろうが" or
          line_msg == "ゴミヤロウが" or
          line_msg == "ゴミヤローが" or
          line_msg == "このごみ" or
          line_msg == "このゴミ" or
          line_msg == "ごみ" or
          line_msg == "ゴミ" or
          line_msg == "このげす野郎め" or
          line_msg == "このげすやろうめ" or
          line_msg == "このげすヤロウめ" or
          line_msg == "このげすヤローめ" or
          line_msg == "このゲス野郎め" or
          line_msg == "このゲスやろうめ" or
          line_msg == "このゲスヤロウめ" or
          line_msg == "このゲスヤローめ" or
          line_msg == "このげす野郎が" or
          line_msg == "このげすやろうが" or
          line_msg == "このげすヤロウが" or
          line_msg == "このげすヤローが" or
          line_msg == "このゲス野郎が" or
          line_msg == "このゲスやろうが" or
          line_msg == "このゲスヤロウが" or
          line_msg == "このゲスヤローが" or
          line_msg == "このげす" or
          line_msg == "このゲス" or
          line_msg == "げす" or
          line_msg == "ゲス"):
            extrctd_intnt = "<罵倒＆貶め>"
    elif (line_msg == "邪魔" or
          line_msg == "じゃま" or
          line_msg == "ジャマ" or
          line_msg == "目障り" or
          line_msg == "うざったい" or
          line_msg == "ウザったい" or
          line_msg == "ウザい" or
          line_msg == "消えてください" or
          line_msg == "消えて" or
          line_msg == "消えな" or
          line_msg == "消え失せろ" or
          line_msg == "消えうせろ" or
          line_msg == "消えろ" or
          line_msg == "死んでください" or
          line_msg == "氏んでください" or
          line_msg == "しんでください" or
          line_msg == "死んで" or
          line_msg == "氏んで" or
          line_msg == "しんで" or
          line_msg == "死ね" or
          line_msg == "氏ね" or
          line_msg == "しね" or
          line_msg == "死になさい" or
          line_msg == "氏になさい" or
          line_msg == "しになさい" or
          line_msg == "死にな" or
          line_msg == "氏にな" or
          line_msg == "しにな" or
          line_msg == "死んでろ" or
          line_msg == "氏んでろ" or
          line_msg == "しんでろ"):
            extrctd_intnt = "<人格・存在否定 罵声に近い>"
    elif (line_msg == "大天才ですか" or
          line_msg == "天才ですか" or
          line_msg == "大秀才ですか" or
          line_msg == "秀才ですか" or
          line_msg == "優秀ですか"):
            extrctd_intnt = "<称賛＆礼賛 半疑問>"
    elif (line_msg == "無能ですか" or
          line_msg == "ばかですか" or
          line_msg == "バカですか" or
          line_msg == "あほですか" or
          line_msg == "アホですか" or
          line_msg == "くずですか" or
          line_msg == "クズですか" or
          line_msg == "かすですか" or
          line_msg == "カスですか" or
          line_msg == "ごみですか" or
          line_msg == "ゴミですか"):
            extrctd_intnt = "<罵詈＆罵倒 半疑問>"
    elif (line_msg == "何をしていますか" or
          line_msg == "なにをしていますか" or
          line_msg == "何をしてますか" or
          line_msg == "なにをしてますか" or
          line_msg == "何してますか" or
          line_msg == "なにしてますか" or
          line_msg == "何してるの" or
          line_msg == "なにしてるの" or
          line_msg == "どうしていますか" or
          line_msg == "どうしてますか" or
          line_msg == "どうしてる"):
            extrctd_intnt = "<疑義＆質問＆確認 現在 状態・状況について>"
    elif (line_msg == "何をしてきましたか" or
          line_msg == "なにをしてきましたか" or
          line_msg == "何をしてましたか" or
          line_msg == "なにをしてましたか" or
          line_msg == "何してましたか" or
          line_msg == "なにしてましたか" or
          line_msg == "何してたの" or
          line_msg == "なにしてたの" or
          line_msg == "何してた" or
          line_msg == "なにしてた" or
          line_msg == "どうしてきましたか" or
          line_msg == "どうしてましたか" or
          line_msg == "どうしてた"):
            extrctd_intnt = "<疑義＆質問＆確認 過去 状態・状況について>"
    elif (line_msg == "何をしたいですか" or
          line_msg == "なにをしたいですか" or
          line_msg == "何がしたいですか" or
          line_msg == "なにがしたいですか" or
          line_msg == "何したいですか" or
          line_msg == "なにしたいですか" or
          line_msg == "何したいの" or
          line_msg == "なにしたいの" or
          line_msg == "何したい" or
          line_msg == "なにしたい" or
          line_msg == "何をしますか" or
          line_msg == "なにをしますか" or
          line_msg == "何しますか" or
          line_msg == "なにしますか" or
          line_msg == "なにします"):
            extrctd_intnt = "<疑義＆質問＆確認 現在 願望・欲求について>"
    elif (line_msg == "何をしたかったのですか" or
          line_msg == "なにをしたかったのですか" or
          line_msg == "何をしたかったんですか" or
          line_msg == "なにをしたかったんですか" or
          line_msg == "何がしたかったのですか" or
          line_msg == "なにがしたかったのですか" or
          line_msg == "何がしたかったんですか" or
          line_msg == "なにがしたかったんですか" or
          line_msg == "何したかったのですか" or
          line_msg == "なにしたかったのですか" or
          line_msg == "何したかったんですか" or
          line_msg == "なにしたかったんですか" or
          line_msg == "何したかったの" or
          line_msg == "なにしたかったの"):
            extrctd_intnt = "<疑義＆質問＆確認 過去 願望・欲求について>"
    elif (line_msg == "何をしていきたいのですか" or
          line_msg == "なにをしていきたいのですか" or
          line_msg == "何をしていきたいですか" or
          line_msg == "なにをしていきたいですか" or
          line_msg == "何をしていきたいの" or
          line_msg == "なにをしていきたいの" or
          line_msg == "何がしていきたいのですか" or
          line_msg == "なにがしていきたいのですか" or
          line_msg == "何がしていきたいですか" or
          line_msg == "なにがしていきたいですか" or
          line_msg == "何していきたいのですか" or
          line_msg == "なにしていきたいのですか" or
          line_msg == "何していきたいんですか" or
          line_msg == "なにしていきたいんですか" or
          line_msg == "何していきたいですか" or
          line_msg == "なにしていきたいですか" or
          line_msg == "何していきたいの" or
          line_msg == "なにしていきたいの" or
          line_msg == "何していきたい" or
          line_msg == "なにしていきたい"):
            extrctd_intnt = "<疑義＆質問＆確認 未来 願望・欲求について>"
    elif (line_msg == "どうしたいのですか" or
          line_msg == "どうしたいんですか" or
          line_msg == "どうしたいですか" or
          line_msg == "どうしたいのかな" or
          line_msg == "どうしたいの" or
          line_msg == "どうしたい"):
            extrctd_intnt = "<疑義＆質問＆確認 現在 願望・欲求について 漠然とした様子・様相>"
    elif (line_msg == "どうしたかったのですか" or
          line_msg == "どうしたかったんですか" or
          line_msg == "どうしたかったの" or
          line_msg == "どうしたかった"):
            extrctd_intnt = "<疑義＆質問＆確認 過去 願望・欲求について 漠然とした様子・様相>"
    elif (line_msg == "どうしていきたいのですか" or
          line_msg == "どうしていきたいんですか" or
          line_msg == "どうしていきたいの" or
          line_msg == "どうしていきたい"):
            extrctd_intnt = "<疑義＆質問＆確認 未来 願望・欲求について 漠然とした様子・様相>"
    elif (line_msg == "どうなのですか" or
          line_msg == "どうなんですか" or
          line_msg == "どうなの" or
          line_msg == "どうなん"):
            extrctd_intnt = "<疑義＆質問＆確認 意図・目的について>"
    elif line_msg == "どう":
            extrctd_intnt = "<疑義＆質問＆確認 感想・感慨について>"
    elif (line_msg == "どうしてなのですか" or
          line_msg == "どうしてなんですか" or
          line_msg == "どうしてですか" or
          line_msg == "どうして"):
            extrctd_intnt = "<疑義＆質問＆確認 理由・事情について>"      
    elif (line_msg == "何故なのですか" or
          line_msg == "なぜなのですか" or
          line_msg == "何故なんですか" or
          line_msg == "なぜなんですか" or
          line_msg == "何故ですか" or
          line_msg == "なぜですか" or
          line_msg == "何故" or
          line_msg == "なぜ" or
          line_msg == "何で" or
          line_msg == "なんで"):
            extrctd_intnt = "<疑義＆質問＆確認 理由・事情について>"
    elif (line_msg == "良いです" or
          line_msg == "よいです" or
          line_msg == "いいです" or
          line_msg == "良い" or
          line_msg == "いい" or
          line_msg == "おっけー" or
          line_msg == "オッケー" or
          line_msg == "おけ" or
          line_msg == "オケ" or
          line_msg == "OK"):
            extrctd_intnt = "<許容＆許可>"
    elif (line_msg == "駄目です" or
          line_msg == "だめです" or
          line_msg == "ダメです" or
          line_msg == "駄目だ" or
          line_msg == "だめだ" or
          line_msg == "ダメだ" or
          line_msg == "駄目" or
          line_msg == "だめ" or
          line_msg == "ダメ" or
          line_msg == "禁止です" or
          line_msg == "禁止だ" or
          line_msg == "禁止" or
          line_msg == "いけません" or
          line_msg == "いけない" or
          line_msg == "しては駄目です" or
          line_msg == "してはだめです" or
          line_msg == "してはダメです" or
          line_msg == "しては駄目だ" or
          line_msg == "してはだめだ" or
          line_msg == "してはダメだ" or
          line_msg == "しては駄目" or
          line_msg == "してはだめ" or
          line_msg == "してはダメ" or
          line_msg == "するのは禁止です" or
          line_msg == "するのは禁止" or
          line_msg == "やるのは禁止です" or
          line_msg == "やるのは禁止" or
          line_msg == "してははいけません" or
          line_msg == "しちゃいけません" or
          line_msg == "やってはいけません" or
          line_msg == "やっちゃいけません" or
          line_msg == "やっちゃ駄目" or
          line_msg == "やっちゃだめ" or
          line_msg == "やっちゃダメ" or
          line_msg == "NG"):
            extrctd_intnt = "<禁止＆不許可>"
    elif (line_msg == "ですねえ" or
          line_msg == "ですねぇ" or
          line_msg == "ですね" or
          line_msg == "そうだねえ" or
          line_msg == "そうだねぇ" or
          line_msg == "そうだね" or
          line_msg == "そだねえ" or
          line_msg == "そだねぇ" or
          line_msg == "そだね" or
          line_msg == "だよねえ" or
          line_msg == "だよねぇ" or
          line_msg == "だよね" or
          line_msg == "だねえ" or
          line_msg == "だねぇ" or
          line_msg == "だね"):
            extrctd_intnt = "<賛意＆賛同>"
    elif (line_msg == "許可を頂きたいです" or
          line_msg == "許可をいただきたいです" or
          line_msg == "許可を頂きたい" or
          line_msg == "許可をいただきたい" or
          line_msg == "許可を下さい" or
          line_msg == "許可をください" or
          line_msg == "許可して下さい" or
          line_msg == "許可してください" or
          line_msg == "許可してくれ" or
          line_msg == "許可して"):
            extrctd_intnt = "<依頼＆要求 許可を求めている>"
    elif (line_msg == "歌ってよ" or
          line_msg == "うたってよ" or
          line_msg == "歌って" or
          line_msg == "うたって" or
          line_msg == "踊ってよ" or
          line_msg == "おどってよ" or
          line_msg == "踊って" or
          line_msg == "おどって" or
          line_msg == "遊んでよ" or
          line_msg == "あそんでよ" or
          line_msg == "遊んで" or
          line_msg == "あそんで"):
            extrctd_intnt = "<依頼＆要求 遊び心を求めている>"
    elif (line_msg == "行きます" or
          line_msg == "いきます" or
          line_msg == "遣ります" or
          line_msg == "やります" or
          line_msg == "遊びます" or
          line_msg == "あそびます" or
          line_msg == "休みます" or
          line_msg == "やすみます"):
            extrctd_intnt = "<宣言＆表明 現在＆未来 自己の行為・行動について>"
    elif (line_msg == "美しい" or
          line_msg == "うつくしい" or
          line_msg == "楽しい" or
          line_msg == "たのしい" or
          line_msg == "苦しい" or
          line_msg == "くるしい" or
          line_msg == "辛い" or
          line_msg == "つらい" or
          line_msg == "嬉しい" or
          line_msg == "うれしい" or
          line_msg == "悲しい" or
          line_msg == "かなしい" or
          line_msg == "哀しい"):
            extrctd_intnt = "<心理・感情>"
    elif (line_msg == "楽" or
          line_msg == "らく" or
          line_msg == "ラク" or
          line_msg == "らくちん" or
          line_msg == "ラクチン" or
          line_msg == "楽勝" or
          line_msg == "らくしょう" or
          line_msg == "ラクショウ" or
          line_msg == "大変" or
          line_msg == "たいへん" or
          line_msg == "タイヘン" or
          line_msg == "疲れた" or
          line_msg == "つかれた"):
            extrctd_intnt = "<精神・肉体>"
    elif (line_msg == "最初は グー" or
          line_msg == "最初はグー" or
          line_msg == "じゃんけんぽん" or
          line_msg == "じゃんけん" or
          line_msg == "ジャンケンポン" or
          line_msg == "ジャンケン"):
            extrctd_intnt = "<児戯＆遊戯>"
    elif (line_msg == "お願い致します" or
          line_msg == "お願いいたします" or
          line_msg == "お願いします" or
          line_msg == "お願いです" or
          line_msg == "お願い"):
            extrctd_intnt = "<依頼＆依願>"
    elif (line_msg == "申し訳ございません" or
          line_msg == "申し訳ありません" or
          line_msg == "御免なさい" or
          line_msg == "ごめんなさい" or
          line_msg == "ゴメンなさい" or
          line_msg == "御免" or
          line_msg == "ごめん" or
          line_msg == "ゴメン" or
          line_msg == "メンゴ メンゴ" or
          line_msg == "メンゴメンゴ" or
          line_msg == "メンゴ" or
          line_msg == "すみません" or
          line_msg == "すいません" or
          line_msg == "すまん"):
            extrctd_intnt = "<感謝＆お礼>"
    elif (line_msg == "申し訳ございません" or
          line_msg == "申し訳ありません" or
          line_msg == "御免なさい" or
          line_msg == "ごめんなさい" or
          line_msg == "ゴメンなさい" or
          line_msg == "御免" or
          line_msg == "ごめん" or
          line_msg == "ゴメン" or
          line_msg == "メンゴ メンゴ" or
          line_msg == "メンゴメンゴ" or
          line_msg == "メンゴ" or
          line_msg == "すみません" or
          line_msg == "すいません" or
          line_msg == "すまん"):
            extrctd_intnt = "<陳謝＆謝罪>"
    elif (line_msg == "承知致しました" or
          line_msg == "承知いたしました" or
          line_msg == "承知しました" or
          line_msg == "承知した" or
          line_msg == "承知" or
          line_msg == "かしこまりました" or
          line_msg == "かしこまり"):
            extrctd_intnt = "<承知＆承諾>"
    elif (line_msg == "了解致しました" or
          line_msg == "了解いたしました" or
          line_msg == "了解しました" or
          line_msg == "了解した" or
          line_msg == "了解" or
          line_msg == "りょ" or
          line_msg == "リョ" or
          line_msg == "分かりました" or
          line_msg == "わかりました" or
          line_msg == "分かった" or
          line_msg == "わかった"):
            extrctd_intnt = "<了承＆了解>"
    elif (line_msg == "愛しています" or
          line_msg == "あいしています" or
          line_msg == "愛してます" or
          line_msg == "あいしてます" or
          line_msg == "愛してる" or
          line_msg == "あいしてる" or
          line_msg == "好きです" or
          line_msg == "すきです" or
          line_msg == "スキです" or
          line_msg == "好きだ" or
          line_msg == "すきだ" or
          line_msg == "スキだ" or
          line_msg == "好き" or
          line_msg == "すき" or
          line_msg == "スキ"):
            extrctd_intnt = "<求愛>"
    elif (line_msg == "Hなことしたい" or
          line_msg == "Hなことしよう" or
          line_msg == "Hしたい" or
          line_msg == "Hしよう" or
          line_msg == "セックスしたい" or
          line_msg == "セックスしよう"):
            extrctd_intnt = "<発情>"
    elif (line_msg == "セックスは好きですか" or
          line_msg == "セックスは好き" or
          line_msg == "どこを責められたい" or
          line_msg == "どこ責められたい"):
            extrctd_intnt = "<卑猥な言動 辱め>"
    elif (line_msg == "何故そうなるのですか" or
          line_msg == "なぜそうなるのですか" or
          line_msg == "何故そうなるんですか" or
          line_msg == "なぜそうなるんですか" or
          line_msg == "何故そうなるのか" or
          line_msg == "なぜそうなるのか" or
          line_msg == "何故そうなるか" or
          line_msg == "なぜそうなるか" or
          line_msg == "何故そうなるのです" or
          line_msg == "なぜそうなるのです" or
          line_msg == "何故そうなるんです" or
          line_msg == "なぜそうなるんです"):
            extrctd_intnt = "<疑義＆確認＆質問 目上に対して 理由・事情について>"
    elif (line_msg == "なんでそうなるのかなあ" or
          line_msg == "なんでそうなるのかなぁ" or
          line_msg == "なんでそうなるのかな" or
          line_msg == "なんでそうなるかなあ" or
          line_msg == "なんでそうなるかなぁ" or
          line_msg == "なんでそうなるかな" or
          line_msg == "なんでそうなるのか" or
          line_msg == "なんでそうなるか" or
          line_msg == "なんでそうなる" or
          line_msg == "何故そうなるの" or
          line_msg == "なぜそうなるの" or
          line_msg == "何故そうなる" or
          line_msg == "なぜそうなる"):
            extrctd_intnt = "<疑義＆確認＆質問 やや反発している やや反感を抱いている 目下に対して 理由・事情について>"
    elif (line_msg == "大丈夫でしょうか" or
          line_msg == "大丈夫ですか" or
          line_msg == "大丈夫"):
            extrctd_intnt = "<疑義＆質問＆確認 安否・健康状態について>"
    elif (line_msg == "ご苦労様でした" or
          line_msg == "ご苦労様です" or
          line_msg == "ご苦労様" or
          line_msg == "ご苦労" or
          line_msg == "お疲れ様でした" or
          line_msg == "お疲れ様です" or
          line_msg == "お疲れ様" or
          line_msg == "お疲れ" or
          line_msg == "大儀であった" or
          line_msg == "大儀だった"):        
            extrctd_intnt = "<慰労＆労い>"
    elif (line_msg == "分かった" or
          line_msg == "わかった"):
            extrctd_intnt = "<理解＆認識>"
    elif (line_msg == "恐悦至極にございます" or
          line_msg == "恐悦至極でございます" or
          line_msg == "恐悦至極です" or
          line_msg == "恐れ入ります" or
          line_msg == "恐れ多いです" or
          line_msg == "とんでもございません" or
          line_msg == "とんでもない"):
            extrctd_intnt = "<訴求＆表現 褒められて 感謝されて 恐縮している>"
    elif (line_msg == "きざったらしい" or
          line_msg == "キザったらしい" or
          line_msg == "きざっぽい" or
          line_msg == "キザっぽい" or
          line_msg == "嫌味ったらしい" or
          line_msg == "イヤミったらしい" or
          line_msg == "嫌味っぽい" or
          line_msg == "イヤミっぽい"):
            extrctd_intnt = "<訴求＆表現 反発している 反感を抱いている 強い嫌悪>"
    elif (line_msg == "しても良いですか" or
          line_msg == "してもよいですか" or
          line_msg == "良いですか" or
          line_msg == "いいですか" or
          line_msg == "良いか" or
          line_msg == "いいか" or
          line_msg == "してもいいですか" or
          line_msg == "してもいいか" or
          line_msg == "していいか" or
          line_msg == "いいか" or
          line_msg == "やっても良いですか" or
          line_msg == "やってもよいですか" or
          line_msg == "やってもいいですか" or
          line_msg == "やってもいいか" or
          line_msg == "やっていいか"):
            extrctd_intnt = "<疑義＆質問＆確認 許容・許可を求める 肯定形>"
    elif (line_msg == "駄目ですか" or
          line_msg == "だめですか" or
          line_msg == "ダメですか" or
          line_msg == "駄目か" or
          line_msg == "だめか" or
          line_msg == "ダメか" or
          line_msg == "禁止ですか" or
          line_msg == "禁止か" or
          line_msg == "いけませんか" or
          line_msg == "いけないか"):
            extrctd_intnt = "<疑義＆質問＆確認 許容・許可を求める 否定形>"
    elif (line_msg == "お伺いします" or
          line_msg == "お聞きします"):
            extrctd_intnt = "<聴取＆傾聴 用件を尋ねる>"
    elif (line_msg == "お聞かせ下さい" or
          line_msg == "お聞かせください"):
            extrctd_intnt = "<聴取＆傾聴 意見・感想を求める>"
    elif (line_msg == "お考えになって下さい" or
          line_msg == "お考え下さい" or
          line_msg == "考えて下さい" or
          line_msg == "考えてください" or
          line_msg == "考えてくれ" or
          line_msg == "考えて"):
            extrctd_intnt = "<要求＆要請 思慮・思考を求める>"
    elif (line_msg == "考え直して下さい" or
          line_msg == "考え直してください" or
          line_msg == "考え直してくれ" or
          line_msg == "考え直して" or
          line_msg == "思い直して下さい" or
          line_msg == "思い直してください" or
          line_msg == "思い直してくれ" or
          line_msg == "思い直して"):
            extrctd_intnt = "<要求＆要請 再度の思慮・思考を求める>"
    elif (line_msg == "良きに計らえ" or
          line_msg == "よきに計らえ" or
          line_msg == "良しなに" or
          line_msg == "よしなに" or
          line_msg == "どうぞ良しなに" or
          line_msg == "どうぞよしなに"):
            extrctd_intnt = "<要求＆要請 善処を求める>"
    elif (line_msg == "うむ" or
          line_msg == "ウム" or
          line_msg == "うん" or
          line_msg == "ウン"):
            extrctd_intnt = "<了承＆承諾 納得する様子でもある>"
    elif (line_msg == "そう言っているのです" or
          line_msg == "そういっているのです" or
          line_msg == "そう言っているんです" or
          line_msg == "そういっているんです" or
          line_msg == "そう言っている" or
          line_msg == "そういっている" or
          line_msg == "そう言ってる" or
          line_msg == "そういってる"):
            extrctd_intnt = "<問答 肯定形 考えに同意する形で>"
    elif (line_msg == "そうは言っていないよ" or
          line_msg == "そうはいっていないよ" or
          line_msg == "そうは言っていない" or
          line_msg == "そうはいっていない" or
          line_msg == "そうは言ってないよ" or
          line_msg == "そうはいってないよ" or
          line_msg == "そうは言ってない" or
          line_msg == "そうはいってない"):
            extrctd_intnt = "<問答 否定形 相手の考えに反意する形で>"
    elif (line_msg == "しますよね" or
          line_msg == "するよね" or
          line_msg == "やるよね"):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 自己の行為・行動について>"
    elif (line_msg == "しませんよね" or
          line_msg == "しないよね" or
          line_msg == "やらないよね"):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 自己の行為・行動について>"
    elif (line_msg == "するよな" or
          line_msg == "やるよな"):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 半強制 自己の行為・行動について>"
    elif (line_msg == "しないよな" or
          line_msg == "せんよな" or
          line_msg == "やらないよな" or
          line_msg == "やらんよな"):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 半強制 自己の行為・行動について>"
    elif (line_msg == "そうなのですね" or
          line_msg == "そうなんですね" or
          line_msg == "そうなのだな" or
          line_msg == "そうなんだな"):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 考えや気持ちを察する形で>"
    elif (line_msg == "そうではないのですね" or
          line_msg == "そうではないんですね" or
          line_msg == "そうではないのだな" or
          line_msg == "そうではないんだな"):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 考えや気持ちを察する形で>"
    elif (line_msg == "そうみたいだよ" or
          line_msg == "そうみたいだね" or
          line_msg == "そうみたいだな" or
          line_msg == "そうみたいだわ" or
          line_msg == "そうみたいだ" or
          line_msg == "そうみたい" or
          line_msg == "そうらしいよ" or
          line_msg == "そうらしいね" or
          line_msg == "そうらしいな" or
          line_msg == "そうらしいわ" or
          line_msg == "そうらしい"):
            extrctd_intnt = "<同意 意見・考えに沿う形で>"
    elif (line_msg == "そうではないらしいよ" or
          line_msg == "そうではないらしいね" or
          line_msg == "そうではないらしいな" or
          line_msg == "そうではないらしいわ" or
          line_msg == "そうではないらしい" or
          line_msg == "ではないらしいよ" or
          line_msg == "ではないらしいね" or
          line_msg == "ではないらしいな" or
          line_msg == "ではないらしいわ" or
          line_msg == "ではないらしい" or
          line_msg == "そうじゃないらしいよ" or
          line_msg == "そうじゃないらしいね" or
          line_msg == "そうじゃないらしいな" or
          line_msg == "そうじゃないらしいわ" or
          line_msg == "そうじゃないらしい"):
            extrctd_intnt = "<反意・不同意 意見・考えに沿わない形で>"
    elif (line_msg == "そうなのですね" or
          line_msg == "そうなんですね" or
          line_msg == "そうなんですね" or
          line_msg == "なのですね" or
          line_msg == "なんですね"):
            extrctd_intnt = "<理解＆納得 肯定形>"
    elif (line_msg == "そうではないのですね" or
          line_msg == "そうではないんですね" or
          line_msg == "そうじゃないんですね" or
          line_msg == "ではないのですね" or
          line_msg == "ではないんですね" or
          line_msg == "じゃないんですね"):
            extrctd_intnt = "<理解＆納得 否定形>"
    elif (line_msg == "お分かりいただけましたか" or
          line_msg == "分かっていただけましたか" or
          line_msg == "分かりましたか" or
          line_msg == "分かっていますか" or
          line_msg == "分かってますか"):
            extrctd_intnt = "<疑義＆質問＆確認 理解力を試すことに近い>"
    elif (line_msg == "いかがなさいますか" or
          line_msg == "いかがいたしましょうか" or
          line_msg == "どういたしますか" or
          line_msg == "どうしますか" or
          line_msg == "どうするのですか" or
          line_msg == "どうするんですか" or
          line_msg == "どうするの" or
          line_msg == "どうするん" or
          line_msg == "どうする"):
            extrctd_intnt = "<疑義＆質問＆確認 丁寧に敬って 今後の動きや活動について>"
    elif (line_msg == "ではどうするのですか" or
          line_msg == "ではどうするんですか" or
          line_msg == "ではどうするのか" or
          line_msg == "ではどうするの" or
          line_msg == "ではどうする" or
          line_msg == "じゃあどうするのか" or
          line_msg == "じゃあどうするの" or
          line_msg == "じゃあどうする"):
            extrctd_intnt = "<疑義＆質問＆確認 追求に近い 今後の動きや活動について>"
    elif (line_msg == "いらっしゃいませ" or
          line_msg == "いらっしゃい" or
          line_msg == "どうぞ ごゆっくりなさって下さい" or
          line_msg == "どうぞ ごゆっくりなさってください" or
          line_msg == "どうぞごゆっくりなさってください" or
          line_msg == "どうぞ ごゆっくりなさって" or
          line_msg == "どうぞごゆっくりなさって" or
          line_msg == "ごゆっくりなさって下さい" or
          line_msg == "ごゆっくりなさってください" or
          line_msg == "ごゆっくりなさって" or
          line_msg == "ごゆっくり どうぞ" or
          line_msg == "ごゆっくりどうぞ" or
          line_msg == "ごゆっくり"):
            extrctd_intnt = "<歓迎＆歓待 くつろいで欲しいという気持ち>"
    elif (line_msg == "いらっしゃいませ" or
          line_msg == "いらっしゃい" or
          line_msg == "どうぞ ごゆっくりなさって下さい" or
          line_msg == "どうぞ ごゆっくりなさってください" or
          line_msg == "どうぞごゆっくりなさってください" or
          line_msg == "どうぞ ごゆっくりなさって" or
          line_msg == "どうぞごゆっくりなさって" or
          line_msg == "ごゆっくりなさって下さい" or
          line_msg == "ごゆっくりなさってください" or
          line_msg == "ごゆっくりなさって" or
          line_msg == "ごゆっくり どうぞ" or
          line_msg == "ごゆっくりどうぞ" or
          line_msg == "ごゆっくり"):
            extrctd_intnt = "<歓迎＆歓待 くつろいで欲しいという気持ち>"
    elif (line_msg == "どうぞ お手柔らかに" or
          line_msg == "どうぞお手柔らかに"):
            extrctd_intnt = "<初見・顔合わせの決まり文句 配慮などを求めて>"
    elif (line_msg == "どうぞ 宜しくお願い致します" or
          line_msg == "どうぞ よろしくお願い致します" or
          line_msg == "どうぞ よろしくお願いいたします" or
          line_msg == "どうぞ お願いいたします" or
          line_msg == "どうぞ よろしくお願いします" or
          line_msg == "どうぞ よろしく" or
          line_msg == "どうぞ宜しくお願い致します" or
          line_msg == "どうぞよろしくお願い致します" or
          line_msg == "どうぞよろしくお願いいたします" or
          line_msg == "どうぞお願いいたします" or
          line_msg == "どうぞよろしくお願いします" or
          line_msg == "どうぞよろしく" or
          line_msg == "よろしく どうぞ" or
          line_msg == "よろしくどうぞ" or
          line_msg == "よろしく"):
            extrctd_intnt = "<初見・顔合わせの決まり文句 良好な関係を求めて>"
    elif (line_msg == "頑張りましょう" or
          line_msg == "がんばりましょう" or
          line_msg == "ぼちぼち やりましょう" or
          line_msg == "ぼちぼちやりましょう" or
          line_msg == "ボチボチ やりましょう" or
          line_msg == "ボチボチやりましょう" or
          line_msg == "ゆっくり 行きましょう" or
          line_msg == "ゆっくり いきましょう" or
          line_msg == "ゆっくり行きましょう" or
          line_msg == "ゆっくりいきましょう" or
          line_msg == "ゆっくりしましょう" or
          line_msg == "急いで行きましょう" or
          line_msg == "急いでいきましょう" or
          line_msg == "急いでやりましょう" or
          line_msg == "急ぎましょう" or
          line_msg == "優しく行きましょう" or
          line_msg == "優しくしましょう" or
          line_msg == "厳しく行きましょう" or
          line_msg == "厳しくしましょう"):
            extrctd_intnt = "<推奨＆強制＆勧告 誘導に近い>"
    elif (line_msg == "本当ですよ" or
          line_msg == "ホントですよ" or
          line_msg == "本当だよ" or
          line_msg == "ホントだよ" or
          line_msg == "本当よ" or
          line_msg == "ホントよ" or
          line_msg == "ホント ホント" or
          line_msg == "ホントホント"):
            extrctd_intnt = "<宣告 真実であることを告げる>"
    elif (line_msg == "嘘ですよ" or
          line_msg == "ウソですよ" or
          line_msg == "嘘だよ" or
          line_msg == "ウソですよ" or
          line_msg == "嘘よ" or
          line_msg == "ウソよ" or
          line_msg == "ウソ ウソ" or
          line_msg == "ウソウソ"):
            extrctd_intnt = "<宣告 虚偽であることを告げる>"
    elif (line_msg == "本当ですか" or
          line_msg == "ホントですか" or
          line_msg == "本当か" or
          line_msg == "ホントか" or
          line_msg == "ホント"):
            extrctd_intnt = "<疑義＆質問＆確認 真実であるかどうか>"
    elif (line_msg == "嘘ですか" or
          line_msg == "ウソですか" or
          line_msg == "嘘か" or
          line_msg == "ウソか" or
          line_msg == "嘘" or
          line_msg == "ウソ"):
            extrctd_intnt = "<疑義＆質問＆確認 虚偽であるかどうか>"
    elif (line_msg == "左様ですか" or
          line_msg == "そうですか" or
          line_msg == "はい はい" or
          line_msg == "はいはい" or
          line_msg == "うん うん" or
          line_msg == "うんうん"):
            extrctd_intnt = "<相槌＆合いの手 傾聴している素振り>"
    elif (line_msg == "その通りです" or
          line_msg == "その通り"):
            extrctd_intnt = "<相槌＆合いの手 正鵠を得た相手に対して>"
    elif (line_msg == "賛成" or
          line_msg == "反対"):
            extrctd_intnt = "<単純な返答 投票 二者択一式>"
    elif (line_msg == "はい" or
          line_msg == "いいえ"):
            extrctd_intnt = "<単純な返答 一般 二者択一式>"
    else:
            extrctd_intnt = "<その他・不明>"
    return extrctd_intnt


#ユーザーから送られるLINEメッセージの中からインテント(＝発話の意図するもの)を抽出する
def extract_intent_from_general(line_msg):
    #メッセージの末尾部分からインテントを抽出して、これを呼出し元に引渡しをする
    if   (check_text_terminate_string(line_msg, "を行います") or
          check_text_terminate_string(line_msg, "を行う") or
          check_text_terminate_string(line_msg, "をします") or
          check_text_terminate_string(line_msg, "をする") or
          check_text_terminate_string(line_msg, "はします") or
          check_text_terminate_string(line_msg, "はする") or
          check_text_terminate_string(line_msg, "します") or
          check_text_terminate_string(line_msg, "する")):
           extrctd_intnt = "<宣言＆表明 現在＆未来 能動 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "を行いません") or
          check_text_terminate_string(line_msg, "を行わない") or
          check_text_terminate_string(line_msg, "をしません") or
          check_text_terminate_string(line_msg, "をしない") or
          check_text_terminate_string(line_msg, "はしません") or
          check_text_terminate_string(line_msg, "はしない") or
          check_text_terminate_string(line_msg, "しません") or
          check_text_terminate_string(line_msg, "しない")):
           extrctd_intnt = "<宣言＆表明 現在＆未来 能動 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "を行っています") or
          check_text_terminate_string(line_msg, "を行っている") or
          check_text_terminate_string(line_msg, "をしています") or
          check_text_terminate_string(line_msg, "をしてます") or
          check_text_terminate_string(line_msg, "をしている") or
          check_text_terminate_string(line_msg, "をしてる") or
          check_text_terminate_string(line_msg, "しています") or
          check_text_terminate_string(line_msg, "してます") or
          check_text_terminate_string(line_msg, "している") or
          check_text_terminate_string(line_msg, "してる")):
           extrctd_intnt = "<宣言＆表明 現在進行 能動 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "を行っていません") or
          check_text_terminate_string(line_msg, "を行ってません") or
          check_text_terminate_string(line_msg, "をしていません") or
          check_text_terminate_string(line_msg, "をしてません") or
          check_text_terminate_string(line_msg, "をしていない") or
          check_text_terminate_string(line_msg, "をしてない") or
          check_text_terminate_string(line_msg, "していません") or
          check_text_terminate_string(line_msg, "してません") or
          check_text_terminate_string(line_msg, "していない") or
          check_text_terminate_string(line_msg, "してない")):
            extrctd_intnt = "<宣言＆表明 現在進行 能動 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "ができています") or
          check_text_terminate_string(line_msg, "ができている") or
          check_text_terminate_string(line_msg, "ができてる") or
          check_text_terminate_string(line_msg, "できています") or
          check_text_terminate_string(line_msg, "できている") or
          check_text_terminate_string(line_msg, "できてる")):
            extrctd_intnt = "<宣言＆表明 現在進行 完了 肯定形>"
    elif (check_text_terminate_string(line_msg, "ができていません") or
          check_text_terminate_string(line_msg, "ができてません") or
          check_text_terminate_string(line_msg, "ができていない") or
          check_text_terminate_string(line_msg, "ができてない") or
          check_text_terminate_string(line_msg, "できていません") or
          check_text_terminate_string(line_msg, "できてません") or
          check_text_terminate_string(line_msg, "できていない") or
          check_text_terminate_string(line_msg, "できてない")):
            extrctd_intnt = "<宣言＆表明 現在進行 未完了 否定形>"
    elif (check_text_terminate_string(line_msg, "ができます") or
          check_text_terminate_string(line_msg, "ができる") or
          check_text_terminate_string(line_msg, "できます") or
          check_text_terminate_string(line_msg, "できる")):
            extrctd_intnt = "<宣言＆表明 可能 肯定形>"
    elif (check_text_terminate_string(line_msg, "ができません") or
          check_text_terminate_string(line_msg, "ができない") or
          check_text_terminate_string(line_msg, "できません") or
          check_text_terminate_string(line_msg, "できない")):
            extrctd_intnt = "<宣言＆表明 不可能 否定形>"
    elif (check_text_terminate_string(line_msg, "をしました") or
          check_text_terminate_string(line_msg, "をした") or
          check_text_terminate_string(line_msg, "はしました") or
          check_text_terminate_string(line_msg, "はした") or
          check_text_terminate_string(line_msg, "しました") or
          check_text_terminate_string(line_msg, "した") or
          check_text_terminate_string(line_msg, "をやりました") or
          check_text_terminate_string(line_msg, "をやった") or
          check_text_terminate_string(line_msg, "はやりました") or
          check_text_terminate_string(line_msg, "はやった")):
            extrctd_intnt = "<宣言＆表明 過去 能動 肯定形>"
    elif (check_text_terminate_string(line_msg, "をしていません") or
          check_text_terminate_string(line_msg, "をしてません") or
          check_text_terminate_string(line_msg, "をしてない") or
          check_text_terminate_string(line_msg, "はしていません") or
          check_text_terminate_string(line_msg, "はしてません") or
          check_text_terminate_string(line_msg, "はしてない") or
          check_text_terminate_string(line_msg, "していません") or
          check_text_terminate_string(line_msg, "してません") or
          check_text_terminate_string(line_msg, "してない") or
          check_text_terminate_string(line_msg, "をやってません") or
          check_text_terminate_string(line_msg, "をやってない") or
          check_text_terminate_string(line_msg, "はやってません") or
          check_text_terminate_string(line_msg, "はやってない")):
            extrctd_intnt = "<宣言＆表明 過去 能動 否定形>"
    elif (check_text_terminate_string(line_msg, "をするのですか") or
          check_text_terminate_string(line_msg, "をするんですか") or
          check_text_terminate_string(line_msg, "をしますか") or
          check_text_terminate_string(line_msg, "はするのですか") or
          check_text_terminate_string(line_msg, "はするんですか") or
          check_text_terminate_string(line_msg, "はしますか") or
          check_text_terminate_string(line_msg, "するのですか") or
          check_text_terminate_string(line_msg, "するんですか") or
          check_text_terminate_string(line_msg, "しますか") or
          check_text_terminate_string(line_msg, "するのか") or
          check_text_terminate_string(line_msg, "するか")):
           extrctd_intnt = "<疑義＆質問＆確認 現在＆未来 能動 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "をしないのですか") or
          check_text_terminate_string(line_msg, "はしないのですか") or
          check_text_terminate_string(line_msg, "をしないんですか") or
          check_text_terminate_string(line_msg, "はしないんですか") or
          check_text_terminate_string(line_msg, "をしないのか") or
          check_text_terminate_string(line_msg, "はしないのか") or
          check_text_terminate_string(line_msg, "しないのですか") or
          check_text_terminate_string(line_msg, "しないんですか") or
          check_text_terminate_string(line_msg, "しないのか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在＆未来 能動 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "をしていますか") or
          check_text_terminate_string(line_msg, "はしていますか") or
          check_text_terminate_string(line_msg, "をしてますか") or
          check_text_terminate_string(line_msg, "はしてますか") or
          check_text_terminate_string(line_msg, "をしているか") or
          check_text_terminate_string(line_msg, "はしているか") or
          check_text_terminate_string(line_msg, "をしてるか") or
          check_text_terminate_string(line_msg, "はしてるか") or
          check_text_terminate_string(line_msg, "していますか") or
          check_text_terminate_string(line_msg, "してますか") or
          check_text_terminate_string(line_msg, "しているか") or
          check_text_terminate_string(line_msg, "してるか")):
           extrctd_intnt = "<疑義＆質問＆確認 現在進行 能動 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "をしていませんか") or
          check_text_terminate_string(line_msg, "はしていませんか") or
          check_text_terminate_string(line_msg, "をしてませんか") or
          check_text_terminate_string(line_msg, "はしてませんか") or
          check_text_terminate_string(line_msg, "をしていないか") or
          check_text_terminate_string(line_msg, "はしていないか") or
          check_text_terminate_string(line_msg, "をしてないか") or
          check_text_terminate_string(line_msg, "はしてないか") or
          check_text_terminate_string(line_msg, "していませんか") or
          check_text_terminate_string(line_msg, "してませんか") or
          check_text_terminate_string(line_msg, "していないか") or
          check_text_terminate_string(line_msg, "してないか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在進行 能動 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "ができていますか") or
          check_text_terminate_string(line_msg, "はできていますか") or
          check_text_terminate_string(line_msg, "ができてますか") or
          check_text_terminate_string(line_msg, "はできてますか") or
          check_text_terminate_string(line_msg, "ができているか") or
          check_text_terminate_string(line_msg, "はできているか") or
          check_text_terminate_string(line_msg, "ができてるか") or
          check_text_terminate_string(line_msg, "はできてるか") or
          check_text_terminate_string(line_msg, "できていますか") or
          check_text_terminate_string(line_msg, "できてますか") or
          check_text_terminate_string(line_msg, "できているか") or
          check_text_terminate_string(line_msg, "できてるか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在 完了 肯定形 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "はできていませんか") or
          check_text_terminate_string(line_msg, "はできてませんか") or
          check_text_terminate_string(line_msg, "はできていないか") or
          check_text_terminate_string(line_msg, "はできてないか") or
          check_text_terminate_string(line_msg, "できていませんか") or
          check_text_terminate_string(line_msg, "できてませんか") or
          check_text_terminate_string(line_msg, "できていないか") or
          check_text_terminate_string(line_msg, "できてないか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在 未完了 否定形 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "ができましたか") or
          check_text_terminate_string(line_msg, "はできましたか") or
          check_text_terminate_string(line_msg, "ができたか") or
          check_text_terminate_string(line_msg, "はできたか") or
          check_text_terminate_string(line_msg, "できましたか") or
          check_text_terminate_string(line_msg, "できたか")):
            extrctd_intnt = "<疑義＆質問＆確認 過去 完了 肯定形 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "はできていませんか") or
          check_text_terminate_string(line_msg, "はできてませんか") or
          check_text_terminate_string(line_msg, "はできてないか") or
          check_text_terminate_string(line_msg, "できていませんか") or
          check_text_terminate_string(line_msg, "できてませんか") or
          check_text_terminate_string(line_msg, "できてないか")):
            extrctd_intnt = "<疑義＆質問＆確認 過去 未完了 否定形 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "ができますか") or
          check_text_terminate_string(line_msg, "はできますか") or
          check_text_terminate_string(line_msg, "ができるか") or
          check_text_terminate_string(line_msg, "はできるか") or
          check_text_terminate_string(line_msg, "できますか") or
          check_text_terminate_string(line_msg, "できるか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在＆未来 肯定形 物事の可能性について>"
    elif (check_text_terminate_string(line_msg, "はできませんか") or
          check_text_terminate_string(line_msg, "はできないか") or
          check_text_terminate_string(line_msg, "できませんか") or
          check_text_terminate_string(line_msg, "できないか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在＆未来 否定形 物事の可能性について>"
    elif (check_text_terminate_string(line_msg, "がされています") or
          check_text_terminate_string(line_msg, "はされています") or
          check_text_terminate_string(line_msg, "がされてます") or
          check_text_terminate_string(line_msg, "はされてます") or
          check_text_terminate_string(line_msg, "がされている") or
          check_text_terminate_string(line_msg, "はされている") or
          check_text_terminate_string(line_msg, "がされてる") or
          check_text_terminate_string(line_msg, "はされてる") or
          check_text_terminate_string(line_msg, "されています") or
          check_text_terminate_string(line_msg, "されてます") or
          check_text_terminate_string(line_msg, "されている") or
          check_text_terminate_string(line_msg, "がやられています") or
          check_text_terminate_string(line_msg, "がやられてます") or
          check_text_terminate_string(line_msg, "がやられてる") or
          check_text_terminate_string(line_msg, "はやられています") or
          check_text_terminate_string(line_msg, "はやられてます") or
          check_text_terminate_string(line_msg, "はやられてる")):
            extrctd_intnt = "<宣言＆表明 現在進行 受動 肯定形>"
    elif (check_text_terminate_string(line_msg, "がされていません") or
          check_text_terminate_string(line_msg, "はされていません") or
          check_text_terminate_string(line_msg, "されていません") or
          check_text_terminate_string(line_msg, "がされてません") or
          check_text_terminate_string(line_msg, "はされてません") or
          check_text_terminate_string(line_msg, "されてません") or
          check_text_terminate_string(line_msg, "がされていない") or
          check_text_terminate_string(line_msg, "はされていない") or
          check_text_terminate_string(line_msg, "されていない") or
          check_text_terminate_string(line_msg, "がされてない") or
          check_text_terminate_string(line_msg, "はされてない") or
          check_text_terminate_string(line_msg, "されてない")):
            extrctd_intnt = "<宣言＆表明 現在進行 受動 否定形>"
    elif (check_text_terminate_string(line_msg, "がされました") or
          check_text_terminate_string(line_msg, "はされました") or
          check_text_terminate_string(line_msg, "されました") or
          check_text_terminate_string(line_msg, "がされた") or
          check_text_terminate_string(line_msg, "はされた") or
          check_text_terminate_string(line_msg, "された")):
            extrctd_intnt = "<宣言＆表明 過去完了 受動 肯定形>"
    elif (check_text_terminate_string(line_msg, "がされませんでした") or
          check_text_terminate_string(line_msg, "はされませんでした") or
          check_text_terminate_string(line_msg, "されませんでした") or
          check_text_terminate_string(line_msg, "がされなかった") or
          check_text_terminate_string(line_msg, "はされなかった") or
          check_text_terminate_string(line_msg, "されなかった")):
            extrctd_intnt = "<宣言＆表明 過去完了 受動 否定形>"
    elif (check_text_terminate_string(line_msg, "でした") or
          check_text_terminate_string(line_msg, "だった")):
            extrctd_intnt = "<宣言＆表明 過去完了 肯定形>"
    elif (check_text_terminate_string(line_msg, "ではなかったです") or
          check_text_terminate_string(line_msg, "でなかったです") or
          check_text_terminate_string(line_msg, "ではなかった") or
          check_text_terminate_string(line_msg, "でなかった")):
            extrctd_intnt = "<宣言＆表明 過去完了 否定形>"
    elif (check_text_terminate_string(line_msg, "をしていきたい") or
          check_text_terminate_string(line_msg, "はしていきたい") or
          check_text_terminate_string(line_msg, "していきたい") or
          check_text_terminate_string(line_msg, "をやっていきたい") or
          check_text_terminate_string(line_msg, "はやっていきたい")):
            extrctd_intnt = "<宣言＆表明 現在＆未来 持続 能動 肯定形>"
    elif (check_text_terminate_string(line_msg, "をしていきたくはない") or
          check_text_terminate_string(line_msg, "はしていきたくはない") or
          check_text_terminate_string(line_msg, "していきたくはない") or
          check_text_terminate_string(line_msg, "をしていきたくない") or
          check_text_terminate_string(line_msg, "はしていきたくない") or
          check_text_terminate_string(line_msg, "していきたくない") or
          check_text_terminate_string(line_msg, "をやっていきたくはない") or
          check_text_terminate_string(line_msg, "はやっていきたくはない") or
          check_text_terminate_string(line_msg, "をやっていきたくない") or
          check_text_terminate_string(line_msg, "はやっていきたくない")):
            extrctd_intnt = "<宣言＆表明 現在＆未来 持続 能動 否定形>"
    elif (check_text_terminate_string(line_msg, "ではありました") or
          check_text_terminate_string(line_msg, "ではあった") or
          check_text_terminate_string(line_msg, "であった")):
            extrctd_intnt = "<宣言＆表明 過去＆現在 肯定形 事実・現実について>"
    elif (check_text_terminate_string(line_msg, "ではありませんでした") or
          check_text_terminate_string(line_msg, "ではなかった") or
          check_text_terminate_string(line_msg, "でなかった")):
            extrctd_intnt = "<宣言＆表明 現在＆未来 否定形 事実・現実について>"
    elif (check_text_terminate_string(line_msg, "で御座います") or
          check_text_terminate_string(line_msg, "でございます") or
          check_text_terminate_string(line_msg, "であります") or
          check_text_terminate_string(line_msg, "です")):
            extrctd_intnt = "<紹介＆説明＆提示 肯定形>"
    elif (check_text_terminate_string(line_msg, "では御座いません") or
          check_text_terminate_string(line_msg, "ではございません") or
          check_text_terminate_string(line_msg, "ではありません")):
            extrctd_intnt = "<紹介＆説明＆提示 否定形>"
    elif (check_text_terminate_string(line_msg, "をやっていました") or
          check_text_terminate_string(line_msg, "をやってました") or
          check_text_terminate_string(line_msg, "をやってた")):
            extrctd_intnt = "<報告＆連絡 過去＆現在 能動 肯定形>"
    elif (check_text_terminate_string(line_msg, "をやっていませんでした") or
          check_text_terminate_string(line_msg, "をやってませんでした") or
          check_text_terminate_string(line_msg, "をやってなかった")):
            extrctd_intnt = "<報告＆連絡 過去＆現在 能動 否定形>"
    elif (check_text_terminate_string(line_msg, "を致しませんか") or
          check_text_terminate_string(line_msg, "をいたしませんか") or
          check_text_terminate_string(line_msg, "致しませんか") or
          check_text_terminate_string(line_msg, "いたしませんか") or
          check_text_terminate_string(line_msg, "しませんか")):
            extrctd_intnt = "<誘導＆勧誘>"
    elif (check_text_terminate_string(line_msg, "を行いたい") or
          check_text_terminate_string(line_msg, "をしたい") or
          check_text_terminate_string(line_msg, "がしたい") or
          check_text_terminate_string(line_msg, "したい") or
          check_text_terminate_string(line_msg, "をやりたい") or
          check_text_terminate_string(line_msg, "がやりたい")):
            extrctd_intnt = "<願望＆欲求 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "を行いたくない") or
          check_text_terminate_string(line_msg, "をしたくない") or
          check_text_terminate_string(line_msg, "がしたくない") or
          check_text_terminate_string(line_msg, "したくない") or
          check_text_terminate_string(line_msg, "をやりたくない") or
          check_text_terminate_string(line_msg, "がやりたくない")):
            extrctd_intnt = "<願望＆欲求 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "を行いたいのですか") or
          check_text_terminate_string(line_msg, "を行いたいんですか") or
          check_text_terminate_string(line_msg, "を行いたいですか") or
          check_text_terminate_string(line_msg, "をしたいのですか") or
          check_text_terminate_string(line_msg, "をしたいんですか") or
          check_text_terminate_string(line_msg, "をしたいですか") or
          check_text_terminate_string(line_msg, "は行いたいのですか") or
          check_text_terminate_string(line_msg, "は行いたいんですか") or
          check_text_terminate_string(line_msg, "は行いたいですか") or
          check_text_terminate_string(line_msg, "はしたいのですか") or
          check_text_terminate_string(line_msg, "はしたいんですか") or
          check_text_terminate_string(line_msg, "はしたいですか") or
          check_text_terminate_string(line_msg, "したいのですか") or
          check_text_terminate_string(line_msg, "したいんですか") or
          check_text_terminate_string(line_msg, "したいですか") or
          check_text_terminate_string(line_msg, "したいのか") or
          check_text_terminate_string(line_msg, "したいか") or
          check_text_terminate_string(line_msg, "をやりたいのですか") or
          check_text_terminate_string(line_msg, "をやりたいんですか") or
          check_text_terminate_string(line_msg, "をやりたいですか") or
          check_text_terminate_string(line_msg, "をやりたいのか") or
          check_text_terminate_string(line_msg, "をやりたいか") or
          check_text_terminate_string(line_msg, "がやりたいのですか") or
          check_text_terminate_string(line_msg, "がやりたいんですか") or
          check_text_terminate_string(line_msg, "がやりたいですか") or
          check_text_terminate_string(line_msg, "がやりたいのか") or
          check_text_terminate_string(line_msg, "がやりたいか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "を行いたくないのですか") or
          check_text_terminate_string(line_msg, "を行いたくないんですか") or
          check_text_terminate_string(line_msg, "を行いたくないですか") or
          check_text_terminate_string(line_msg, "をしたくないのですか") or
          check_text_terminate_string(line_msg, "をしたくないんですか") or
          check_text_terminate_string(line_msg, "をしたくないですか") or
          check_text_terminate_string(line_msg, "は行いたくないのですか") or
          check_text_terminate_string(line_msg, "は行いたくないんですか") or
          check_text_terminate_string(line_msg, "は行いたくないですか") or
          check_text_terminate_string(line_msg, "はしたくないのですか") or
          check_text_terminate_string(line_msg, "はしたくないんですか") or
          check_text_terminate_string(line_msg, "はしたくないですか") or
          check_text_terminate_string(line_msg, "したくないのですか") or
          check_text_terminate_string(line_msg, "したくないんですか") or
          check_text_terminate_string(line_msg, "したくないですか") or
          check_text_terminate_string(line_msg, "したくないか") or
          check_text_terminate_string(line_msg, "をやりたくないのですか") or
          check_text_terminate_string(line_msg, "をやりたくないんですか") or
          check_text_terminate_string(line_msg, "をやりたくないですか") or
          check_text_terminate_string(line_msg, "をやりたくないか") or
          check_text_terminate_string(line_msg, "がやりたくないのですか") or
          check_text_terminate_string(line_msg, "がやりたくないんですか") or
          check_text_terminate_string(line_msg, "がやりたくないですか") or
          check_text_terminate_string(line_msg, "がやりたくないのか") or
          check_text_terminate_string(line_msg, "がやりたくないか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "をしていきたいですか") or
          check_text_terminate_string(line_msg, "をしていきたいか") or
          check_text_terminate_string(line_msg, "していきたいか") or
          check_text_terminate_string(line_msg, "をやっていきたいですか") or
          check_text_terminate_string(line_msg, "をやっていきたいか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在＆未来 肯定形 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "をしていきたくないですか") or
          check_text_terminate_string(line_msg, "はしていきたくないですか") or
          check_text_terminate_string(line_msg, "していきたくないですか") or
          check_text_terminate_string(line_msg, "をしていきたくないか") or
          check_text_terminate_string(line_msg, "はしていきたくないか") or
          check_text_terminate_string(line_msg, "していきたくないか") or
          check_text_terminate_string(line_msg, "はやっていきたくないか") or
          check_text_terminate_string(line_msg, "をやっていきたくないか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在＆未来 否定形 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "をやり続けたいですか") or
          check_text_terminate_string(line_msg, "をやり続けたいか") or
          check_text_terminate_string(line_msg, "をやってたいですか") or
          check_text_terminate_string(line_msg, "をやってたいか") or
          check_text_terminate_string(line_msg, "をし続けたいですか") or
          check_text_terminate_string(line_msg, "をし続けたいか") or
          check_text_terminate_string(line_msg, "をしてたいですか") or
          check_text_terminate_string(line_msg, "をしてたいか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在＆未来 肯定形 持続的 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "をやり続けたくないですか") or
          check_text_terminate_string(line_msg, "をやり続けたくないか") or
          check_text_terminate_string(line_msg, "をやってたくないですか") or
          check_text_terminate_string(line_msg, "をやってたくないか") or
          check_text_terminate_string(line_msg, "をし続けたくないですか") or
          check_text_terminate_string(line_msg, "をし続けたくないか") or
          check_text_terminate_string(line_msg, "をしてたくないですか") or
          check_text_terminate_string(line_msg, "をしてたくないか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在＆未来 肯定形 持続的 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "をしましたか") or
          check_text_terminate_string(line_msg, "をしたか") or
          check_text_terminate_string(line_msg, "はしましたか") or
          check_text_terminate_string(line_msg, "はしたか") or
          check_text_terminate_string(line_msg, "しましたか") or
          check_text_terminate_string(line_msg, "したか") or
          check_text_terminate_string(line_msg, "をやりましたか") or
          check_text_terminate_string(line_msg, "をやったか") or
          check_text_terminate_string(line_msg, "はやりましたか") or
          check_text_terminate_string(line_msg, "はやったか")):
            extrctd_intnt = "<疑義＆質問＆確認 過去 能動 肯定形 他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "をしていませんか") or
          check_text_terminate_string(line_msg, "をしてませんか") or
          check_text_terminate_string(line_msg, "をしてないか") or
          check_text_terminate_string(line_msg, "はしていませんか") or
          check_text_terminate_string(line_msg, "はしてませんか") or
          check_text_terminate_string(line_msg, "はしてないか") or
          check_text_terminate_string(line_msg, "していませんか") or
          check_text_terminate_string(line_msg, "してませんか") or
          check_text_terminate_string(line_msg, "してないか")):
            extrctd_intnt = "<疑義＆質問＆確認 過去 能動 否定形 他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg, "はされていますか") or
          check_text_terminate_string(line_msg, "されていますか") or
          check_text_terminate_string(line_msg, "されてますか") or
          check_text_terminate_string(line_msg, "されてますか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在 受動 肯定形 他者の行為・行動について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "はされていませんか") or
          check_text_terminate_string(line_msg, "されていませんか") or
          check_text_terminate_string(line_msg, "されてませんか") or
          check_text_terminate_string(line_msg, "されていないか") or
          check_text_terminate_string(line_msg, "されてないか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在 受動 否定形 他者の行為・行動について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "はされていましたか") or
          check_text_terminate_string(line_msg, "はされてましたか") or
          check_text_terminate_string(line_msg, "されてましたか") or
          check_text_terminate_string(line_msg, "されてたか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在 受動 肯定形 他者の行為・行動について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "はされていませんでしたか") or
          check_text_terminate_string(line_msg, "はされていなかったか") or
          check_text_terminate_string(line_msg, "されていませんでしたか") or
          check_text_terminate_string(line_msg, "されていなかったか")):
            extrctd_intnt = "<疑義＆質問＆確認 現在 受動 否定形 他者の行為・行動について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "だったですか") or
          check_text_terminate_string(line_msg, "だったか") or
          check_text_terminate_string(line_msg, "でしたか")):
            extrctd_intnt = "<疑義＆質問＆確認 過去完了 肯定形 他者の状況・状態について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "ではなかったですか") or
          check_text_terminate_string(line_msg, "ではなかったか") or
          check_text_terminate_string(line_msg, "でなかったか")):
            extrctd_intnt = "<疑義＆質問＆確認 過去完了 否定形 他者の状況・状態について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "をしなさい") or
          check_text_terminate_string(line_msg, "をしろ") or
          check_text_terminate_string(line_msg, "はしなさい") or
          check_text_terminate_string(line_msg, "はしろ") or
          check_text_terminate_string(line_msg, "しなさい") or
          check_text_terminate_string(line_msg, "しろ")):
            extrctd_intnt = "<指示＆命令>"
    elif (check_text_terminate_string(line_msg, "をしなければならない") or
          check_text_terminate_string(line_msg, "をしなければ") or
          check_text_terminate_string(line_msg, "をしないといけないです") or
          check_text_terminate_string(line_msg, "をしないといけない") or
          check_text_terminate_string(line_msg, "をしなきゃいけないです") or
          check_text_terminate_string(line_msg, "をしなきゃいけない") or
          check_text_terminate_string(line_msg, "をしなきゃならない") or
          check_text_terminate_string(line_msg, "をしなきゃ") or
          check_text_terminate_string(line_msg, "はしなければならない") or
          check_text_terminate_string(line_msg, "はしなければ") or
          check_text_terminate_string(line_msg, "はしないといけないです") or
          check_text_terminate_string(line_msg, "はしないといけない") or
          check_text_terminate_string(line_msg, "はしなきゃいけないです") or
          check_text_terminate_string(line_msg, "はしなきゃいけない") or
          check_text_terminate_string(line_msg, "はしなきゃならない") or
          check_text_terminate_string(line_msg, "はしなきゃ") or
          check_text_terminate_string(line_msg, "しなければならない") or
          check_text_terminate_string(line_msg, "しなければ") or
          check_text_terminate_string(line_msg, "しないといけないです") or
          check_text_terminate_string(line_msg, "しないといけない") or
          check_text_terminate_string(line_msg, "しなきゃいけないです") or
          check_text_terminate_string(line_msg, "しなきゃいけない") or
          check_text_terminate_string(line_msg, "しなきゃならない") or
          check_text_terminate_string(line_msg, "しなきゃ")):
            extrctd_intnt = "<強制＆勧告 肯定形>"
    elif (check_text_terminate_string(line_msg, "がしなければならない") or
          check_text_terminate_string(line_msg, "がしなければ") or
          check_text_terminate_string(line_msg, "がしないといけないです") or
          check_text_terminate_string(line_msg, "がしないといけない") or
          check_text_terminate_string(line_msg, "がしなきゃいけないです") or
          check_text_terminate_string(line_msg, "がしなきゃいけない") or
          check_text_terminate_string(line_msg, "がしなきゃならない") or
          check_text_terminate_string(line_msg, "がしなきゃ")):
            extrctd_intnt = "<強制＆勧告 肯定形 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg, "はしてはならない") or
          check_text_terminate_string(line_msg, "はしてはいけない") or
          check_text_terminate_string(line_msg, "はしたらいけない") or
          check_text_terminate_string(line_msg, "はしちゃいけない") or
          check_text_terminate_string(line_msg, "をしてはならない") or
          check_text_terminate_string(line_msg, "をしてはいけない") or
          check_text_terminate_string(line_msg, "をしたらいけない") or
          check_text_terminate_string(line_msg, "をしちゃいけない") or
          check_text_terminate_string(line_msg, "してはならない") or
          check_text_terminate_string(line_msg, "してはいけない") or
          check_text_terminate_string(line_msg, "したらいけない") or
          check_text_terminate_string(line_msg, "しちゃいけない")):
            extrctd_intnt = "<強制＆勧告 否定形>"
    elif (check_text_terminate_string(line_msg, "がしてはならない") or
          check_text_terminate_string(line_msg, "がしてはいけない") or
          check_text_terminate_string(line_msg, "がしたらいけない") or
          check_text_terminate_string(line_msg, "がしちゃいけない")):
            extrctd_intnt = "<強制＆勧告 否定形 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg, "はしなければならないのですか") or
          check_text_terminate_string(line_msg, "はしなければならないんですか") or
          check_text_terminate_string(line_msg, "はしなければならないですか") or
          check_text_terminate_string(line_msg, "はしなければいけないですか") or
          check_text_terminate_string(line_msg, "はしないといけないですか") or
          check_text_terminate_string(line_msg, "はしなきゃいけないですか") or
          check_text_terminate_string(line_msg, "はしなきゃいけないか") or
          check_text_terminate_string(line_msg, "はしなきゃならないか") or
          check_text_terminate_string(line_msg, "をしなければならないのですか") or
          check_text_terminate_string(line_msg, "をしなければならないんですか") or
          check_text_terminate_string(line_msg, "をしなければならないですか") or
          check_text_terminate_string(line_msg, "をしなければいけないですか") or
          check_text_terminate_string(line_msg, "をしないといけないですか") or
          check_text_terminate_string(line_msg, "をしなきゃいけないですか") or
          check_text_terminate_string(line_msg, "をしなきゃいけないか") or
          check_text_terminate_string(line_msg, "をしなきゃならないか") or
          check_text_terminate_string(line_msg, "しなければならないのですか") or
          check_text_terminate_string(line_msg, "しなければならないんですか") or
          check_text_terminate_string(line_msg, "しなければならないですか") or
          check_text_terminate_string(line_msg, "しなければいけないですか") or
          check_text_terminate_string(line_msg, "しないといけないですか") or
          check_text_terminate_string(line_msg, "しなきゃいけないですか") or
          check_text_terminate_string(line_msg, "しなきゃいけないか") or
          check_text_terminate_string(line_msg, "しなきゃならないか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 強制・勧告について>"
    elif (check_text_terminate_string(line_msg, "がしなければならないのですか") or
          check_text_terminate_string(line_msg, "がしなければならないんですか") or
          check_text_terminate_string(line_msg, "がしなければならないのか") or
          check_text_terminate_string(line_msg, "がしなければならないか") or
          check_text_terminate_string(line_msg, "がしないといけないですか") or
          check_text_terminate_string(line_msg, "がしないといけないか") or
          check_text_terminate_string(line_msg, "がしなきゃいけないですか") or
          check_text_terminate_string(line_msg, "がしなきゃいけないのか") or
          check_text_terminate_string(line_msg, "がしなきゃいけないか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 強制・勧告について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg, "はしてはならないのか") or
          check_text_terminate_string(line_msg, "はしてはならないか") or
          check_text_terminate_string(line_msg, "はしてはいけないか") or
          check_text_terminate_string(line_msg, "はしたらいけないか") or
          check_text_terminate_string(line_msg, "はしちゃいけないか") or
          check_text_terminate_string(line_msg, "をしてはならないのか") or
          check_text_terminate_string(line_msg, "をしてはならないか") or
          check_text_terminate_string(line_msg, "をしてはいけないか") or
          check_text_terminate_string(line_msg, "をしたらいけないか") or
          check_text_terminate_string(line_msg, "をしちゃいけないか") or
          check_text_terminate_string(line_msg, "してはならないのか") or
          check_text_terminate_string(line_msg, "してはならないか") or
          check_text_terminate_string(line_msg, "してはいけないか") or
          check_text_terminate_string(line_msg, "したらいけないか") or
          check_text_terminate_string(line_msg, "しちゃいけないか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 強制・勧告について>"
    elif (check_text_terminate_string(line_msg, "がしてはならないのか") or
          check_text_terminate_string(line_msg, "がしてはならないか") or
          check_text_terminate_string(line_msg, "がしてはいけないか") or
          check_text_terminate_string(line_msg, "がしたらいけないか") or
          check_text_terminate_string(line_msg, "がしちゃいけないか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 強制・勧告について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg, "はするべきです") or
          check_text_terminate_string(line_msg, "をするべきです") or
          check_text_terminate_string(line_msg, "はすべきです") or
          check_text_terminate_string(line_msg, "をすべきです") or
          check_text_terminate_string(line_msg, "するべきです") or
          check_text_terminate_string(line_msg, "すべきです")):
            extrctd_intnt = "<宣言＆表明 肯定形 行為・行動の是非について>"
    elif (check_text_terminate_string(line_msg, "はするべきではないです") or
          check_text_terminate_string(line_msg, "をするべきではないです") or
          check_text_terminate_string(line_msg, "はすべきではないです") or
          check_text_terminate_string(line_msg, "をすべきではないです") or
          check_text_terminate_string(line_msg, "はすべきではないです") or
          check_text_terminate_string(line_msg, "をすべきではないです") or
          check_text_terminate_string(line_msg, "するべきではないです") or
          check_text_terminate_string(line_msg, "するべきでない") or
          check_text_terminate_string(line_msg, "すべきでない")):
            extrctd_intnt = "<宣言＆表明 否定形 行為・行動の是非について>"
    elif (check_text_terminate_string(line_msg, "をするべきでしょうか") or
          check_text_terminate_string(line_msg, "はするべきでしょうか") or
          check_text_terminate_string(line_msg, "をすべきでしょうか") or
          check_text_terminate_string(line_msg, "はすべきでしょうか") or
          check_text_terminate_string(line_msg, "するべきでしょうか") or
          check_text_terminate_string(line_msg, "すべきでしょうか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 行為・行動の是非について>"
    elif (check_text_terminate_string(line_msg, "をするべきではないのでしょうか") or
          check_text_terminate_string(line_msg, "はするべきではないのでしょうか") or
          check_text_terminate_string(line_msg, "をすべきではないのでしょうか") or
          check_text_terminate_string(line_msg, "はすべきではないのでしょうか") or
          check_text_terminate_string(line_msg, "するべきではないのでしょうか") or
          check_text_terminate_string(line_msg, "すべきではないのでしょうか") or
          check_text_terminate_string(line_msg, "すべきでないのでしょうか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 行為・行動の是非について>"
    elif (check_text_terminate_string(line_msg, "をしても良いです") or
          check_text_terminate_string(line_msg, "をしてもいいです") or
          check_text_terminate_string(line_msg, "をして良いです") or
          check_text_terminate_string(line_msg, "をしていいです") or
          check_text_terminate_string(line_msg, "をしても良い") or
          check_text_terminate_string(line_msg, "をしてもいい") or
          check_text_terminate_string(line_msg, "をして良い") or
          check_text_terminate_string(line_msg, "をしていい") or
          check_text_terminate_string(line_msg, "はしても良いです") or
          check_text_terminate_string(line_msg, "はしてもいいです") or
          check_text_terminate_string(line_msg, "はして良いです") or
          check_text_terminate_string(line_msg, "はしていいです") or
          check_text_terminate_string(line_msg, "はしても良い") or
          check_text_terminate_string(line_msg, "はしてもいい") or
          check_text_terminate_string(line_msg, "はして良い") or
          check_text_terminate_string(line_msg, "はしていい") or
          check_text_terminate_string(line_msg, "をやっても良いです") or
          check_text_terminate_string(line_msg, "をやってもいいです") or
          check_text_terminate_string(line_msg, "はやっても良いです") or
          check_text_terminate_string(line_msg, "はやってもいいです") or
          check_text_terminate_string(line_msg, "しても良いです") or
          check_text_terminate_string(line_msg, "してもいいです") or
          check_text_terminate_string(line_msg, "して良いです") or
          check_text_terminate_string(line_msg, "していいです") or
          check_text_terminate_string(line_msg, "しても良い") or
          check_text_terminate_string(line_msg, "してもいい") or
          check_text_terminate_string(line_msg, "して良い") or
          check_text_terminate_string(line_msg, "していい")):
            extrctd_intnt = "<許容＆許可>"
    elif (check_text_terminate_string(line_msg, "をしないように") or
          check_text_terminate_string(line_msg, "をしないよう") or
          check_text_terminate_string(line_msg, "をするな") or
          check_text_terminate_string(line_msg, "をしてはいけない") or
          check_text_terminate_string(line_msg, "をしちゃいけない") or
          check_text_terminate_string(line_msg, "はしないように") or
          check_text_terminate_string(line_msg, "はしないよう") or
          check_text_terminate_string(line_msg, "はするな") or
          check_text_terminate_string(line_msg, "はしてはいけない") or
          check_text_terminate_string(line_msg, "はしちゃいけない") or
          check_text_terminate_string(line_msg, "をやってはいけない") or
          check_text_terminate_string(line_msg, "をやっちゃいけない") or
          check_text_terminate_string(line_msg, "はやってはいけない") or
          check_text_terminate_string(line_msg, "はやっちゃいけない") or
          check_text_terminate_string(line_msg, "をしちゃ駄目だ") or
          check_text_terminate_string(line_msg, "をしちゃだめだ") or
          check_text_terminate_string(line_msg, "をしちゃダメだ") or
          check_text_terminate_string(line_msg, "はしちゃ駄目だ") or
          check_text_terminate_string(line_msg, "はしちゃだめだ") or
          check_text_terminate_string(line_msg, "をしちゃ駄目") or
          check_text_terminate_string(line_msg, "をしちゃだめ") or
          check_text_terminate_string(line_msg, "をしちゃダメ") or
          check_text_terminate_string(line_msg, "はしちゃ駄目") or
          check_text_terminate_string(line_msg, "はしちゃだめ") or
          check_text_terminate_string(line_msg, "しないように") or
          check_text_terminate_string(line_msg, "しないよう") or
          check_text_terminate_string(line_msg, "するな") or
          check_text_terminate_string(line_msg, "してはいけない") or
          check_text_terminate_string(line_msg, "しちゃいけない") or
          check_text_terminate_string(line_msg, "はいけない") or
          check_text_terminate_string(line_msg, "しちゃ駄目だ") or
          check_text_terminate_string(line_msg, "しちゃだめだ") or
          check_text_terminate_string(line_msg, "しちゃダメだ") or
          check_text_terminate_string(line_msg, "しちゃ駄目") or
          check_text_terminate_string(line_msg, "しちゃだめ") or
          check_text_terminate_string(line_msg, "しちゃダメ")):
            extrctd_intnt = "<禁止＆制限>"
    elif (check_text_terminate_string(line_msg, "がしないように") or
          check_text_terminate_string(line_msg, "がしないよう") or
          check_text_terminate_string(line_msg, "がするな") or
          check_text_terminate_string(line_msg, "がやってはいけない") or
          check_text_terminate_string(line_msg, "がやっちゃいけない") or
          check_text_terminate_string(line_msg, "がやっちゃ駄目だ") or
          check_text_terminate_string(line_msg, "がやっちゃだめだ") or
          check_text_terminate_string(line_msg, "がやっちゃダメだ") or
          check_text_terminate_string(line_msg, "がやっちゃ駄目") or
          check_text_terminate_string(line_msg, "がやっちゃだめ") or
          check_text_terminate_string(line_msg, "がやっちゃダメ") or
          check_text_terminate_string(line_msg, "がしちゃ駄目だ") or
          check_text_terminate_string(line_msg, "がしちゃだめだ") or
          check_text_terminate_string(line_msg, "がしちゃダメだ") or
          check_text_terminate_string(line_msg, "がしちゃ駄目") or
          check_text_terminate_string(line_msg, "がしちゃだめ") or
          check_text_terminate_string(line_msg, "がしちゃダメ")):
            extrctd_intnt = "<禁止＆制限 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg, "をしてはいけませんか") or
          check_text_terminate_string(line_msg, "をしてはいけないですか") or
          check_text_terminate_string(line_msg, "をしてはいけないか") or
          check_text_terminate_string(line_msg, "はしてはいけませんか") or
          check_text_terminate_string(line_msg, "はしてはいけないですか") or
          check_text_terminate_string(line_msg, "はしてはいけないか") or
          check_text_terminate_string(line_msg, "をやってはいけませんか") or
          check_text_terminate_string(line_msg, "をやってはいけないですか") or
          check_text_terminate_string(line_msg, "をやってはいけないか") or
          check_text_terminate_string(line_msg, "をやっちゃ駄目か") or
          check_text_terminate_string(line_msg, "をやっちゃだめか") or
          check_text_terminate_string(line_msg, "をやっちゃダメか") or
          check_text_terminate_string(line_msg, "をしちゃ駄目ですか") or
          check_text_terminate_string(line_msg, "をしちゃだめですか") or
          check_text_terminate_string(line_msg, "をしちゃダメですか") or
          check_text_terminate_string(line_msg, "はしちゃ駄目ですか") or
          check_text_terminate_string(line_msg, "はしちゃだめですか") or
          check_text_terminate_string(line_msg, "はしちゃダメですか") or
          check_text_terminate_string(line_msg, "をしちゃ駄目か") or
          check_text_terminate_string(line_msg, "をしちゃだめか") or
          check_text_terminate_string(line_msg, "をしちゃダメか") or
          check_text_terminate_string(line_msg, "はしちゃ駄目か") or
          check_text_terminate_string(line_msg, "はしちゃだめか") or
          check_text_terminate_string(line_msg, "はしちゃダメか") or
          check_text_terminate_string(line_msg, "しちゃ駄目か") or
          check_text_terminate_string(line_msg, "しちゃだめか") or
          check_text_terminate_string(line_msg, "しちゃダメか")):
            extrctd_intnt = "<疑義＆質問＆確認 禁止・制限事項について>"
    elif (check_text_terminate_string(line_msg, "がしてはいけませんか") or
          check_text_terminate_string(line_msg, "がしてはいけないか") or
          check_text_terminate_string(line_msg, "がやってはいけないか") or
          check_text_terminate_string(line_msg, "がやっちゃ駄目か") or
          check_text_terminate_string(line_msg, "がやっちゃだめか") or
          check_text_terminate_string(line_msg, "がやっちゃダメか") or
          check_text_terminate_string(line_msg, "がしちゃ駄目か") or
          check_text_terminate_string(line_msg, "がしちゃだめか") or
          check_text_terminate_string(line_msg, "がしちゃダメか")):
            extrctd_intnt = "<疑義＆質問＆確認 禁止・制限事項について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg, "をして下さい") or
          check_text_terminate_string(line_msg, "をしてください") or
          check_text_terminate_string(line_msg, "をしてくれ") or
          check_text_terminate_string(line_msg, "をして") or
          check_text_terminate_string(line_msg, "はして下さい") or
          check_text_terminate_string(line_msg, "はしてください") or
          check_text_terminate_string(line_msg, "して下さい") or
          check_text_terminate_string(line_msg, "してください") or
          check_text_terminate_string(line_msg, "下さい") or
          check_text_terminate_string(line_msg, "ください") or
          check_text_terminate_string(line_msg, "はしてくれ") or
          check_text_terminate_string(line_msg, "はして") or 
          check_text_terminate_string(line_msg, "してくれ") or
          check_text_terminate_string(line_msg, "くれ")):
            extrctd_intnt = "<依頼＆要求>"
    elif (check_text_terminate_string(line_msg, "がして下さい") or
          check_text_terminate_string(line_msg, "がしてください") or
          check_text_terminate_string(line_msg, "がしてくれ") or
          check_text_terminate_string(line_msg, "がして")):
            extrctd_intnt = "<依頼＆要求 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg, "をして下さいますか") or
          check_text_terminate_string(line_msg, "をしてくださいますか") or
          check_text_terminate_string(line_msg, "して下さいますか") or
          check_text_terminate_string(line_msg, "してくださいますか") or
          check_text_terminate_string(line_msg, "下さいますか") or
          check_text_terminate_string(line_msg, "くださいますか") or
          check_text_terminate_string(line_msg, "をしてくれますか") or
          check_text_terminate_string(line_msg, "をしてくれますか") or
          check_text_terminate_string(line_msg, "はしてくれますか") or
          check_text_terminate_string(line_msg, "くれますか") or
          check_text_terminate_string(line_msg, "してくれるか") or
          check_text_terminate_string(line_msg, "くれるか") or
          check_text_terminate_string(line_msg, "をやって下さいますか") or
          check_text_terminate_string(line_msg, "をやってくださいますか") or
          check_text_terminate_string(line_msg, "をやってくれますか") or
          check_text_terminate_string(line_msg, "をやってくれるか") or
          check_text_terminate_string(line_msg, "はやって下さいますか") or
          check_text_terminate_string(line_msg, "はやってくださいますか") or
          check_text_terminate_string(line_msg, "はやってくれますか") or
          check_text_terminate_string(line_msg, "はやってくれるか")):
            extrctd_intnt = "<疑義＆質問＆確認 依頼・要求について>"
    elif (check_text_terminate_string(line_msg, "がして下さいますか") or
          check_text_terminate_string(line_msg, "がしてくださいますか") or
          check_text_terminate_string(line_msg, "がしてくれますか") or
          check_text_terminate_string(line_msg, "がやってくれますか") or
          check_text_terminate_string(line_msg, "がやってくれるか")):
            extrctd_intnt = "<疑義＆質問＆確認 依頼・要求について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg, "がして下さいますか") or
          check_text_terminate_string(line_msg, "がしてくださいますか") or
          check_text_terminate_string(line_msg, "がしてくれますか") or
          check_text_terminate_string(line_msg, "がやってくれますか") or
          check_text_terminate_string(line_msg, "がやってくれるか")):
            extrctd_intnt = "<疑義＆質問＆確認 依頼・要求について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg, "をお願い致します") or
          check_text_terminate_string(line_msg, "をお願いいたします") or
          check_text_terminate_string(line_msg, "をお願いします") or
          check_text_terminate_string(line_msg, "をお願い")):
            extrctd_intnt = "<依頼＆依願>"
    elif (check_text_terminate_string(line_msg, "しいです")):
            extrctd_intnt = "<紹介＆説明＆提示 形容的な表現>"
    elif check_text_terminate_string(line_msg, "だ"):
            extrctd_intnt = "<宣言＆表明＆紹介＆説明＆提示 誇示・顕示して>"
    elif (check_text_terminate_string(line_msg, "でしょう") or
          check_text_terminate_string(line_msg, "だろう") or
          check_text_terminate_string(line_msg, "だろ")):
            extrctd_intnt = "<推定＆推測＆推量 肯定形>"
    elif (check_text_terminate_string(line_msg, "ではないでしょう") or
          check_text_terminate_string(line_msg, "ではないだろう") or
          check_text_terminate_string(line_msg, "ではないだろ")):
            extrctd_intnt = "<推定＆推測＆推量 否定形>"
    elif (check_text_terminate_string(line_msg, "でしょうか") or
          check_text_terminate_string(line_msg, "だろうか") or
          check_text_terminate_string(line_msg, "だろか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 推定・推測・推量について>"
    elif (check_text_terminate_string(line_msg, "ではないでしょうか") or
          check_text_terminate_string(line_msg, "ではないだろうか") or
          check_text_terminate_string(line_msg, "ではないだろか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 推定・推測・推量について>"
    elif (check_text_terminate_string(line_msg, "だそうです") or
          check_text_terminate_string(line_msg, "だそう")):
            extrctd_intnt = "<報告＆連絡 肯定形 推定・推測・推量して>"
    elif (check_text_terminate_string(line_msg, "ではないそうです") or
          check_text_terminate_string(line_msg, "ではないそう")):
            extrctd_intnt = "<報告＆連絡 否定形 推定・推測・推量して>"
    elif (check_text_terminate_string(line_msg, "はいます") or
          check_text_terminate_string(line_msg, "はいる")):
            extrctd_intnt = "<報告＆連絡 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg, "がいます") or
          check_text_terminate_string(line_msg, "がいる")):
            extrctd_intnt = "<報告＆連絡 肯定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg, "はいません") or
          check_text_terminate_string(line_msg, "はいない")):
            extrctd_intnt = "<報告＆連絡 否定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg, "がいません") or
          check_text_terminate_string(line_msg, "がいない")):
            extrctd_intnt = "<報告＆連絡 否定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg, "はいますか") or
          check_text_terminate_string(line_msg, "はいるか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg, "がいますか") or
          check_text_terminate_string(line_msg, "がいるか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg, "はいませんか") or
          check_text_terminate_string(line_msg, "はいないか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg, "がいませんか") or
          check_text_terminate_string(line_msg, "がいないか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg, "にいます") or
          check_text_terminate_string(line_msg, "にいる")):
            extrctd_intnt = "<報告＆連絡 肯定形 所在・場所について>"
    elif (check_text_terminate_string(line_msg, "にいません") or
          check_text_terminate_string(line_msg, "にいない")):
            extrctd_intnt = "<報告＆連絡 否定形 所在・場所について>"
    elif (check_text_terminate_string(line_msg, "はあります") or
          check_text_terminate_string(line_msg, "はある")):
            extrctd_intnt = "<報告＆連絡 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg, "があります") or
          check_text_terminate_string(line_msg, "がある")):
            extrctd_intnt = "<報告＆連絡 肯定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg, "はありません") or
          check_text_terminate_string(line_msg, "はない")):
            extrctd_intnt = "<報告＆連絡 否定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg, "がありません") or
          check_text_terminate_string(line_msg, "がない")):
            extrctd_intnt = "<報告＆連絡 否定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg, "にいますか") or
          check_text_terminate_string(line_msg, "にいるか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg, "にいませんか") or
          check_text_terminate_string(line_msg, "にいないか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg, "はありますか") or
          check_text_terminate_string(line_msg, "はあるか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg, "がありますか") or
          check_text_terminate_string(line_msg, "があるか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg, "はありませんか") or
          check_text_terminate_string(line_msg, "はあるか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 存在の有無について"
    elif (check_text_terminate_string(line_msg, "がありませんか") or
          check_text_terminate_string(line_msg, "がないか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg, "っている") or
          check_text_terminate_string(line_msg, "ている") or
          check_text_terminate_string(line_msg, "ってある") or
          check_text_terminate_string(line_msg, "ている")):
            extrctd_intnt = "<報告＆連絡 肯定形 存在の状態について"
    elif (check_text_terminate_string(line_msg, "ってない") or
          check_text_terminate_string(line_msg, "てない")):
            extrctd_intnt = "<報告＆連絡 否定形 存在の状態について"
    elif (check_text_terminate_string(line_msg, "で御座います") or
          check_text_terminate_string(line_msg, "でございます") or
          check_text_terminate_string(line_msg, "であります") or
          check_text_terminate_string(line_msg, "です")):
            extrctd_intnt = "<宣言＆表明＆紹介＆説明＆提示 肯定形 漠然として>"
    elif (check_text_terminate_string(line_msg, "では御座いません") or
          check_text_terminate_string(line_msg, "ではございません") or
          check_text_terminate_string(line_msg, "ではありません") or
          check_text_terminate_string(line_msg, "ではないです")):
            extrctd_intnt = "<宣言＆表明＆紹介＆説明＆提示 否定形 漠然として>"
    elif (check_text_terminate_string(line_msg, "で御座いますか") or
          check_text_terminate_string(line_msg, "でございますか") or
          check_text_terminate_string(line_msg, "でありますか") or
          check_text_terminate_string(line_msg, "ですか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 漠然として>"
    elif (check_text_terminate_string(line_msg, "では御座いませんか") or
          check_text_terminate_string(line_msg, "ではございませんか") or
          check_text_terminate_string(line_msg, "ではありませんか") or
          check_text_terminate_string(line_msg, "ではないですか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 漠然として>"
    elif (check_text_terminate_string(line_msg, "で御座いましたか") or
          check_text_terminate_string(line_msg, "でございましたか") or
          check_text_terminate_string(line_msg, "でありましたか") or
          check_text_terminate_string(line_msg, "でしたか") or
          check_text_terminate_string(line_msg, "だったか")):
            extrctd_intnt = "<疑義＆質問＆確認 過去 肯定形 他者の状況・状態について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg, "という事で御座います") or
          check_text_terminate_string(line_msg, "という事でございます") or
          check_text_terminate_string(line_msg, "ということで御座います") or
          check_text_terminate_string(line_msg, "ということでございます") or
          check_text_terminate_string(line_msg, "という事であります") or
          check_text_terminate_string(line_msg, "ということであります") or
          check_text_terminate_string(line_msg, "という事です") or
          check_text_terminate_string(line_msg, "ということです") or
          check_text_terminate_string(line_msg, "って事です") or
          check_text_terminate_string(line_msg, "ってことです")):
            extrctd_intnt = "<紹介＆説明＆提示 肯定形 なんらかの内容についての叙述>"
    elif (check_text_terminate_string(line_msg, "という事では御座いません") or
          check_text_terminate_string(line_msg, "という事ではございません") or
          check_text_terminate_string(line_msg, "ということでは御座いません") or
          check_text_terminate_string(line_msg, "ということではございません") or
          check_text_terminate_string(line_msg, "という事ではありません") or
          check_text_terminate_string(line_msg, "ということではありません") or
          check_text_terminate_string(line_msg, "って事ではないです") or
          check_text_terminate_string(line_msg, "ってことではないです")):
            extrctd_intnt = "<紹介＆説明＆提示 否定形 なんらかの内容についての叙述>"
    elif (check_text_terminate_string(line_msg, "という事で御座いますか") or
          check_text_terminate_string(line_msg, "という事でございますか") or
          check_text_terminate_string(line_msg, "ということで御座いますか") or
          check_text_terminate_string(line_msg, "ということでございますか") or
          check_text_terminate_string(line_msg, "という事でありますか") or
          check_text_terminate_string(line_msg, "ということでありますか") or
          check_text_terminate_string(line_msg, "という事ですか") or
          check_text_terminate_string(line_msg, "ということですか") or
          check_text_terminate_string(line_msg, "って事ですか") or
          check_text_terminate_string(line_msg, "ってことですか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 なんらかの内容についての叙述>"
    elif (check_text_terminate_string(line_msg, "という事では御座いませんか") or
          check_text_terminate_string(line_msg, "という事ではございませんか") or
          check_text_terminate_string(line_msg, "ということでは御座いませんか") or
          check_text_terminate_string(line_msg, "ということではございませんか") or
          check_text_terminate_string(line_msg, "という事ではありませんか") or
          check_text_terminate_string(line_msg, "ということではありませんか") or
          check_text_terminate_string(line_msg, "って事ではないのですか") or
          check_text_terminate_string(line_msg, "ってことではなのですか") or
          check_text_terminate_string(line_msg, "って事ではないんですか") or
          check_text_terminate_string(line_msg, "ってことではないんですか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 なんらかの内容についての叙述>"
    elif (check_text_terminate_string(line_msg, "は大丈夫です") or
          check_text_terminate_string(line_msg, "は大丈夫だ") or
          check_text_terminate_string(line_msg, "は大丈夫")):
            extrctd_intnt = "<宣言＆表明 肯定形 安否・健康状態について>"
    elif (check_text_terminate_string(line_msg, "は大丈夫ではない") or
          check_text_terminate_string(line_msg, "は大丈夫でない") or
          check_text_terminate_string(line_msg, "は大丈夫じゃない")):
            extrctd_intnt = "<宣言＆表明 否定形 安否・健康状態について>"
    elif (check_text_terminate_string(line_msg, "は大丈夫でしょうか") or
          check_text_terminate_string(line_msg, "は大丈夫ですか") or
          check_text_terminate_string(line_msg, "は大丈夫か")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 安否・健康状態について>"
    elif (check_text_terminate_string(line_msg, "は大丈夫ではないのでしょうか") or
          check_text_terminate_string(line_msg, "は大丈夫ではないんですか") or
          check_text_terminate_string(line_msg, "は大丈夫じゃないんですか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 安否・健康状態について>"
    elif (check_text_terminate_string(line_msg, "が必要です") or
          check_text_terminate_string(line_msg, "は必要です") or
          check_text_terminate_string(line_msg, "が必要だ") or
          check_text_terminate_string(line_msg, "は必要だ") or
          check_text_terminate_string(line_msg, "が必要") or
          check_text_terminate_string(line_msg, "は必要") or
          check_text_terminate_string(line_msg, "が要ります") or
          check_text_terminate_string(line_msg, "は要ります") or
          check_text_terminate_string(line_msg, "が要る") or
          check_text_terminate_string(line_msg, "は要る")):
            extrctd_intnt = "<宣言＆表明 肯定形 物事の要否について>"
    elif (check_text_terminate_string(line_msg, "が不要です") or
          check_text_terminate_string(line_msg, "は不要です") or
          check_text_terminate_string(line_msg, "が不要だ") or
          check_text_terminate_string(line_msg, "は不要だ") or
          check_text_terminate_string(line_msg, "が不要") or
          check_text_terminate_string(line_msg, "は不要") or
          check_text_terminate_string(line_msg, "が要りません") or
          check_text_terminate_string(line_msg, "は要りません") or
          check_text_terminate_string(line_msg, "が要らない") or
          check_text_terminate_string(line_msg, "は要らない")):
            extrctd_intnt = "<宣言＆表明 否定形 物事の要否について>"
    elif (check_text_terminate_string(line_msg, "が必要でしょうか") or
          check_text_terminate_string(line_msg, "は必要でしょうか") or
          check_text_terminate_string(line_msg, "が必要ですか") or
          check_text_terminate_string(line_msg, "は必要ですか") or
          check_text_terminate_string(line_msg, "が要りますでしょうか") or
          check_text_terminate_string(line_msg, "は要りますでしょうか") or
          check_text_terminate_string(line_msg, "が要りますか") or
          check_text_terminate_string(line_msg, "は要りますか")):
            extrctd_intnt = "<疑義＆質問＆確認 肯定形 物事の要否について>"
    elif (check_text_terminate_string(line_msg, "が不要でしょうか") or
          check_text_terminate_string(line_msg, "は不要でしょうか") or
          check_text_terminate_string(line_msg, "が不要ですか") or
          check_text_terminate_string(line_msg, "は不要ですか") or
          check_text_terminate_string(line_msg, "が要りませんか") or
          check_text_terminate_string(line_msg, "は要りませんか") or
          check_text_terminate_string(line_msg, "が要らないのですか") or
          check_text_terminate_string(line_msg, "は要らないのですか") or
          check_text_terminate_string(line_msg, "が要らないのか") or
          check_text_terminate_string(line_msg, "は要らないのか") or
          check_text_terminate_string(line_msg, "が要らないか") or
          check_text_terminate_string(line_msg, "は要らないか")):
            extrctd_intnt = "<疑義＆質問＆確認 否定形 物事の要否について>"
    elif (check_text_terminate_string(line_msg, "という事でしょう") or
          check_text_terminate_string(line_msg, "ということでしょう")):
            extrctd_intnt = "<推定＆推測＆推量 肯定形 進言・提言に近い>"
    elif (check_text_terminate_string(line_msg, "という事ではないでしょう") or
          check_text_terminate_string(line_msg, "ということではないでしょう")):
            extrctd_intnt = "<推定＆推測＆推量 否定形 進言・提言に近い>"
    elif (check_text_terminate_string(line_msg, "かも知れないです") or
          check_text_terminate_string(line_msg, "かもしれないです") or
          check_text_terminate_string(line_msg, "かも知れない") or
          check_text_terminate_string(line_msg, "かもしれない")):
            extrctd_intnt = "<推定＆推測＆推量 肯定形>"
    elif (check_text_terminate_string(line_msg, "ではないかも知れないです") or
          check_text_terminate_string(line_msg, "ではないかもしれないです") or
          check_text_terminate_string(line_msg, "ではないかも知れない") or
          check_text_terminate_string(line_msg, "ではないかもしれない")):
            extrctd_intnt = "<推定＆推測＆推量 否定形>"
    elif (check_text_terminate_string(line_msg, "かと存じ上げます" or
          check_text_terminate_string(line_msg, "と存じます" or
          check_text_terminate_string(line_msg, "かと思います" or
          check_text_terminate_string(line_msg, "と思います"):
            extrctd_intnt = "<既知＆認知 肯定形>"
    elif (check_text_terminate_string(line_msg, "とは存じ上げませんでした" or
          check_text_terminate_string(line_msg, "と存じまませんでした" or
          check_text_terminate_string(line_msg, "とは思いません" or
          check_text_terminate_string(line_msg, "と思いません"):
            extrctd_intnt = "<既知＆認知 否定形>"
    elif (check_text_terminate_string(line_msg, "とは思っています" or
          check_text_terminate_string(line_msg, "とは思ってます" or
          check_text_terminate_string(line_msg, "とは思っている" or
          check_text_terminate_string(line_msg, "とは思ってる" or
          check_text_terminate_string(line_msg, "とは思う" or
          check_text_terminate_string(line_msg, "と思っています" or
          check_text_terminate_string(line_msg, "と思ってます" or
          check_text_terminate_string(line_msg, "と思っている" or
          check_text_terminate_string(line_msg, "と思ってる" or
          check_text_terminate_string(line_msg, "と思う"):
            extrctd_intnt = "<思慮＆考慮 現在 肯定形>"
    elif (check_text_terminate_string(line_msg, "とは思っていません") or
          check_text_terminate_string(line_msg, "とは思ってません") or
          check_text_terminate_string(line_msg, "とは思っていない") or
          check_text_terminate_string(line_msg, "とは思ってない") or
          check_text_terminate_string(line_msg, "とは思わない") or
          check_text_terminate_string(line_msg, "と思っていません") or
          check_text_terminate_string(line_msg, "と思ってません") or
          check_text_terminate_string(line_msg, "と思っていない") or
          check_text_terminate_string(line_msg, "と思ってない") or
          check_text_terminate_string(line_msg, "と思わない")):
            extrctd_intnt = "<思慮＆考慮 現在 否定形>"
    elif (check_text_terminate_string(line_msg, "とは思っていました") or
          check_text_terminate_string(line_msg, "とは思ってました") or
          check_text_terminate_string(line_msg, "とは思っていた") or
          check_text_terminate_string(line_msg, "とは思ってた") or
          check_text_terminate_string(line_msg, "と思っていました") or
          check_text_terminate_string(line_msg, "と思ってました") or
          check_text_terminate_string(line_msg, "と思っていた") or
          check_text_terminate_string(line_msg, "と思ってた")):
            extrctd_intnt = "<思慮＆考慮 過去 肯定形>"
    elif (check_text_terminate_string(line_msg, "とは思っていませんでした") or
          check_text_terminate_string(line_msg, "とは思っていなかった") or
          check_text_terminate_string(line_msg, "とは思ってなかった") or
          check_text_terminate_string(line_msg, "と思っていませんでした") or
          check_text_terminate_string(line_msg, "と思っていなかった") or
          check_text_terminate_string(line_msg, "と思ってなかった")):
            extrctd_intnt = "<思慮＆考慮 過去 否定形>"
    elif (check_text_terminate_string(line_msg, "について考えて参ります" or
          check_text_terminate_string(line_msg, "について考えてまいります" or
          check_text_terminate_string(line_msg, "について考えて行きます" or
          check_text_terminate_string(line_msg, "について考えていきます" or
          check_text_terminate_string(line_msg, "について考えます" or
          check_text_terminate_string(line_msg, "を考えます" or
          check_text_terminate_string(line_msg, "が考えます" or
          check_text_terminate_string(line_msg, "は考えます")):
            extrctd_intnt = "<感想＆感慨 否定形 形容的な表現>"
    elif (check_text_terminate_string(line_msg, "と申します") or
          check_text_terminate_string(line_msg, "と言います")):
            extrctd_intnt = "<感想＆感慨 否定形 形容的な表現>"
    elif (check_text_terminate_string(line_msg, "らしいです") or
          check_text_terminate_string(line_msg, "らしい")):
            extrctd_intnt = "<感想＆感慨 肯定形 形容的な表現>"
    elif (check_text_terminate_string(line_msg, "らしくないです") or
          check_text_terminate_string(line_msg, "らしくない")):
            extrctd_intnt = "<感想＆感慨 否定形 形容的な表現>"
    elif (check_text_terminate_string(line_msg, "とは何でしょうか") or
          check_text_terminate_string(line_msg, "とはなんでしょうか") or
          check_text_terminate_string(line_msg, "とは何ですか") or
          check_text_terminate_string(line_msg, "とはなんですか") or
          check_text_terminate_string(line_msg, "とは何なのか") or
          check_text_terminate_string(line_msg, "とはなんなのか") or
          check_text_terminate_string(line_msg, "とは何か") or
          check_text_terminate_string(line_msg, "とはなにか") or
          check_text_terminate_string(line_msg, "とは何") or
          check_text_terminate_string(line_msg, "とはなに") or
          check_text_terminate_string(line_msg, "とは") or
          check_text_terminate_string(line_msg, "って何") or
          check_text_terminate_string(line_msg, "ってなに") or
          check_text_terminate_string(line_msg, "って")):
            extrctd_intnt = "<単純質問>"
    elif (check_text_terminate_string(line_msg, "でございます") or
          check_text_terminate_string(line_msg, "にございます") or
          check_text_terminate_string(line_msg, "となります") or
          check_text_terminate_string(line_msg, "になります")):
            extrctd_intnt = "<紹介＆提示＆説明 単純>"
    elif (check_text_terminate_string(line_msg, "にありまして") or
          check_text_terminate_string(line_msg, "におりまして") or
          check_text_terminate_string(line_msg, "がありまして") or
          check_text_terminate_string(line_msg, "がおりまして")):
            extrctd_intnt = "<申立て>"
    elif (check_text_terminate_string(line_msg, "ですので") or
          check_text_terminate_string(line_msg, "なので") or
          check_text_terminate_string(line_msg, "ので")):
            extrctd_intnt = "<説得＆説明>"
    elif (check_text_terminate_string(line_msg, "なものでして") or
          check_text_terminate_string(line_msg, "なもので") or
          check_text_terminate_string(line_msg, "でして")):
            extrctd_intnt = "<説得＆説明 言い訳に近い>"
    else:
            extrctd_intnt = "<その他・不明>"
    return extrctd_intnt


#ユーザーから送られるLINEメッセージの中からコンテント(＝発話の意図されるもの)を抽出する
def extract_content(line_msg):
    rmvd_etc_msg     = remove_etc(line_msg)
    rmvd_symbl_msg   = remove_symbol(rmvd_etc_msg)
    rmvd_edprtcl_msg = remove_endparticle(rmvd_symbl_msg)
    extrctd_cntnt    = remove_intent(rmvd_edprtcl_msg)
    return extrctd_cntnt


#ユーザーから送られるLINEメッセージの中からトピック(＝新旧６件分のメッセージに共通して出現する名詞)を抽出する
def extract_topic(line_msg, line_msg2, line_msg3, line_msg4, line_msg5, line_msg6):
    #メッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr = Tokenizer()
    tkns  = tknzr.tokenize(line_msg + line_msg2 + line_msg3 + line_msg4 + line_msg5 + line_msg6)

    #分解後のメッセージをリストに格納して、これを呼出し元に引渡しをする
    anlyzd_msg = []
    for tkn in tkns:
        anlyzd_msg.append([tkn.surface, tkn.part_of_speech])

    #新旧６件分のメッセージの中から共通して出現する名詞を抜き出して、これを呼出し元に引渡しをする
    wrddc = {}
    idx   = 0
    while len(anlyzd_msg) > idx:
          if anlyzd_msg[idx][1] == "名詞":
          wrddc[anlyzd_msg[idx][0]] += 1
          idx += 1
    tpc = max(wrddc, key=wrddc.get)
    return tpc


#ユーザーから送られるLINEメッセージの中から文型(＝文全体を構成する品詞の連なり)を抽出する
def conversion_message_to_sentencepattern(line_msg):
    anlyzd_msg         = line_msg_morpho_analyze2(line_msg)
    extrctd_sntncpttrn = []
    idx                = 0
    while len(anlyzd_msg) > idx:
          extrctd_sntncpttrn.append("[" + anlyzd_msg[idx][1] + " " + anlyzd_msg[idx][0] + "]")
          idx += 1
    return extrctd_sntncpttrn