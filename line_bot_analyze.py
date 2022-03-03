# coding: utf-8




import re
from janome.tokenizer import Tokenizer




#ユーザーから送られるLINEメッセージの中に含まれる記号を除去する
def remove_symbol(line_msg_txt):
    #メッセージの中に含まれる日本語固有の記号を除去する
    rmv_symbl_rslt   = re.sub("(’)",  "",line_msg_txt)
    rmv_symbl_rslt2  = re.sub("(”)",  "",rmv_symbl_rslt)
    rmv_symbl_rslt3  = re.sub("(（)", "", rmv_symbl_rslt2)
    rmv_symbl_rslt4  = re.sub("(）)", "", rmv_symbl_rslt3)
    rmv_symbl_rslt5  = re.sub("(「)", "", rmv_symbl_rslt4)
    rmv_symbl_rslt6  = re.sub("(」)", "", rmv_symbl_rslt5)
    rmv_symbl_rslt7  = re.sub("(、)", "", rmv_symbl_rslt6)
    rmv_symbl_rslt8  = re.sub("(。)", "", rmv_symbl_rslt7)
    rmv_symbl_rslt9  = re.sub("(！)", "", rmv_symbl_rslt8)
    rmv_symbl_rslt10 = re.sub("(？)", "", rmv_symbl_rslt9)
    rmv_symbl_rslt11 = re.sub("(ー)", "", rmv_symbl_rslt10)
    rmv_symbl_rslt12 = re.sub("(～)", "", rmv_symbl_rslt11)
    rmv_symbl_rslt13 = re.sub("(・)", "", rmv_symbl_rslt12)
    rmv_symbl_rslt14 = re.sub("(＝)", "", rmv_symbl_rslt13)
    rmv_symbl_rslt15 = re.sub("(＆)", "", rmv_symbl_rslt14)
    rmv_symbl_rslt16 = re.sub("(＋)", "", rmv_symbl_rslt15)

    #メッセージの中に含まれる先頭と末尾の空白と改行を除去する
    rmv_symbl_rslt_end = rmv_symbl_rslt16.strip()
    return rmv_symbl_rslt_end


#ユーザーから送られるLINEメッセージの中に含まれる終助詞を除去する
def remove_endparticle(rmv_symbl_rslt):
    #メッセージの中に含まれる日本語固有の助詞・終助詞を除去する
    rmv_edprtcl_rslt   = re.sub("(なあ)", "", rmv_symbl_rslt)
    rmv_edprtcl_rslt2  = re.sub("(なぁ)", "", rmv_edprtcl_rslt)
    rmv_edprtcl_rslt3  = re.sub("(なっ)", "", rmv_edprtcl_rslt2)
    rmv_edprtcl_rslt4  = re.sub("(ねえ)", "", rmv_edprtcl_rslt3)
    rmv_edprtcl_rslt5  = re.sub("(ねぇ)", "", rmv_edprtcl_rslt4)
    rmv_edprtcl_rslt6  = re.sub("(わ)",   "", rmv_edprtcl_rslt5)
    rmv_edprtcl_rslt7  = re.sub("(わあ)", "", rmv_edprtcl_rslt6)
    rmv_edprtcl_rslt8  = re.sub("(わぁ)", "", rmv_edprtcl_rslt7)
    rmv_edprtcl_rslt9  = re.sub("(ぜ)",   "", rmv_edprtcl_rslt8)
    rmv_edprtcl_rslt10 = re.sub("(ぜっ)", "", rmv_edprtcl_rslt9)
    rmv_edprtcl_rslt11 = re.sub("(よ)",   "", rmv_edprtcl_rslt10)
    rmv_edprtcl_rslt12 = re.sub("(よお)", "", rmv_edprtcl_rslt11)
    rmv_edprtcl_rslt13 = re.sub("(よぉ)", "", rmv_edprtcl_rslt12)
    rmv_edprtcl_rslt14 = re.sub("(よっ)", "", rmv_edprtcl_rslt13)
    rmv_edprtcl_rslt15 = re.sub("(っす)", "", rmv_edprtcl_rslt14)
    rmv_edprtcl_rslt16 = re.sub("(だね)", "", rmv_edprtcl_rslt15)
    rmv_edprtcl_rslt17 = re.sub("(だわ)", "", rmv_edprtcl_rslt16)
    rmv_edprtcl_rslt18 = re.sub("(ってもの)", "", rmv_edprtcl_rslt17)
    rmv_edprtcl_rslt19 = re.sub("(ってこと)", "", rmv_edprtcl_rslt18)
    rmv_edprtcl_rslt20 = re.sub("(ってばよ)", "", rmv_edprtcl_rslt19)

    #メッセージの中に含まれる日本語固有の感情表現を伴う記号類を除去する
    rmv_edprtcl_rslt21 = re.sub("( 笑)",   "",  rmv_edprtcl_rslt20)
    rmv_edprtcl_rslt22 = re.sub("( わら)", "",  rmv_edprtcl_rslt21)
    rmv_edprtcl_rslt23 = re.sub("( ワラ)", "",  rmv_edprtcl_rslt22)
    rmv_edprtcl_rslt24 = re.sub("( 草)", "",    rmv_edprtcl_rslt23)
    rmv_edprtcl_rslt25 = re.sub("( w)",  "",    rmv_edprtcl_rslt24)
    rmv_edprtcl_rslt26 = re.sub("( W)",  "",    rmv_edprtcl_rslt25)
    rmv_edprtcl_rslt27 = re.sub("(　笑)",   "", rmv_edprtcl_rslt26)
    rmv_edprtcl_rslt28 = re.sub("(　わら)", "", rmv_edprtcl_rslt27)
    rmv_edprtcl_rslt29 = re.sub("(　ワラ)", "", rmv_edprtcl_rslt28)
    rmv_edprtcl_rslt30 = re.sub("(　草)",   "", rmv_edprtcl_rslt29)
    rmv_edprtcl_rslt31 = re.sub("(　w)",    "", rmv_edprtcl_rslt30)
    rmv_edprtcl_rslt32 = re.sub("(　W)",    "", rmv_edprtcl_rslt31)
    
    #メッセージの中に含まれる先頭と末尾の空白と改行を除去する
    rmv_edprtcl_rslt_end = rmv_edprtcl_rslt32.strip()
    return rmv_edprtcl_rslt_end 


