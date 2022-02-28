import re
from janome.tokenizer import Tokenizer




#ユーザーから送られるLINEメッセージの中に含まれる記号を除去する
def remove_symbol(line_msg_txt):
    #メッセージの中に含まれる日本語固有の記号を除去する
    rmv_symbl_rslt   = re.sub("(’)",  "", line_msg_txt)
    rmv_symbl_rslt2  = re.sub("(”)",  "", rmv_symbl_rslt)
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

    #メッセージの中に含まれる先頭と末尾の空白と改行を除去する
    rmv_symbl_rslt_end = rmv_symbl_rslt14.strip()
    return rmv_symbl_rslt_end


#ユーザーから送られるLINEメッセージの中に含まれる終助詞を除去する
def remove_endparticle(rmv_symbl_rslt):
    #メッセージの中に含まれる日本語固有の助詞を除去する
    rmv_edprtcl_rslt   = re.sub("(なあ)", "", rmv_symbl_rslt)
    rmv_edprtcl_rslt2  = re.sub("(なぁ)", "", rmv_edprtcl_rslt)
    rmv_edprtcl_rslt3  = re.sub("(なっ)", "", rmv_edprtcl_rslt2)
    rmv_edprtcl_rslt4  = re.sub("(ねえ)", "", rmv_edprtcl_rslt3)
    rmv_edprtcl_rslt5  = re.sub("(ねぇ)", "", rmv_edprtcl_rslt4)
    rmv_edprtcl_rslt6  = re.sub("(わ)",   "", rmv_edprtcl_rslt5)
    rmv_edprtcl_rslt7  = re.sub("(わあ)", "", rmv_edprtcl_rslt6)
    rmv_edprtcl_rslt8  = re.sub("(わぁ)",  "", rmv_edprtcl_rslt7)
    rmv_edprtcl_rslt9  = re.sub("(ぜ)",    "", rmv_edprtcl_rslt8)
    rmv_edprtcl_rslt10 = re.sub("(ぜっ)", "", rmv_edprtcl_rslt9)
    rmv_edprtcl_rslt11 = re.sub("(よ)",   "", rmv_edprtcl_rslt10)
    rmv_edprtcl_rslt12 = re.sub("(よお)", "", rmv_edprtcl_rslt11)
    rmv_edprtcl_rslt13 = re.sub("(よぉ)", "", rmv_edprtcl_rslt12)
    rmv_edprtcl_rslt14 = re.sub("(よっ)", "", rmv_edprtcl_rslt13)
    
    #メッセージの中に含まれる先頭と末尾の空白と改行を除去する
    rmv_edprtcl_rslt_end = rmv_edprtcl_rslt14.strip()
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
          line_msg_txt == "ピィヤ～"):
            extrct_intnt_frm_gg_vocl_crd_cpy_and_etc_rslt = "モノマネ(ギャグ＆一発芸)"
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
            extrct_intnt_frm_gg_vocl_crd_cpy_and_etc_rslt = "モノマネ(声帯模写)"
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
            extrct_intnt_frm_gg_vocl_crd_cpy_and_etc_rslt = "生理現象"
    else:
            extrct_intnt_frm_gg_vocl_crd_cpy_and_etc_rslt = "その他・不明"
    return extrct_intnt_frm_gg_vocl_crd_cpy_and_etc_rslt


#LINEメッセージが短文＆定型文だったとして、これからインテント(＝意図するもの)を抽出する
def extract_intent_from_short_and_boilerplate(rmv_edprtcl_rslt):
    #短文＆定型文となっているメッセージからインテントを抽出して、これを呼出し元に引渡しをする
    if   (rmv_edprtcl_rslt == "おはよう" or
          rmv_edprtcl_rslt == "おは" or
          rmv_edprtcl_rslt == "こんにちは" or
          rmv_edprtcl_rslt == "こんばんは" or
          rmv_edprtcl_rslt == "こんばんわ" or
          rmv_edprtcl_rslt == "ばんわ" or
          rmv_edprtcl_rslt == "やあ" or
          rmv_edprtcl_rslt == "どうも"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "挨拶"
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
          rmv_edprtcl_rslt == "あなたに感動"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "称賛＆礼賛"
    elif (rmv_edprtcl_rslt == "最低" or
          rmv_edprtcl_rslt == "無能" or
          rmv_edprtcl_rslt == "バカ" or
          rmv_edprtcl_rslt == "アホ" or
          rmv_edprtcl_rslt == "クズ" or
          rmv_edprtcl_rslt == "カス" or
          rmv_edprtcl_rslt == "ゴミ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "罵詈＆罵倒"
    elif (rmv_edprtcl_rslt == "死んでください" or
          rmv_edprtcl_rslt == "死んで" or
          rmv_edprtcl_rslt == "死ね" or
          rmv_edprtcl_rslt == "氏んでください" or
          rmv_edprtcl_rslt == "氏んで" or
          rmv_edprtcl_rslt == "氏ね" or
          rmv_edprtcl_rslt == "しんでください" or
          rmv_edprtcl_rslt == "しんで" or
          rmv_edprtcl_rslt == "しね"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "人格・存在否定"
    elif (rmv_edprtcl_rslt == "大天才ですか" or
          rmv_edprtcl_rslt == "天才ですか" or
          rmv_edprtcl_rslt == "秀才ですか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "称賛＆礼賛(半疑問)"
    elif (rmv_edprtcl_rslt == "無能ですか" or
          rmv_edprtcl_rslt == "バカですか" or
          rmv_edprtcl_rslt == "アホですか" or
          rmv_edprtcl_rslt == "クズですか" or
          rmv_edprtcl_rslt == "カスですか" or
          rmv_edprtcl_rslt == "ゴミですか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "罵詈＆罵倒(半疑問)"
    elif (rmv_edprtcl_rslt == "何をしていますか" or
          rmv_edprtcl_rslt == "何をしてますか" or
          rmv_edprtcl_rslt == "何してますか" or
          rmv_edprtcl_rslt == "なにをしていますか" or
          rmv_edprtcl_rslt == "なにをしてますか" or
          rmv_edprtcl_rslt == "なにしてますか" or
          rmv_edprtcl_rslt == "どうしていますか" or
          rmv_edprtcl_rslt == "どうしてますか"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(現在進行)(状態＆状況)"
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
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(過去完了)(状態＆状況)"
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
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(現在)(欲求＆欲動)"
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
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(過去)(欲求＆欲動)"
    elif (rmv_edprtcl_rslt == "何をしていきたいですか" or
          rmv_edprtcl_rslt == "何していきたいですか" or
          rmv_edprtcl_rslt == "何していきたい" or
          rmv_edprtcl_rslt == "なにをしていきたいですか" or
          rmv_edprtcl_rslt == "なにしていきたいですか" or
          rmv_edprtcl_rslt == "なにしていきたい" or
          rmv_edprtcl_rslt == "どうしていきたいですか" or
          rmv_edprtcl_rslt == "どうしていきたい"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(未来)(欲求＆欲動)"
    elif (rmv_edprtcl_rslt == "どうなのですか" or
          rmv_edprtcl_rslt == "どうなんですか" or
          rmv_edprtcl_rslt == "どうなの"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(時制不明)(意図＆目的)"
    elif rmv_edprtcl_rslt == "どう":
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(時制不明)(感想＆感慨)"
    elif (rmv_edprtcl_rslt == "どうしてなのですか" or
          rmv_edprtcl_rslt == "どうしてなんですか" or
          rmv_edprtcl_rslt == "どうしてですか" or
          rmv_edprtcl_rslt == "どうして"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "確認(時制不明)(事由＆理由)"
    elif (rmv_edprtcl_rslt == "いいです" or
          rmv_edprtcl_rslt == "いい" or
          rmv_edprtcl_rslt == "OK" or
          rmv_edprtcl_rslt == "おけ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "許容＆許可"
    elif (rmv_edprtcl_rslt == "駄目です" or
          rmv_edprtcl_rslt == "駄目です" or
          rmv_edprtcl_rslt == "駄目だ" or
          rmv_edprtcl_rslt == "駄目" or
          rmv_edprtcl_rslt == "だめです" or
          rmv_edprtcl_rslt == "だめです" or
          rmv_edprtcl_rslt == "だめだ" or
          rmv_edprtcl_rslt == "だめ" or
          rmv_edprtcl_rslt == "ダメです" or
          rmv_edprtcl_rslt == "ダメです" or
          rmv_edprtcl_rslt == "ダメだ" or
          rmv_edprtcl_rslt == "ダメ" or
          rmv_edprtcl_rslt == "禁止です" or
          rmv_edprtcl_rslt == "禁止です" or
          rmv_edprtcl_rslt == "禁止だ" or
          rmv_edprtcl_rslt == "禁止" or
          rmv_edprtcl_rslt == "いけません" or
          rmv_edprtcl_rslt == "いけない"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "禁止＆不許可"
    elif (rmv_edprtcl_rslt == "おい" or
          rmv_edprtcl_rslt == "ねぇ" or
          rmv_edprtcl_rslt == "なぁ" or
          rmv_edprtcl_rslt == "へい"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "呼掛け"        
    elif (rmv_edprtcl_rslt == "ですね" or
          rmv_edprtcl_rslt == "そうだね" or
          rmv_edprtcl_rslt == "そだね" or
          rmv_edprtcl_rslt == "だよねえ" or
          rmv_edprtcl_rslt == "だよねぇ" or
          rmv_edprtcl_rslt == "だねえ" or
          rmv_edprtcl_rslt == "だねぇ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "賛意＆賛同"   
    elif (rmv_edprtcl_rslt == "歌って" or
          rmv_edprtcl_rslt == "うたって" or
          rmv_edprtcl_rslt == "踊って" or
          rmv_edprtcl_rslt == "おどって" or
          rmv_edprtcl_rslt == "遊んで" or
          rmv_edprtcl_rslt == "あそんで"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "依頼＆懇願"
    elif (rmv_edprtcl_rslt == "行きます" or
          rmv_edprtcl_rslt == "いきます" or
          rmv_edprtcl_rslt == "遣ります" or
          rmv_edprtcl_rslt == "やります" or
          rmv_edprtcl_rslt == "遊びます" or
          rmv_edprtcl_rslt == "あそびます" or
          rmv_edprtcl_rslt == "休みます" or
          rmv_edprtcl_rslt == "やすみます"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在＆未来)"
    elif rmv_edprtcl_rslt == "海":
            extrct_intnt_frm_shrt_and_blrplt_rslt = "掛合い"
    elif (rmv_edprtcl_rslt == "最初は グ" or
          rmv_edprtcl_rslt == "最初はグ" or
          rmv_edprtcl_rslt == "じゃんけんぽん" or
          rmv_edprtcl_rslt == "じゃんけん" or
          rmv_edprtcl_rslt == "ジャンケンポン" or
          rmv_edprtcl_rslt == "ジャンケン" or
          rmv_edprtcl_rslt == "ジャンケンぽん"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "遊戯"
    else:
         extrct_intnt_frm_shrt_and_blrplt_rslt = "その他・不明"
    return extrct_intnt_frm_shrt_and_blrplt_rslt


#LINEメッセージの末尾部分からインテント(＝意図するもの)を抽出する
def extract_intent_from_endnotes(rmv_edprtcl_rslt):
    #メッセージの末尾部分からインテントを抽出して、これを呼出し元に引渡しをする
    if   (check_text_terminated_string(rmv_edprtcl_rslt, "します") or
          check_text_terminated_string(rmv_edprtcl_rslt, "する")):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在＆未来＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しない")):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在＆未来＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "している") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してる")):
           extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在進行＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "していない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明(現在進行＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できている") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてる")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在進行＆能動＆可能＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できていない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてません")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在進行＆能動＆可能＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できた")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(過去＆能受不明＆可能＝完了)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(過去＆能受不明＆不可能＝未完了)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できる") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できると思います") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できると思う")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在＆能動＆可能)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在＆能動＆不可能)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しようと思います") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しようと思う" or
          check_text_terminated_string(rmv_edprtcl_rslt, "しよう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "したいと思います") or
          check_text_terminated_string(rmv_edprtcl_rslt, "したいと思う") or
          check_text_terminated_string(rmv_edprtcl_rslt, "したい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやりたいと思います") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやりたいと思う") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやります")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(未来＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しないと思う") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやらないと思います") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやらないと思う") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやらない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(未来＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "した") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやりました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやった")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(過去＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(過去進行＆能動＆否定)"      
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてます")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(過去進行＆受動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されていない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(過去進行＆受動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "された")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(過去完了＆受動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "でした") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だったです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だった")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(過去完了＆能受不明＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でなかった")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(過去完了＆能受不明＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していきたいと思います") or
           check_text_terminated_string(rmv_edprtcl_rslt, "していきたいと思う") or
           check_text_terminated_string(rmv_edprtcl_rslt, "していきたい") or
           check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたいと思います") or
           check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたいと思う") or
           check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたい")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在＆未来＆持続＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していきたいとは思わない") or
           check_text_terminated_string(rmv_edprtcl_rslt, "していきたいと思わない") or
           check_text_terminated_string(rmv_edprtcl_rslt, "していきたくない") or
           check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたいとは思わない") or
           check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたいと思わない") or
           check_text_terminated_string(rmv_edprtcl_rslt, "をやっていかない")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在＆未来＆持続＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でなかった")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "表明＆宣言(現在＆未来＆持続＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "です") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ます")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "紹介＆説明＆提示＆表明＆宣言(時制不明＆能受不明)"
    elif check_text_terminated_string(rmv_edprtcl_rslt, "ってました"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "紹介＆説明＆提示＆表明＆宣言(過去＆能動)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ですよね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だね")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "疑義＆質問"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しません")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "誘導＆勧誘"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "したい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "たい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "やりたい")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "欲求＆欲動"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "いいです")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "許可＆認可" 
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しないように") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないよう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "するな")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "制止＆禁止"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "してください") or
          check_text_terminated_string(rmv_edprtcl_rslt, "して")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "依頼＆要求"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しなさい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しろ")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "指示＆命令"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しなければならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなければ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないといけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないといけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃいけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "せにゃならん")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "強制＆勧告(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "してはならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してはいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "したらいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃならん")):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "強制＆勧告(否定)"
    elif check_text_terminated_string(rmv_edprtcl_rslt, "だ"):
            extrct_intnt_frm_shrt_and_blrplt_rslt = "顕示＆強調"
    else:
            extrct_intnt_frm_shrt_and_blrplt_rslt = "その他・不明"
    return extrct_intnt_frm_shrt_and_blrplt_rslt


#LINEメッセージの先頭・中間部分からコンテント(＝意図されるもの)を抽出する
def extract_content_from_top_and_middle(rmv_edprtcl_rslt):
    #メッセージの中に含まれる記号を除去して、メッセージの先頭・中間部分部分からコンテントを抽出して、これを呼出し元に引渡しをする
    if   check_text_terminated_string(rmv_edprtcl_rslt, "する"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(する)", "", rmv_edprtcl_rslt)
    elif check_text_terminated_string(rmv_edprtcl_rslt, "しない"):
           extrct_cntnt_frm_tp_and_mddl_rslt = re.sub("(しない)", "", rmv_edprtcl_rslt)
    else:
           extrct_cntnt_frm_tp_and_mddl_rslt = "その他・不明"
    return extrct_cntnt_frm_tp_and_mddl_rslt


#LINEの返信メッセージをインテントとコンテントから生成する
def line_msg_generate_from_intent_and_content(intnt, cntnt):
    #返信メッセージをインテントとコンテントから生成して、これを呼出し元に引渡しをする
    line_msg_gnrt_frm_intnt_and_cntnt_rslt = "test"
    return line_msg_gnrt_frm_intnt_and_cntnt_rslt