#ユーザーから送られるLINEメッセージが指定された文字列で開始するかを判定する
def check_text_start_string(line_msg_txt, str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で開始するかを判定する
    rmv_symbl_rslt        = remove_symbol(line_msg_txt)
    chk_txt_strt_str_rslt = rmv_symbl_rslt.startswith(str)
    return chk_txt_strt_str_rslt


#ユーザーから送られるLINEメッセージが指定された文字列で終結するかを判定する
def check_text_terminated_string(line_msg_txt, str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で終結するかを判定する
    rmv_symbl_rslt          = remove_symbol(line_msg_txt)
    chk_txt_trmntd_str_rslt = rmv_symbl_rslt.endswith(str)
    return chk_txt_trmntd_str_rslt


#ユーザーから送られるLINEメッセージの中に含まれるインテントを除去する
def remove_intent(rmv_edprtcl_rslt):
    #メッセージの中に含まれる日本語固有のインテントを除去する
    rmv_cnddt_intnt = []
    if check_text_terminated_string(rmv_edprtcl_rslt, "します"):
         rmv_cnddt_intnt.append("します")
    if check_text_terminated_string(rmv_edprtcl_rslt, "する"):
         rmv_cnddt_intnt.append("する")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しません"):
         rmv_cnddt_intnt.append("しません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しない"):
         rmv_cnddt_intnt.append("しない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しています"):
         rmv_cnddt_intnt.append("しています")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してます"):
         rmv_cnddt_intnt.append("してます")
    if check_text_terminated_string(rmv_edprtcl_rslt, "している"):
         rmv_cnddt_intnt.append("している")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してる"):
         rmv_cnddt_intnt.append("してる")
    if check_text_terminated_string(rmv_edprtcl_rslt, "していません"):
         rmv_cnddt_intnt.append("していません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してません"):
         rmv_cnddt_intnt.append("してません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "していない"):
         rmv_cnddt_intnt.append("していない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してない"):
         rmv_cnddt_intnt.append("してない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できている"):
         rmv_cnddt_intnt.append("できている")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できてる"):
         rmv_cnddt_intnt.append("できてる")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できていない"):
         rmv_cnddt_intnt.append("できていない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できてない"):
         rmv_cnddt_intnt.append("できてない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できていません"):
         rmv_cnddt_intnt.append("できていません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できてません"):
         rmv_cnddt_intnt.append("できてません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できました"):
         rmv_cnddt_intnt.append("できました")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できた"):
         rmv_cnddt_intnt.append("できた")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できていません"):
         rmv_cnddt_intnt.append("できていません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できてません"):
         rmv_cnddt_intnt.append("できてません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できてない"):
         rmv_cnddt_intnt.append("できてない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できます"):
         rmv_cnddt_intnt.append("できます")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できる"):
         rmv_cnddt_intnt.append("できる")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できません"):
         rmv_cnddt_intnt.append("できません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "できない"):
         rmv_cnddt_intnt.append("できない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しない"):
         rmv_cnddt_intnt.append("しない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しました"):
         rmv_cnddt_intnt.append("しました")
    if check_text_terminated_string(rmv_edprtcl_rslt, "した")
         rmv_cnddt_intnt.append("した")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をやりました"):
         rmv_cnddt_intnt.append("をやりました")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をやった"):
         rmv_cnddt_intnt.append("をやった")
    if check_text_terminated_string(rmv_edprtcl_rslt, "していません"):
         rmv_cnddt_intnt.append("していません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してません"):
         rmv_cnddt_intnt.append("してません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してない"):
         rmv_cnddt_intnt.append("してない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がされています"):
         rmv_cnddt_intnt.append("がされています")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はされています"):
         rmv_cnddt_intnt.append("はされています")
    if check_text_terminated_string(rmv_edprtcl_rslt, "されています"):
         rmv_cnddt_intnt.append("されています")
    if check_text_terminated_string(rmv_edprtcl_rslt, "されてます"):
         rmv_cnddt_intnt.append("されてます")
    if check_text_terminated_string(rmv_edprtcl_rslt, "されてます"):
         rmv_cnddt_intnt.append("されてます")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がされていません"):
         rmv_cnddt_intnt.append("がされていません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はされていません"):
         rmv_cnddt_intnt.append("はされていません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "されていません"):
         rmv_cnddt_intnt.append("されていません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "されてません"):
         rmv_cnddt_intnt.append("されてません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "されていない"):
         rmv_cnddt_intnt.append("されていない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "されてない"):
         rmv_cnddt_intnt.append("されてない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がされました"):
         rmv_cnddt_intnt.append("がされました")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はされました"):
         rmv_cnddt_intnt.append("はされました")
    if check_text_terminated_string(rmv_edprtcl_rslt, "されました"):
         rmv_cnddt_intnt.append("されました")
    if check_text_terminated_string(rmv_edprtcl_rslt, "された"):
         rmv_cnddt_intnt.append("された")
    if check_text_terminated_string(rmv_edprtcl_rslt, "でした"):
         rmv_cnddt_intnt.append("でした")
    if check_text_terminated_string(rmv_edprtcl_rslt, "だったです"):
         rmv_cnddt_intnt.append("だったです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "だった"):
         rmv_cnddt_intnt.append("だった")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったです"):
         rmv_cnddt_intnt.append("ではなかったです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ではなかった"):
         rmv_cnddt_intnt.append("ではなかった")
    if check_text_terminated_string(rmv_edprtcl_rslt, "でなかった"):
         rmv_cnddt_intnt.append("でなかった")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしていきたい"):
         rmv_cnddt_intnt.append("をしていきたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしてたい"):
         rmv_cnddt_intnt.append("をしてたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたい"):
         rmv_cnddt_intnt.append("をやっていきたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をやってたい"):
         rmv_cnddt_intnt.append("をやってたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしていきたい"):
         rmv_cnddt_intnt.append("はしていきたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしてたい"):
         rmv_cnddt_intnt.append("はしてたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はやっていきたい"):
         rmv_cnddt_intnt.append("はやっていきたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はやってたい"):
         rmv_cnddt_intnt.append("はやってたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "していきたい"):
         rmv_cnddt_intnt.append("していきたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してたい"):
         rmv_cnddt_intnt.append("してたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "いたい"):
         rmv_cnddt_intnt.append("いたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしていきたくない"):
         rmv_cnddt_intnt.append("はしていきたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "していきたくない"):
         rmv_cnddt_intnt.append("していきたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしてたくない"):
         rmv_cnddt_intnt.append("はしてたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してたくない"):
         rmv_cnddt_intnt.append("してたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしていきたくない"):
         rmv_cnddt_intnt.append("をしていきたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしてたくない"):
         rmv_cnddt_intnt.append("をしてたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してたくない"):
         rmv_cnddt_intnt.append("してたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたくない"):
         rmv_cnddt_intnt.append("をやっていきたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をやってたくない"):
         rmv_cnddt_intnt.append("をやってたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はやっていきたくない"):
         rmv_cnddt_intnt.append("はやっていきたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はやってたくない"):
         rmv_cnddt_intnt.append("はやってたくない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をやっていかない"):
         rmv_cnddt_intnt.append("をやっていかない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はやっていかない"):
         rmv_cnddt_intnt.append("はやっていかない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をやってかない"):
         rmv_cnddt_intnt.append("をやってかない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はやってかない"):
         rmv_cnddt_intnt.append("はやってかない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったです"):
         rmv_cnddt_intnt.append("ではなかったです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ではなかった"):
         rmv_cnddt_intnt.append("ではなかった")
    if check_text_terminated_string(rmv_edprtcl_rslt, "でなかった"):
         rmv_cnddt_intnt.append("でなかった")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ですから"):
         rmv_cnddt_intnt.append("ですから")
    if check_text_terminated_string(rmv_edprtcl_rslt, "です"):
         rmv_cnddt_intnt.append("です")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ます"):
         rmv_cnddt_intnt.append("ます")
    if check_text_terminated_string(rmv_edprtcl_rslt, "っていました"):
         rmv_cnddt_intnt.append("っていました")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ってました"):
         rmv_cnddt_intnt.append("ってました")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ってた"):
         rmv_cnddt_intnt.append("ってた")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ということでしょうか"):
         rmv_cnddt_intnt.append("ということでしょうか")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ということですか"):
         rmv_cnddt_intnt.append("ということですか")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ということですよね"):
         rmv_cnddt_intnt.append("ということですよね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ということですね"):
         rmv_cnddt_intnt.append("ということですね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ということだね"):
         rmv_cnddt_intnt.append("ということだね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ってことでしょうか"):
         rmv_cnddt_intnt.append("ってことでしょうか")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ってことですか"):
         rmv_cnddt_intnt.append("ってことですか")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ってことですよね"):
         rmv_cnddt_intnt.append("ってことですよね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ってことですね"):
         rmv_cnddt_intnt.append("ってことですね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ってことだね"):
         rmv_cnddt_intnt.append("ってことだね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "でしょうか"):
         rmv_cnddt_intnt.append("でしょうか")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ですか"):
         rmv_cnddt_intnt.append("ですか")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ですよね"):
         rmv_cnddt_intnt.append("ですよね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "ですね"):
         rmv_cnddt_intnt.append("ですね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "だね"):
         rmv_cnddt_intnt.append("だね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しませんか"):
         rmv_cnddt_intnt.append("しませんか")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しません"):
         rmv_cnddt_intnt.append("しません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "したい"):
         rmv_cnddt_intnt.append("したい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "たい"):
         rmv_cnddt_intnt.append("たい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "やりたい"):
         rmv_cnddt_intnt.append("やりたい")
    if check_text_terminated_string(rmv_edprtcl_rslt, "いです"):
         rmv_cnddt_intnt.append("いです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしなければならない"):
         rmv_cnddt_intnt.append("はしなければならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしなければ"):
         rmv_cnddt_intnt.append("はしなければ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしないといけないです"):
         rmv_cnddt_intnt.append("はしないといけないです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしないといけない"):
         rmv_cnddt_intnt.append("はしないといけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃいけないです"):
         rmv_cnddt_intnt.append("はしなきゃいけないです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃいけない"):
         rmv_cnddt_intnt.append("はしなきゃいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃならない"):
         rmv_cnddt_intnt.append("はしなきゃならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃ"):
         rmv_cnddt_intnt.append("はしなきゃ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はせにゃならん"):
         rmv_cnddt_intnt.append("はせにゃならん")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしなければならない"):
         rmv_cnddt_intnt.append("をしなければならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしなければ"):
         rmv_cnddt_intnt.append("をしなければ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしないといけないです"):
         rmv_cnddt_intnt.append("をしないといけないです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしないといけない"):
         rmv_cnddt_intnt.append("をしないといけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃいけないです"):
         rmv_cnddt_intnt.append("をしなきゃいけないです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃいけない"):
         rmv_cnddt_intnt.append("をしなきゃいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃならない"):
         rmv_cnddt_intnt.append("をしなきゃならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃ"):
         rmv_cnddt_intnt.append("をしなきゃ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をせにゃならん"):
         rmv_cnddt_intnt.append("をせにゃならん")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しなければならない"):
         rmv_cnddt_intnt.append("しなければならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しなければ"):
         rmv_cnddt_intnt.append("しなければ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しないといけないです"):
         rmv_cnddt_intnt.append("しないといけないです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しないといけない"):
         rmv_cnddt_intnt.append("しないといけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃいけないです"):
         rmv_cnddt_intnt.append("しなきゃいけないです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃいけない"):
         rmv_cnddt_intnt.append("しなきゃいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃならない"):
         rmv_cnddt_intnt.append("しなきゃならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃ"):
         rmv_cnddt_intnt.append("しなきゃ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "せにゃならん"):
         rmv_cnddt_intnt.append("せにゃならん")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしなければならない"):
         rmv_cnddt_intnt.append("がしなければならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしなければ"):
         rmv_cnddt_intnt.append("がしなければ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしないといけないです"):
         rmv_cnddt_intnt.append("がしないといけないです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしないといけない"):
         rmv_cnddt_intnt.append("がしないといけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけないです"):
        rmv_cnddt_intnt.append("がしなきゃいけないです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけない"):
        rmv_cnddt_intnt.append("がしなきゃいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃならない"):
        rmv_cnddt_intnt.append("がしなきゃならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃ"):
        rmv_cnddt_intnt.append("がしなきゃ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がせにゃならん"):
        rmv_cnddt_intnt.append("がせにゃならん")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしてはならない"):
        rmv_cnddt_intnt.append("はしてはならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしてはいけない"):
        rmv_cnddt_intnt.append("はしてはいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしたらいけない"):
        rmv_cnddt_intnt.append("はしたらいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃいけない"):
        rmv_cnddt_intnt.append("はしちゃいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃならん"):
        rmv_cnddt_intnt.append("はしちゃならん")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしてはならない"):
        rmv_cnddt_intnt.append("をしてはならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしてはいけない"):
        rmv_cnddt_intnt.append("をしてはいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしたらいけない"):
        rmv_cnddt_intnt.append("をしたらいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃいけない"):
        rmv_cnddt_intnt.append("をしちゃいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃならん"):
        rmv_cnddt_intnt.append("をしちゃならん")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してはならない"):
        rmv_cnddt_intnt.append("してはならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "してはいけない"):
        rmv_cnddt_intnt.append("してはいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "したらいけない"):
        rmv_cnddt_intnt.append("したらいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しちゃいけない"):
        rmv_cnddt_intnt.append("しちゃいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "しちゃならん"):
        rmv_cnddt_intnt.append("しちゃならん")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしてはならない"):
        rmv_cnddt_intnt.append("がしてはならない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしてはいけない"):
        rmv_cnddt_intnt.append("がしてはいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしたらいけない"):
        rmv_cnddt_intnt.append("がしたらいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃいけない"):
         rmv_cnddt_intnt.append("がしちゃいけない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃならん"):
         rmv_cnddt_intnt.append("がしちゃならん")
    if check_text_terminated_string(rmv_edprtcl_rslt, "だ"):
         rmv_cnddt_intnt.append("だ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "でしょう"):
         rmv_cnddt_intnt.append("でしょう")
    if check_text_terminated_string(rmv_edprtcl_rslt, "だろう"):
         rmv_cnddt_intnt.append("だろう")
    if check_text_terminated_string(rmv_edprtcl_rslt, "だろ"):
         rmv_cnddt_intnt.append("だろ")
    if check_text_terminated_string(rmv_edprtcl_rslt, "だそうです"):
         rmv_cnddt_intnt.append("だそうです")
    if check_text_terminated_string(rmv_edprtcl_rslt, "だろう"):
         rmv_cnddt_intnt.append("だろう")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はいます"):
         rmv_cnddt_intnt.append("はいます")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はいる"):
         rmv_cnddt_intnt.append("はいる")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がいます"):
         rmv_cnddt_intnt.append("がいます")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がいる"):
         rmv_cnddt_intnt.append("がいる")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はいません"):
         rmv_cnddt_intnt.append("はいません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はいない"):
         rmv_cnddt_intnt.append("はいない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がいません"):
         rmv_cnddt_intnt.append("がいません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がいない"):
         rmv_cnddt_intnt.append("がいない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "にいます"):
         rmv_cnddt_intnt.append("にいます")
    if check_text_terminated_string(rmv_edprtcl_rslt, "にいる"):
         rmv_cnddt_intnt.append("にいる")
    if check_text_terminated_string(rmv_edprtcl_rslt, "にいません"):
         rmv_cnddt_intnt.append("にいません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "にいない"):
         rmv_cnddt_intnt.append("にいない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はあります"):
         rmv_cnddt_intnt.append("はあります")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はある"):
         rmv_cnddt_intnt.append("はある")
    if check_text_terminated_string(rmv_edprtcl_rslt, "があります"):
         rmv_cnddt_intnt.append("があります")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がある"):
         rmv_cnddt_intnt.append("がある")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はありません"):
         rmv_cnddt_intnt.append("はありません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はない"):
         rmv_cnddt_intnt.append("はない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がありません"):
         rmv_cnddt_intnt.append("がありません")
    if check_text_terminated_string(rmv_edprtcl_rslt, "がない"):
         rmv_cnddt_intnt.append("がない")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はですね"):
         rmv_cnddt_intnt.append("はですね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "をですね"):
         rmv_cnddt_intnt.append("をですね")
    if check_text_terminated_string(rmv_edprtcl_rslt, "はだね"):
         rmv_cnddt_intnt.append("はだね")
    if  check_text_terminated_string(rmv_edprtcl_rslt, "をだね"):
         rmv_cnddt_intnt.append("をだね")

    #前段で取得した削除候補の中から実際に削除するインテントを決定して、これを呼出し元に引渡しをする
    rmv_cnddt_intnt_list = []
    for intnt in rmv_cnddt_intnt
        rmv_cnddt_intnt_list.append([len(intnt), intnt])
    idx       = 0
    tmp_intnt = ""
    for i in rmv_cnddt_intnt_list
        if len(rmv_cnddt_intnt_list) > (i+1):
           if rmv_cnddt_intnt_list[i+1][0] > rmv_cnddt_intnt_list[idx][0]:
              tmp_intnt = rmv_cnddt_intnt_list[i+1][1]
              idx = i + 1
           else:
              continue

    rmv_intnt_rslt = tmp_intnt
    return rmv_intnt_rslt


#ユーザーから送られるLINEメッセージをJanomeで形態素解析する(見出しのみをリストにして出力する)
def line_msg_morpho_analyze(line_msg_txt):
    #メッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr   = Tokenizer()
    tkns    = tknzr.tokenize(line_msg_txt)

    #分解後のメッセージをリストに格納、これを呼出し元に引渡しをする
    anlyz_rslt = []
    for tkn in tkns:
        anlyz_rslt.append(tkn.surface)
    return anlyz_rslt


#ユーザーから送られるLINEメッセージをJanomeで形態素解析する(見出しと品詞のセットをリストにして出力する)
def line_msg_morpho_analyze2(line_msg_txt):
    #メッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr = Tokenizer()
    tkns  = tknzr.tokenize(line_msg_txt)

    #分解後のメッセージをリストに格納、これを呼出し元に引渡しをする
    anlyz2_rslt = []
    for tkn in tkns:
        anlyz2_rslt.append([tkn.surface, tkn.part_of_speech])
    return [anlyz2_rslt]


#LINEメッセージがギャグ＆声帯模写＆その他だったとして、これからインテント(＝意図するもの)を抽出する
def extract_intent_from_gag_vocal_cord_copy_and_etc(line_msg_txt):
    #ギャグ＆声帯模写＆その他となっているメッセージからインテントを抽出して、これを呼出し元に引渡しをする
    if   (line_msg_txt == "はい ひょっこりはん" or
          line_msg_txt == "はいひょっこりはん" or
          line_msg_txt == "プレゼント フォー 肩幅" or
          line_msg_txt == "プレゼントフォー肩幅" or
          line_msg_txt == "うぃーん合唱団" or
          line_msg_txt == "早く大人になれ 膝小僧" or
          line_msg_txt == "早く大人になれ膝小僧" or
          line_msg_txt == "プレゼントフォー肩幅" or
          line_msg_txt == "おったまげ" or
          line_msg_txt == "おったまげー" or
          line_msg_txt == "おったまげ～" or
          line_msg_txt == "しもしも" or
          line_msg_txt == "しもしも？" or
          line_msg_txt == "マンモスうれぴー" or
          line_msg_txt == "マンモスうれぴ～" or
          line_msg_txt == "湯飲みじゃなくて ホタルを守る" or
          line_msg_txt == "湯飲みじゃなくてホタルを守る" or
          line_msg_txt == "ウーパールーパー" or
          line_msg_txt == "スフィンクス" or
          line_msg_txt == "しゃか" or
          line_msg_txt == "ホップステップ キャンプ" or
          line_msg_txt == "ホップステップキャンプ" or
          line_msg_txt == "落ち着いていきや" or
          line_msg_txt == "落ち着いていきやー" or
          line_msg_txt == "落ち着いていきや～" or
          line_msg_txt == "PPAP" or
          line_msg_txt == "PPAP!" or
          line_msg_txt == "PPAP！" or
          line_msg_txt == "パーフェクト ヒューマン" or
          line_msg_txt == "パーフェクトヒューマン" or
          line_msg_txt == "ボク ミッキーだよ" or
          line_msg_txt == "ボクミッキーだよ" or
          line_msg_txt == "あのね 芦田愛菜だよ" or
          line_msg_txt == "あのね芦田愛菜だよ" or
          line_msg_txt == "ピカピカ" or
          line_msg_txt == "ピカチュウ" or
          line_msg_txt == "ブンブン ハローYouTube" or
          line_msg_txt == "ブンブンハローYouTube" or
          line_msg_txt == "ブンブン ハロー" or
          line_msg_txt == "ブンブンハロー" or
          line_msg_txt == "ぶんぶん はろー" or
          line_msg_txt == "ぶんぶんはろー" or
          line_msg_txt == "ダンカン コノヤロ！" or
          line_msg_txt == "ダンカンコノヤロ！" or
          line_msg_txt == "大阪名物 パチパチパンチ" or
          line_msg_txt == "大阪名物パチパチパンチ" or
          line_msg_txt == "パチパチパンチ" or
          line_msg_txt == "大阪名物 パチパチパンチ！" or
          line_msg_txt == "大阪名物パチパチパンチ！" or
          line_msg_txt == "パチパチパンチ！" or
          line_msg_txt == "かいーの" or
          line_msg_txt == "かい～の" or
          line_msg_txt == "かいーのー" or
          line_msg_txt == "かい～の～" or
          line_msg_txt == "バカちゃいまんねん アホでんねん" or
          line_msg_txt == "バカちゃいまんねんアホでんねん" or
          line_msg_txt == "アホでんねん" or
          line_msg_txt == "おっぱっぴー" or
          line_msg_txt == "オッパッピー" or
          line_msg_txt == "おっぱっぴ～" or
          line_msg_txt == "オッパッピ～" or
          line_msg_txt == "ぴぃやー" or
          line_msg_txt == "ピィヤー" or
          line_msg_txt == "ぴぃや～" or
          line_msg_txt == "ピィヤ～" or
          line_msg_txt == "俺の武勇伝" or
          line_msg_txt == "おれの武勇伝" or
          line_msg_txt == "オレの武勇伝" or
          line_msg_txt == "武勇伝" or
          line_msg_txt == "俺の武勇伝！" or
          line_msg_txt == "おれの武勇伝！" or
          line_msg_txt == "オレの武勇伝！" or
          line_msg_txt == "武勇伝！" or
          line_msg_txt == "俺の武勇伝を聞きたいか" or
          line_msg_txt == "おれの武勇伝を聞きたいか" or
          line_msg_txt == "オレの武勇伝を聞きたいか" or
          line_msg_txt == "俺の武勇伝を聞きたいか？" or
          line_msg_txt == "おれの武勇伝を聞きたいか？" or
          line_msg_txt == "オレの武勇伝を聞きたいか？" or
          line_msg_txt == "武勇伝武勇伝" or
          line_msg_txt == "武勇伝 武勇伝" or
          line_msg_txt == "武勇伝！武勇伝！" or
          line_msg_txt == "武勇伝！ 武勇伝！" or
          line_msg_txt == "空前絶後" or
          line_msg_txt == "空 前 絶 後" or
          line_msg_txt == "空！前！絶！後！" or
          line_msg_txt == "空！ 前！ 絶！ 後！" or
          line_msg_txt == "空前絶後！"):
            extrct_intnt_frm_gag_vocl_crd_cpy_and_etc_rslt = "(モノマネ＝ギャグ＆一発芸)"
    elif (line_msg_txt == "にゃー にゃー" or
          line_msg_txt == "ニャー ニャー" or
          line_msg_txt == "にゃーにゃー" or
          line_msg_txt == "ニャーニャー" or
          line_msg_txt == "にゃ" or
          line_msg_txt == "ニャ" or
          line_msg_txt == "にゃー" or
          line_msg_txt == "ニャー" or
          line_msg_txt == "にゃ～" or
          line_msg_txt == "ニャ～" or
          line_msg_txt == "わんわん" or
          line_msg_txt == "ワンワン" or
          line_msg_txt == "わん" or
          line_msg_txt == "ワン" or
          line_msg_txt == "しゃー" or
          line_msg_txt == "シャー" or
          line_msg_txt == "ぎゃん ぎゃん" or
          line_msg_txt == "ぎゃんぎゃん" or
          line_msg_txt == "ぎゃん" or
          line_msg_txt == "ギャン ギャン" or
          line_msg_txt == "ギャンギャン" or
          line_msg_txt == "ギャン" or
          line_msg_txt == "うほ うほ" or         
          line_msg_txt == "うほうほ" or
          line_msg_txt == "うほ" or
          line_msg_txt == "ウホ ウホ" or
          line_msg_txt == "ウホウホ" or
          line_msg_txt == "ウホ" or
          line_msg_txt == "こけこっこ" or
          line_msg_txt == "コケコッコー" or
          line_msg_txt == "こけ" or
          line_msg_txt == "コケ" or
          line_msg_txt == "にゃん にゃん" or
          line_msg_txt == "にゃんにゃん" or
          line_msg_txt == "ニャン ニャン" or
          line_msg_txt == "ニャンニャン" or
          line_msg_txt == "にゃん" or
          line_msg_txt == "ニャン" or
          line_msg_txt == "ぶひ ぶひ" or
          line_msg_txt == "ぶひぶひ" or
          line_msg_txt == "ブヒ ブヒ" or
          line_msg_txt == "ブヒブヒ" or
          line_msg_txt == "ぶひ" or
          line_msg_txt == "ブヒ" or
          line_msg_txt == "ちゅん ちゅん" or
          line_msg_txt == "ちゅんちゅん" or
          line_msg_txt == "ちゅん" or
          line_msg_txt == "チュン チュン" or
          line_msg_txt == "チュンチュン" or
          line_msg_txt == "チュン" or
          line_msg_txt == "げろ げろ" or
          line_msg_txt == "げろげろ" or
          line_msg_txt == "げろ" or
          line_msg_txt == "ゲロ ゲロ" or
          line_msg_txt == "ゲロゲロ" or
          line_msg_txt == "ゲロ" or
          line_msg_txt == "げこ げこ" or
          line_msg_txt == "げこげこ" or
          line_msg_txt == "げこ" or
          line_msg_txt == "ゲコ ゲコ" or
          line_msg_txt == "ゲコゲコ" or
          line_msg_txt == "ゲコ" or
          line_msg_txt == "ぶ ぶ" or
          line_msg_txt == "ぶぶ" or
          line_msg_txt == "ブ ブ" or
          line_msg_txt == "ブブ" or
          line_msg_txt == "がったん ごっとん" or
          line_msg_txt == "がったんごっとん" or
          line_msg_txt == "ガッタン ゴットン" or
          line_msg_txt == "ガッタンゴットン"):
            extrct_intnt_frm_gag_vocl_crd_cpy_and_etc_rslt = "(モノマネ＝声帯模写)"
    elif (line_msg_txt == "ぷー" or
          line_msg_txt == "プー" or
          line_msg_txt == "ぷ～" or
          line_msg_txt == "プ～" or
          line_msg_txt == "ごほ ごほ" or
          line_msg_txt == "ごほごほ" or
          line_msg_txt == "ゴホ ゴホ" or
          line_msg_txt == "ゴホゴホ" or
          line_msg_txt == "ごほ" or
          line_msg_txt == "ゴホ" or
          line_msg_txt == "ごほっ ごほっ" or
          line_msg_txt == "ごほっごほっ" or
          line_msg_txt == "ゴホッ ゴホッ" or
          line_msg_txt == "ゴホッゴホッ" or
          line_msg_txt == "ごほっ" or
          line_msg_txt == "ゴホッ" or
          line_msg_txt == "へぶしっ" or
          line_msg_txt == "ヘブシッ" or
          line_msg_txt == "はっくしょん" or
          line_msg_txt == "ハックション"):
            extrct_intnt_frm_gag_vocl_crd_cpy_and_etc_rslt = "(生理現象)"
    elif (line_msg_txt == "なあ" or
          line_msg_txt == "なぁ" or
          line_msg_txt == "なあ？" or
          line_msg_txt == "なぁ？" or
          line_msg_txt == "なあ！" or
          line_msg_txt == "なぁ！"):
            extrct_intnt_frm_gag_vocl_crd_cpy_and_etc_rslt = "(呼掛け＆問掛け)"        
    elif (line_msg_txt == "ブー！ブー！" or
          line_msg_txt == "ブー！ ブー！"):
            extrct_intnt_frm_gag_vocl_crd_cpy_and_etc_rslt = "(ブーイング)"
    elif (line_msg_txt == "分かった" or
          line_msg_txt == "わかった" or
          line_msg_txt == "分かった！" or
          line_msg_txt == "わかった！"):
            extrct_intnt_frm_gag_vocl_crd_cpy_and_etc_rslt = "(理解＆認識)(感動＆感激)"
    else:
            extrct_intnt_frm_gag_vocl_crd_cpy_and_etc_rslt = "(その他・不明)"
    return extrct_intnt_frm_gag_vocl_crd_cpy_and_etc_rslt


#LINEメッセージが短文＆定型文だったとして、これからインテント(＝意図するもの)を抽出する
def extract_intent_from_short_and_boilerplate(rmv_edprtcl_rslt):
    #短文＆定型文となっているメッセージからインテントを抽出して、これを呼出し元に引渡しをする
    if   (rmv_edprtcl_rslt == "おはよう" or
          rmv_edprtcl_rslt == "おは" or
          rmv_edprtcl_rslt == "こんにちは" or
          rmv_edprtcl_rslt == "こんにち" or
          rmv_edprtcl_rslt == "こんばん" or
          rmv_edprtcl_rslt == "ばんは" or
          rmv_edprtcl_rslt == "ばん" or
          rmv_edprtcl_rslt == "やあ" or
          rmv_edprtcl_rslt == "どうも"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(挨拶)"
    elif (rmv_edprtcl_rslt == "流石ですね" or
          rmv_edprtcl_rslt == "流石です" or
          rmv_edprtcl_rslt == "流石" or
          rmv_edprtcl_rslt == "さすがですね" or
          rmv_edprtcl_rslt == "さすがです" or
          rmv_edprtcl_rslt == "さすが" or
          rmv_edprtcl_rslt == "すごいですね" or
          rmv_edprtcl_rslt == "すごい" or
          rmv_edprtcl_rslt == "凄いですね" or
          rmv_edprtcl_rslt == "凄いです" or
          rmv_edprtcl_rslt == "凄い" or
          rmv_edprtcl_rslt == "素晴らしい" or
          rmv_edprtcl_rslt == "すばらしい" or
          rmv_edprtcl_rslt == "賢いですね" or
          rmv_edprtcl_rslt == "賢いです" or
          rmv_edprtcl_rslt == "賢い" or
          rmv_edprtcl_rslt == "偉いですね" or
          rmv_edprtcl_rslt == "偉いです" or
          rmv_edprtcl_rslt == "偉い" or
          rmv_edprtcl_rslt == "エラいですね" or
          rmv_edprtcl_rslt == "エラいです" or
          rmv_edprtcl_rslt == "エラい" or
          rmv_edprtcl_rslt == "立派ですね" or
          rmv_edprtcl_rslt == "立派です" or
          rmv_edprtcl_rslt == "立派" or
          rmv_edprtcl_rslt == "感服しました" or
          rmv_edprtcl_rslt == "感服した" or
          rmv_edprtcl_rslt == "感服" or
          rmv_edprtcl_rslt == "敬服いたします" or
          rmv_edprtcl_rslt == "敬服します" or
          rmv_edprtcl_rslt == "敬服" or
          rmv_edprtcl_rslt == "最高ですね" or
          rmv_edprtcl_rslt == "最高です" or
          rmv_edprtcl_rslt == "最高" or
          rmv_edprtcl_rslt == "あなたに感動しました" or
          rmv_edprtcl_rslt == "あなたに感動した" or
          rmv_edprtcl_rslt == "あなたに感動" or
          rmv_edprtcl_rslt == "かっこいい" or
          rmv_edprtcl_rslt == "カッコいい" or
          rmv_edprtcl_rslt == "カッコイイ" or
          rmv_edprtcl_rslt == "可愛い" or
          rmv_edprtcl_rslt == "かいい" or
          rmv_edprtcl_rslt == "カワイい" or
          rmv_edprtcl_rslt == "カワイイ" or
          rmv_edprtcl_rslt == "かい" or
          rmv_edprtcl_rslt == "カワイ" or
          rmv_edprtcl_rslt == "かわゆす" or
          rmv_edprtcl_rslt == "カワゆす" or
          rmv_edprtcl_rslt == "カワユス" or
          rmv_edprtcl_rslt == "綺麗" or
          rmv_edprtcl_rslt == "きれい" or
          rmv_edprtcl_rslt == "キレい" or
          rmv_edprtcl_rslt == "キレイ" or
          rmv_edprtcl_rslt == "いけてる" or
          rmv_edprtcl_rslt == "イケてる" or
          rmv_edprtcl_rslt == "イケテル" or
          rmv_edprtcl_rslt == "素敵" or
          rmv_edprtcl_rslt == "すてき" or
          rmv_edprtcl_rslt == "ステキ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(称賛＆礼賛)"
    elif (rmv_edprtcl_rslt == "変態" or
          rmv_edprtcl_rslt == "へんたい" or
          rmv_edprtcl_rslt == "ヘンタイ" or
          rmv_edprtcl_rslt == "ブス" or
          rmv_edprtcl_rslt == "ぶす" or
          rmv_edprtcl_rslt == "不細工" or
          rmv_edprtcl_rslt == "ぶさいく" or
          rmv_edprtcl_rslt == "ブサイク" or
          rmv_edprtcl_rslt == "最低" or
          rmv_edprtcl_rslt == "さいて" or
          rmv_edprtcl_rslt == "サイテ" or
          rmv_edprtcl_rslt == "無能" or
          rmv_edprtcl_rslt == "ばか" or
          rmv_edprtcl_rslt == "バカ" or
          rmv_edprtcl_rslt == "あほ" or
          rmv_edprtcl_rslt == "アホ" or
          rmv_edprtcl_rslt == "くず" or
          rmv_edprtcl_rslt == "クズ" or
          rmv_edprtcl_rslt == "かす" or
          rmv_edprtcl_rslt == "カス" or
          rmv_edprtcl_rslt == "ゴミ" or
          rmv_edprtcl_rslt == "ごみ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(罵詈＆罵倒)"
    elif (rmv_edprtcl_rslt == "消えてください" or
          rmv_edprtcl_rslt == "消えて" or
          rmv_edprtcl_rslt == "消えろ" or
          rmv_edprtcl_rslt == "消えな" or
          rmv_edprtcl_rslt == "死んでください" or
          rmv_edprtcl_rslt == "死んで" or
          rmv_edprtcl_rslt == "死ね" or
          rmv_edprtcl_rslt == "氏んでください" or
          rmv_edprtcl_rslt == "氏んで" or
          rmv_edprtcl_rslt == "氏ね" or
          rmv_edprtcl_rslt == "しんでください" or
          rmv_edprtcl_rslt == "しんで" or
          rmv_edprtcl_rslt == "しね" or
          rmv_edprtcl_rslt == "死にな" or
          rmv_edprtcl_rslt == "氏にな" or
          rmv_edprtcl_rslt == "しにな" or
          rmv_edprtcl_rslt == "死んでろ" or
          rmv_edprtcl_rslt == "氏んでろ" or
          rmv_edprtcl_rslt == "しんでろ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(人格・存在否定)"
    elif (rmv_edprtcl_rslt == "大天才ですか" or
          rmv_edprtcl_rslt == "天才ですか" or
          rmv_edprtcl_rslt == "秀才ですか" or
          rmv_edprtcl_rslt == "優秀ですか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(称賛＆礼賛)(半疑問)"
    elif (rmv_edprtcl_rslt == "無能ですか" or
          rmv_edprtcl_rslt == "バカですか" or
          rmv_edprtcl_rslt == "アホですか" or
          rmv_edprtcl_rslt == "クズですか" or
          rmv_edprtcl_rslt == "カスですか" or
          rmv_edprtcl_rslt == "ゴミですか" or
          rmv_edprtcl_rslt == "ばかですか" or
          rmv_edprtcl_rslt == "あほですか" or
          rmv_edprtcl_rslt == "くずですか" or
          rmv_edprtcl_rslt == "かすですか" or
          rmv_edprtcl_rslt == "ごみですか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(罵詈＆罵倒)(半疑問)"
    elif (rmv_edprtcl_rslt == "何をしていますか" or
          rmv_edprtcl_rslt == "何をしてますか" or
          rmv_edprtcl_rslt == "何してますか" or
          rmv_edprtcl_rslt == "なにをしていますか" or
          rmv_edprtcl_rslt == "なにをしてますか" or
          rmv_edprtcl_rslt == "なにしてますか" or
          rmv_edprtcl_rslt == "どうしていますか" or
          rmv_edprtcl_rslt == "どうしてますか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(質問＆確認)(現在進行)(状態＆状況)"
    elif (rmv_edprtcl_rslt == "何をしてきましたか" or
          rmv_edprtcl_rslt == "何をしてましたか" or
          rmv_edprtcl_rslt == "何してましたか" or
          rmv_edprtcl_rslt == "何してた" or
          rmv_edprtcl_rslt == "なにをしてきましたか" or
          rmv_edprtcl_rslt == "なにをしてましたか" or
          rmv_edprtcl_rslt == "なにしてましたか" or
          rmv_edprtcl_rslt == "なにしてた" or
          rmv_edprtcl_rslt == "どうしてきましたか" or
          rmv_edprtcl_rslt == "どうしてましたか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(質問＆確認)(過去完了)(状態＆状況)"
    elif (rmv_edprtcl_rslt == "何をしますか" or
          rmv_edprtcl_rslt == "何しますか" or
          rmv_edprtcl_rslt == "なにをしますか" or
          rmv_edprtcl_rslt == "なにしますか" or
          rmv_edprtcl_rslt == "何をしたいですか" or
          rmv_edprtcl_rslt == "何したいですか" or
          rmv_edprtcl_rslt == "なにをしたいですか" or
          rmv_edprtcl_rslt == "なにしたいですか" or
          rmv_edprtcl_rslt == "なにしたい" or
          rmv_edprtcl_rslt == "なにしますか" or
          rmv_edprtcl_rslt == "なにします" or
          rmv_edprtcl_rslt == "どうしたいですか" or
          rmv_edprtcl_rslt == "どうしますか" or
          rmv_edprtcl_rslt == "どうします"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(質問＆確認)(現在)(欲求＆欲動)"
    elif (rmv_edprtcl_rslt == "何をしたかったのですか" or
          rmv_edprtcl_rslt == "何をしたかったんですか" or
          rmv_edprtcl_rslt == "何したかったのですか" or
          rmv_edprtcl_rslt == "何したかったんですか" or
          rmv_edprtcl_rslt == "なにをしたかったのですか" or
          rmv_edprtcl_rslt == "なにをしたかったんですか" or
          rmv_edprtcl_rslt == "なにしたかったのですか" or
          rmv_edprtcl_rslt == "なにしたかったんですか" or
          rmv_edprtcl_rslt == "どうしたかったのですか" or
          rmv_edprtcl_rslt == "どうしたかったんですか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(質問＆確認)(過去)(欲求＆欲動)"
    elif (rmv_edprtcl_rslt == "何をしていきたいですか" or
          rmv_edprtcl_rslt == "何していきたいですか" or
          rmv_edprtcl_rslt == "何していきたい" or
          rmv_edprtcl_rslt == "なにをしていきたいですか" or
          rmv_edprtcl_rslt == "なにしていきたいですか" or
          rmv_edprtcl_rslt == "なにしていきたい" or
          rmv_edprtcl_rslt == "どうしていきたいですか" or
          rmv_edprtcl_rslt == "どうしていきたい"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(質問＆確認)(未来)(欲求＆欲動)"
    elif (rmv_edprtcl_rslt == "どうなのですか" or
          rmv_edprtcl_rslt == "どうなんですか" or
          rmv_edprtcl_rslt == "どうなの"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(質問＆確認)(時制不明)(意図＆目的)"
    elif rmv_edprtcl_rslt == "どう":
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(質問＆確認)(時制不明)(感想＆感慨)"
    elif (rmv_edprtcl_rslt == "どうしてなのですか" or
          rmv_edprtcl_rslt == "どうしてなんですか" or
          rmv_edprtcl_rslt == "どうしてですか" or
          rmv_edprtcl_rslt == "どうして"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(質問＆確認)(時制不明)(事由＆理由＆事情)"        
    elif (rmv_edprtcl_rslt == "何故なのですか" or
          rmv_edprtcl_rslt == "何故なんですか" or
          rmv_edprtcl_rslt == "何故ですか" or
          rmv_edprtcl_rslt == "何故" or
          rmv_edprtcl_rslt == "なぜなのですか" or
          rmv_edprtcl_rslt == "なぜなんですか" or
          rmv_edprtcl_rslt == "なぜですか" or
          rmv_edprtcl_rslt == "なぜ" or
          rmv_edprtcl_rslt == "何で" or
          rmv_edprtcl_rslt == "なんで"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(質問＆確認)(時制不明)(事由＆理由＆事情)"
    elif (rmv_edprtcl_rslt == "いいです" or
          rmv_edprtcl_rslt == "いい" or
          rmv_edprtcl_rslt == "OK" or
          rmv_edprtcl_rslt == "おけ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(許容＆許可)"
    elif (rmv_edprtcl_rslt == "駄目です" or
          rmv_edprtcl_rslt == "駄目です" or
          rmv_edprtcl_rslt == "駄目だ" or
          rmv_edprtcl_rslt == "駄目" or
          rmv_edprtcl_rslt == "だめです" or
          rmv_edprtcl_rslt == "だめだ" or
          rmv_edprtcl_rslt == "だめ" or
          rmv_edprtcl_rslt == "ダメです" or
          rmv_edprtcl_rslt == "ダメだ" or
          rmv_edprtcl_rslt == "ダメ" or
          rmv_edprtcl_rslt == "禁止です" or
          rmv_edprtcl_rslt == "禁止だ" or
          rmv_edprtcl_rslt == "禁止" or
          rmv_edprtcl_rslt == "いけません" or
          rmv_edprtcl_rslt == "いけない"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(禁止＆不許可)"
    elif (rmv_edprtcl_rslt == "おい" or
          rmv_edprtcl_rslt == "ねぇ" or
          rmv_edprtcl_rslt == "へい"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(呼掛け)"
    elif (rmv_edprtcl_rslt == "ですね" or
          rmv_edprtcl_rslt == "そうだね" or
          rmv_edprtcl_rslt == "そだね" or
          rmv_edprtcl_rslt == "だよねえ" or
          rmv_edprtcl_rslt == "だよねぇ" or
          rmv_edprtcl_rslt == "だねえ" or
          rmv_edprtcl_rslt == "だねぇ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(賛意＆賛同)"   
    elif (rmv_edprtcl_rslt == "歌って" or
          rmv_edprtcl_rslt == "うたって" or
          rmv_edprtcl_rslt == "踊って" or
          rmv_edprtcl_rslt == "おどって" or
          rmv_edprtcl_rslt == "遊んで" or
          rmv_edprtcl_rslt == "あそんで"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(依頼＆懇願)"
    elif (rmv_edprtcl_rslt == "行きます" or
          rmv_edprtcl_rslt == "いきます" or
          rmv_edprtcl_rslt == "遣ります" or
          rmv_edprtcl_rslt == "やります" or
          rmv_edprtcl_rslt == "遊びます" or
          rmv_edprtcl_rslt == "あそびます" or
          rmv_edprtcl_rslt == "休みます" or
          rmv_edprtcl_rslt == "やすみます"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在＆未来)"
    elif (rmv_edprtcl_rslt == "楽しい" or
          rmv_edprtcl_rslt == "たのしい" or
          rmv_edprtcl_rslt == "苦しい" or
          rmv_edprtcl_rslt == "くるしい" or
          rmv_edprtcl_rslt == "辛い" or
          rmv_edprtcl_rslt == "つらい" or
          rmv_edprtcl_rslt == "嬉しい" or
          rmv_edprtcl_rslt == "うれしい" or
          rmv_edprtcl_rslt == "悲しい" or
          rmv_edprtcl_rslt == "かなしい" or
          rmv_edprtcl_rslt == "哀しい" or
          rmv_edprtcl_rslt == "楽" or
          rmv_edprtcl_rslt == "らく" or
          rmv_edprtcl_rslt == "ラク" or
          rmv_edprtcl_rslt == "らくちん" or
          rmv_edprtcl_rslt == "ラクチン" or
          rmv_edprtcl_rslt == "楽勝" or
          rmv_edprtcl_rslt == "らくしょう" or
          rmv_edprtcl_rslt == "ラクショウ" or
          rmv_edprtcl_rslt == "大変" or
          rmv_edprtcl_rslt == "疲れた" or
          rmv_edprtcl_rslt == "つかれた"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(訴求＆表現)(感情＆心理＆精神＆肉体)"
    elif rmv_edprtcl_rslt == "海":
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(掛合い)"
    elif (rmv_edprtcl_rslt == "最初は グ" or
          rmv_edprtcl_rslt == "最初はグ" or
          rmv_edprtcl_rslt == "じゃんけんぽん" or
          rmv_edprtcl_rslt == "じゃんけん" or
          rmv_edprtcl_rslt == "ジャンケンポン" or
          rmv_edprtcl_rslt == "ジャンケン" or
          rmv_edprtcl_rslt == "ジャンケンぽん"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(遊戯)"
    elif (rmv_edprtcl_rslt == "お願いします" or
          rmv_edprtcl_rslt == "お願いです" or
          rmv_edprtcl_rslt == "お願い"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(依頼・依願)"
    elif (rmv_edprtcl_rslt == "御免なさい" or
          rmv_edprtcl_rslt == "御免" or
          rmv_edprtcl_rslt == "ごめんなさい" or
          rmv_edprtcl_rslt == "ごめん" or
          rmv_edprtcl_rslt == "ゴメン" or
          rmv_edprtcl_rslt == "メンゴ メンゴ" or
          rmv_edprtcl_rslt == "メンゴメンゴ" or
          rmv_edprtcl_rslt == "メンゴ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(陳謝・謝罪)"
    elif (rmv_edprtcl_rslt == "承知いたしました" or
          rmv_edprtcl_rslt == "承知しました" or
          rmv_edprtcl_rslt == "承知した" or
          rmv_edprtcl_rslt == "承知" or
          rmv_edprtcl_rslt == "かしこまりました" or
          rmv_edprtcl_rslt == "かしこまり"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(承知・承諾)"
    elif (rmv_edprtcl_rslt == "了解いたしました" or
          rmv_edprtcl_rslt == "了解しました" or
          rmv_edprtcl_rslt == "了解した" or
          rmv_edprtcl_rslt == "了解" or
          rmv_edprtcl_rslt == "りょ" or
          rmv_edprtcl_rslt == "リョ" or
          rmv_edprtcl_rslt == "分かりました" or
          rmv_edprtcl_rslt == "わかりました" or
          rmv_edprtcl_rslt == "分かった" or
          rmv_edprtcl_rslt == "わかった"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(了承・了解)"
    elif (rmv_edprtcl_rslt == "愛しています" or
          rmv_edprtcl_rslt == "愛してます" or
          rmv_edprtcl_rslt == "愛してる" or
          rmv_edprtcl_rslt == "あいしています" or
          rmv_edprtcl_rslt == "あいしてます" or
          rmv_edprtcl_rslt == "あいしてる" or
          rmv_edprtcl_rslt == "好きです" or
          rmv_edprtcl_rslt == "好き" or
          rmv_edprtcl_rslt == "すき" or
          rmv_edprtcl_rslt == "スキ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(訴求＆表現)(求愛＆発情)"
    elif (rmv_edprtcl_rslt == "なぜそうなるのですか" or
          rmv_edprtcl_rslt == "なぜそうなるんですか" or
          rmv_edprtcl_rslt == "なぜそうなるのか" or
          rmv_edprtcl_rslt == "なぜそうなるか" or
          rmv_edprtcl_rslt == "なぜそうなるのです" or
          rmv_edprtcl_rslt == "なぜそうなるんです"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(単純)"
    elif (rmv_edprtcl_rslt == "なんでそうなるのなぁ" or
          rmv_edprtcl_rslt == "なんでそうなるかなぁ" or
          rmv_edprtcl_rslt == "なぜそうなるの" or
          rmv_edprtcl_rslt == "なぜそうなる" or
          rmv_edprtcl_rslt == "なんでそうなるのか" or
          rmv_edprtcl_rslt == "なんでそうなるか" or
          rmv_edprtcl_rslt == "なんでそうなる"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(疑義＆質問＆確認(反発＆反感)"
    else:
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(その他・不明)"
    return extrct_intnt_frm_shrt_and_blrplt_rslt


#LINEメッセージの末尾部分からインテント(＝意図するもの)を抽出する
def extract_intent_from_endnotes(rmv_edprtcl_rslt):
    #メッセージの末尾部分からインテントを抽出して、これを呼出し元に引渡しをする
    if   (check_text_terminated_string(rmv_edprtcl_rslt, "します") or
          check_text_terminated_string(rmv_edprtcl_rslt, "する")):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在＆未来＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しない")):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在＆未来＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "している") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してる")):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在進行＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "していない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在進行＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できている") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてる")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在進行＆能動＆可能＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できていない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてません")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在進行＆能動＆可能＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できた")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(過去＆能受不明＆可能＝完了)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(過去＆能受不明＆不可能＝未完了)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できる")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在＆能動＆可能)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在＆能動＆不可能)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(未来)(能動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "した") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやりました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやった")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(過去)(能動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(過去進行)(能動)(否定)"      
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてます")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(過去進行)(受動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されていない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(過去進行)(受動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "された")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(過去完了)(受動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "でした") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だったです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だった")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(過去完了)(能受不明)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でなかった")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(過去完了)(能受不明)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "をしていきたい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてたい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたい")
          check_text_terminated_string(rmv_edprtcl_rslt, "をやってたい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしていきたい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてたい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやっていきたい")
          check_text_terminated_string(rmv_edprtcl_rslt, "はやってたい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "していきたい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してたい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "いたい")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在＆未来)(持続)(能動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はしていきたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "していきたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしていきたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやってたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやっていきたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやってたくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやっていかない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやっていかない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやってかない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやってかない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在＆未来)(持続)(能動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でなかった")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(表明＆宣言)(現在＆未来)(持続)(能動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ですから") or
          check_text_terminated_string(rmv_edprtcl_rslt, "です") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ます")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(紹介＆説明＆提示)(表明＆宣言)(時制不明)(能受不明)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "っていました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってた")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(過去＆能動)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ということでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということですよね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということだね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってことでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってことですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってことですよね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってことですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってことだね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ですよね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だね")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しません")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(誘導＆勧誘)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "したい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "たい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "やりたい")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(欲求＆欲動)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "いです")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(紹介＆説明＆提示)(時制不明)(能受不明)")
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "をしないように") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしないよう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をするな") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃ駄目") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃだめ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃダメ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしないように") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしないよう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はするな") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃ駄目") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃだめ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃダメ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないように") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないよう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "するな") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃ駄目") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃだめ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃダメ")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(制止＆禁止)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしないように") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしないよう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がするな") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃ駄目") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃだめ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃダメ")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(制止＆禁止)(個人特定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "をしてください") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をして") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてください") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はして") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してください") or
          check_text_terminated_string(rmv_edprtcl_rslt, "して")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(依頼＆要求)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしてください") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がして")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(依頼＆要求)(個人特定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しなさい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しろ")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(指示＆命令)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はしなければならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなければ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしないといけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしないといけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃいけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はせにゃならん") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなければならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなければ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしないといけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしないといけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃいけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をせにゃならん") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなければならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなければ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないといけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないといけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃいけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "せにゃならん")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(勧告)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしなければならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなければ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしないといけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしないといけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がせにゃならん")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(勧告)(肯定)(個人特定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はしてはならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてはいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしたらいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃならん") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてはならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてはいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしたらいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃならん"
          check_text_terminated_string(rmv_edprtcl_rslt, "してはならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してはいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "したらいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃならん"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(勧告)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしてはならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしてはいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしたらいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃならん")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(勧告)(否定)(個人特定)"
    elif check_text_terminated_string(rmv_edprtcl_rslt, "だ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(誇示＆顕示)(強調)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "でしょう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だろう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だろ")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(推定＆推測＆推量)(文末)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "だそうです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だろう")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(推定＆推測＆推量)(報告＆連絡)(文末)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はいます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はいる")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がいます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がいる")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(個人・個物特定)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はいません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はいない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がいません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がいない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(個人・個物特定)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "にいます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "にいる")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(所在＆場所)(人間＆動物＆その他)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "にいません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "にいない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(所在＆場所)(人間＆動物＆その他)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はあります") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はある")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(存在＆有無)(物体＆モノ全般)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "があります") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がある")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(存在＆有無)(物体＆モノ全般)(個人・個物特定)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はありません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(存在＆有無)(物体＆モノ全般)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がありません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(報告＆連絡)(存在＆有無)(物体＆モノ全般)(個人・個物特定)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はだね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をだね")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(紹介＆説明＆提示)(継続＆前段)"
    else:
            extrct_intnt_frm_shrt_and_blrplt_rslt = "(その他・不明)"
    return extrct_intnt_frm_shrt_and_blrplt_rslt


#LINEメッセージの先頭・中間部分からコンテント(＝意図されるもの)を抽出する
def extract_content_from_top_and_middle(rmv_edprtcl_rslt):
    #メッセージの先頭・中間部分部分からコンテントを抽出して、これを呼出し元に引渡しをする
    if   (check_text_start_string(rmv_edprtcl_rslt, "さて") or
          check_text_start_string(rmv_edprtcl_rslt, "ところで")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(転換＆切替)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "そして") or
          check_text_start_string(rmv_edprtcl_rslt, "それで") or
          check_text_start_string(rmv_edprtcl_rslt, "そんで")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(結論＆結末)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "加えて") or
          check_text_start_string(rmv_edprtcl_rslt, "さらに") or
          check_text_start_string(rmv_edprtcl_rslt, "又") or
          check_text_start_string(rmv_edprtcl_rslt, "また")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(添加＆追加)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "多分") or
          check_text_start_string(rmv_edprtcl_rslt, "たぶん") or
          check_text_start_string(rmv_edprtcl_rslt, "恐らくは") or
          check_text_start_string(rmv_edprtcl_rslt, "おそらくは") or
          check_text_start_string(rmv_edprtcl_rslt, "恐らく") or
          check_text_start_string(rmv_edprtcl_rslt, "おそらく")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(推定＆推測＆推量)(文頭)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "又は") or
          check_text_start_string(rmv_edprtcl_rslt, "または")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(論理和)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "且つ") or
          check_text_start_string(rmv_edprtcl_rslt, "かつ")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(論理積)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "得てして") or
          check_text_start_string(rmv_edprtcl_rslt, "えてして") or
          check_text_start_string(rmv_edprtcl_rslt, "概して") or
          check_text_start_string(rmv_edprtcl_rslt, "大抵は") or
          check_text_start_string(rmv_edprtcl_rslt, "大抵") or
          check_text_start_string(rmv_edprtcl_rslt, "大概は") or
          check_text_start_string(rmv_edprtcl_rslt, "大概")): 
            extrct_cntnt_frm_tp_and_mddl_rslt = "(概要＆概略)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "確実に") or
          check_text_start_string(rmv_edprtcl_rslt, "明らかに") or
          check_text_start_string(rmv_edprtcl_rslt, "多くの場合には") or
          check_text_start_string(rmv_edprtcl_rslt, "多くの場合は") or
          check_text_start_string(rmv_edprtcl_rslt, "多くの場合") or
          check_text_start_string(rmv_edprtcl_rslt, "多くは") or
          check_text_start_string(rmv_edprtcl_rslt, "多く") or
          check_text_start_string(rmv_edprtcl_rslt, "少なくとも") or
          check_text_start_string(rmv_edprtcl_rslt, "少なくても")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(断定＆確定)"
    elif  check_text_start_string(rmv_edprtcl_rslt, "(大層"):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(程度強調)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "なので") or
          check_text_start_string(rmv_edprtcl_rslt, "ですから")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(説明＆説得)(事由＆理由＆事情＆状況)"
    elif check_text_start_string(rmv_edprtcl_rslt, "さては"):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(推定＆推測＆推量)(自然接続＝文末決定型)(文頭)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "もしも") or
          check_text_start_string(rmv_edprtcl_rslt, "もし")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(仮定＆仮説)(原因＆要因＆事情＆状況＆状態)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "例えば") or
          check_text_start_string(rmv_edprtcl_rslt, "たとえば") or
          check_text_start_string(rmv_edprtcl_rslt, "例すれば") or
          check_text_start_string(rmv_edprtcl_rslt, "例せば")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(比喩＆類例)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "類すれば") or
          check_text_start_string(rmv_edprtcl_rslt, "類せば")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(仮定＆仮説)(比較＆類似)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "譬え") or
          check_text_start_string(rmv_edprtcl_rslt, "たとえ") or
          check_text_start_string(rmv_edprtcl_rslt, "仮に")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(仮定＆仮説)(特別・特例言及)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "或いは") or
          check_text_start_string(rmv_edprtcl_rslt, "あるいは")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(選択＆追求)(可能性)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "若しくは") or
          check_text_start_string(rmv_edprtcl_rslt, "もしくは") or
          check_text_start_string(rmv_edprtcl_rslt, "もしか")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(選択＆追求)(可能性)(代理＆代替)(対名詞・存在)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "乃至は") or
          check_text_start_string(rmv_edprtcl_rslt, "ないしは") or
          check_text_start_string(rmv_edprtcl_rslt, "ないし")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(選択＆追求)(可能性)(代理＆代替)(対動詞・行為)"
    else:
            extrct_cntnt_frm_tp_and_mddl_rslt = "(その他・不明)"
    return extrct_cntnt_frm_tp_and_mddl_rslt


#ユーザーから送られるLINEメッセージの中に含まれるコンテントを解析する
def content_analyze(rmv_intnt_rslt):
    cntnt_anlyz_rslt = ""
    return cntnt_anlyz_rslt


#ユーザーから送られるLINEメッセージの中に含まれるコンテントを除去する
def remove_content(rmv_edprtcl_rslt):
    #メッセージの中に含まれる日本語固有のコンテントを除去する
    rmv_cnddt_cntnt = []
    if   (check_text_start_string(rmv_edprtcl_rslt, "さて"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "ところで"):
rmv_cnddt_cntnt.append("")
    if (check_text_start_string(rmv_edprtcl_rslt, "そして"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "それで"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "そんで"):
rmv_cnddt_cntnt.append("")
    if (check_text_start_string(rmv_edprtcl_rslt, "加えて"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "さらに"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "又"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "また"):
rmv_cnddt_cntnt.append("")
    if check_text_start_string(rmv_edprtcl_rslt, "多分"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "たぶん"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "恐らくは"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "おそらくは"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "恐らく"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "おそらく"):
rmv_cnddt_cntnt.append("")
    if (check_text_start_string(rmv_edprtcl_rslt, "又は"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "または"):
rmv_cnddt_cntnt.append("")
    if (check_text_start_string(rmv_edprtcl_rslt, "且つ"):
rmv_cnddt_cntnt.append("")
          check_text_start_string(rmv_edprtcl_rslt, "かつ")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(論理積)"
    if (check_text_start_string(rmv_edprtcl_rslt, "得てして") or
          check_text_start_string(rmv_edprtcl_rslt, "えてして") or
          check_text_start_string(rmv_edprtcl_rslt, "概して") or
          check_text_start_string(rmv_edprtcl_rslt, "大抵は") or
          check_text_start_string(rmv_edprtcl_rslt, "大抵") or
          check_text_start_string(rmv_edprtcl_rslt, "大概は") or
          check_text_start_string(rmv_edprtcl_rslt, "大概")): 
            extrct_cntnt_frm_tp_and_mddl_rslt = "(概要＆概略)"
    if (check_text_start_string(rmv_edprtcl_rslt, "確実に") or
          check_text_start_string(rmv_edprtcl_rslt, "明らかに") or
          check_text_start_string(rmv_edprtcl_rslt, "多くの場合には") or
          check_text_start_string(rmv_edprtcl_rslt, "多くの場合は") or
          check_text_start_string(rmv_edprtcl_rslt, "多くの場合") or
          check_text_start_string(rmv_edprtcl_rslt, "多くは") or
          check_text_start_string(rmv_edprtcl_rslt, "多く") or
          check_text_start_string(rmv_edprtcl_rslt, "少なくとも") or
          check_text_start_string(rmv_edprtcl_rslt, "少なくても")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(断定＆確定)"
    if  check_text_start_string(rmv_edprtcl_rslt, "(大層"):
          extrct_cntnt_frm_tp_and_mddl_rslt = "(程度強調)"
    if (check_text_start_string(rmv_edprtcl_rslt, "なので") or
          check_text_start_string(rmv_edprtcl_rslt, "ですから")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(説明＆説得)(事由＆理由＆事情＆状況)"
    if check_text_start_string(rmv_edprtcl_rslt, "さては"):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(推定＆推測＆推量)(自然接続＝文末決定型)(文頭)"
    if (check_text_start_string(rmv_edprtcl_rslt, "もしも") or
          check_text_start_string(rmv_edprtcl_rslt, "もし")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(仮定＆仮説)(原因＆要因＆事情＆状況＆状態)"
    if (check_text_start_string(rmv_edprtcl_rslt, "例えば") or
          check_text_start_string(rmv_edprtcl_rslt, "たとえば") or
          check_text_start_string(rmv_edprtcl_rslt, "例すれば") or
          check_text_start_string(rmv_edprtcl_rslt, "例せば")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(比喩＆類例)"
    if (check_text_start_string(rmv_edprtcl_rslt, "類すれば") or
          check_text_start_string(rmv_edprtcl_rslt, "類せば")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(仮定＆仮説)(比較＆類似)"
    if (check_text_start_string(rmv_edprtcl_rslt, "譬え") or
          check_text_start_string(rmv_edprtcl_rslt, "たとえ") or
          check_text_start_string(rmv_edprtcl_rslt, "仮に")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(仮定＆仮説)(特別・特例言及)"
    if (check_text_start_string(rmv_edprtcl_rslt, "或いは") or
          check_text_start_string(rmv_edprtcl_rslt, "あるいは")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(選択＆追求)(可能性)"
    if (check_text_start_string(rmv_edprtcl_rslt, "若しくは") or
          check_text_start_string(rmv_edprtcl_rslt, "もしくは") or
          check_text_start_string(rmv_edprtcl_rslt, "もしか")):
            extrct_cntnt_frm_tp_and_mddl_rslt = "(選択＆追求)(可能性)(代理＆代替)(対名詞・存在)"
    if (check_text_start_string(rmv_edprtcl_rslt, "乃至は") or
         check_text_start_string(rmv_edprtcl_rslt, "ないしは") or
          check_text_start_string(rmv_edprtcl_rslt, "ないし")):
         rmv_cnddt_cntnt.append("")

    #前段で取得した削除候補の中から実際に削除するインテントを決定して、これを呼出し元に引渡しをする
    rmv_cnddt_cntnt_list = []
    for cntnt in rmv_cnddt_cntnt
        rmv_cnddt_cntnt_list.append([len(cntnt), cntnt])
    idx       = 0
    tmp_cntnt = ""
    for i in rmv_cnddt_cntnt_list
        if len(rmv_cnddt_cntnt_list) > (i+1):
           if rmv_cnddt_cntnt_list[i+1][0] > rmv_cnddt_cntnt_list[idx][0]:
              tmp_cntnt = rmv_cnddt_cntnt_list[i+1][1]
              idx = i + 1
           else:
              continue

    rmv_cntnt_rslt = tmp_cntnt
    return rmv_cntnt_rslt