# coding: utf-8




import re
from janome.tokenizer import Tokenizer




#ユーザーから送られるLINEメッセージが指定された文字列で開始するかを判定する
def check_text_start_string(line_msg_txt, str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で開始するかを判定する
    rmv_symbl_rslt        = remove_symbol(line_msg_txt)
    chk_txt_strt_str_rslt = rmv_symbl_rslt.startswith(str)
    return chk_txt_strt_str_rslt


#ユーザーから送られるLINEメッセージが指定された文字列で終結するかを判定する
def check_text_terminate_string(line_msg_txt, str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で終結するかを判定する
    rmv_symbl_rslt          = remove_symbol(line_msg_txt)
    chk_txt_trmntd_str_rslt = rmv_symbl_rslt.endswith(str)
    return chk_txt_trmntd_str_rslt


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


#ユーザーから送られるLINEメッセージの中に含まれるその他のもの(＝感情表現のためのもの)を除去する
def remove_etc(line_msg_txt):
    #メッセージの中に含まれるその他のものを除去する
    if   bool(re.search(r"怒$",      line_msg_txt)) == True:
         rmv_etc = re.sub(r"怒$", "", line_msg_txt)
    elif bool(re.search(r"泣$",      line_msg_txt)) == True:
         rmv_etc = re.sub(r"泣$", "", line_msg_txt)
    elif bool(re.search(r"汗$",      line_msg_txt)) == True:
         rmv_etc = re.sub(r"汗$", "", line_msg_txt)
    elif bool(re.search(r"爆$",      line_msg_txt)) == True:
         rmv_etc = re.sub(r"爆$", "", line_msg_txt)
    elif bool(re.search(r"(爆笑)$",  line_msg_txt)) == True:
         rmv_etc = re.sub(r"(爆笑)$", "", line_msg_txt)
    elif bool(re.search(r"笑+$",     line_msg_txt)) == True:
         rmv_etc = re.sub(r"笑+$", "", line_msg_txt)
    elif bool(re.search(r"(わら)+$", line_msg_txt)) == True:
         rmv_etc = re.sub(r"(わら)+$", "", line_msg_txt)
    elif bool(re.search(r"(ワラ)+$", line_msg_txt)) == True:
         rmv_etc = re.sub(r"(ワラ)+$", "", line_msg_txt)
    elif bool(re.search(r"草+$",     line_msg_txt)) == True:
         rmv_etc = re.sub(r"草+$", "", line_msg_txt)
    elif bool(re.search(r"(くさ)+$", line_msg_txt)) == True:
         rmv_etc = re.sub(r"(くさ)+$", "", line_msg_txt)
    elif bool(re.search(r"(クサ)+$", line_msg_txt)) == True:
         rmv_etc = re.sub(r"(クサ)+$", "", line_msg_txt)
    elif bool(re.search(r"w+$",      line_msg_txt)) == True:
         rmv_etc = re.sub(r"w+$", "", line_msg_txt)
    elif bool(re.search(r"W+$",      line_msg_txt)) == True:
         rmv_etc = re.sub(r"W+$", "", line_msg_txt)
    else:
         rmv_etc = line_msg_txt
    return rmv_etc


#ユーザーから送られるLINEメッセージの中に含まれる記号を除去する
def remove_symbol(line_msg_txt):
    #メッセージの中に含まれる各種の記号・空白を除去する
    rmv_symbl_rslt   = re.sub("(’)", "", line_msg_txt)
    rmv_symbl_rslt2  = re.sub("(”)", "", rmv_symbl_rslt)
    rmv_symbl_rslt3  = re.sub("(「)", "", rmv_symbl_rslt2)
    rmv_symbl_rslt4  = re.sub("(」)", "", rmv_symbl_rslt3)
    rmv_symbl_rslt5  = re.sub("(、)", "", rmv_symbl_rslt4)
    rmv_symbl_rslt6  = re.sub("(。)", "", rmv_symbl_rslt5)
    rmv_symbl_rslt7  = re.sub("(！)", "", rmv_symbl_rslt6)
    rmv_symbl_rslt8  = re.sub("(？)", "", rmv_symbl_rslt7)
    rmv_symbl_rslt9  = re.sub("(ー)", "", rmv_symbl_rslt8)
    rmv_symbl_rslt10 = re.sub("(～)", "", rmv_symbl_rslt9)
    rmv_symbl_rslt11 = re.sub("(・)", "", rmv_symbl_rslt10)
    rmv_symbl_rslt12 = re.sub("(＝)", "", rmv_symbl_rslt11)
    rmv_symbl_rslt13 = re.sub("(＆)", "", rmv_symbl_rslt12)
    rmv_symbl_rslt14 = re.sub("(＋)", "", rmv_symbl_rslt13)
    rmv_symbl_rslt15 = re.sub("( )",  "", rmv_symbl_rslt14)
    rmv_symbl_rslt16 = re.sub("(　)", "", rmv_symbl_rslt15)
    return rmv_symbl_rslt16


#ユーザーから送られるLINEメッセージの中に含まれる終助詞を除去する
def remove_endparticle(line_msg_txt):
    #メッセージの中に含まれる終助詞を除去する
    if   bool(re.search(r"よお$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"よお$", "", line_msg_txt)
    elif bool(re.search(r"よぉ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"よぉ$", "", line_msg_txt)
    elif bool(re.search(r"よっ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"よっ$", "", line_msg_txt)
    elif bool(re.search(r"よ$", line_msg_txt))   == True:
         rmv_edprtcl_rslt = re.sub(r"よ$",   "", line_msg_txt)
    elif bool(re.search(r"ねえ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"ねえ$", "", line_msg_txt)
    elif bool(re.search(r"ねぇ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"ねぇ$", "", line_msg_txt)
    elif bool(re.search(r"ねっ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"ねっ$", "", line_msg_txt)
    elif bool(re.search(r"ね$", line_msg_txt))   == True:
         rmv_edprtcl_rslt = re.sub(r"ね$",   "", line_msg_txt)
    elif bool(re.search(r"なあ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"なあ$", "", line_msg_txt)
    elif bool(re.search(r"なぁ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"なぁ$", "", line_msg_txt)
    elif bool(re.search(r"なっ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"なっ$", "", line_msg_txt)
    elif bool(re.search(r"な$", line_msg_txt))   == True:
         rmv_edprtcl_rslt = re.sub(r"な$",   "", line_msg_txt)
    elif bool(re.search(r"わあ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"わあ$", "", line_msg_txt)
    elif bool(re.search(r"わぁ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"わぁ$", "", line_msg_txt)
    elif bool(re.search(r"わっ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"わっ$", "", line_msg_txt)
    elif bool(re.search(r"わ$", line_msg_txt))   == True:
         rmv_edprtcl_rslt = re.sub(r"わ$",   "", line_msg_txt)
    elif bool(re.search(r"ぜえ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"ぜえ$", "", line_msg_txt)
    elif bool(re.search(r"ぜぇ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"ぜぇ$", "", line_msg_txt)
    elif bool(re.search(r"ぜっ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"ぜっ$", "", line_msg_txt)
    elif bool(re.search(r"ぜ$", line_msg_txt))   == True:
         rmv_edprtcl_rslt = re.sub(r"ぜ$",   "", line_msg_txt)
    elif bool(re.search(r"っすよ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"っすよ$",   "", line_msg_txt)
    elif bool(re.search(r"っすね$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"っすね$",   "", line_msg_txt)
    elif bool(re.search(r"でっす$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"でっす$",   "", line_msg_txt)
    elif bool(re.search(r"っす$", line_msg_txt))   == True:
         rmv_edprtcl_rslt = re.sub(r"っす$",     "", line_msg_txt)
    elif bool(re.search(r"わよ$", line_msg_txt))   == True:
         rmv_edprtcl_rslt = re.sub(r"わよ$",     "", line_msg_txt)
    elif bool(re.search(r"わよっ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"わよっ$",   "", line_msg_txt)
    elif bool(re.search(r"わね$", line_msg_txt)) ==   True:
         rmv_edprtcl_rslt = re.sub(r"わね$",     "", line_msg_txt)
    elif bool(re.search(r"わねっ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"わねっ$",   "", line_msg_txt)
    elif bool(re.search(r"ってね$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"ってね$",   "", line_msg_txt)
    elif bool(re.search(r"ってば$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"ってば$",   "", line_msg_txt)
    elif bool(re.search(r"ってばよ$", line_msg_txt)) == True:
         rmv_edprtcl_rslt = re.sub(r"ってばよ$", "", line_msg_txt)
    elif bool(re.search(r"っ$", line_msg_txt))       == True:
         rmv_edprtcl_rslt = re.sub(r"っ$",       "", line_msg_txt)
    elif bool(re.search(r"から$", line_msg_txt))     == True:
         rmv_edprtcl_rslt = re.sub(r"から$",     "", line_msg_txt)
    else:
         rmv_edprtcl_rslt = line_msg_txt
    return rmv_edprtcl_rslt


#ユーザーから送られるLINEメッセージがギャグ＆声帯模写だったとして、これからインテント(＝発話の意図するもの)を抽出する
def extract_intent_from_gag_and_vocalcordcopy(line_msg_txt):
    #ギャグ＆声帯模写＆その他となっているメッセージからインテントを抽出して、これを呼出し元に引渡しをする
    if   (line_msg_txt == "はい ひょっこりはん" or
          line_msg_txt == "はいひょっこりはん" or
          line_msg_txt == "プレゼント フォー 肩幅" or
          line_msg_txt == "プレゼントフォー肩幅" or
          line_msg_txt == "うぃーん合唱団" or
          line_msg_txt == "早く大人になれ 膝小僧" or
          line_msg_txt == "早く大人になれ膝小僧" or
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
          line_msg_txt == "武勇伝 武勇伝" or
          line_msg_txt == "武勇伝武勇伝" or
          line_msg_txt == "武勇伝！ 武勇伝！" or
          line_msg_txt == "武勇伝！武勇伝！" or
          line_msg_txt == "キミ カワイーね" or
          line_msg_txt == "キミカワイーね" or
          line_msg_txt == "キミ カワイーね！" or
          line_msg_txt == "キミカワイーね！" or
          line_msg_txt == "空前絶後" or
          line_msg_txt == "空 前 絶 後" or
          line_msg_txt == "空！ 前！ 絶！ 後！" or
          line_msg_txt == "空！前！絶！後！" or
          line_msg_txt == "空前絶後！"):
            extrct_intnt_from_gag_and_vclcrdcpy_rslt = "<モノマネ＆ギャグ＆一発芸 人物・キャラクターに基づいて>"
    elif (line_msg_txt == "にゃー にゃー" or
          line_msg_txt == "にゃーにゃー" or
          line_msg_txt == "ニャー ニャー" or
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
          line_msg_txt == "ギャン ギャン" or
          line_msg_txt == "ギャンギャン" or
          line_msg_txt == "ぎゃん" or
          line_msg_txt == "ギャン" or
          line_msg_txt == "うほ うほ" or         
          line_msg_txt == "うほうほ" or
          line_msg_txt == "ウホ ウホ" or
          line_msg_txt == "ウホウホ" or
          line_msg_txt == "うほ" or
          line_msg_txt == "ウホ" or
          line_msg_txt == "こけこっこー" or
          line_msg_txt == "コケコッコー" or
          line_msg_txt == "こけ" or
          line_msg_txt == "コケ" or
          line_msg_txt == "がお がおー" or
          line_msg_txt == "がおがおー" or
          line_msg_txt == "ガオ ガオー" or
          line_msg_txt == "ガオガオー" or
          line_msg_txt == "がおー" or
          line_msg_txt == "ガオー" or
          line_msg_txt == "ぶひ ぶひ" or
          line_msg_txt == "ぶひぶひ" or
          line_msg_txt == "ブヒ ブヒ" or
          line_msg_txt == "ブヒブヒ" or
          line_msg_txt == "ぶひ" or
          line_msg_txt == "ブヒ" or
          line_msg_txt == "ちゅん ちゅん" or
          line_msg_txt == "ちゅんちゅん" or
          line_msg_txt == "チュン チュン" or
          line_msg_txt == "チュンチュン" or
          line_msg_txt == "ちゅん" or
          line_msg_txt == "チュン" or
          line_msg_txt == "げろ げろ" or
          line_msg_txt == "げろげろ" or
          line_msg_txt == "ゲロ ゲロ" or
          line_msg_txt == "ゲロゲロ" or
          line_msg_txt == "げろ" or
          line_msg_txt == "ゲロ" or
          line_msg_txt == "げこ げこ" or
          line_msg_txt == "げこげこ" or
          line_msg_txt == "ゲコ ゲコ" or
          line_msg_txt == "ゲコゲコ" or
          line_msg_txt == "げこ" or
          line_msg_txt == "ゲコ" or
          line_msg_txt == "ぶー ぶー" or
          line_msg_txt == "ぶーぶー" or
          line_msg_txt == "ブー ブー" or
          line_msg_txt == "ブーブー" or
          line_msg_txt == "がったん ごっとん" or
          line_msg_txt == "がったんごっとん" or
          line_msg_txt == "ガッタン ゴットン" or
          line_msg_txt == "ガッタンゴットン"):
            extrct_intnt_from_gag_and_vclcrdcpy_rslt = "<モノマネ＆声帯模写 モノ・動物に基づいて>"
    elif (line_msg_txt == "ぷー" or
          line_msg_txt == "プー" or
          line_msg_txt == "ぷ～" or
          line_msg_txt == "プ～" or
          line_msg_txt == "ぶりぶり" or
          line_msg_txt == "ブリブリ" or
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
          line_msg_txt == "へぶし" or
          line_msg_txt == "ヘブシ" or
          line_msg_txt == "へぶしっ" or
          line_msg_txt == "ヘブシッ" or
          line_msg_txt == "はっくしょん" or
          line_msg_txt == "ハックション"):
            extrct_intnt_from_gag_and_vclcrdcpy_rslt = "<生理現象に伴う音>"
    elif (line_msg_txt == "おい" or
          line_msg_txt == "ねぇ" or
          line_msg_txt == "なあ" or
          line_msg_txt == "なぁ" or
          line_msg_txt == "なあ？" or
          line_msg_txt == "なぁ？" or
          line_msg_txt == "なあ！" or
          line_msg_txt == "なぁ！"):
            extrct_intnt_from_gag_and_vclcrdcpy_rslt = "<呼掛け＆問掛け>"      
    elif (line_msg_txt == "あのー" or
          line_msg_txt == "あの～" or
          line_msg_txt == "あー" or
          line_msg_txt == "あ～" or
          line_msg_txt == "えーと" or
          line_msg_txt == "え～と" or
          line_msg_txt == "えー" or
          line_msg_txt == "え～" or
          line_msg_txt == "うーん" or
          line_msg_txt == "う～ん" or
          line_msg_txt == "うー" or
          line_msg_txt == "う～"):
            extrct_intnt_from_gag_and_vclcrdcpy_rslt = "<フィラー 間の引き延ばし>"
    elif (line_msg_txt == "ブー ブー" or
          line_msg_txt == "ブーブー" or
          line_msg_txt == "ブー！ ブー！" or
          line_msg_txt == "ブー！ブー！"):
            extrct_intnt_from_gag_and_vclcrdcpy_rslt = "<ブーイング>"
    elif (line_msg_txt == "海" or
          line_msg_txt == "うみ" or
          line_msg_txt == "海！" or
          line_msg_txt == "うみ！" or
          line_msg_txt == "セイ イェーイ" or
          line_msg_txt == "セイイェーイ" or
          line_msg_txt == "セイ イェーイ！" or
          line_msg_txt == "セイイェーイ！"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<掛合い＆コールアンドレスポンス>"
    else:
            extrct_intnt_from_gag_and_vclcrdcpy_rslt = "<その他・不明>"
    return extrct_intnt_from_gag_and_vclcrdcpy_rslt


#LINEメッセージが短文＆定型文だったとして、これからインテント(＝発話の意図するもの)を抽出する
def extract_intent_from_short_and_boilerplate(line_msg_txt):
    #短文＆定型文となっているメッセージからインテントを抽出して、これを呼出し元に引渡しをする
    if   (line_msg_txt == "おはよう御座います" or
          line_msg_txt == "おはようございます" or
          line_msg_txt == "おはよう" or
          line_msg_txt == "おはっす" or
          line_msg_txt == "おは" or
          line_msg_txt == "こんにちは" or
          line_msg_txt == "こんにちわ" or
          line_msg_txt == "ちはっす" or
          line_msg_txt == "ちわっす" or
          line_msg_txt == "こんばんは" or
          line_msg_txt == "こんばんわ" or
          line_msg_txt == "ばんわ" or
          line_msg_txt == "ばんは" or
          line_msg_txt == "ばんっす" or
          line_msg_txt == "ばん" or
          line_msg_txt == "やあ" or
          line_msg_txt == "どうも" or
          line_msg_txt == "御免遊ばせ" or
          line_msg_txt == "御免あそばせ" or
          line_msg_txt == "ごめん遊ばせ" or
          line_msg_txt == "ごめんあそばせ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<挨拶>"
    elif (line_msg_txt == "流石ですね" or
          line_msg_txt == "流石です" or
          line_msg_txt == "流石ね" or
          line_msg_txt == "流石" or
          line_msg_txt == "さすがですね" or
          line_msg_txt == "さすがです" or
          line_msg_txt == "さすがね" or
          line_msg_txt == "さすが" or
          line_msg_txt == "凄いですね" or
          line_msg_txt == "凄いです" or
          line_msg_txt == "凄いね" or
          line_msg_txt == "凄い" or
          line_msg_txt == "すごいですね" or
          line_msg_txt == "すごいです" or
          line_msg_txt == "すごいね" or
          line_msg_txt == "すごい" or
          line_msg_txt == "素晴らしいですね" or
          line_msg_txt == "すばらしいですね" or
          line_msg_txt == "素晴らしいです" or
          line_msg_txt == "すばらしいです" or
          line_msg_txt == "素晴らしい" or
          line_msg_txt == "すばらしい" or
          line_msg_txt == "賢いですね" or
          line_msg_txt == "賢いです" or
          line_msg_txt == "賢いね" or
          line_msg_txt == "賢い" or
          line_msg_txt == "偉いですね" or
          line_msg_txt == "偉いです" or
          line_msg_txt == "偉いね" or
          line_msg_txt == "偉い" or
          line_msg_txt == "エラいですね" or
          line_msg_txt == "エラいです" or
          line_msg_txt == "エラいね" or
          line_msg_txt == "エラい" or
          line_msg_txt == "立派ですね" or
          line_msg_txt == "立派です" or
          line_msg_txt == "立派ね" or
          line_msg_txt == "立派" or
          line_msg_txt == "感服しました" or
          line_msg_txt == "感服したわ" or
          line_msg_txt == "感服した" or
          line_msg_txt == "敬服いたします" or
          line_msg_txt == "敬服しますわ" or
          line_msg_txt == "敬服します" or
          line_msg_txt == "感動しました" or
          line_msg_txt == "感動したわ" or
          line_msg_txt == "感動した" or
          line_msg_txt == "かっこいいですね" or
          line_msg_txt == "カッコいいですね" or
          line_msg_txt == "カッコイイですね" or
          line_msg_txt == "かっこいいです" or
          line_msg_txt == "カッコいいです" or
          line_msg_txt == "カッコイイです" or
          line_msg_txt == "かっこいいわね" or
          line_msg_txt == "カッコいいわね" or
          line_msg_txt == "カッコイイわね" or
          line_msg_txt == "かっこいい" or
          line_msg_txt == "カッコいい" or
          line_msg_txt == "カッコイイ" or
          line_msg_txt == "可愛いですね" or
          line_msg_txt == "かわいいですね" or
          line_msg_txt == "カワイいですね" or
          line_msg_txt == "カワイイですね" or
          line_msg_txt == "可愛いです" or
          line_msg_txt == "かわいいです" or
          line_msg_txt == "カワイいです" or
          line_msg_txt == "カワイイです" or
          line_msg_txt == "可愛いわね" or
          line_msg_txt == "かわいいわね" or
          line_msg_txt == "カワイいわね" or
          line_msg_txt == "カワイイわね" or
          line_msg_txt == "可愛いね" or
          line_msg_txt == "かわいいね" or
          line_msg_txt == "カワイいね" or
          line_msg_txt == "カワイイね" or
          line_msg_txt == "可愛い" or
          line_msg_txt == "かわいい" or
          line_msg_txt == "カワイい" or
          line_msg_txt == "カワイイ" or
          line_msg_txt == "かわい" or
          line_msg_txt == "カワイ" or
          line_msg_txt == "かわゆす" or
          line_msg_txt == "カワゆす" or
          line_msg_txt == "カワユス" or
          line_msg_txt == "美しいですね" or
          line_msg_txt == "うつくしいですね" or
          line_msg_txt == "美しいです" or
          line_msg_txt == "うつくしいです" or
          line_msg_txt == "美しいわね" or
          line_msg_txt == "うつくしいわね" or
          line_msg_txt == "美しいわ" or
          line_msg_txt == "うつくしいわ" or
          line_msg_txt == "美しい" or
          line_msg_txt == "うつくしい" or
          line_msg_txt == "綺麗ですね" or
          line_msg_txt == "きれいですね" or
          line_msg_txt == "キレいですね" or
          line_msg_txt == "キレイですね" or
          line_msg_txt == "綺麗だわ" or
          line_msg_txt == "きれいだわ" or
          line_msg_txt == "キレいだわ" or
          line_msg_txt == "キレイだわ" or
          line_msg_txt == "綺麗だ" or
          line_msg_txt == "きれいだ" or
          line_msg_txt == "キレいだ" or
          line_msg_txt == "キレイだ" or
          line_msg_txt == "綺麗ね" or
          line_msg_txt == "きれいね" or
          line_msg_txt == "キレいね" or
          line_msg_txt == "キレイね" or
          line_msg_txt == "綺麗" or
          line_msg_txt == "きれい" or
          line_msg_txt == "キレい" or
          line_msg_txt == "キレイ" or
          line_msg_txt == "いけてるよ" or
          line_msg_txt == "イケてるよ" or
          line_msg_txt == "イケテルよ" or
          line_msg_txt == "いけてるね" or
          line_msg_txt == "イケてるね" or
          line_msg_txt == "イケテルね" or
          line_msg_txt == "いけてるな" or
          line_msg_txt == "イケてるな" or
          line_msg_txt == "イケテルな" or
          line_msg_txt == "いけてるわ" or
          line_msg_txt == "イケてるわ" or
          line_msg_txt == "イケテルわ" or
          line_msg_txt == "いけてる" or
          line_msg_txt == "イケてる" or
          line_msg_txt == "イケテル" or
          line_msg_txt == "素敵ですよ" or
          line_msg_txt == "すてきですよ" or
          line_msg_txt == "ステキですよ" or
          line_msg_txt == "素敵ですね" or
          line_msg_txt == "すてきですね" or
          line_msg_txt == "ステキですね" or
          line_msg_txt == "素敵です" or
          line_msg_txt == "すてきです" or
          line_msg_txt == "ステキです" or
          line_msg_txt == "素敵だわ" or
          line_msg_txt == "すてきだわ" or
          line_msg_txt == "ステキだわ" or
          line_msg_txt == "素敵よ" or
          line_msg_txt == "すてきよ" or
          line_msg_txt == "ステキよ" or
          line_msg_txt == "素敵ね" or
          line_msg_txt == "すてきね" or
          line_msg_txt == "ステキね" or
          line_msg_txt == "素敵" or
          line_msg_txt == "すてき" or
          line_msg_txt == "ステキ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<称賛＆礼賛>"
    elif (line_msg_txt == "この変態め" or
          line_msg_txt == "このへんたいめ" or
          line_msg_txt == "このヘンタイめ" or
          line_msg_txt == "この変態が" or
          line_msg_txt == "このへんたいが" or
          line_msg_txt == "このヘンタイが" or
          line_msg_txt == "変態め" or
          line_msg_txt == "へんたいめ" or
          line_msg_txt == "ヘンタイめ" or
          line_msg_txt == "変態が" or
          line_msg_txt == "へんたいが" or
          line_msg_txt == "ヘンタイが" or
          line_msg_txt == "変態ですね" or
          line_msg_txt == "へんたいですね" or
          line_msg_txt == "ヘンタイですね" or
          line_msg_txt == "変態だわ" or
          line_msg_txt == "へんたいだわ" or
          line_msg_txt == "ヘンタイだわ" or
          line_msg_txt == "変態ね" or
          line_msg_txt == "へんたいね" or
          line_msg_txt == "ヘンタイね" or
          line_msg_txt == "変態" or
          line_msg_txt == "へんたい" or
          line_msg_txt == "ヘンタイ" or
          line_msg_txt == "このぶすめ" or
          line_msg_txt == "このブスめ" or
          line_msg_txt == "この不細工め" or
          line_msg_txt == "このぶさいくめ" or
          line_msg_txt == "このブサイクめ" or
          line_msg_txt == "このぶすが" or
          line_msg_txt == "このブスが" or
          line_msg_txt == "この不細工が" or
          line_msg_txt == "このぶさいくが" or
          line_msg_txt == "このブサイクが" or
          line_msg_txt == "ぶすめ" or
          line_msg_txt == "ブスめ" or
          line_msg_txt == "不細工め" or
          line_msg_txt == "ぶさいくめ" or
          line_msg_txt == "ブサイクめ" or
          line_msg_txt == "ぶすが" or
          line_msg_txt == "ブスが" or
          line_msg_txt == "不細工が" or
          line_msg_txt == "ぶさいくが" or
          line_msg_txt == "ブサイクが" or
          line_msg_txt == "ぶすですね" or
          line_msg_txt == "ブスですね" or
          line_msg_txt == "不細工ですね" or
          line_msg_txt == "ぶさいくですね" or
          line_msg_txt == "ブサイクですね" or
          line_msg_txt == "ぶすだわ" or
          line_msg_txt == "ブスだわ" or
          line_msg_txt == "不細工だわ" or
          line_msg_txt == "ぶさいくだわ" or
          line_msg_txt == "ブサイクだわ" or
          line_msg_txt == "ぶすね" or
          line_msg_txt == "ブスね" or
          line_msg_txt == "不細工ね" or
          line_msg_txt == "ぶさいくね" or
          line_msg_txt == "ブサイクね" or
          line_msg_txt == "ぶす" or
          line_msg_txt == "ブス" or
          line_msg_txt == "不細工" or
          line_msg_txt == "ぶさいく" or
          line_msg_txt == "ブサイク" or
          line_msg_txt == "最低ですね" or
          line_msg_txt == "さいていですね" or
          line_msg_txt == "サイテーですね" or
          line_msg_txt == "最低だね" or
          line_msg_txt == "さいていだね" or
          line_msg_txt == "サイテーだね" or
          line_msg_txt == "最低だな" or
          line_msg_txt == "さいていだな" or
          line_msg_txt == "サイテーだな" or
          line_msg_txt == "最低だわ" or
          line_msg_txt == "さいていだわ" or
          line_msg_txt == "サイテーだわ" or
          line_msg_txt == "最低よ" or
          line_msg_txt == "さいていよ" or
          line_msg_txt == "サイテーよ" or
          line_msg_txt == "最低ね" or
          line_msg_txt == "さいていね" or
          line_msg_txt == "サイテーね" or
          line_msg_txt == "最低" or
          line_msg_txt == "さいてい" or
          line_msg_txt == "サイテー" or
          line_msg_txt == "この無能野郎め" or
          line_msg_txt == "この無能やろうめ" or
          line_msg_txt == "この無能ヤロウめ" or
          line_msg_txt == "この無能ヤローめ" or
          line_msg_txt == "この無能め" or
          line_msg_txt == "この無能野郎が" or
          line_msg_txt == "この無能やろうが" or
          line_msg_txt == "この無能ヤロウが" or
          line_msg_txt == "この無能ヤローが" or
          line_msg_txt == "無能野郎め" or
          line_msg_txt == "無能やろうめ" or
          line_msg_txt == "無能ヤロウめ" or
          line_msg_txt == "無能ヤローめ" or
          line_msg_txt == "無能め" or
          line_msg_txt == "無能野郎が" or
          line_msg_txt == "無能やろうが" or
          line_msg_txt == "無能ヤロウが" or
          line_msg_txt == "無能ヤローが" or
          line_msg_txt == "無能ですね" or
          line_msg_txt == "無能だね" or
          line_msg_txt == "無能だわ" or
          line_msg_txt == "無能よ" or
          line_msg_txt == "無能ね" or
          line_msg_txt == "無能" or
          line_msg_txt == "この馬鹿野郎め" or
          line_msg_txt == "このばか野郎め" or
          line_msg_txt == "このバカ野郎め" or
          line_msg_txt == "この馬鹿やろうめ" or
          line_msg_txt == "このばかやろうめ" or
          line_msg_txt == "このバカやろうめ" or
          line_msg_txt == "この馬鹿ヤロウめ" or
          line_msg_txt == "この馬鹿ヤローめ" or
          line_msg_txt == "この馬鹿野郎が" or
          line_msg_txt == "このばか野郎が" or
          line_msg_txt == "このバカ野郎が" or
          line_msg_txt == "この馬鹿やろうが" or
          line_msg_txt == "このばかやろうが" or
          line_msg_txt == "このバカやろうが" or
          line_msg_txt == "この馬鹿ヤロウが" or
          line_msg_txt == "この馬鹿ヤロが" or
          line_msg_txt == "このばかヤロウが" or
          line_msg_txt == "このばかヤローが" or
          line_msg_txt == "この馬鹿野郎" or
          line_msg_txt == "このばか野郎" or
          line_msg_txt == "このバカ野郎" or
          line_msg_txt == "この馬鹿やろう" or
          line_msg_txt == "このばかやろう" or
          line_msg_txt == "このバカやろう" or
          line_msg_txt == "この馬鹿ヤロウ" or
          line_msg_txt == "この馬鹿ヤロー" or
          line_msg_txt == "このばかヤロウ" or
          line_msg_txt == "このばかヤロー" or
          line_msg_txt == "このバカヤロウ" or
          line_msg_txt == "このバカヤロー" or
          line_msg_txt == "馬鹿野郎ですね" or
          line_msg_txt == "ばか野郎ですね" or
          line_msg_txt == "バカ野郎ですね" or
          line_msg_txt == "馬鹿やろうですね" or
          line_msg_txt == "ばかやろうですね" or
          line_msg_txt == "バカやろうですね" or
          line_msg_txt == "馬鹿ヤロウですね" or
          line_msg_txt == "馬鹿ヤローですね" or
          line_msg_txt == "ばかヤロウですね" or
          line_msg_txt == "ばかヤロですね" or
          line_msg_txt == "バカヤロウですね" or
          line_msg_txt == "バカヤローですね" or
          line_msg_txt == "馬鹿野郎" or
          line_msg_txt == "ばか野郎" or
          line_msg_txt == "バカ野郎" or
          line_msg_txt == "馬鹿やろう" or
          line_msg_txt == "ばかやろう" or
          line_msg_txt == "バカやろう" or
          line_msg_txt == "馬鹿ヤロウ" or
          line_msg_txt == "ばかヤロウ" or
          line_msg_txt == "バカヤロウ" or
          line_msg_txt == "バカヤロー" or
          line_msg_txt == "馬鹿だわ" or
          line_msg_txt == "ばかだわ" or
          line_msg_txt == "バカだわ" or
          line_msg_txt == "馬鹿ね" or
          line_msg_txt == "ばかね" or
          line_msg_txt == "バカね" or
          line_msg_txt == "馬鹿め" or
          line_msg_txt == "ばかめ" or
          line_msg_txt == "バカめ" or
          line_msg_txt == "馬鹿が" or
          line_msg_txt == "ばかが" or
          line_msg_txt == "バカが" or
          line_msg_txt == "馬鹿" or
          line_msg_txt == "ばか" or
          line_msg_txt == "バカ" or
          line_msg_txt == "あほですね" or
          line_msg_txt == "アホですね" or
          line_msg_txt == "あほだね" or
          line_msg_txt == "アホだね" or
          line_msg_txt == "あほだわ" or
          line_msg_txt == "アホだわ" or
          line_msg_txt == "あほね" or
          line_msg_txt == "アホね" or
          line_msg_txt == "あほ" or
          line_msg_txt == "アホ" or
          line_msg_txt == "このあほ垂れ" or
          line_msg_txt == "このアホ垂れ" or
          line_msg_txt == "あほ垂れ" or
          line_msg_txt == "アホ垂れ" or
          line_msg_txt == "このあほたれ" or
          line_msg_txt == "このアホたれ" or
          line_msg_txt == "あほたれ" or
          line_msg_txt == "アホたれ" or
          line_msg_txt == "このあほタレ" or
          line_msg_txt == "このアホタレ" or
          line_msg_txt == "あほタレ" or
          line_msg_txt == "アホタレ" or
          line_msg_txt == "このくず野郎め" or
          line_msg_txt == "このくずやろうめ" or
          line_msg_txt == "このくずヤロウめ" or
          line_msg_txt == "このくずヤローめ" or
          line_msg_txt == "このクズ野郎め" or
          line_msg_txt == "このクズやろうめ" or
          line_msg_txt == "このクズヤロウめ" or
          line_msg_txt == "このクズヤローめ" or
          line_msg_txt == "このくず野郎が" or
          line_msg_txt == "このくずやろうが" or
          line_msg_txt == "このくずヤロウが" or
          line_msg_txt == "このくずヤローが" or
          line_msg_txt == "このクズ野郎が" or
          line_msg_txt == "このクズやろうが" or
          line_msg_txt == "このクズヤロウが" or
          line_msg_txt == "このクズヤローが" or
          line_msg_txt == "くず野郎め" or
          line_msg_txt == "くずやろうめ" or
          line_msg_txt == "くずヤロウめ" or
          line_msg_txt == "くずヤローめ" or
          line_msg_txt == "クズ野郎め" or
          line_msg_txt == "クズやろうめ" or
          line_msg_txt == "クズヤロウめ" or
          line_msg_txt == "クズヤローめ" or
          line_msg_txt == "くず野郎が" or
          line_msg_txt == "くずやろうが" or
          line_msg_txt == "くずヤロウが" or
          line_msg_txt == "くずヤロが" or
          line_msg_txt == "クズ野郎が" or
          line_msg_txt == "クズやろうが" or
          line_msg_txt == "クズヤロウが" or
          line_msg_txt == "クズヤローが" or
          line_msg_txt == "このくず" or
          line_msg_txt == "このクズ" or
          line_msg_txt == "くず" or
          line_msg_txt == "クズ" or
          line_msg_txt == "このかす野郎め" or
          line_msg_txt == "このかすやろうめ" or
          line_msg_txt == "このかすヤロウめ" or
          line_msg_txt == "このかすヤローめ" or
          line_msg_txt == "このカス野郎め" or
          line_msg_txt == "このカスやろうめ" or
          line_msg_txt == "このカスヤロウめ" or
          line_msg_txt == "このカスヤローめ" or
          line_msg_txt == "このかす野郎が" or
          line_msg_txt == "このかすやろうが" or
          line_msg_txt == "このかすヤロウが" or
          line_msg_txt == "このかすヤローが" or
          line_msg_txt == "このカス野郎が" or
          line_msg_txt == "このカスやろうが" or
          line_msg_txt == "このカスヤロウが" or
          line_msg_txt == "このカスヤローが" or
          line_msg_txt == "かす野郎め" or
          line_msg_txt == "かすやろうめ" or
          line_msg_txt == "かすヤロウめ" or
          line_msg_txt == "かすヤローめ" or
          line_msg_txt == "カス野郎め" or
          line_msg_txt == "カスやろうめ" or
          line_msg_txt == "カスヤロウめ" or
          line_msg_txt == "カスヤローめ" or
          line_msg_txt == "かす野郎が" or
          line_msg_txt == "かすやろうが" or
          line_msg_txt == "かすヤロウが" or
          line_msg_txt == "かすヤローが" or
          line_msg_txt == "カス野郎が" or
          line_msg_txt == "カスやろうが" or
          line_msg_txt == "カスヤロウが" or
          line_msg_txt == "カスヤローが" or
          line_msg_txt == "このかす" or
          line_msg_txt == "このカス" or
          line_msg_txt == "かす" or
          line_msg_txt == "カス" or
          line_msg_txt == "このごみ野郎め" or
          line_msg_txt == "このごみやろうめ" or
          line_msg_txt == "このごみヤロウめ" or
          line_msg_txt == "このごみヤローめ" or
          line_msg_txt == "このゴミ野郎め" or
          line_msg_txt == "このゴミやろうめ" or
          line_msg_txt == "このゴミヤロウめ" or
          line_msg_txt == "このゴミヤローめ" or
          line_msg_txt == "このかす野郎が" or
          line_msg_txt == "このかすやろうが" or
          line_msg_txt == "このかすヤロウが" or
          line_msg_txt == "このかすヤローが" or
          line_msg_txt == "このゴミ野郎が" or
          line_msg_txt == "このゴミやろうが" or
          line_msg_txt == "このゴミヤロウが" or
          line_msg_txt == "このゴミヤローが" or
          line_msg_txt == "ごみ野郎め" or
          line_msg_txt == "ごみやろうめ" or
          line_msg_txt == "ごみヤロウめ" or
          line_msg_txt == "ごみヤローめ" or
          line_msg_txt == "ゴミ野郎め" or
          line_msg_txt == "ゴミやろうめ" or
          line_msg_txt == "ゴミヤロウめ" or
          line_msg_txt == "ゴミヤローめ" or
          line_msg_txt == "かす野郎が" or
          line_msg_txt == "かすやろうが" or
          line_msg_txt == "かすヤロウが" or
          line_msg_txt == "かすヤローが" or
          line_msg_txt == "ゴミ野郎が" or
          line_msg_txt == "ゴミやろうが" or
          line_msg_txt == "ゴミヤロウが" or
          line_msg_txt == "ゴミヤローが" or
          line_msg_txt == "このごみ" or
          line_msg_txt == "このゴミ" or
          line_msg_txt == "ごみ" or
          line_msg_txt == "ゴミ" or
          line_msg_txt == "このげす野郎め" or
          line_msg_txt == "このげすやろうめ" or
          line_msg_txt == "このげすヤロウめ" or
          line_msg_txt == "このげすヤローめ" or
          line_msg_txt == "このゲス野郎め" or
          line_msg_txt == "このゲスやろうめ" or
          line_msg_txt == "このゲスヤロウめ" or
          line_msg_txt == "このゲスヤローめ" or
          line_msg_txt == "このげす野郎が" or
          line_msg_txt == "このげすやろうが" or
          line_msg_txt == "このげすヤロウが" or
          line_msg_txt == "このげすヤローが" or
          line_msg_txt == "このゲス野郎が" or
          line_msg_txt == "このゲスやろうが" or
          line_msg_txt == "このゲスヤロウが" or
          line_msg_txt == "このゲスヤローが" or
          line_msg_txt == "このげす" or
          line_msg_txt == "このゲス" or
          line_msg_txt == "げす" or
          line_msg_txt == "ゲス"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<罵倒＆貶め>"
    elif (line_msg_txt == "消えてください" or
          line_msg_txt == "消えて" or
          line_msg_txt == "消えな" or
          line_msg_txt == "消え失せろ" or
          line_msg_txt == "消えうせろ" or
          line_msg_txt == "消えろ" or
          line_msg_txt == "死んでください" or
          line_msg_txt == "氏んでください" or
          line_msg_txt == "しんでください" or
          line_msg_txt == "死んで" or
          line_msg_txt == "氏んで" or
          line_msg_txt == "しんで" or
          line_msg_txt == "死ね" or
          line_msg_txt == "氏ね" or
          line_msg_txt == "しね" or
          line_msg_txt == "死になさい" or
          line_msg_txt == "氏になさい" or
          line_msg_txt == "しになさい" or
          line_msg_txt == "死にな" or
          line_msg_txt == "氏にな" or
          line_msg_txt == "しにな" or
          line_msg_txt == "死んでろ" or
          line_msg_txt == "氏んでろ" or
          line_msg_txt == "しんでろ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<人格・存在の否定>"
    elif (line_msg_txt == "大天才ですか" or
          line_msg_txt == "天才ですか" or
          line_msg_txt == "大秀才ですか" or
          line_msg_txt == "秀才ですか" or
          line_msg_txt == "優秀ですか"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<称賛＆礼賛 半疑問>"
    elif (line_msg_txt == "無能ですか" or
          line_msg_txt == "ばかですか" or
          line_msg_txt == "バカですか" or
          line_msg_txt == "あほですか" or
          line_msg_txt == "アホですか" or
          line_msg_txt == "くずですか" or
          line_msg_txt == "クズですか" or
          line_msg_txt == "かすですか" or
          line_msg_txt == "カスですか" or
          line_msg_txt == "ごみですか" or
          line_msg_txt == "ゴミですか"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<罵詈＆罵倒 半疑問>"
    elif (line_msg_txt == "何をしていますか" or
          line_msg_txt == "なにをしていますか" or
          line_msg_txt == "何をしてますか" or
          line_msg_txt == "なにをしてますか" or
          line_msg_txt == "何してますか" or
          line_msg_txt == "なにしてますか" or
          line_msg_txt == "何してるの" or
          line_msg_txt == "なにしてるの" or
          line_msg_txt == "どうしていますか" or
          line_msg_txt == "どうしてますか" or
          line_msg_txt == "どうしてる"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 現在 状態・状況について>"
    elif (line_msg_txt == "何をしてきましたか" or
          line_msg_txt == "なにをしてきましたか" or
          line_msg_txt == "何をしてましたか" or
          line_msg_txt == "なにをしてましたか" or
          line_msg_txt == "何してましたか" or
          line_msg_txt == "なにしてましたか" or
          line_msg_txt == "何してたの" or
          line_msg_txt == "なにしてたの" or
          line_msg_txt == "何してた" or
          line_msg_txt == "なにしてた" or
          line_msg_txt == "どうしてきましたか" or
          line_msg_txt == "どうしてましたか" or
          line_msg_txt == "どうしてた"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 過去 状態・状況について>"
    elif (line_msg_txt == "何をしたいですか" or
          line_msg_txt == "なにをしたいですか" or
          line_msg_txt == "何がしたいですか" or
          line_msg_txt == "なにがしたいですか" or
          line_msg_txt == "何したいですか" or
          line_msg_txt == "なにしたいですか" or
          line_msg_txt == "何したいの" or
          line_msg_txt == "なにしたいの" or
          line_msg_txt == "何したい" or
          line_msg_txt == "なにしたい" or
          line_msg_txt == "何をしますか" or
          line_msg_txt == "なにをしますか" or
          line_msg_txt == "何しますか" or
          line_msg_txt == "なにしますか" or
          line_msg_txt == "なにします"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 現在 願望・欲求について>"
    elif (line_msg_txt == "何をしたかったのですか" or
          line_msg_txt == "なにをしたかったのですか" or
          line_msg_txt == "何をしたかったんですか" or
          line_msg_txt == "なにをしたかったんですか" or
          line_msg_txt == "何がしたかったのですか" or
          line_msg_txt == "なにがしたかったのですか" or
          line_msg_txt == "何がしたかったんですか" or
          line_msg_txt == "なにがしたかったんですか" or
          line_msg_txt == "何したかったのですか" or
          line_msg_txt == "なにしたかったのですか" or
          line_msg_txt == "何したかったんですか" or
          line_msg_txt == "なにしたかったんですか" or
          line_msg_txt == "何したかったの" or
          line_msg_txt == "なにしたかったの"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 過去 願望・欲求について>"
    elif (line_msg_txt == "何をしていきたいのですか" or
          line_msg_txt == "なにをしていきたいのですか" or
          line_msg_txt == "何をしていきたいですか" or
          line_msg_txt == "なにをしていきたいですか" or
          line_msg_txt == "何をしていきたいの" or
          line_msg_txt == "なにをしていきたいの" or
          line_msg_txt == "何がしていきたいのですか" or
          line_msg_txt == "なにがしていきたいのですか" or
          line_msg_txt == "何がしていきたいですか" or
          line_msg_txt == "なにがしていきたいですか" or
          line_msg_txt == "何していきたいのですか" or
          line_msg_txt == "なにしていきたいのですか" or
          line_msg_txt == "何していきたいんですか" or
          line_msg_txt == "なにしていきたいんですか" or
          line_msg_txt == "何していきたいですか" or
          line_msg_txt == "なにしていきたいですか" or
          line_msg_txt == "何していきたいの" or
          line_msg_txt == "なにしていきたいの" or
          line_msg_txt == "何していきたい" or
          line_msg_txt == "なにしていきたい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 未来 願望・欲求について>"
    elif (line_msg_txt == "どうしたいのですか" or
          line_msg_txt == "どうしたいんですか" or
          line_msg_txt == "どうしたいですか" or
          line_msg_txt == "どうしたいのかな" or
          line_msg_txt == "どうしたいの" or
          line_msg_txt == "どうしたい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 現在 願望・欲求について 漠然とした様子・様相>"
    elif (line_msg_txt == "どうしたかったのですか" or
          line_msg_txt == "どうしたかったんですか" or
          line_msg_txt == "どうしたかったの" or
          line_msg_txt == "どうしたかった"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 過去 願望・欲求について 漠然とした様子・様相>"
    elif (line_msg_txt == "どうしていきたいのですか" or
          line_msg_txt == "どうしていきたいんですか" or
          line_msg_txt == "どうしていきたいの" or
          line_msg_txt == "どうしていきたい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 未来 願望・欲求について 漠然とした様子・様相>"
    elif (line_msg_txt == "どうなのですか" or
          line_msg_txt == "どうなんですか" or
          line_msg_txt == "どうなの" or
          line_msg_txt == "どうなん"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 意図・目的について>"
    elif line_msg_txt == "どう":
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 感想・感慨について>"
    elif (line_msg_txt == "どうしてなのですか" or
          line_msg_txt == "どうしてなんですか" or
          line_msg_txt == "どうしてですか" or
          line_msg_txt == "どうして"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 理由・事情について>"      
    elif (line_msg_txt == "何故なのですか" or
          line_msg_txt == "なぜなのですか" or
          line_msg_txt == "何故なんですか" or
          line_msg_txt == "なぜなんですか" or
          line_msg_txt == "何故ですか" or
          line_msg_txt == "なぜですか" or
          line_msg_txt == "何故" or
          line_msg_txt == "なぜ" or
          line_msg_txt == "何で" or
          line_msg_txt == "なんで"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 理由・事情について>"
    elif (line_msg_txt == "良いです" or
          line_msg_txt == "よいです" or
          line_msg_txt == "いいです" or
          line_msg_txt == "良い" or
          line_msg_txt == "いい" or
          line_msg_txt == "おっけー" or
          line_msg_txt == "オッケー" or
          line_msg_txt == "おけ" or
          line_msg_txt == "オケ" or
          line_msg_txt == "OK"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<許容＆許可>"
    elif (line_msg_txt == "駄目です" or
          line_msg_txt == "だめです" or
          line_msg_txt == "ダメです" or
          line_msg_txt == "駄目だ" or
          line_msg_txt == "だめだ" or
          line_msg_txt == "ダメだ" or
          line_msg_txt == "駄目" or
          line_msg_txt == "だめ" or
          line_msg_txt == "ダメ" or
          line_msg_txt == "禁止です" or
          line_msg_txt == "禁止だ" or
          line_msg_txt == "禁止" or
          line_msg_txt == "いけません" or
          line_msg_txt == "いけない" or
          line_msg_txt == "しては駄目です" or
          line_msg_txt == "してはだめです" or
          line_msg_txt == "してはダメです" or
          line_msg_txt == "しては駄目だ" or
          line_msg_txt == "してはだめだ" or
          line_msg_txt == "してはダメだ" or
          line_msg_txt == "しては駄目" or
          line_msg_txt == "してはだめ" or
          line_msg_txt == "してはダメ" or
          line_msg_txt == "するのは禁止です" or
          line_msg_txt == "するのは禁止" or
          line_msg_txt == "やるのは禁止です" or
          line_msg_txt == "やるのは禁止" or
          line_msg_txt == "してははいけません" or
          line_msg_txt == "しちゃいけません" or
          line_msg_txt == "やってはいけません" or
          line_msg_txt == "やっちゃいけません" or
          line_msg_txt == "やっちゃ駄目" or
          line_msg_txt == "やっちゃだめ" or
          line_msg_txt == "やっちゃダメ" or
          line_msg_txt == "NG"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<禁止＆不許可>"
    elif (line_msg_txt == "ですねえ" or
          line_msg_txt == "ですねぇ" or
          line_msg_txt == "ですね" or
          line_msg_txt == "そうだねえ" or
          line_msg_txt == "そうだねぇ" or
          line_msg_txt == "そうだね" or
          line_msg_txt == "そだねえ" or
          line_msg_txt == "そだねぇ" or
          line_msg_txt == "そだね" or
          line_msg_txt == "だよねえ" or
          line_msg_txt == "だよねぇ" or
          line_msg_txt == "だよね" or
          line_msg_txt == "だねえ" or
          line_msg_txt == "だねぇ" or
          line_msg_txt == "だね"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<賛意＆賛同>" 
    elif (line_msg_txt == "歌ってよ" or
          line_msg_txt == "うたってよ" or
          line_msg_txt == "歌って" or
          line_msg_txt == "うたって" or
          line_msg_txt == "踊ってよ" or
          line_msg_txt == "おどってよ" or
          line_msg_txt == "踊って" or
          line_msg_txt == "おどって" or
          line_msg_txt == "遊んでよ" or
          line_msg_txt == "あそんでよ" or
          line_msg_txt == "遊んで" or
          line_msg_txt == "あそんで"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<依頼＆要求>"
    elif (line_msg_txt == "行きます" or
          line_msg_txt == "いきます" or
          line_msg_txt == "遣ります" or
          line_msg_txt == "やります" or
          line_msg_txt == "遊びます" or
          line_msg_txt == "あそびます" or
          line_msg_txt == "休みます" or
          line_msg_txt == "やすみます"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<宣言＆表明 現在＆未来 自己の行為・行動について>"
    elif (line_msg_txt == "美しい" or
          line_msg_txt == "うつくしい" or
          line_msg_txt == "楽しい" or
          line_msg_txt == "たのしい" or
          line_msg_txt == "苦しい" or
          line_msg_txt == "くるしい" or
          line_msg_txt == "辛い" or
          line_msg_txt == "つらい" or
          line_msg_txt == "嬉しい" or
          line_msg_txt == "うれしい" or
          line_msg_txt == "悲しい" or
          line_msg_txt == "かなしい" or
          line_msg_txt == "哀しい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<訴求＆表出 心理・感情について>"
    elif (line_msg_txt == "楽" or
          line_msg_txt == "らく" or
          line_msg_txt == "ラク" or
          line_msg_txt == "らくちん" or
          line_msg_txt == "ラクチン" or
          line_msg_txt == "楽勝" or
          line_msg_txt == "らくしょう" or
          line_msg_txt == "ラクショウ" or
          line_msg_txt == "大変" or
          line_msg_txt == "たいへん" or
          line_msg_txt == "タイヘン" or
          line_msg_txt == "疲れた" or
          line_msg_txt == "つかれた"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<訴求＆表出 精神・肉体について>"
    elif (line_msg_txt == "最初は グー" or
          line_msg_txt == "最初はグー" or
          line_msg_txt == "じゃんけんぽん" or
          line_msg_txt == "じゃんけん" or
          line_msg_txt == "ジャンケンポン" or
          line_msg_txt == "ジャンケン"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<児戯＆遊戯>"
    elif (line_msg_txt == "お願い致します" or
          line_msg_txt == "お願いいたします" or
          line_msg_txt == "お願いします" or
          line_msg_txt == "お願いです" or
          line_msg_txt == "お願い"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<依頼＆依願>"
    elif (line_msg_txt == "御免なさい" or
          line_msg_txt == "ごめんなさい" or
          line_msg_txt == "ゴメンなさい" or
          line_msg_txt == "御免" or
          line_msg_txt == "ごめん" or
          line_msg_txt == "ゴメン" or
          line_msg_txt == "メンゴ メンゴ" or
          line_msg_txt == "メンゴメンゴ" or
          line_msg_txt == "メンゴ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<陳謝＆謝罪>"
    elif (line_msg_txt == "承知致しました" or
          line_msg_txt == "承知いたしました" or
          line_msg_txt == "承知しました" or
          line_msg_txt == "承知した" or
          line_msg_txt == "承知" or
          line_msg_txt == "かしこまりました" or
          line_msg_txt == "かしこまり"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<承知＆承諾>"
    elif (line_msg_txt == "了解致しました" or
          line_msg_txt == "了解いたしました" or
          line_msg_txt == "了解しました" or
          line_msg_txt == "了解した" or
          line_msg_txt == "了解" or
          line_msg_txt == "りょ" or
          line_msg_txt == "リョ" or
          line_msg_txt == "分かりました" or
          line_msg_txt == "わかりました" or
          line_msg_txt == "分かった" or
          line_msg_txt == "わかった"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<了承＆了解>"
    elif (line_msg_txt == "愛しています" or
          line_msg_txt == "あいしています" or
          line_msg_txt == "愛してます" or
          line_msg_txt == "あいしてます" or
          line_msg_txt == "愛してる" or
          line_msg_txt == "あいしてる" or
          line_msg_txt == "好きです" or
          line_msg_txt == "すきです" or
          line_msg_txt == "スキです" or
          line_msg_txt == "好きだ" or
          line_msg_txt == "すきだ" or
          line_msg_txt == "スキだ" or
          line_msg_txt == "好き" or
          line_msg_txt == "すき" or
          line_msg_txt == "スキ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<訴求＆表出 求愛している>"
    elif (line_msg_txt == "Hなことしたい" or
          line_msg_txt == "Hなことしよう" or
          line_msg_txt == "Hしたい" or
          line_msg_txt == "Hしよう" or
          line_msg_txt == "セックスしたい" or
          line_msg_txt == "セックスしよう"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<訴求＆表出 発情している>"
    elif (line_msg_txt == "アナルは好きですか" or
          line_msg_txt == "アナルは好き" or
          line_msg_txt == "どこを責められたい" or
          line_msg_txt == "どこ責められたい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<辱め 卑猥な言動>"
    elif (line_msg_txt == "何故そうなるのですか" or
          line_msg_txt == "なぜそうなるのですか" or
          line_msg_txt == "何故そうなるんですか" or
          line_msg_txt == "なぜそうなるんですか" or
          line_msg_txt == "何故そうなるのか" or
          line_msg_txt == "なぜそうなるのか" or
          line_msg_txt == "何故そうなるか" or
          line_msg_txt == "なぜそうなるか" or
          line_msg_txt == "何故そうなるのです" or
          line_msg_txt == "なぜそうなるのです" or
          line_msg_txt == "何故そうなるんです" or
          line_msg_txt == "なぜそうなるんです"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆確認＆質問 理由・事情について>"
    elif (line_msg_txt == "なんでそうなるのかなあ" or
          line_msg_txt == "なんでそうなるのかなぁ" or
          line_msg_txt == "なんでそうなるのかな" or
          line_msg_txt == "なんでそうなるかなあ" or
          line_msg_txt == "なんでそうなるかなぁ" or
          line_msg_txt == "なんでそうなるかな" or
          line_msg_txt == "なんでそうなるのか" or
          line_msg_txt == "なんでそうなるか" or
          line_msg_txt == "なんでそうなる" or
          line_msg_txt == "何故そうなるの" or
          line_msg_txt == "なぜそうなるの" or
          line_msg_txt == "何故そうなる" or
          line_msg_txt == "なぜそうなる"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆確認＆質問 やや反発している、やや反感を抱いている>"
    elif (line_msg_txt == "大丈夫でしょうか" or
          line_msg_txt == "大丈夫ですか" or
          line_msg_txt == "大丈夫"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 安否・健康状態について>"
    elif (line_msg_txt == "うむ" or
          line_msg_txt == "うん"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<了承＆承諾 理解・同意・納得する様子でも>"
    elif (line_msg_txt == "お疲れ様でした" or
          line_msg_txt == "お疲れ様です" or
          line_msg_txt == "お疲れ様" or
          line_msg_txt == "お疲れ" or
          line_msg_txt == "ご苦労様でした" or
          line_msg_txt == "ご苦労様です" or
          line_msg_txt == "ご苦労様" or
          line_msg_txt == "ご苦労" or
          line_msg_txt == "大儀であった" or
          line_msg_txt == "大儀だった"):        
            extrct_intnt_from_shrt_and_blrplt_rslt = "<慰労＆労い>"
    elif (line_msg_txt == "分かった" or
          line_msg_txt == "わかった"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<理解＆認識>"
    elif (line_msg_txt == "きざったらしい" or
          line_msg_txt == "キザったらしい" or
          line_msg_txt == "きざっぽい" or
          line_msg_txt == "キザっぽい" or
          line_msg_txt == "嫌味ったらしい" or
          line_msg_txt == "イヤミったらしい" or
          line_msg_txt == "嫌味っぽい" or
          line_msg_txt == "イヤミっぽい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<訴求＆表現 反発している、反感を抱いている 強い嫌悪>"
    elif (line_msg_txt == "しても良いですか" or
          line_msg_txt == "してもよいですか" or
          line_msg_txt == "良いですか" or
          line_msg_txt == "いいですか" or
          line_msg_txt == "良いか" or
          line_msg_txt == "いいか" or
          line_msg_txt == "してもいいですか" or
          line_msg_txt == "してもいいか" or
          line_msg_txt == "していいか" or
          line_msg_txt == "いいか" or
          line_msg_txt == "やっても良いですか" or
          line_msg_txt == "やってもよいですか" or
          line_msg_txt == "やってもいいですか" or
          line_msg_txt == "やってもいいか" or
          line_msg_txt == "やっていいか"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 許容・許可を求める 肯定形>"
    elif (line_msg_txt == "駄目ですか" or
          line_msg_txt == "だめですか" or
          line_msg_txt == "ダメですか" or
          line_msg_txt == "駄目か" or
          line_msg_txt == "だめか" or
          line_msg_txt == "ダメか" or
          line_msg_txt == "禁止ですか" or
          line_msg_txt == "禁止か" or
          line_msg_txt == "いけませんか" or
          line_msg_txt == "いけないか"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 許容・許可を求める 否定形>"
    elif (line_msg_txt == "お伺いします" or
          line_msg_txt == "お聞きします"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<聴取＆傾聴 用件を尋ねる>"
    elif (line_msg_txt == "お聞かせ下さい" or
          line_msg_txt == "お聞かせください"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<聴取＆傾聴 意見・感想を求める>"
    elif (line_msg_txt == "お考えになって下さい" or
          line_msg_txt == "お考え下さい" or
          line_msg_txt == "考えて下さい" or
          line_msg_txt == "考えてください" or
          line_msg_txt == "考えてくれ" or
          line_msg_txt == "考えて"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<要求＆要請 思慮・思考を求める>"
    elif (line_msg_txt == "考え直して下さい" or
          line_msg_txt == "考え直してください" or
          line_msg_txt == "考え直してくれ" or
          line_msg_txt == "考え直して" or
          line_msg_txt == "思い直して下さい" or
          line_msg_txt == "思い直してください" or
          line_msg_txt == "思い直してくれ" or
          line_msg_txt == "思い直して"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<要求＆要請 再度の思慮・思考を求める>"
    elif (line_msg_txt == "良きに計らえ" or
          line_msg_txt == "よきに計らえ" or
          line_msg_txt == "良しなに" or
          line_msg_txt == "よしなに" or
          line_msg_txt == "どうぞ良しなに" or
          line_msg_txt == "どうぞよしなに"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<要求＆要請 善処を求める>"
    elif (line_msg_txt == "うむ" or
          line_msg_txt == "ウム" or
          line_msg_txt == "うん" or
          line_msg_txt == "ウン"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<了承＆承諾 納得する様子>"
    elif (line_msg_txt == "そう言っているのです" or
          line_msg_txt == "そういっているのです" or
          line_msg_txt == "そう言っているんです" or
          line_msg_txt == "そういっているんです" or
          line_msg_txt == "そう言っている" or
          line_msg_txt == "そういっている" or
          line_msg_txt == "そう言ってる" or
          line_msg_txt == "そういってる"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<問答 肯定形 考えに同意する形で>"
    elif (line_msg_txt == "そうは言っていないよ" or
          line_msg_txt == "そうはいっていないよ" or
          line_msg_txt == "そうは言っていない" or
          line_msg_txt == "そうはいっていない" or
          line_msg_txt == "そうは言ってないよ" or
          line_msg_txt == "そうはいってないよ" or
          line_msg_txt == "そうは言ってない" or
          line_msg_txt == "そうはいってない"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<問答 否定形 相手の考えに反意する形で>"
    elif (line_msg_txt == "しますよね" or
          line_msg_txt == "するよね" or
          line_msg_txt == "やるよね"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 肯定形 自己の行為・行動について>"
    elif (line_msg_txt == "しませんよね" or
          line_msg_txt == "しないよね" or
          line_msg_txt == "やらないよね"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 否定形 自己の行為・行動について>"
    elif (line_msg_txt == "するよな" or
          line_msg_txt == "やるよな"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 肯定形 半強制 自己の行為・行動について>"
    elif (line_msg_txt == "しないよな" or
          line_msg_txt == "せんよな" or
          line_msg_txt == "やらないよな" or
          line_msg_txt == "やらんよな"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 否定形 半強制 自己の行為・行動について>"
    elif (line_msg_txt == "そうなのですね" or
          line_msg_txt == "そうなんですね" or
          line_msg_txt == "そうなのだな" or
          line_msg_txt == "そうなんだな"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 肯定形 考えや気持ちを察する形で>"
    elif (line_msg_txt == "そうではないのですね" or
          line_msg_txt == "そうではないんですね" or
          line_msg_txt == "そうではないのだな" or
          line_msg_txt == "そうではないんだな"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 否定形 考えや気持ちを察する形で>"
    elif (line_msg_txt == "そうみたいだよ" or
          line_msg_txt == "そうみたいだね" or
          line_msg_txt == "そうみたいだな" or
          line_msg_txt == "そうみたいだわ" or
          line_msg_txt == "そうみたいだ" or
          line_msg_txt == "そうみたい" or
          line_msg_txt == "そうらしいよ" or
          line_msg_txt == "そうらしいね" or
          line_msg_txt == "そうらしいな" or
          line_msg_txt == "そうらしいわ" or
          line_msg_txt == "そうらしい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<同意 意見・考えに沿う形で>"
    elif (line_msg_txt == "そうではないらしいよ" or
          line_msg_txt == "そうではないらしいね" or
          line_msg_txt == "そうではないらしいな" or
          line_msg_txt == "そうではないらしいわ" or
          line_msg_txt == "そうではないらしい" or
          line_msg_txt == "ではないらしいよ" or
          line_msg_txt == "ではないらしいね" or
          line_msg_txt == "ではないらしいな" or
          line_msg_txt == "ではないらしいわ" or
          line_msg_txt == "ではないらしい" or
          line_msg_txt == "そうじゃないらしいよ" or
          line_msg_txt == "そうじゃないらしいね" or
          line_msg_txt == "そうじゃないらしいな" or
          line_msg_txt == "そうじゃないらしいわ" or
          line_msg_txt == "そうじゃないらしい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<反意・不同意 意見・考えに沿わない形で>"
    elif (line_msg_txt == "そうなのですね" or
          line_msg_txt == "そうなんですね" or
          line_msg_txt == "そうなんですね" or
          line_msg_txt == "なのですね" or
          line_msg_txt == "なんですね"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<理解＆納得 肯定形>"
    elif (line_msg_txt == "そうではないのですね" or
          line_msg_txt == "そうではないんですね" or
          line_msg_txt == "そうじゃないんですね" or
          line_msg_txt == "ではないのですね" or
          line_msg_txt == "ではないんですね" or
          line_msg_txt == "じゃないんですね"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<理解＆納得 否定形>"
    elif (line_msg_txt == "ではどうするのですか" or
          line_msg_txt == "ではどうするんですか" or
          line_msg_txt == "ではどうするのか" or
          line_msg_txt == "ではどうするの" or
          line_msg_txt == "ではどうする" or
          line_msg_txt == "どうするのですか" or
          line_msg_txt == "どうするんですか" or
          line_msg_txt == "じゃあどうするのか" or
          line_msg_txt == "じゃあどうするの" or
          line_msg_txt == "じゃあどうする" or
          line_msg_txt == "どうするの" or
          line_msg_txt == "どうするん" or
          line_msg_txt == "どうする"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 追求 今後の動きや活動について>"
    elif (line_msg_txt == "どうぞ ごゆっくりなさって下さい" or
          line_msg_txt == "どうぞ ごゆっくりなさってください" or
          line_msg_txt == "どうぞごゆっくりなさってください" or
          line_msg_txt == "どうぞ ごゆっくりなさって" or
          line_msg_txt == "どうぞごゆっくりなさって" or
          line_msg_txt == "ごゆっくりなさって下さい" or
          line_msg_txt == "ごゆっくりなさってください" or
          line_msg_txt == "ごゆっくりなさって" or
          line_msg_txt == "ごゆっくり どうぞ" or
          line_msg_txt == "ごゆっくりどうぞ" or
          line_msg_txt == "ごゆっくり"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<歓迎＆歓待 くつろいで欲しいという気持ち>"
    elif (line_msg_txt == "どうぞ お手柔らかに" or
          line_msg_txt == "どうぞお手柔らかに"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<初見・顔合わせの決まり文句 配慮などを求めて>"
    elif (line_msg_txt == "どうぞ 宜しくお願い致します" or
          line_msg_txt == "どうぞ よろしくお願い致します" or
          line_msg_txt == "どうぞ よろしくお願いいたします" or
          line_msg_txt == "どうぞ お願いいたします" or
          line_msg_txt == "どうぞ よろしくお願いします" or
          line_msg_txt == "どうぞ よろしく" or
          line_msg_txt == "どうぞ宜しくお願い致します" or
          line_msg_txt == "どうぞよろしくお願い致します" or
          line_msg_txt == "どうぞよろしくお願いいたします" or
          line_msg_txt == "どうぞお願いいたします" or
          line_msg_txt == "どうぞよろしくお願いします" or
          line_msg_txt == "どうぞよろしく" or
          line_msg_txt == "よろしく どうぞ" or
          line_msg_txt == "よろしくどうぞ" or
          line_msg_txt == "よろしく"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<初見・顔合わせの決まり文句 良好な関係を求めて>"
    elif (line_msg_txt == "頑張りましょう" or
          line_msg_txt == "がんばりましょう" or
          line_msg_txt == "ぼちぼち やりましょう" or
          line_msg_txt == "ぼちぼちやりましょう" or
          line_msg_txt == "ボチボチ やりましょう" or
          line_msg_txt == "ボチボチやりましょう" or
          line_msg_txt == "ゆっくり 行きましょう" or
          line_msg_txt == "ゆっくり いきましょう" or
          line_msg_txt == "ゆっくり行きましょう" or
          line_msg_txt == "ゆっくりいきましょう" or
          line_msg_txt == "ゆっくりしましょう" or
          line_msg_txt == "急いで行きましょう" or
          line_msg_txt == "急いでいきましょう" or
          line_msg_txt == "急いでやりましょう" or
          line_msg_txt == "急ぎましょう" or
          line_msg_txt == "優しく行きましょう" or
          line_msg_txt == "優しくしましょう" or
          line_msg_txt == "厳しく行きましょう" or
          line_msg_txt == "厳しくしましょう"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<推奨＆強制＆勧告 誘導に近い>"
    elif (line_msg_txt == "本当ですよ" or
          line_msg_txt == "ホントですよ" or
          line_msg_txt == "本当だよ" or
          line_msg_txt == "ホントだよ" or
          line_msg_txt == "本当よ" or
          line_msg_txt == "ホントよ" or
          line_msg_txt == "ホント ホント" or
          line_msg_txt == "ホントホント"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<宣告 真実であることを告げる>"
    elif (line_msg_txt == "嘘ですよ" or
          line_msg_txt == "ウソですよ" or
          line_msg_txt == "嘘だよ" or
          line_msg_txt == "ウソですよ" or
          line_msg_txt == "嘘よ" or
          line_msg_txt == "ウソよ" or
          line_msg_txt == "ウソ ウソ" or
          line_msg_txt == "ウソウソ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<宣告 虚偽であることを告げる>"
    elif (line_msg_txt == "本当ですか" or
          line_msg_txt == "ホントですか" or
          line_msg_txt == "本当か" or
          line_msg_txt == "ホントか" or
          line_msg_txt == "ホント"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 真実であるかどうか>"
    elif (line_msg_txt == "嘘ですか" or
          line_msg_txt == "ウソですか" or
          line_msg_txt == "嘘か" or
          line_msg_txt == "ウソか" or
          line_msg_txt == "嘘" or
          line_msg_txt == "ウソ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<疑義＆質問＆確認 虚偽であるかどうか>"
    elif (line_msg_txt == "左様ですか" or
          line_msg_txt == "そうですか" or
          line_msg_txt == "はい はい" or
          line_msg_txt == "はいはい" or
          line_msg_txt == "うん うん" or
          line_msg_txt == "うんうん"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<相槌＆合いの手 傾聴している素振り>"
    elif (line_msg_txt == "その通りです" or
          line_msg_txt == "その通り"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "<相槌＆合いの手 正鵠を得た相手に対して>"
    else:
            extrct_intnt_from_shrt_and_blrplt_rslt = "<その他・不明>"
    return extrct_intnt_from_shrt_and_blrplt_rslt


#ユーザーから送られるLINEメッセージの中からインテント(＝発話の意図するもの ＝助詞・助動詞)を抽出する
def extract_intent(line_msg_txt):
    #メッセージの末尾部分からインテントを抽出して、これを呼出し元に引渡しをする
    if   (check_text_terminate_string(line_msg_txt, "を行います") or
          check_text_terminate_string(line_msg_txt, "を行う") or
          check_text_terminate_string(line_msg_txt, "をします") or
          check_text_terminate_string(line_msg_txt, "をする") or
          check_text_terminate_string(line_msg_txt, "はします") or
          check_text_terminate_string(line_msg_txt, "はする") or
          check_text_terminate_string(line_msg_txt, "します") or
          check_text_terminate_string(line_msg_txt, "する")):
           extrct_intnt_rslt = "<宣言＆表明 現在＆未来 能動 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "を行いません") or
          check_text_terminate_string(line_msg_txt, "を行わない") or
          check_text_terminate_string(line_msg_txt, "をしません") or
          check_text_terminate_string(line_msg_txt, "をしない") or
          check_text_terminate_string(line_msg_txt, "はしません") or
          check_text_terminate_string(line_msg_txt, "はしない") or
          check_text_terminate_string(line_msg_txt, "しません") or
          check_text_terminate_string(line_msg_txt, "しない")):
           extrct_intnt_rslt = "<宣言＆表明 現在＆未来 能動 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "を行っています") or
          check_text_terminate_string(line_msg_txt, "を行っている") or
          check_text_terminate_string(line_msg_txt, "をしています") or
          check_text_terminate_string(line_msg_txt, "をしてます") or
          check_text_terminate_string(line_msg_txt, "をしている") or
          check_text_terminate_string(line_msg_txt, "をしてる") or
          check_text_terminate_string(line_msg_txt, "しています") or
          check_text_terminate_string(line_msg_txt, "してます") or
          check_text_terminate_string(line_msg_txt, "している") or
          check_text_terminate_string(line_msg_txt, "してる")):
           extrct_intnt_rslt = "<宣言＆表明 現在進行 能動 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "を行っていません") or
          check_text_terminate_string(line_msg_txt, "を行ってません") or
          check_text_terminate_string(line_msg_txt, "をしていません") or
          check_text_terminate_string(line_msg_txt, "をしてません") or
          check_text_terminate_string(line_msg_txt, "をしていない") or
          check_text_terminate_string(line_msg_txt, "をしてない") or
          check_text_terminate_string(line_msg_txt, "していません") or
          check_text_terminate_string(line_msg_txt, "してません") or
          check_text_terminate_string(line_msg_txt, "していない") or
          check_text_terminate_string(line_msg_txt, "してない")):
            extrct_intnt_rslt = "<宣言＆表明 現在進行 能動 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "ができています") or
          check_text_terminate_string(line_msg_txt, "ができている") or
          check_text_terminate_string(line_msg_txt, "ができてる") or
          check_text_terminate_string(line_msg_txt, "できています") or
          check_text_terminate_string(line_msg_txt, "できている") or
          check_text_terminate_string(line_msg_txt, "できてる")):
            extrct_intnt_rslt = "<宣言＆表明 現在進行 完了 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "ができていません") or
          check_text_terminate_string(line_msg_txt, "ができてません") or
          check_text_terminate_string(line_msg_txt, "ができていない") or
          check_text_terminate_string(line_msg_txt, "ができてない") or
          check_text_terminate_string(line_msg_txt, "できていません") or
          check_text_terminate_string(line_msg_txt, "できてません") or
          check_text_terminate_string(line_msg_txt, "できていない") or
          check_text_terminate_string(line_msg_txt, "できてない")):
            extrct_intnt_rslt = "<宣言＆表明 現在進行 未完了 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "ができます") or
          check_text_terminate_string(line_msg_txt, "ができる") or
          check_text_terminate_string(line_msg_txt, "できます") or
          check_text_terminate_string(line_msg_txt, "できる")):
            extrct_intnt_rslt = "<宣言＆表明 可能 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "ができません") or
          check_text_terminate_string(line_msg_txt, "ができない") or
          check_text_terminate_string(line_msg_txt, "できません") or
          check_text_terminate_string(line_msg_txt, "できない")):
            extrct_intnt_rslt = "<宣言＆表明 不可能 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "をしました") or
          check_text_terminate_string(line_msg_txt, "をした") or
          check_text_terminate_string(line_msg_txt, "はしました") or
          check_text_terminate_string(line_msg_txt, "はした") or
          check_text_terminate_string(line_msg_txt, "しました") or
          check_text_terminate_string(line_msg_txt, "した") or
          check_text_terminate_string(line_msg_txt, "をやりました") or
          check_text_terminate_string(line_msg_txt, "をやった") or
          check_text_terminate_string(line_msg_txt, "はやりました") or
          check_text_terminate_string(line_msg_txt, "はやった")):
            extrct_intnt_rslt = "<宣言＆表明 過去 能動 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "をしていません") or
          check_text_terminate_string(line_msg_txt, "をしてません") or
          check_text_terminate_string(line_msg_txt, "をしてない") or
          check_text_terminate_string(line_msg_txt, "はしていません") or
          check_text_terminate_string(line_msg_txt, "はしてません") or
          check_text_terminate_string(line_msg_txt, "はしてない") or
          check_text_terminate_string(line_msg_txt, "していません") or
          check_text_terminate_string(line_msg_txt, "してません") or
          check_text_terminate_string(line_msg_txt, "してない") or
          check_text_terminate_string(line_msg_txt, "をやってません") or
          check_text_terminate_string(line_msg_txt, "をやってない") or
          check_text_terminate_string(line_msg_txt, "はやってません") or
          check_text_terminate_string(line_msg_txt, "はやってない")):
            extrct_intnt_rslt = "<宣言＆表明 過去 能動 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "をするのですか") or
          check_text_terminate_string(line_msg_txt, "をするんですか") or
          check_text_terminate_string(line_msg_txt, "をしますか") or
          check_text_terminate_string(line_msg_txt, "はするのですか") or
          check_text_terminate_string(line_msg_txt, "はするんですか") or
          check_text_terminate_string(line_msg_txt, "はしますか") or
          check_text_terminate_string(line_msg_txt, "するのですか") or
          check_text_terminate_string(line_msg_txt, "するんですか") or
          check_text_terminate_string(line_msg_txt, "しますか") or
          check_text_terminate_string(line_msg_txt, "するのか") or
          check_text_terminate_string(line_msg_txt, "するか")):
           extrct_intnt_rslt = "<疑義＆質問＆確認 現在＆未来 能動 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "をしないのですか") or
          check_text_terminate_string(line_msg_txt, "はしないのですか") or
          check_text_terminate_string(line_msg_txt, "をしないんですか") or
          check_text_terminate_string(line_msg_txt, "はしないんですか") or
          check_text_terminate_string(line_msg_txt, "をしないのか") or
          check_text_terminate_string(line_msg_txt, "はしないのか") or
          check_text_terminate_string(line_msg_txt, "しないのですか") or
          check_text_terminate_string(line_msg_txt, "しないんですか") or
          check_text_terminate_string(line_msg_txt, "しないのか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在＆未来 能動 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "をしていますか") or
          check_text_terminate_string(line_msg_txt, "はしていますか") or
          check_text_terminate_string(line_msg_txt, "をしてますか") or
          check_text_terminate_string(line_msg_txt, "はしてますか") or
          check_text_terminate_string(line_msg_txt, "をしているか") or
          check_text_terminate_string(line_msg_txt, "はしているか") or
          check_text_terminate_string(line_msg_txt, "をしてるか") or
          check_text_terminate_string(line_msg_txt, "はしてるか") or
          check_text_terminate_string(line_msg_txt, "していますか") or
          check_text_terminate_string(line_msg_txt, "してますか") or
          check_text_terminate_string(line_msg_txt, "しているか") or
          check_text_terminate_string(line_msg_txt, "してるか")):
           extrct_intnt_rslt = "<疑義＆質問＆確認 現在進行 能動 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "をしていませんか") or
          check_text_terminate_string(line_msg_txt, "はしていませんか") or
          check_text_terminate_string(line_msg_txt, "をしてませんか") or
          check_text_terminate_string(line_msg_txt, "はしてませんか") or
          check_text_terminate_string(line_msg_txt, "をしていないか") or
          check_text_terminate_string(line_msg_txt, "はしていないか") or
          check_text_terminate_string(line_msg_txt, "をしてないか") or
          check_text_terminate_string(line_msg_txt, "はしてないか") or
          check_text_terminate_string(line_msg_txt, "していませんか") or
          check_text_terminate_string(line_msg_txt, "してませんか") or
          check_text_terminate_string(line_msg_txt, "していないか") or
          check_text_terminate_string(line_msg_txt, "してないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在進行 能動 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "ができていますか") or
          check_text_terminate_string(line_msg_txt, "はできていますか") or
          check_text_terminate_string(line_msg_txt, "ができてますか") or
          check_text_terminate_string(line_msg_txt, "はできてますか") or
          check_text_terminate_string(line_msg_txt, "ができているか") or
          check_text_terminate_string(line_msg_txt, "はできているか") or
          check_text_terminate_string(line_msg_txt, "ができてるか") or
          check_text_terminate_string(line_msg_txt, "はできてるか") or
          check_text_terminate_string(line_msg_txt, "できていますか") or
          check_text_terminate_string(line_msg_txt, "できてますか") or
          check_text_terminate_string(line_msg_txt, "できているか") or
          check_text_terminate_string(line_msg_txt, "できてるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在 完了 肯定形 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "はできていませんか") or
          check_text_terminate_string(line_msg_txt, "はできてませんか") or
          check_text_terminate_string(line_msg_txt, "はできていないか") or
          check_text_terminate_string(line_msg_txt, "はできてないか") or
          check_text_terminate_string(line_msg_txt, "できていませんか") or
          check_text_terminate_string(line_msg_txt, "できてませんか") or
          check_text_terminate_string(line_msg_txt, "できていないか") or
          check_text_terminate_string(line_msg_txt, "できてないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在 未完了 否定形 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "ができましたか") or
          check_text_terminate_string(line_msg_txt, "はできましたか") or
          check_text_terminate_string(line_msg_txt, "ができたか") or
          check_text_terminate_string(line_msg_txt, "はできたか") or
          check_text_terminate_string(line_msg_txt, "できましたか") or
          check_text_terminate_string(line_msg_txt, "できたか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 過去 完了 肯定形 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "はできていませんか") or
          check_text_terminate_string(line_msg_txt, "はできてませんか") or
          check_text_terminate_string(line_msg_txt, "はできてないか") or
          check_text_terminate_string(line_msg_txt, "できていませんか") or
          check_text_terminate_string(line_msg_txt, "できてませんか") or
          check_text_terminate_string(line_msg_txt, "できてないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 過去 未完了 否定形 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "ができますか") or
          check_text_terminate_string(line_msg_txt, "はできますか") or
          check_text_terminate_string(line_msg_txt, "ができるか") or
          check_text_terminate_string(line_msg_txt, "はできるか") or
          check_text_terminate_string(line_msg_txt, "できますか") or
          check_text_terminate_string(line_msg_txt, "できるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在＆未来 肯定形 物事の可能性について>"
    elif (check_text_terminate_string(line_msg_txt, "はできませんか") or
          check_text_terminate_string(line_msg_txt, "はできないか") or
          check_text_terminate_string(line_msg_txt, "できませんか") or
          check_text_terminate_string(line_msg_txt, "できないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在＆未来 否定形 物事の可能性について>"
    elif (check_text_terminate_string(line_msg_txt, "がされています") or
          check_text_terminate_string(line_msg_txt, "はされています") or
          check_text_terminate_string(line_msg_txt, "がされてます") or
          check_text_terminate_string(line_msg_txt, "はされてます") or
          check_text_terminate_string(line_msg_txt, "がされている") or
          check_text_terminate_string(line_msg_txt, "はされている") or
          check_text_terminate_string(line_msg_txt, "がされてる") or
          check_text_terminate_string(line_msg_txt, "はされてる") or
          check_text_terminate_string(line_msg_txt, "されています") or
          check_text_terminate_string(line_msg_txt, "されてます") or
          check_text_terminate_string(line_msg_txt, "されている") or
          check_text_terminate_string(line_msg_txt, "がやられています") or
          check_text_terminate_string(line_msg_txt, "がやられてます") or
          check_text_terminate_string(line_msg_txt, "がやられてる") or
          check_text_terminate_string(line_msg_txt, "はやられています") or
          check_text_terminate_string(line_msg_txt, "はやられてます") or
          check_text_terminate_string(line_msg_txt, "はやられてる")):
            extrct_intnt_rslt = "<宣言＆表明 現在進行 受動 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "がされていません") or
          check_text_terminate_string(line_msg_txt, "はされていません") or
          check_text_terminate_string(line_msg_txt, "されていません") or
          check_text_terminate_string(line_msg_txt, "がされてません") or
          check_text_terminate_string(line_msg_txt, "はされてません") or
          check_text_terminate_string(line_msg_txt, "されてません") or
          check_text_terminate_string(line_msg_txt, "がされていない") or
          check_text_terminate_string(line_msg_txt, "はされていない") or
          check_text_terminate_string(line_msg_txt, "されていない") or
          check_text_terminate_string(line_msg_txt, "がされてない") or
          check_text_terminate_string(line_msg_txt, "はされてない") or
          check_text_terminate_string(line_msg_txt, "されてない")):
            extrct_intnt_rslt = "<宣言＆表明 現在進行 受動 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "がされました") or
          check_text_terminate_string(line_msg_txt, "はされました") or
          check_text_terminate_string(line_msg_txt, "されました") or
          check_text_terminate_string(line_msg_txt, "がされた") or
          check_text_terminate_string(line_msg_txt, "はされた") or
          check_text_terminate_string(line_msg_txt, "された")):
            extrct_intnt_rslt = "<宣言＆表明 過去完了 受動 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "がされませんでした") or
          check_text_terminate_string(line_msg_txt, "はされませんでした") or
          check_text_terminate_string(line_msg_txt, "されませんでした") or
          check_text_terminate_string(line_msg_txt, "がされなかった") or
          check_text_terminate_string(line_msg_txt, "はされなかった") or
          check_text_terminate_string(line_msg_txt, "されなかった")):
            extrct_intnt_rslt = "<宣言＆表明 過去完了 受動 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "でした") or
          check_text_terminate_string(line_msg_txt, "だった")):
            extrct_intnt_rslt = "<宣言＆表明 過去完了 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "ではなかったです") or
          check_text_terminate_string(line_msg_txt, "でなかったです") or
          check_text_terminate_string(line_msg_txt, "ではなかった") or
          check_text_terminate_string(line_msg_txt, "でなかった")):
            extrct_intnt_rslt = "<宣言＆表明 過去完了 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "をしていきたい") or
          check_text_terminate_string(line_msg_txt, "はしていきたい") or
          check_text_terminate_string(line_msg_txt, "していきたい") or
          check_text_terminate_string(line_msg_txt, "をやっていきたい") or
          check_text_terminate_string(line_msg_txt, "はやっていきたい")):
            extrct_intnt_rslt = "<宣言＆表明 現在＆未来 持続 能動 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "をしていきたくはない") or
          check_text_terminate_string(line_msg_txt, "はしていきたくはない") or
          check_text_terminate_string(line_msg_txt, "していきたくはない") or
          check_text_terminate_string(line_msg_txt, "をしていきたくない") or
          check_text_terminate_string(line_msg_txt, "はしていきたくない") or
          check_text_terminate_string(line_msg_txt, "していきたくない") or
          check_text_terminate_string(line_msg_txt, "をやっていきたくはない") or
          check_text_terminate_string(line_msg_txt, "はやっていきたくはない") or
          check_text_terminate_string(line_msg_txt, "をやっていきたくない") or
          check_text_terminate_string(line_msg_txt, "はやっていきたくない")):
            extrct_intnt_rslt = "<宣言＆表明 現在＆未来 持続 能動 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "ではありました") or
          check_text_terminate_string(line_msg_txt, "ではあった") or
          check_text_terminate_string(line_msg_txt, "であった")):
            extrct_intnt_rslt = "<宣言＆表明 過去＆現在 肯定形 事実・現実について>"
    elif (check_text_terminate_string(line_msg_txt, "ではありませんでした") or
          check_text_terminate_string(line_msg_txt, "ではなかった") or
          check_text_terminate_string(line_msg_txt, "でなかった")):
            extrct_intnt_rslt = "<宣言＆表明 現在＆未来 否定形 事実・現実について>"
    elif (check_text_terminate_string(line_msg_txt, "で御座います") or
          check_text_terminate_string(line_msg_txt, "でございます") or
          check_text_terminate_string(line_msg_txt, "であります") or
          check_text_terminate_string(line_msg_txt, "です")):
            extrct_intnt_rslt = "<紹介＆説明＆提示 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "では御座いません") or
          check_text_terminate_string(line_msg_txt, "ではございません") or
          check_text_terminate_string(line_msg_txt, "ではありません")):
            extrct_intnt_rslt = "<紹介＆説明＆提示 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "をやっていました") or
          check_text_terminate_string(line_msg_txt, "をやってました") or
          check_text_terminate_string(line_msg_txt, "をやってた")):
            extrct_intnt_rslt = "<報告＆連絡 過去＆現在 能動 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "をやっていませんでした") or
          check_text_terminate_string(line_msg_txt, "をやってませんでした") or
          check_text_terminate_string(line_msg_txt, "をやってなかった")):
            extrct_intnt_rslt = "<報告＆連絡 過去＆現在 能動 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "を致しませんか") or
          check_text_terminate_string(line_msg_txt, "をいたしませんか") or
          check_text_terminate_string(line_msg_txt, "致しませんか") or
          check_text_terminate_string(line_msg_txt, "いたしませんか") or
          check_text_terminate_string(line_msg_txt, "しませんか")):
            extrct_intnt_rslt = "<誘導＆勧誘>"
    elif (check_text_terminate_string(line_msg_txt, "を行いたい") or
          check_text_terminate_string(line_msg_txt, "をしたい") or
          check_text_terminate_string(line_msg_txt, "がしたい") or
          check_text_terminate_string(line_msg_txt, "したい") or
          check_text_terminate_string(line_msg_txt, "をやりたい") or
          check_text_terminate_string(line_msg_txt, "がやりたい")):
            extrct_intnt_rslt = "<願望＆欲求 肯定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "を行いたくない") or
          check_text_terminate_string(line_msg_txt, "をしたくない") or
          check_text_terminate_string(line_msg_txt, "がしたくない") or
          check_text_terminate_string(line_msg_txt, "したくない") or
          check_text_terminate_string(line_msg_txt, "をやりたくない") or
          check_text_terminate_string(line_msg_txt, "がやりたくない")):
            extrct_intnt_rslt = "<願望＆欲求 否定形 自己の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "を行いたいのですか") or
          check_text_terminate_string(line_msg_txt, "を行いたいんですか") or
          check_text_terminate_string(line_msg_txt, "を行いたいですか") or
          check_text_terminate_string(line_msg_txt, "をしたいのですか") or
          check_text_terminate_string(line_msg_txt, "をしたいんですか") or
          check_text_terminate_string(line_msg_txt, "をしたいですか") or
          check_text_terminate_string(line_msg_txt, "は行いたいのですか") or
          check_text_terminate_string(line_msg_txt, "は行いたいんですか") or
          check_text_terminate_string(line_msg_txt, "は行いたいですか") or
          check_text_terminate_string(line_msg_txt, "はしたいのですか") or
          check_text_terminate_string(line_msg_txt, "はしたいんですか") or
          check_text_terminate_string(line_msg_txt, "はしたいですか") or
          check_text_terminate_string(line_msg_txt, "したいのですか") or
          check_text_terminate_string(line_msg_txt, "したいんですか") or
          check_text_terminate_string(line_msg_txt, "したいですか") or
          check_text_terminate_string(line_msg_txt, "したいのか") or
          check_text_terminate_string(line_msg_txt, "したいか") or
          check_text_terminate_string(line_msg_txt, "をやりたいのですか") or
          check_text_terminate_string(line_msg_txt, "をやりたいんですか") or
          check_text_terminate_string(line_msg_txt, "をやりたいですか") or
          check_text_terminate_string(line_msg_txt, "をやりたいのか") or
          check_text_terminate_string(line_msg_txt, "をやりたいか") or
          check_text_terminate_string(line_msg_txt, "がやりたいのですか") or
          check_text_terminate_string(line_msg_txt, "がやりたいんですか") or
          check_text_terminate_string(line_msg_txt, "がやりたいですか") or
          check_text_terminate_string(line_msg_txt, "がやりたいのか") or
          check_text_terminate_string(line_msg_txt, "がやりたいか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "を行いたくないのですか") or
          check_text_terminate_string(line_msg_txt, "を行いたくないんですか") or
          check_text_terminate_string(line_msg_txt, "を行いたくないですか") or
          check_text_terminate_string(line_msg_txt, "をしたくないのですか") or
          check_text_terminate_string(line_msg_txt, "をしたくないんですか") or
          check_text_terminate_string(line_msg_txt, "をしたくないですか") or
          check_text_terminate_string(line_msg_txt, "は行いたくないのですか") or
          check_text_terminate_string(line_msg_txt, "は行いたくないんですか") or
          check_text_terminate_string(line_msg_txt, "は行いたくないですか") or
          check_text_terminate_string(line_msg_txt, "はしたくないのですか") or
          check_text_terminate_string(line_msg_txt, "はしたくないんですか") or
          check_text_terminate_string(line_msg_txt, "はしたくないですか") or
          check_text_terminate_string(line_msg_txt, "したくないのですか") or
          check_text_terminate_string(line_msg_txt, "したくないんですか") or
          check_text_terminate_string(line_msg_txt, "したくないですか") or
          check_text_terminate_string(line_msg_txt, "したくないか") or
          check_text_terminate_string(line_msg_txt, "をやりたくないのですか") or
          check_text_terminate_string(line_msg_txt, "をやりたくないんですか") or
          check_text_terminate_string(line_msg_txt, "をやりたくないですか") or
          check_text_terminate_string(line_msg_txt, "をやりたくないか") or
          check_text_terminate_string(line_msg_txt, "がやりたくないのですか") or
          check_text_terminate_string(line_msg_txt, "がやりたくないんですか") or
          check_text_terminate_string(line_msg_txt, "がやりたくないですか") or
          check_text_terminate_string(line_msg_txt, "がやりたくないのか") or
          check_text_terminate_string(line_msg_txt, "がやりたくないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "をしていきたいですか") or
          check_text_terminate_string(line_msg_txt, "をしていきたいか") or
          check_text_terminate_string(line_msg_txt, "していきたいか") or
          check_text_terminate_string(line_msg_txt, "をやっていきたいですか") or
          check_text_terminate_string(line_msg_txt, "をやっていきたいか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在＆未来 肯定形 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "をしていきたくないですか") or
          check_text_terminate_string(line_msg_txt, "はしていきたくないですか") or
          check_text_terminate_string(line_msg_txt, "していきたくないですか") or
          check_text_terminate_string(line_msg_txt, "をしていきたくないか") or
          check_text_terminate_string(line_msg_txt, "はしていきたくないか") or
          check_text_terminate_string(line_msg_txt, "していきたくないか") or
          check_text_terminate_string(line_msg_txt, "はやっていきたくないか") or
          check_text_terminate_string(line_msg_txt, "をやっていきたくないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在＆未来 否定形 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "をやり続けたいですか") or
          check_text_terminate_string(line_msg_txt, "をやり続けたいか") or
          check_text_terminate_string(line_msg_txt, "をやってたいですか") or
          check_text_terminate_string(line_msg_txt, "をやってたいか") or
          check_text_terminate_string(line_msg_txt, "をし続けたいですか") or
          check_text_terminate_string(line_msg_txt, "をし続けたいか") or
          check_text_terminate_string(line_msg_txt, "をしてたいですか") or
          check_text_terminate_string(line_msg_txt, "をしてたいか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在＆未来 肯定形 持続的 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "をやり続けたくないですか") or
          check_text_terminate_string(line_msg_txt, "をやり続けたくないか") or
          check_text_terminate_string(line_msg_txt, "をやってたくないですか") or
          check_text_terminate_string(line_msg_txt, "をやってたくないか") or
          check_text_terminate_string(line_msg_txt, "をし続けたくないですか") or
          check_text_terminate_string(line_msg_txt, "をし続けたくないか") or
          check_text_terminate_string(line_msg_txt, "をしてたくないですか") or
          check_text_terminate_string(line_msg_txt, "をしてたくないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在＆未来 肯定形 持続的 他者の願望・欲求に適う、他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "をしましたか") or
          check_text_terminate_string(line_msg_txt, "をしたか") or
          check_text_terminate_string(line_msg_txt, "はしましたか") or
          check_text_terminate_string(line_msg_txt, "はしたか") or
          check_text_terminate_string(line_msg_txt, "しましたか") or
          check_text_terminate_string(line_msg_txt, "したか") or
          check_text_terminate_string(line_msg_txt, "をやりましたか") or
          check_text_terminate_string(line_msg_txt, "をやったか") or
          check_text_terminate_string(line_msg_txt, "はやりましたか") or
          check_text_terminate_string(line_msg_txt, "はやったか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 過去 能動 肯定形 他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "をしていませんか") or
          check_text_terminate_string(line_msg_txt, "をしてませんか") or
          check_text_terminate_string(line_msg_txt, "をしてないか") or
          check_text_terminate_string(line_msg_txt, "はしていませんか") or
          check_text_terminate_string(line_msg_txt, "はしてませんか") or
          check_text_terminate_string(line_msg_txt, "はしてないか") or
          check_text_terminate_string(line_msg_txt, "していませんか") or
          check_text_terminate_string(line_msg_txt, "してませんか") or
          check_text_terminate_string(line_msg_txt, "してないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 過去 能動 否定形 他者の行為・行動について>"
    elif (check_text_terminate_string(line_msg_txt, "はされていますか") or
          check_text_terminate_string(line_msg_txt, "されていますか") or
          check_text_terminate_string(line_msg_txt, "されてますか") or
          check_text_terminate_string(line_msg_txt, "されてますか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在 受動 肯定形 他者の行為・行動について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "はされていませんか") or
          check_text_terminate_string(line_msg_txt, "されていませんか") or
          check_text_terminate_string(line_msg_txt, "されてませんか") or
          check_text_terminate_string(line_msg_txt, "されていないか") or
          check_text_terminate_string(line_msg_txt, "されてないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在 受動 否定形 他者の行為・行動について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "はされていましたか") or
          check_text_terminate_string(line_msg_txt, "はされてましたか") or
          check_text_terminate_string(line_msg_txt, "されてましたか") or
          check_text_terminate_string(line_msg_txt, "されてたか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在 受動 肯定形 他者の行為・行動について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "はされていませんでしたか") or
          check_text_terminate_string(line_msg_txt, "はされていなかったか") or
          check_text_terminate_string(line_msg_txt, "されていませんでしたか") or
          check_text_terminate_string(line_msg_txt, "されていなかったか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 現在 受動 否定形 他者の行為・行動について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "だったですか") or
          check_text_terminate_string(line_msg_txt, "だったか") or
          check_text_terminate_string(line_msg_txt, "でしたか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 過去完了 肯定形 他者の状況・状態について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "ではなかったですか") or
          check_text_terminate_string(line_msg_txt, "ではなかったか") or
          check_text_terminate_string(line_msg_txt, "でなかったか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 過去完了 否定形 他者の状況・状態について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "をしなさい") or
          check_text_terminate_string(line_msg_txt, "をしろ") or
          check_text_terminate_string(line_msg_txt, "はしなさい") or
          check_text_terminate_string(line_msg_txt, "はしろ") or
          check_text_terminate_string(line_msg_txt, "しなさい") or
          check_text_terminate_string(line_msg_txt, "しろ")):
            extrct_intnt_rslt = "<指示＆命令>"
    elif (check_text_terminate_string(line_msg_txt, "をしなければならない") or
          check_text_terminate_string(line_msg_txt, "をしなければ") or
          check_text_terminate_string(line_msg_txt, "をしないといけないです") or
          check_text_terminate_string(line_msg_txt, "をしないといけない") or
          check_text_terminate_string(line_msg_txt, "をしなきゃいけないです") or
          check_text_terminate_string(line_msg_txt, "をしなきゃいけない") or
          check_text_terminate_string(line_msg_txt, "をしなきゃならない") or
          check_text_terminate_string(line_msg_txt, "をしなきゃ") or
          check_text_terminate_string(line_msg_txt, "はしなければならない") or
          check_text_terminate_string(line_msg_txt, "はしなければ") or
          check_text_terminate_string(line_msg_txt, "はしないといけないです") or
          check_text_terminate_string(line_msg_txt, "はしないといけない") or
          check_text_terminate_string(line_msg_txt, "はしなきゃいけないです") or
          check_text_terminate_string(line_msg_txt, "はしなきゃいけない") or
          check_text_terminate_string(line_msg_txt, "はしなきゃならない") or
          check_text_terminate_string(line_msg_txt, "はしなきゃ") or
          check_text_terminate_string(line_msg_txt, "しなければならない") or
          check_text_terminate_string(line_msg_txt, "しなければ") or
          check_text_terminate_string(line_msg_txt, "しないといけないです") or
          check_text_terminate_string(line_msg_txt, "しないといけない") or
          check_text_terminate_string(line_msg_txt, "しなきゃいけないです") or
          check_text_terminate_string(line_msg_txt, "しなきゃいけない") or
          check_text_terminate_string(line_msg_txt, "しなきゃならない") or
          check_text_terminate_string(line_msg_txt, "しなきゃ")):
            extrct_intnt_rslt = "<強制＆勧告 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "がしなければならない") or
          check_text_terminate_string(line_msg_txt, "がしなければ") or
          check_text_terminate_string(line_msg_txt, "がしないといけないです") or
          check_text_terminate_string(line_msg_txt, "がしないといけない") or
          check_text_terminate_string(line_msg_txt, "がしなきゃいけないです") or
          check_text_terminate_string(line_msg_txt, "がしなきゃいけない") or
          check_text_terminate_string(line_msg_txt, "がしなきゃならない") or
          check_text_terminate_string(line_msg_txt, "がしなきゃ")):
            extrct_intnt_rslt = "<強制＆勧告 肯定形 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "はしてはならない") or
          check_text_terminate_string(line_msg_txt, "はしてはいけない") or
          check_text_terminate_string(line_msg_txt, "はしたらいけない") or
          check_text_terminate_string(line_msg_txt, "はしちゃいけない") or
          check_text_terminate_string(line_msg_txt, "をしてはならない") or
          check_text_terminate_string(line_msg_txt, "をしてはいけない") or
          check_text_terminate_string(line_msg_txt, "をしたらいけない") or
          check_text_terminate_string(line_msg_txt, "をしちゃいけない") or
          check_text_terminate_string(line_msg_txt, "してはならない") or
          check_text_terminate_string(line_msg_txt, "してはいけない") or
          check_text_terminate_string(line_msg_txt, "したらいけない") or
          check_text_terminate_string(line_msg_txt, "しちゃいけない")):
            extrct_intnt_rslt = "<強制＆勧告 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "がしてはならない") or
          check_text_terminate_string(line_msg_txt, "がしてはいけない") or
          check_text_terminate_string(line_msg_txt, "がしたらいけない") or
          check_text_terminate_string(line_msg_txt, "がしちゃいけない")):
            extrct_intnt_rslt = "<強制＆勧告 否定形 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "はしなければならないのですか") or
          check_text_terminate_string(line_msg_txt, "はしなければならないんですか") or
          check_text_terminate_string(line_msg_txt, "はしなければならないですか") or
          check_text_terminate_string(line_msg_txt, "はしなければいけないですか") or
          check_text_terminate_string(line_msg_txt, "はしないといけないですか") or
          check_text_terminate_string(line_msg_txt, "はしなきゃいけないですか") or
          check_text_terminate_string(line_msg_txt, "はしなきゃいけないか") or
          check_text_terminate_string(line_msg_txt, "はしなきゃならないか") or
          check_text_terminate_string(line_msg_txt, "をしなければならないのですか") or
          check_text_terminate_string(line_msg_txt, "をしなければならないんですか") or
          check_text_terminate_string(line_msg_txt, "をしなければならないですか") or
          check_text_terminate_string(line_msg_txt, "をしなければいけないですか") or
          check_text_terminate_string(line_msg_txt, "をしないといけないですか") or
          check_text_terminate_string(line_msg_txt, "をしなきゃいけないですか") or
          check_text_terminate_string(line_msg_txt, "をしなきゃいけないか") or
          check_text_terminate_string(line_msg_txt, "をしなきゃならないか") or
          check_text_terminate_string(line_msg_txt, "しなければならないのですか") or
          check_text_terminate_string(line_msg_txt, "しなければならないんですか") or
          check_text_terminate_string(line_msg_txt, "しなければならないですか") or
          check_text_terminate_string(line_msg_txt, "しなければいけないですか") or
          check_text_terminate_string(line_msg_txt, "しないといけないですか") or
          check_text_terminate_string(line_msg_txt, "しなきゃいけないですか") or
          check_text_terminate_string(line_msg_txt, "しなきゃいけないか") or
          check_text_terminate_string(line_msg_txt, "しなきゃならないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 強制・勧告について>"
    elif (check_text_terminate_string(line_msg_txt, "がしなければならないのですか") or
          check_text_terminate_string(line_msg_txt, "がしなければならないんですか") or
          check_text_terminate_string(line_msg_txt, "がしなければならないのか") or
          check_text_terminate_string(line_msg_txt, "がしなければならないか") or
          check_text_terminate_string(line_msg_txt, "がしないといけないですか") or
          check_text_terminate_string(line_msg_txt, "がしないといけないか") or
          check_text_terminate_string(line_msg_txt, "がしなきゃいけないですか") or
          check_text_terminate_string(line_msg_txt, "がしなきゃいけないのか") or
          check_text_terminate_string(line_msg_txt, "がしなきゃいけないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 強制・勧告について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "はしてはならないのか") or
          check_text_terminate_string(line_msg_txt, "はしてはならないか") or
          check_text_terminate_string(line_msg_txt, "はしてはいけないか") or
          check_text_terminate_string(line_msg_txt, "はしたらいけないか") or
          check_text_terminate_string(line_msg_txt, "はしちゃいけないか") or
          check_text_terminate_string(line_msg_txt, "をしてはならないのか") or
          check_text_terminate_string(line_msg_txt, "をしてはならないか") or
          check_text_terminate_string(line_msg_txt, "をしてはいけないか") or
          check_text_terminate_string(line_msg_txt, "をしたらいけないか") or
          check_text_terminate_string(line_msg_txt, "をしちゃいけないか") or
          check_text_terminate_string(line_msg_txt, "してはならないのか") or
          check_text_terminate_string(line_msg_txt, "してはならないか") or
          check_text_terminate_string(line_msg_txt, "してはいけないか") or
          check_text_terminate_string(line_msg_txt, "したらいけないか") or
          check_text_terminate_string(line_msg_txt, "しちゃいけないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 強制・勧告について>"
    elif (check_text_terminate_string(line_msg_txt, "がしてはならないのか") or
          check_text_terminate_string(line_msg_txt, "がしてはならないか") or
          check_text_terminate_string(line_msg_txt, "がしてはいけないか") or
          check_text_terminate_string(line_msg_txt, "がしたらいけないか") or
          check_text_terminate_string(line_msg_txt, "がしちゃいけないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 強制・勧告について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "はするべきです") or
          check_text_terminate_string(line_msg_txt, "をするべきです") or
          check_text_terminate_string(line_msg_txt, "はすべきです") or
          check_text_terminate_string(line_msg_txt, "をすべきです") or
          check_text_terminate_string(line_msg_txt, "するべきです") or
          check_text_terminate_string(line_msg_txt, "すべきです")):
            extrct_intnt_rslt = "<宣言＆表明 肯定形 行為・行動の是非について>"
    elif (check_text_terminate_string(line_msg_txt, "はするべきではないです") or
          check_text_terminate_string(line_msg_txt, "をするべきではないです") or
          check_text_terminate_string(line_msg_txt, "はすべきではないです") or
          check_text_terminate_string(line_msg_txt, "をすべきではないです") or
          check_text_terminate_string(line_msg_txt, "はすべきではないです") or
          check_text_terminate_string(line_msg_txt, "をすべきではないです") or
          check_text_terminate_string(line_msg_txt, "するべきではないです") or
          check_text_terminate_string(line_msg_txt, "するべきでない") or
          check_text_terminate_string(line_msg_txt, "すべきでない")):
            extrct_intnt_rslt = "<宣言＆表明 否定形 行為・行動の是非について>"
    elif (check_text_terminate_string(line_msg_txt, "をするべきでしょうか") or
          check_text_terminate_string(line_msg_txt, "はするべきでしょうか") or
          check_text_terminate_string(line_msg_txt, "をすべきでしょうか") or
          check_text_terminate_string(line_msg_txt, "はすべきでしょうか") or
          check_text_terminate_string(line_msg_txt, "するべきでしょうか") or
          check_text_terminate_string(line_msg_txt, "すべきでしょうか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 行為・行動の是非について>"
    elif (check_text_terminate_string(line_msg_txt, "をするべきではないのでしょうか") or
          check_text_terminate_string(line_msg_txt, "はするべきではないのでしょうか") or
          check_text_terminate_string(line_msg_txt, "をすべきではないのでしょうか") or
          check_text_terminate_string(line_msg_txt, "はすべきではないのでしょうか") or
          check_text_terminate_string(line_msg_txt, "するべきではないのでしょうか") or
          check_text_terminate_string(line_msg_txt, "すべきではないのでしょうか") or
          check_text_terminate_string(line_msg_txt, "すべきでないのでしょうか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 行為・行動の是非について>"
    elif (check_text_terminate_string(line_msg_txt, "をしても良いです") or
          check_text_terminate_string(line_msg_txt, "をしてもいいです") or
          check_text_terminate_string(line_msg_txt, "をして良いです") or
          check_text_terminate_string(line_msg_txt, "をしていいです") or
          check_text_terminate_string(line_msg_txt, "をしても良い") or
          check_text_terminate_string(line_msg_txt, "をしてもいい") or
          check_text_terminate_string(line_msg_txt, "をして良い") or
          check_text_terminate_string(line_msg_txt, "をしていい") or
          check_text_terminate_string(line_msg_txt, "はしても良いです") or
          check_text_terminate_string(line_msg_txt, "はしてもいいです") or
          check_text_terminate_string(line_msg_txt, "はして良いです") or
          check_text_terminate_string(line_msg_txt, "はしていいです") or
          check_text_terminate_string(line_msg_txt, "はしても良い") or
          check_text_terminate_string(line_msg_txt, "はしてもいい") or
          check_text_terminate_string(line_msg_txt, "はして良い") or
          check_text_terminate_string(line_msg_txt, "はしていい") or
          check_text_terminate_string(line_msg_txt, "をやっても良いです") or
          check_text_terminate_string(line_msg_txt, "をやってもいいです") or
          check_text_terminate_string(line_msg_txt, "はやっても良いです") or
          check_text_terminate_string(line_msg_txt, "はやってもいいです") or
          check_text_terminate_string(line_msg_txt, "しても良いです") or
          check_text_terminate_string(line_msg_txt, "してもいいです") or
          check_text_terminate_string(line_msg_txt, "して良いです") or
          check_text_terminate_string(line_msg_txt, "していいです") or
          check_text_terminate_string(line_msg_txt, "しても良い") or
          check_text_terminate_string(line_msg_txt, "してもいい") or
          check_text_terminate_string(line_msg_txt, "して良い") or
          check_text_terminate_string(line_msg_txt, "していい")):
            extrct_intnt_rslt = "<許容＆許可>"
    elif (check_text_terminate_string(line_msg_txt, "をしないように") or
          check_text_terminate_string(line_msg_txt, "をしないよう") or
          check_text_terminate_string(line_msg_txt, "をするな") or
          check_text_terminate_string(line_msg_txt, "をしてはいけない") or
          check_text_terminate_string(line_msg_txt, "をしちゃいけない") or
          check_text_terminate_string(line_msg_txt, "はしないように") or
          check_text_terminate_string(line_msg_txt, "はしないよう") or
          check_text_terminate_string(line_msg_txt, "はするな") or
          check_text_terminate_string(line_msg_txt, "はしてはいけない") or
          check_text_terminate_string(line_msg_txt, "はしちゃいけない") or
          check_text_terminate_string(line_msg_txt, "をやってはいけない") or
          check_text_terminate_string(line_msg_txt, "をやっちゃいけない") or
          check_text_terminate_string(line_msg_txt, "はやってはいけない") or
          check_text_terminate_string(line_msg_txt, "はやっちゃいけない") or
          check_text_terminate_string(line_msg_txt, "をしちゃ駄目だ") or
          check_text_terminate_string(line_msg_txt, "をしちゃだめだ") or
          check_text_terminate_string(line_msg_txt, "をしちゃダメだ") or
          check_text_terminate_string(line_msg_txt, "はしちゃ駄目だ") or
          check_text_terminate_string(line_msg_txt, "はしちゃだめだ") or
          check_text_terminate_string(line_msg_txt, "をしちゃ駄目") or
          check_text_terminate_string(line_msg_txt, "をしちゃだめ") or
          check_text_terminate_string(line_msg_txt, "をしちゃダメ") or
          check_text_terminate_string(line_msg_txt, "はしちゃ駄目") or
          check_text_terminate_string(line_msg_txt, "はしちゃだめ") or
          check_text_terminate_string(line_msg_txt, "しないように") or
          check_text_terminate_string(line_msg_txt, "しないよう") or
          check_text_terminate_string(line_msg_txt, "するな") or
          check_text_terminate_string(line_msg_txt, "してはいけない") or
          check_text_terminate_string(line_msg_txt, "しちゃいけない") or
          check_text_terminate_string(line_msg_txt, "はいけない") or
          check_text_terminate_string(line_msg_txt, "しちゃ駄目だ") or
          check_text_terminate_string(line_msg_txt, "しちゃだめだ") or
          check_text_terminate_string(line_msg_txt, "しちゃダメだ") or
          check_text_terminate_string(line_msg_txt, "しちゃ駄目") or
          check_text_terminate_string(line_msg_txt, "しちゃだめ") or
          check_text_terminate_string(line_msg_txt, "しちゃダメ")):
            extrct_intnt_rslt = "<禁止＆制限>"
    elif (check_text_terminate_string(line_msg_txt, "がしないように") or
          check_text_terminate_string(line_msg_txt, "がしないよう") or
          check_text_terminate_string(line_msg_txt, "がするな") or
          check_text_terminate_string(line_msg_txt, "がやってはいけない") or
          check_text_terminate_string(line_msg_txt, "がやっちゃいけない") or
          check_text_terminate_string(line_msg_txt, "がやっちゃ駄目だ") or
          check_text_terminate_string(line_msg_txt, "がやっちゃだめだ") or
          check_text_terminate_string(line_msg_txt, "がやっちゃダメだ") or
          check_text_terminate_string(line_msg_txt, "がやっちゃ駄目") or
          check_text_terminate_string(line_msg_txt, "がやっちゃだめ") or
          check_text_terminate_string(line_msg_txt, "がやっちゃダメ") or
          check_text_terminate_string(line_msg_txt, "がしちゃ駄目だ") or
          check_text_terminate_string(line_msg_txt, "がしちゃだめだ") or
          check_text_terminate_string(line_msg_txt, "がしちゃダメだ") or
          check_text_terminate_string(line_msg_txt, "がしちゃ駄目") or
          check_text_terminate_string(line_msg_txt, "がしちゃだめ") or
          check_text_terminate_string(line_msg_txt, "がしちゃダメ")):
            extrct_intnt_rslt = "<禁止＆制限 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "をしてはいけませんか") or
          check_text_terminate_string(line_msg_txt, "をしてはいけないですか") or
          check_text_terminate_string(line_msg_txt, "をしてはいけないか") or
          check_text_terminate_string(line_msg_txt, "はしてはいけませんか") or
          check_text_terminate_string(line_msg_txt, "はしてはいけないですか") or
          check_text_terminate_string(line_msg_txt, "はしてはいけないか") or
          check_text_terminate_string(line_msg_txt, "をやってはいけませんか") or
          check_text_terminate_string(line_msg_txt, "をやってはいけないですか") or
          check_text_terminate_string(line_msg_txt, "をやってはいけないか") or
          check_text_terminate_string(line_msg_txt, "をやっちゃ駄目か") or
          check_text_terminate_string(line_msg_txt, "をやっちゃだめか") or
          check_text_terminate_string(line_msg_txt, "をやっちゃダメか") or
          check_text_terminate_string(line_msg_txt, "をしちゃ駄目ですか") or
          check_text_terminate_string(line_msg_txt, "をしちゃだめですか") or
          check_text_terminate_string(line_msg_txt, "をしちゃダメですか") or
          check_text_terminate_string(line_msg_txt, "はしちゃ駄目ですか") or
          check_text_terminate_string(line_msg_txt, "はしちゃだめですか") or
          check_text_terminate_string(line_msg_txt, "はしちゃダメですか") or
          check_text_terminate_string(line_msg_txt, "をしちゃ駄目か") or
          check_text_terminate_string(line_msg_txt, "をしちゃだめか") or
          check_text_terminate_string(line_msg_txt, "をしちゃダメか") or
          check_text_terminate_string(line_msg_txt, "はしちゃ駄目か") or
          check_text_terminate_string(line_msg_txt, "はしちゃだめか") or
          check_text_terminate_string(line_msg_txt, "はしちゃダメか") or
          check_text_terminate_string(line_msg_txt, "しちゃ駄目か") or
          check_text_terminate_string(line_msg_txt, "しちゃだめか") or
          check_text_terminate_string(line_msg_txt, "しちゃダメか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 禁止・制限事項について>"
    elif (check_text_terminate_string(line_msg_txt, "がしてはいけませんか") or
          check_text_terminate_string(line_msg_txt, "がしてはいけないか") or
          check_text_terminate_string(line_msg_txt, "がやってはいけないか") or
          check_text_terminate_string(line_msg_txt, "がやっちゃ駄目か") or
          check_text_terminate_string(line_msg_txt, "がやっちゃだめか") or
          check_text_terminate_string(line_msg_txt, "がやっちゃダメか") or
          check_text_terminate_string(line_msg_txt, "がしちゃ駄目か") or
          check_text_terminate_string(line_msg_txt, "がしちゃだめか") or
          check_text_terminate_string(line_msg_txt, "がしちゃダメか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 禁止・制限事項について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "をして下さい") or
          check_text_terminate_string(line_msg_txt, "をしてください") or
          check_text_terminate_string(line_msg_txt, "をしてくれ") or
          check_text_terminate_string(line_msg_txt, "をして") or
          check_text_terminate_string(line_msg_txt, "はして下さい") or
          check_text_terminate_string(line_msg_txt, "はしてください") or
          check_text_terminate_string(line_msg_txt, "して下さい") or
          check_text_terminate_string(line_msg_txt, "してください") or
          check_text_terminate_string(line_msg_txt, "はしてくれ") or
          check_text_terminate_string(line_msg_txt, "はして") or 
          check_text_terminate_string(line_msg_txt, "してくれ")):
            extrct_intnt_rslt = "<依頼＆要求>"
    elif (check_text_terminate_string(line_msg_txt, "がして下さい") or
          check_text_terminate_string(line_msg_txt, "がしてください") or
          check_text_terminate_string(line_msg_txt, "がしてくれ") or
          check_text_terminate_string(line_msg_txt, "がして")):
            extrct_intnt_rslt = "<依頼＆要求 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "をして下さいますか") or
          check_text_terminate_string(line_msg_txt, "をしてくださいますか") or
          check_text_terminate_string(line_msg_txt, "して下さいますか") or
          check_text_terminate_string(line_msg_txt, "してくださいますか") or
          check_text_terminate_string(line_msg_txt, "をしてくれますか") or
          check_text_terminate_string(line_msg_txt, "をしてくれますか") or
          check_text_terminate_string(line_msg_txt, "はしてくれますか") or
          check_text_terminate_string(line_msg_txt, "してくれるか") or
          check_text_terminate_string(line_msg_txt, "をやって下さいますか") or
          check_text_terminate_string(line_msg_txt, "をやってくださいますか") or
          check_text_terminate_string(line_msg_txt, "をやってくれますか") or
          check_text_terminate_string(line_msg_txt, "をやってくれるか") or
          check_text_terminate_string(line_msg_txt, "はやって下さいますか") or
          check_text_terminate_string(line_msg_txt, "はやってくださいますか") or
          check_text_terminate_string(line_msg_txt, "はやってくれますか") or
          check_text_terminate_string(line_msg_txt, "はやってくれるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 依頼・要求について>"
    elif (check_text_terminate_string(line_msg_txt, "をして下さいますか") or
          check_text_terminate_string(line_msg_txt, "をしてくださいますか") or
          check_text_terminate_string(line_msg_txt, "して下さいますか") or
          check_text_terminate_string(line_msg_txt, "してくださいますか") or
          check_text_terminate_string(line_msg_txt, "をしてくれますか") or
          check_text_terminate_string(line_msg_txt, "をしてくれますか") or
          check_text_terminate_string(line_msg_txt, "はしてくれますか") or
          check_text_terminate_string(line_msg_txt, "してくれるか") or
          check_text_terminate_string(line_msg_txt, "をやって下さいますか") or
          check_text_terminate_string(line_msg_txt, "をやってくださいますか") or
          check_text_terminate_string(line_msg_txt, "をやってくれますか") or
          check_text_terminate_string(line_msg_txt, "をやってくれるか") or
          check_text_terminate_string(line_msg_txt, "はやって下さいますか") or
          check_text_terminate_string(line_msg_txt, "はやってくださいますか") or
          check_text_terminate_string(line_msg_txt, "はやってくれますか") or
          check_text_terminate_string(line_msg_txt, "はやってくれるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 依頼・要求について>"
    elif (check_text_terminate_string(line_msg_txt, "がして下さいますか") or
          check_text_terminate_string(line_msg_txt, "がしてくださいますか") or
          check_text_terminate_string(line_msg_txt, "がしてくれますか") or
          check_text_terminate_string(line_msg_txt, "がやってくれますか") or
          check_text_terminate_string(line_msg_txt, "がやってくれるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 依頼・要求について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "がして下さいますか") or
          check_text_terminate_string(line_msg_txt, "がしてくださいますか") or
          check_text_terminate_string(line_msg_txt, "がしてくれますか") or
          check_text_terminate_string(line_msg_txt, "がやってくれますか") or
          check_text_terminate_string(line_msg_txt, "がやってくれるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 依頼・要求について 特定個人についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "をお願い致します") or
          check_text_terminate_string(line_msg_txt, "をお願いいたします") or
          check_text_terminate_string(line_msg_txt, "をお願いします") or
          check_text_terminate_string(line_msg_txt, "をお願い")):
            extrct_intnt_rslt = "<依頼＆依願>"
    elif (check_text_terminate_string(line_msg_txt, "しいです")):
            extrct_intnt_rslt = "<紹介＆説明＆提示 形容的な表現>"
    elif check_text_terminate_string(line_msg_txt, "だ"):
            extrct_intnt_rslt = "<宣言＆表明＆紹介＆説明＆提示 誇示・顕示して>"
    elif (check_text_terminate_string(line_msg_txt, "でしょう") or
          check_text_terminate_string(line_msg_txt, "だろう") or
          check_text_terminate_string(line_msg_txt, "だろ")):
            extrct_intnt_rslt = "<推定＆推測＆推量 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "ではないでしょう") or
          check_text_terminate_string(line_msg_txt, "ではないだろう") or
          check_text_terminate_string(line_msg_txt, "ではないだろ")):
            extrct_intnt_rslt = "<推定＆推測＆推量 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "でしょうか") or
          check_text_terminate_string(line_msg_txt, "だろうか") or
          check_text_terminate_string(line_msg_txt, "だろか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 推定・推測・推量について>"
    elif (check_text_terminate_string(line_msg_txt, "ではないでしょうか") or
          check_text_terminate_string(line_msg_txt, "ではないだろうか") or
          check_text_terminate_string(line_msg_txt, "ではないだろか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 推定・推測・推量について>"
    elif (check_text_terminate_string(line_msg_txt, "だそうです") or
          check_text_terminate_string(line_msg_txt, "だそう")):
            extrct_intnt_rslt = "<報告＆連絡 肯定形 推定・推測・推量して>"
    elif (check_text_terminate_string(line_msg_txt, "ではないそうです") or
          check_text_terminate_string(line_msg_txt, "ではないそう")):
            extrct_intnt_rslt = "<報告＆連絡 否定形 推定・推測・推量して>"
    elif (check_text_terminate_string(line_msg_txt, "はいます") or
          check_text_terminate_string(line_msg_txt, "はいる")):
            extrct_intnt_rslt = "<報告＆連絡 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "がいます") or
          check_text_terminate_string(line_msg_txt, "がいる")):
            extrct_intnt_rslt = "<報告＆連絡 肯定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "はいません") or
          check_text_terminate_string(line_msg_txt, "はいない")):
            extrct_intnt_rslt = "<報告＆連絡 否定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "がいません") or
          check_text_terminate_string(line_msg_txt, "がいない")):
            extrct_intnt_rslt = "<報告＆連絡 否定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "はいますか") or
          check_text_terminate_string(line_msg_txt, "はいるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "がいますか") or
          check_text_terminate_string(line_msg_txt, "がいるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "はいませんか") or
          check_text_terminate_string(line_msg_txt, "はいないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "がいませんか") or
          check_text_terminate_string(line_msg_txt, "がいないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "にいます") or
          check_text_terminate_string(line_msg_txt, "にいる")):
            extrct_intnt_rslt = "<報告＆連絡 肯定形 所在・場所について>"
    elif (check_text_terminate_string(line_msg_txt, "にいません") or
          check_text_terminate_string(line_msg_txt, "にいない")):
            extrct_intnt_rslt = "<報告＆連絡 否定形 所在・場所について>"
    elif (check_text_terminate_string(line_msg_txt, "はあります") or
          check_text_terminate_string(line_msg_txt, "はある")):
            extrct_intnt_rslt = "<報告＆連絡 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "があります") or
          check_text_terminate_string(line_msg_txt, "がある")):
            extrct_intnt_rslt = "<報告＆連絡 肯定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "はありません") or
          check_text_terminate_string(line_msg_txt, "はない")):
            extrct_intnt_rslt = "<報告＆連絡 否定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "がありません") or
          check_text_terminate_string(line_msg_txt, "がない")):
            extrct_intnt_rslt = "<報告＆連絡 否定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "にいますか") or
          check_text_terminate_string(line_msg_txt, "にいるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "にいませんか") or
          check_text_terminate_string(line_msg_txt, "にいないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "はありますか") or
          check_text_terminate_string(line_msg_txt, "はあるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "がありますか") or
          check_text_terminate_string(line_msg_txt, "があるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "はありませんか") or
          check_text_terminate_string(line_msg_txt, "はあるか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 存在の有無について>"
    elif (check_text_terminate_string(line_msg_txt, "がありませんか") or
          check_text_terminate_string(line_msg_txt, "がないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 存在の有無について 特定個人・個物についてのみ>"
    elif (check_text_terminate_string(line_msg_txt, "で御座います") or
          check_text_terminate_string(line_msg_txt, "でございます") or
          check_text_terminate_string(line_msg_txt, "であります") or
          check_text_terminate_string(line_msg_txt, "です")):
            extrct_intnt_rslt = "<宣言＆表明＆紹介＆説明＆提示 肯定形 漠然として>"
    elif (check_text_terminate_string(line_msg_txt, "では御座いません") or
          check_text_terminate_string(line_msg_txt, "ではございません") or
          check_text_terminate_string(line_msg_txt, "ではありません") or
          check_text_terminate_string(line_msg_txt, "ではないです")):
            extrct_intnt_rslt = "<宣言＆表明＆紹介＆説明＆提示 否定形 漠然として>"
    elif (check_text_terminate_string(line_msg_txt, "で御座いますか") or
          check_text_terminate_string(line_msg_txt, "でございますか") or
          check_text_terminate_string(line_msg_txt, "でありますか") or
          check_text_terminate_string(line_msg_txt, "ですか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 漠然として>"
    elif (check_text_terminate_string(line_msg_txt, "では御座いませんか") or
          check_text_terminate_string(line_msg_txt, "ではございませんか") or
          check_text_terminate_string(line_msg_txt, "ではありませんか") or
          check_text_terminate_string(line_msg_txt, "ではないですか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 漠然として>"
    elif (check_text_terminate_string(line_msg_txt, "で御座いましたか") or
          check_text_terminate_string(line_msg_txt, "でございましたか") or
          check_text_terminate_string(line_msg_txt, "でありましたか") or
          check_text_terminate_string(line_msg_txt, "でしたか") or
          check_text_terminate_string(line_msg_txt, "だったか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 過去 肯定形 漠然として 他者の状況・状態について 物事の進行・進捗について>"
    elif (check_text_terminate_string(line_msg_txt, "という事で御座います") or
          check_text_terminate_string(line_msg_txt, "という事でございます") or
          check_text_terminate_string(line_msg_txt, "ということで御座います") or
          check_text_terminate_string(line_msg_txt, "ということでございます") or
          check_text_terminate_string(line_msg_txt, "という事であります") or
          check_text_terminate_string(line_msg_txt, "ということであります") or
          check_text_terminate_string(line_msg_txt, "という事です") or
          check_text_terminate_string(line_msg_txt, "ということです") or
          check_text_terminate_string(line_msg_txt, "って事です") or
          check_text_terminate_string(line_msg_txt, "ってことです")):
            extrct_intnt_rslt = "<紹介＆説明＆提示 肯定形 なんらかの内容についての叙述>"
    elif (check_text_terminate_string(line_msg_txt, "という事では御座いません") or
          check_text_terminate_string(line_msg_txt, "という事ではございません") or
          check_text_terminate_string(line_msg_txt, "ということでは御座いません") or
          check_text_terminate_string(line_msg_txt, "ということではございません") or
          check_text_terminate_string(line_msg_txt, "という事ではありません") or
          check_text_terminate_string(line_msg_txt, "ということではありません") or
          check_text_terminate_string(line_msg_txt, "って事ではないです") or
          check_text_terminate_string(line_msg_txt, "ってことではないです")):
            extrct_intnt_rslt = "<紹介＆説明＆提示 否定形 なんらかの内容についての叙述>"
    elif (check_text_terminate_string(line_msg_txt, "という事で御座いますか") or
          check_text_terminate_string(line_msg_txt, "という事でございますか") or
          check_text_terminate_string(line_msg_txt, "ということで御座いますか") or
          check_text_terminate_string(line_msg_txt, "ということでございますか") or
          check_text_terminate_string(line_msg_txt, "という事でありますか") or
          check_text_terminate_string(line_msg_txt, "ということでありますか") or
          check_text_terminate_string(line_msg_txt, "という事ですか") or
          check_text_terminate_string(line_msg_txt, "ということですか") or
          check_text_terminate_string(line_msg_txt, "って事ですか") or
          check_text_terminate_string(line_msg_txt, "ってことですか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 なんらかの内容についての叙述>"
    elif (check_text_terminate_string(line_msg_txt, "という事では御座いませんか") or
          check_text_terminate_string(line_msg_txt, "という事ではございませんか") or
          check_text_terminate_string(line_msg_txt, "ということでは御座いませんか") or
          check_text_terminate_string(line_msg_txt, "ということではございませんか") or
          check_text_terminate_string(line_msg_txt, "という事ではありませんか") or
          check_text_terminate_string(line_msg_txt, "ということではありませんか") or
          check_text_terminate_string(line_msg_txt, "って事ではないのですか") or
          check_text_terminate_string(line_msg_txt, "ってことではなのですか") or
          check_text_terminate_string(line_msg_txt, "って事ではないんですか") or
          check_text_terminate_string(line_msg_txt, "ってことではないんですか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 なんらかの内容についての叙述>"
    elif (check_text_terminate_string(line_msg_txt, "は大丈夫です") or
          check_text_terminate_string(line_msg_txt, "は大丈夫だ") or
          check_text_terminate_string(line_msg_txt, "は大丈夫")):
            extrct_intnt_rslt = "<宣言＆表明 肯定形 安否・健康状態について>"
    elif (check_text_terminate_string(line_msg_txt, "は大丈夫ではない") or
          check_text_terminate_string(line_msg_txt, "は大丈夫でない") or
          check_text_terminate_string(line_msg_txt, "は大丈夫じゃない")):
            extrct_intnt_rslt = "<宣言＆表明 否定形 安否・健康状態について>"
    elif (check_text_terminate_string(line_msg_txt, "は大丈夫でしょうか") or
          check_text_terminate_string(line_msg_txt, "は大丈夫ですか") or
          check_text_terminate_string(line_msg_txt, "は大丈夫か")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 安否・健康状態について>"
    elif (check_text_terminate_string(line_msg_txt, "は大丈夫ではないのでしょうか") or
          check_text_terminate_string(line_msg_txt, "は大丈夫ではないんですか") or
          check_text_terminate_string(line_msg_txt, "は大丈夫じゃないんですか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 安否・健康状態について>"
    elif (check_text_terminate_string(line_msg_txt, "が必要です") or
          check_text_terminate_string(line_msg_txt, "は必要です") or
          check_text_terminate_string(line_msg_txt, "が必要だ") or
          check_text_terminate_string(line_msg_txt, "は必要だ") or
          check_text_terminate_string(line_msg_txt, "が必要") or
          check_text_terminate_string(line_msg_txt, "は必要") or
          check_text_terminate_string(line_msg_txt, "が要ります") or
          check_text_terminate_string(line_msg_txt, "は要ります") or
          check_text_terminate_string(line_msg_txt, "が要る") or
          check_text_terminate_string(line_msg_txt, "は要る")):
            extrct_intnt_rslt = "<宣言＆表明 肯定形 物事の要否について>"
    elif (check_text_terminate_string(line_msg_txt, "が不要です") or
          check_text_terminate_string(line_msg_txt, "は不要です") or
          check_text_terminate_string(line_msg_txt, "が不要だ") or
          check_text_terminate_string(line_msg_txt, "は不要だ") or
          check_text_terminate_string(line_msg_txt, "が不要") or
          check_text_terminate_string(line_msg_txt, "は不要") or
          check_text_terminate_string(line_msg_txt, "が要りません") or
          check_text_terminate_string(line_msg_txt, "は要りません") or
          check_text_terminate_string(line_msg_txt, "が要らない") or
          check_text_terminate_string(line_msg_txt, "は要らない")):
            extrct_intnt_rslt = "<宣言＆表明 否定形 物事の要否について>"
    elif (check_text_terminate_string(line_msg_txt, "が必要でしょうか") or
          check_text_terminate_string(line_msg_txt, "は必要でしょうか") or
          check_text_terminate_string(line_msg_txt, "が必要ですか") or
          check_text_terminate_string(line_msg_txt, "は必要ですか") or
          check_text_terminate_string(line_msg_txt, "が要りますでしょうか") or
          check_text_terminate_string(line_msg_txt, "は要りますでしょうか") or
          check_text_terminate_string(line_msg_txt, "が要りますか") or
          check_text_terminate_string(line_msg_txt, "は要りますか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 肯定形 物事の要否について>"
    elif (check_text_terminate_string(line_msg_txt, "が不要でしょうか") or
          check_text_terminate_string(line_msg_txt, "は不要でしょうか") or
          check_text_terminate_string(line_msg_txt, "が不要ですか") or
          check_text_terminate_string(line_msg_txt, "は不要ですか") or
          check_text_terminate_string(line_msg_txt, "が要りませんか") or
          check_text_terminate_string(line_msg_txt, "は要りませんか") or
          check_text_terminate_string(line_msg_txt, "が要らないのですか") or
          check_text_terminate_string(line_msg_txt, "は要らないのですか") or
          check_text_terminate_string(line_msg_txt, "が要らないのか") or
          check_text_terminate_string(line_msg_txt, "は要らないのか") or
          check_text_terminate_string(line_msg_txt, "が要らないか") or
          check_text_terminate_string(line_msg_txt, "は要らないか")):
            extrct_intnt_rslt = "<疑義＆質問＆確認 否定形 物事の要否について>"
    elif (check_text_terminate_string(line_msg_txt, "という事でしょう") or
          check_text_terminate_string(line_msg_txt, "ということでしょう")):
            extrct_intnt_rslt = "<推定＆推測＆推量 肯定形 進言・提言に近い>"
    elif (check_text_terminate_string(line_msg_txt, "という事ではないでしょう") or
          check_text_terminate_string(line_msg_txt, "ということではないでしょう")):
            extrct_intnt_rslt = "<推定＆推測＆推量 否定形 進言・提言に近い>"
    elif (check_text_terminate_string(line_msg_txt, "かも知れないです") or
          check_text_terminate_string(line_msg_txt, "かもしれないです") or
          check_text_terminate_string(line_msg_txt, "かも知れない") or
          check_text_terminate_string(line_msg_txt, "かもしれない")):
            extrct_intnt_rslt = "<推定＆推測＆推量 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "ではないかも知れないです") or
          check_text_terminate_string(line_msg_txt, "ではないかもしれないです") or
          check_text_terminate_string(line_msg_txt, "ではないかも知れない") or
          check_text_terminate_string(line_msg_txt, "ではないかもしれない")):
            extrct_intnt_rslt = "<推定＆推測＆推量 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "とは思っています") or
          check_text_terminate_string(line_msg_txt, "とは思ってます") or
          check_text_terminate_string(line_msg_txt, "とは思っている") or
          check_text_terminate_string(line_msg_txt, "とは思ってる") or
          check_text_terminate_string(line_msg_txt, "とは思う") or
          check_text_terminate_string(line_msg_txt, "と思っています") or
          check_text_terminate_string(line_msg_txt, "と思っている") or
          check_text_terminate_string(line_msg_txt, "と思ってる") or
          check_text_terminate_string(line_msg_txt, "と思う")):
            extrct_intnt_rslt = "<思慮＆考慮 現在 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "とは思っていません") or
          check_text_terminate_string(line_msg_txt, "とは思ってません") or
          check_text_terminate_string(line_msg_txt, "とは思っていない") or
          check_text_terminate_string(line_msg_txt, "とは思ってない") or
          check_text_terminate_string(line_msg_txt, "とは思わない") or
          check_text_terminate_string(line_msg_txt, "と思っていません") or
          check_text_terminate_string(line_msg_txt, "と思ってません") or
          check_text_terminate_string(line_msg_txt, "と思っていない") or
          check_text_terminate_string(line_msg_txt, "と思ってない") or
          check_text_terminate_string(line_msg_txt, "と思わない")):
            extrct_intnt_rslt = "<思慮＆考慮 現在 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "とは思っていました") or
          check_text_terminate_string(line_msg_txt, "とは思っていた") or
          check_text_terminate_string(line_msg_txt, "とは思ってた") or
          check_text_terminate_string(line_msg_txt, "と思っていました") or
          check_text_terminate_string(line_msg_txt, "と思っていた") or
          check_text_terminate_string(line_msg_txt, "と思ってた")):
            extrct_intnt_rslt = "<思慮＆考慮 過去 肯定形>"
    elif (check_text_terminate_string(line_msg_txt, "とは思っていませんでした") or
          check_text_terminate_string(line_msg_txt, "とは思っていなかった") or
          check_text_terminate_string(line_msg_txt, "とは思ってなかった") or
          check_text_terminate_string(line_msg_txt, "と思っていませんでした") or
          check_text_terminate_string(line_msg_txt, "と思っていなかった") or                           
          check_text_terminate_string(line_msg_txt, "と思ってなかった")):
            extrct_intnt_rslt = "<思慮＆考慮 過去 否定形>"
    elif (check_text_terminate_string(line_msg_txt, "らしいです") or
          check_text_terminate_string(line_msg_txt, "らしい")):
            extrct_intnt_rslt = "<感想＆感慨 肯定形 形容的な表現>"
    elif (check_text_terminate_string(line_msg_txt, "らしくないです") or
          check_text_terminate_string(line_msg_txt, "らしくない")):
            extrct_intnt_rslt = "<感想＆感慨 否定形 形容的な表現>"
    else:
            extrct_intnt_rslt = "<その他・不明>"
    return extrct_intnt_rslt


#ユーザーから送られるLINEメッセージの中からサブコンテント(＝発話の意図される内容 ＝副詞＆前置詞＆接続詞)を抽出する
def extract_subcontent(line_msg_txt):
    #メッセージの先頭部分からサブコンテントを抽出して、これを呼出し元に引渡しをする
    if   (check_text_start_string(line_msg_txt, "さて") or
          check_text_start_string(line_msg_txt, "ところで")):
            extrct_subcntnt_rslt = "<転換＆切替>"
    elif (check_text_start_string(line_msg_txt, "そして") or
          check_text_start_string(line_msg_txt, "それで") or
          check_text_start_string(line_msg_txt, "そんで")):
            extrct_subcntnt_rslt = "<結論＆結末>"
    elif (check_text_start_string(line_msg_txt, "加えて") or
          check_text_start_string(line_msg_txt, "更に") or
          check_text_start_string(line_msg_txt, "さらに") or
          check_text_start_string(line_msg_txt, "又") or
          check_text_start_string(line_msg_txt, "また")):
            extrct_subcntnt_rslt = "<添加＆追加>"
    elif (check_text_start_string(line_msg_txt, "多分") or
          check_text_start_string(line_msg_txt, "たぶん") or
          check_text_start_string(line_msg_txt, "恐らくは") or
          check_text_start_string(line_msg_txt, "おそらくは") or
          check_text_start_string(line_msg_txt, "恐らく") or
          check_text_start_string(line_msg_txt, "おそらく")):
            extrct_subcntnt_rslt = "<推定＆推測＆推量 揣摩＆憶測 理知・理性的に言う>"
    elif (check_text_start_string(line_msg_txt, "又は") or
          check_text_start_string(line_msg_txt, "または")):
            extrct_subcntnt_rslt = "<論理和>"
    elif (check_text_start_string(line_msg_txt, "且つ") or
          check_text_start_string(line_msg_txt, "かつ")):
            extrct_subcntnt_rslt = "<論理積>"
    elif (check_text_start_string(line_msg_txt, "得てして") or
          check_text_start_string(line_msg_txt, "えてして") or
          check_text_start_string(line_msg_txt, "概して") or
          check_text_start_string(line_msg_txt, "大抵は") or
          check_text_start_string(line_msg_txt, "大抵") or
          check_text_start_string(line_msg_txt, "大概は") or
          check_text_start_string(line_msg_txt, "大概")): 
            extrct_subcntnt_rslt = "<概要＆概略>"
    elif (check_text_start_string(line_msg_txt, "確実に") or
          check_text_start_string(line_msg_txt, "明らかに") or
          check_text_start_string(line_msg_txt, "多くの場合には") or
          check_text_start_string(line_msg_txt, "多くの場合は") or
          check_text_start_string(line_msg_txt, "多くの場合") or
          check_text_start_string(line_msg_txt, "多くは") or
          check_text_start_string(line_msg_txt, "多く") or
          check_text_start_string(line_msg_txt, "少なくとも") or
          check_text_start_string(line_msg_txt, "少なくても")):
            extrct_subcntnt_rslt = "<断定＆確定>"
    elif  check_text_start_string(line_msg_txt, "<大層"):
            extrct_subcntnt_rslt = "<程度強調 情緒・感情的に言う>"
    elif (check_text_start_string(line_msg_txt, "なので") or
          check_text_start_string(line_msg_txt, "ですから")):
            extrct_subcntnt_rslt = "<説得＆説明 事由＆理由＆事情＆状況>"
    elif check_text_start_string(line_msg_txt, "さては"):
            extrct_subcntnt_rslt = "<推定＆推測＆推量 確定＆断定 事実>"
    elif check_text_start_string(line_msg_txt, "もしや"):
            extrct_subcntnt_rslt = "<推定＆推測＆推量 揣摩＆憶測 仮定＆仮説>"
    elif (check_text_start_string(line_msg_txt, "もしも") or
          check_text_start_string(line_msg_txt, "もし")):
            extrct_subcntnt_rslt = "<仮定＆仮説 原因＆要因＆事情＆状況＆状態的>"
    elif (check_text_start_string(line_msg_txt, "例えば") or
          check_text_start_string(line_msg_txt, "たとえば") or
          check_text_start_string(line_msg_txt, "例すれば") or
          check_text_start_string(line_msg_txt, "例せば")):
            extrct_subcntnt_rslt = "<比喩＆類例>"
    elif (check_text_start_string(line_msg_txt, "類すれば") or
          check_text_start_string(line_msg_txt, "類せば")):
            extrct_subcntnt_rslt = "<仮定＆仮説 比較＆類似>"
    elif (check_text_start_string(line_msg_txt, "譬え") or
          check_text_start_string(line_msg_txt, "たとえ") or
          check_text_start_string(line_msg_txt, "仮に")):
            extrct_subcntnt_rslt = "<仮定＆仮説 特別・特例言及>"
    elif (check_text_start_string(line_msg_txt, "或いは") or
          check_text_start_string(line_msg_txt, "あるいは")):
            extrct_subcntnt_rslt = "<選択＆追求 可能性>"
    elif (check_text_start_string(line_msg_txt, "よしんば")):
            extrct_subcntnt_rslt = "<仮定＆仮説>"
    elif (check_text_start_string(line_msg_txt, "若しくは") or
          check_text_start_string(line_msg_txt, "もしくは") or
          check_text_start_string(line_msg_txt, "もしか")):
            extrct_subcntnt_rslt = "<選択＆追求 可能性 代理＆代替 対名詞・存在>"
    elif (check_text_start_string(line_msg_txt, "乃至は") or
          check_text_start_string(line_msg_txt, "ないしは") or
          check_text_start_string(line_msg_txt, "ないし")):
            extrct_subcntnt_rslt = "<選択＆追求 可能性 代理＆代替 対動詞・行為>"
    elif (check_text_start_string(line_msg_txt, "さぞかし") or
          check_text_start_string(line_msg_txt, "さぞ")):
            extrct_subcntnt_rslt = "<推定＆推測＆推量 揣摩＆憶測 感情＆感性>"
    elif (check_text_start_string(line_msg_txt, "決して") or
          check_text_start_string(line_msg_txt, "決まって")):
            extrct_subcntnt_rslt = "<断定＆確定 限定>"
    elif (check_text_start_string(line_msg_txt, "ひょっとして") or
          check_text_start_string(line_msg_txt, "もしかして")):
            extrct_subcntnt_rslt = "<推定＆推測＆推量 揣摩＆憶測 中立＆中性>"
    elif  check_text_start_string(line_msg_txt, "もしかしたら"):
            extrct_subcntnt_rslt = "<推定＆推測＆推量 揣摩＆憶測 場合分け>"
    elif (check_text_start_string(line_msg_txt, "必ずしも") or
          check_text_start_string(line_msg_txt, "必ずしも")):
            extrct_subcntnt_rslt = "<確信・約束に至らない場合>"
    elif (check_text_start_string(line_msg_txt, "必ずや") or
          check_text_start_string(line_msg_txt, "必ず")):
            extrct_subcntnt_rslt = "<確信＆約束>"
    elif (check_text_start_string(line_msg_txt, "もっと言えば") or
          check_text_start_string(line_msg_txt, "もっといえば") or
          check_text_start_string(line_msg_txt, "更に言えば") or
          check_text_start_string(line_msg_txt, "さらに言えば")):
            extrct_subcntnt_rslt = "<添加＆追加 条件付け 補足>"
    elif (check_text_start_string(line_msg_txt, "欲を言えば") or
          check_text_start_string(line_msg_txt, "欲をいえば")):
            extrct_subcntnt_rslt = "<添加＆追加 条件付け 願望・欲求について>"
    elif (check_text_start_string(line_msg_txt, "強ち") or
          check_text_start_string(line_msg_txt, "あながち")):
            extrct_subcntnt_rslt = "<推定＆推測＆推量 揣摩＆憶測 意外なことにも考えを巡らす>"
    elif (check_text_start_string(line_msg_txt, "最も") or
          check_text_start_string(line_msg_txt, "もっとも")):
            extrct_subcntnt_rslt = "<結果＆結論 皮相＆皮肉>"
    elif  check_text_start_string(line_msg_txt, "実に"):
            extrct_subcntnt_rslt = "<認知・認識強調 事実＆現実>"
    elif (check_text_start_string(line_msg_txt, "畢竟") or
          check_text_start_string(line_msg_txt, "詮ずる所") or
          check_text_start_string(line_msg_txt, "詮ずるところ") or
          check_text_start_string(line_msg_txt, "詮ずると") or
          check_text_start_string(line_msg_txt, "詰まる所") or
          check_text_start_string(line_msg_txt, "詰まるところ") or
          check_text_start_string(line_msg_txt, "詰まりは") or
          check_text_start_string(line_msg_txt, "つまりは") or
          check_text_start_string(line_msg_txt, "詰まり") or
          check_text_start_string(line_msg_txt, "つまり")):
            extrct_subcntnt_rslt = "<結果＆結論>"
    elif (check_text_start_string(line_msg_txt,"まさか") or
          check_text_start_string(line_msg_txt,"よもや")):
            extrct_subcntnt_rslt = "<臆見＆憶測 思惑＆感情>"
    elif (check_text_start_string(line_msg_txt,"当然にして") or
          check_text_start_string(line_msg_txt, "当然")):
            extrct_subcntnt_rslt = "<推理＆推論>"
    elif (check_text_start_string(line_msg_txt, "非常に") or
          check_text_start_string(line_msg_txt,"とても")):
            extrct_subcntnt_rslt = "<程度強調>"
    elif (check_text_start_string(line_msg_txt,"極めて") or
          check_text_start_string(line_msg_txt,"かなり")):
            extrct_subcntnt_rslt = "<程度強調>"
    elif (check_text_start_string(line_msg_txt, "纏めると") or
          check_text_start_string(line_msg_txt, "まとめると")):
            extrct_subcntnt_rslt = "<総括＆概括>"
    elif (check_text_start_string(line_msg_txt, "初めに") or
          check_text_start_string(line_msg_txt, "はじめに")):
            extrct_subcntnt_rslt = "<前置き 最初>"
    elif (check_text_start_string(line_msg_txt, "終わりに") or
          check_text_start_string(line_msg_txt, "おわりに")):
            extrct_subcntnt_rslt = "<前置き 最後>"
    elif (check_text_start_string(line_msg_txt, "だけども") or
          check_text_start_string(line_msg_txt, "だけど") or
          check_text_start_string(line_msg_txt, "それでも") or
          check_text_start_string(line_msg_txt, "でも")):
            extrct_subcntnt_rslt = "<反駁＆反論>"
    elif (check_text_start_string(line_msg_txt, "如何せん") or
          check_text_start_string(line_msg_txt, "いかんせん") or
          check_text_start_string(line_msg_txt, "残念ながら")):
            extrct_subcntnt_rslt = "<言い訳>"
    elif (check_text_start_string(line_msg_txt, "言い換えれば") or
          check_text_start_string(line_msg_txt, "言い換えると")):
            extrct_subcntnt_rslt = "<換言＆言換え>"
    elif (check_text_start_string(line_msg_txt, "初めに言っておくと") or
          check_text_start_string(line_msg_txt, "はじめに言っておくと") or
          check_text_start_string(line_msg_txt, "先に言っておくと") or
          check_text_start_string(line_msg_txt, "先に言っておくけど")):
            extrct_subcntnt_rslt = "<前置き＆先述>"
    elif (check_text_start_string(line_msg_txt, "初めに断っておくと") or
          check_text_start_string(line_msg_txt, "はじめに断っておくと") or
          check_text_start_string(line_msg_txt, "初めに断っておくけど") or
          check_text_start_string(line_msg_txt, "はじめに断っておくけど")):
            extrct_subcntnt_rslt = "<断り＆先述>"
    else:
            extrct_subcntnt_rslt = "<その他・不明>"
    return extrct_subcntnt_rslt


#ユーザーから送られるLINEメッセージの中に含まれるインテントを除去する
def remove_intent(line_msg_txt):
    #メッセージの中に含まれる日本語固有のインテントの削除候補をリストアップする
    rmv_cnddt_intnt_list = []
    #if check_text_terminate_string(line_msg_txt, "します"):
    #     rmv_cnddt_intnt_list.append("します")


    #前段で取得した削除候補の中から実際に削除するインテントを決定して、これを呼出し元に引渡しをする
    rmv_cnddt_intnt_list_tmp = []
    for intnt in rmv_cnddt_intnt_list:
        rmv_cnddt_intnt_list_tmp.append([len(intnt), intnt])
    if  len(rmv_cnddt_intnt_list_tmp) == 0:
        rmv_intnt_rslt = line_msg_txt
        return rmv_intnt_rslt
    if  len(rmv_cnddt_intnt_list_tmp) == 1:
        tmp_intnt      = rmv_cnddt_intnt_list_tmp[0][1]
        rmv_intnt_rslt = re.sub(tmp_intnt, "", line_msg_txt)
        return rmv_intnt_rslt
    idx       = 0
    tmp_intnt = ""
    while len(rmv_cnddt_intnt_list_tmp) > (idx+1):
          if rmv_cnddt_intnt_list_tmp[idx+1][0] > rmv_cnddt_intnt_list_tmp[idx][0]:
             tmp_intnt = rmv_cnddt_intnt_list_tmp[idx+1][1]
             idx = idx + 1
          else:
             continue
    rmv_intnt_rslt = re.sub(tmp_intnt, "", line_msg_txt)
    return rmv_intnt_rslt


#ユーザーから送られるLINEメッセージの中に含まれるサブコンテント(＝発話の意図される内容 ＝副詞＆前置詞＆接続詞)を除去する
def remove_subcontent(line_msg_txt):
    #メッセージの中に含まれる日本語固有のサブコンテントの削除候補をリストアップする
    rmv_cnddt_subcntnt_list = []
    if check_text_start_string(line_msg_txt, "さて"):
         rmv_cnddt_subcntnt_list.append("さて")
    if check_text_start_string(line_msg_txt, "ところで"):
         rmv_cnddt_subcntnt_list.append("ところで")
    if check_text_start_string(line_msg_txt, "そして"):
         rmv_cnddt_subcntnt_list.append("そして")
    if check_text_start_string(line_msg_txt, "それで"):
         rmv_cnddt_subcntnt_list.append("それで")
    if check_text_start_string(line_msg_txt, "そんで"):
         rmv_cnddt_subcntnt_list.append("そんで")
    if check_text_start_string(line_msg_txt, "加えて"):
         rmv_cnddt_subcntnt_list.append("加えて")
    if check_text_start_string(line_msg_txt, "更に"):
         rmv_cnddt_subcntnt_list.append("更に")
    if check_text_start_string(line_msg_txt, "さらに"):
         rmv_cnddt_subcntnt_list.append("さらに")
    if check_text_start_string(line_msg_txt, "又"):
         rmv_cnddt_subcntnt_list.append("又")
    if check_text_start_string(line_msg_txt, "また"):
         rmv_cnddt_subcntnt_list.append("また")
    if check_text_start_string(line_msg_txt, "多分"):
         rmv_cnddt_subcntnt_list.append("多分")
    if check_text_start_string(line_msg_txt, "たぶん"):
         rmv_cnddt_subcntnt_list.append("たぶん")
    if check_text_start_string(line_msg_txt, "恐らくは"):
         rmv_cnddt_subcntnt_list.append("恐らくは")
    if check_text_start_string(line_msg_txt, "おそらくは"):
         rmv_cnddt_subcntnt_list.append("おそらくは")
    if check_text_start_string(line_msg_txt, "恐らく"):
         rmv_cnddt_subcntnt_list.append("恐らく")
    if check_text_start_string(line_msg_txt, "おそらく"):
       rmv_cnddt_subcntnt_list.append("おそらく")
    if check_text_start_string(line_msg_txt, "又は"):
         rmv_cnddt_subcntnt_list.append("又は")
    if check_text_start_string(line_msg_txt, "または"):
         rmv_cnddt_subcntnt_list.append("または")
    if check_text_start_string(line_msg_txt, "且つ"):
         rmv_cnddt_subcntnt_list.append("且つ")
    if check_text_start_string(line_msg_txt, "かつ"):
         rmv_cnddt_subcntnt_list.append("かつ")
    if check_text_start_string(line_msg_txt, "得てして"):
         rmv_cnddt_subcntnt_list.append("得てして")
    if check_text_start_string(line_msg_txt, "えてして"):
         rmv_cnddt_subcntnt_list.append("えてして")
    if check_text_start_string(line_msg_txt, "概して"):
         rmv_cnddt_subcntnt_list.append("概して")
    if check_text_start_string(line_msg_txt, "大抵は"):
         rmv_cnddt_subcntnt_list.append("大抵は")
    if check_text_start_string(line_msg_txt, "大抵"):
         rmv_cnddt_subcntnt_list.append("大抵")
    if check_text_start_string(line_msg_txt, "大概は"):
         rmv_cnddt_subcntnt_list.append("大概は")
    if check_text_start_string(line_msg_txt, "大概"):
         rmv_cnddt_subcntnt_list.append("大概")
    if check_text_start_string(line_msg_txt, "確実に"):
         rmv_cnddt_subcntnt_list.append("確実に")
    if check_text_start_string(line_msg_txt, "明らかに"):
         rmv_cnddt_subcntnt_list.append("明らかに")
    if check_text_start_string(line_msg_txt, "多くの場合には"):
         rmv_cnddt_subcntnt_list.append("多くの場合には")
    if check_text_start_string(line_msg_txt, "多くの場合は"):
         rmv_cnddt_subcntnt_list.append("多くの場合は")
    if check_text_start_string(line_msg_txt, "多くの場合"):
         rmv_cnddt_subcntnt_list.append("多くの場合")
    if check_text_start_string(line_msg_txt, "多くは"):
         rmv_cnddt_subcntnt_list.append("多くは")
    if check_text_start_string(line_msg_txt, "多く"):
         rmv_cnddt_subcntnt_list.append("多く")
    if check_text_start_string(line_msg_txt, "少なくとも"):
         rmv_cnddt_subcntnt_list.append("少なくとも")
    if check_text_start_string(line_msg_txt, "少なくても"):
         rmv_cnddt_subcntnt_list.append("少なくても")
    if check_text_start_string(line_msg_txt, "大層"):
         rmv_cnddt_subcntnt_list.append("大層")
    if check_text_start_string(line_msg_txt, "なので"):
         rmv_cnddt_subcntnt_list.append("なので")
    if check_text_start_string(line_msg_txt, "ですから"):
         rmv_cnddt_subcntnt_list.append("ですから")
    if check_text_start_string(line_msg_txt, "さては"):
         rmv_cnddt_subcntnt_list.append("さては")
    if check_text_start_string(line_msg_txt, "もしや"):
         rmv_cnddt_subcntnt_list.append("もしや")
    if check_text_start_string(line_msg_txt, "もしも"):
         rmv_cnddt_subcntnt_list.append("もしも")
    if check_text_start_string(line_msg_txt, "もし"):
         rmv_cnddt_subcntnt_list.append("もし")
    if check_text_start_string(line_msg_txt, "例えば"):
         rmv_cnddt_subcntnt_list.append("例えば")
    if check_text_start_string(line_msg_txt, "たとえば"):
         rmv_cnddt_subcntnt_list.append("たとえば")
    if check_text_start_string(line_msg_txt, "例すれば"):
         rmv_cnddt_subcntnt_list.append("例すれば")
    if check_text_start_string(line_msg_txt, "例せば"):
         rmv_cnddt_subcntnt_list.append("例せば")
    if check_text_start_string(line_msg_txt, "類すれば"):
         rmv_cnddt_subcntnt_list.append("類すれば")
    if check_text_start_string(line_msg_txt, "類せば"):
         rmv_cnddt_subcntnt_list.append("類せば")
    if check_text_start_string(line_msg_txt, "譬え"):
         rmv_cnddt_subcntnt_list.append("譬え")
    if check_text_start_string(line_msg_txt, "たとえ"):
         rmv_cnddt_subcntnt_list.append("たとえ")
    if check_text_start_string(line_msg_txt, "仮に"):
         rmv_cnddt_subcntnt_list.append("仮に")
    if check_text_start_string(line_msg_txt, "或いは"):
         rmv_cnddt_subcntnt_list.append("或いは")
    if check_text_start_string(line_msg_txt, "よしんば"):
         rmv_cnddt_subcntnt_list.append("よしんば")
    if check_text_start_string(line_msg_txt, "あるいは"):
         rmv_cnddt_subcntnt_list.append("あるいは")
    if check_text_start_string(line_msg_txt, "若しくは"):
         rmv_cnddt_subcntnt_list.append("若しくは")
    if check_text_start_string(line_msg_txt, "もしくは"):
         rmv_cnddt_subcntnt_list.append("もしくは")
    if check_text_start_string(line_msg_txt, "もしか"):
         rmv_cnddt_subcntnt_list.append("もしか")
    if check_text_start_string(line_msg_txt, "乃至は"):
         rmv_cnddt_subcntnt_list.append("乃至は")
    if check_text_start_string(line_msg_txt, "ないしは"):
         rmv_cnddt_subcntnt_list.append("ないしは")
    if check_text_start_string(line_msg_txt, "ないし"):
         rmv_cnddt_subcntnt_list.append("ないし")
    if check_text_start_string(line_msg_txt, "さぞかし"):
         rmv_cnddt_subcntnt_list.append("さぞかし")
    if check_text_start_string(line_msg_txt, "さぞ"):
         rmv_cnddt_subcntnt_list.append("さぞ")
    if check_text_start_string(line_msg_txt, "決して"):
         rmv_cnddt_subcntnt_list.append("決して")
    if check_text_start_string(line_msg_txt, "決まって"):
         rmv_cnddt_subcntnt_list.append("決まって")
    if check_text_start_string(line_msg_txt, "ひょっとして"):
         rmv_cnddt_subcntnt_list.append("ひょっとして")
    if check_text_start_string(line_msg_txt, "もしかして"):
         rmv_cnddt_subcntnt_list.append("もしかして")
    if check_text_start_string(line_msg_txt, "もしかしたら"):
         rmv_cnddt_subcntnt_list.append("もしかしたら")
    if check_text_start_string(line_msg_txt, "必ずしも"):
         rmv_cnddt_subcntnt_list.append("必ずしも")
    if check_text_start_string(line_msg_txt, "必ずや"):
         rmv_cnddt_subcntnt_list.append("必ずや")
    if check_text_start_string(line_msg_txt, "必ず"):
         rmv_cnddt_subcntnt_list.append("必ず")
    if check_text_start_string(line_msg_txt, "もっと言えば"):
         rmv_cnddt_subcntnt_list.append("もっと言えば")
    if check_text_start_string(line_msg_txt, "もっといえば"):
         rmv_cnddt_subcntnt_list.append("もっといえば")
    if check_text_start_string(line_msg_txt, "更に言えば"):
         rmv_cnddt_subcntnt_list.append("更に言えば")
    if check_text_start_string(line_msg_txt, "さらに言えば"):
         rmv_cnddt_subcntnt_list.append("さらに言えば")
    if check_text_start_string(line_msg_txt, "欲を言えば"):
         rmv_cnddt_subcntnt_list.append("欲を言えば")
    if check_text_start_string(line_msg_txt, "欲をいえば"):
         rmv_cnddt_subcntnt_list.append("欲をいえば")
    if check_text_start_string(line_msg_txt, "強ち"):
         rmv_cnddt_subcntnt_list.append("強ち")
    if check_text_start_string(line_msg_txt, "あながち"):
         rmv_cnddt_subcntnt_list.append("あながち")
    if check_text_start_string(line_msg_txt, "最も"):
         rmv_cnddt_subcntnt_list.append("最も")
    if check_text_start_string(line_msg_txt, "もっとも"):
         rmv_cnddt_subcntnt_list.append("もっとも")
    if check_text_start_string(line_msg_txt, "実に"):
         rmv_cnddt_subcntnt_list.append("実に")
    if check_text_start_string(line_msg_txt, "畢竟"):
         rmv_cnddt_subcntnt_list.append("畢竟")
    if check_text_start_string(line_msg_txt, "詮ずる所"):
         rmv_cnddt_subcntnt_list.append("詮ずる所")
    if check_text_start_string(line_msg_txt, "詮ずるところ"):
         rmv_cnddt_subcntnt_list.append("詮ずるところ")
    if check_text_start_string(line_msg_txt, "詮ずると"):
         rmv_cnddt_subcntnt_list.append("詮ずると")
    if check_text_start_string(line_msg_txt, "詰まる所"):
         rmv_cnddt_subcntnt_list.append("詰まる所")
    if check_text_start_string(line_msg_txt, "詰まるところ"):
         rmv_cnddt_subcntnt_list.append("詰まるところ")
    if check_text_start_string(line_msg_txt, "詰まりは"):
         rmv_cnddt_subcntnt_list.append("つまりは")
    if check_text_start_string(line_msg_txt, "つまりは"):
         rmv_cnddt_subcntnt_list.append("つまりは")
    if check_text_start_string(line_msg_txt, "詰まり"):
         rmv_cnddt_subcntnt_list.append("詰まり")
    if check_text_start_string(line_msg_txt, "つまり"):
         rmv_cnddt_subcntnt_list.append("つまり")
    if check_text_start_string(line_msg_txt, "まさか"):
         rmv_cnddt_subcntnt_list.append("まさか")
    if check_text_start_string(line_msg_txt, "よもや"):
         rmv_cnddt_subcntnt_list.append("よもや")
    if check_text_start_string(line_msg_txt, "当然にして"):
         rmv_cnddt_subcntnt_list.append("当然にして")
    if check_text_start_string(line_msg_txt, "当然"):
         rmv_cnddt_subcntnt_list.append("当然")
    if check_text_start_string(line_msg_txt, "非常に"):
         rmv_cnddt_subcntnt_list.append("非常に")
    if check_text_start_string(line_msg_txt, "とても"):
         rmv_cnddt_subcntnt_list.append("とても")
    if check_text_start_string(line_msg_txt, "極めて"):
         rmv_cnddt_subcntnt_list.append("極めて")
    if check_text_start_string(line_msg_txt, "かなり"):
         rmv_cnddt_subcntnt_list.append("かなり")
    if check_text_start_string(line_msg_txt, "纏めると"):
         rmv_cnddt_subcntnt_list.append("纏めると")
    if check_text_start_string(line_msg_txt, "まとめると"):
         rmv_cnddt_subcntnt_list.append("まとめると")
    if check_text_start_string(line_msg_txt, "初めに"):
         rmv_cnddt_subcntnt_list.append("初めに")
    if check_text_start_string(line_msg_txt, "はじめに"):
         rmv_cnddt_subcntnt_list.append("はじめに")
    if check_text_start_string(line_msg_txt, "終わりに"):
         rmv_cnddt_subcntnt_list.append("終わりに")
    if check_text_start_string(line_msg_txt, "おわりに"):
         rmv_cnddt_subcntnt_list.append("おわりに")
    if check_text_start_string(line_msg_txt, "だけども"):
         rmv_cnddt_subcntnt_list.append("だけども")
    if check_text_start_string(line_msg_txt, "だけど"):
         rmv_cnddt_subcntnt_list.append("だけど")
    if check_text_start_string(line_msg_txt, "それでも"):
         rmv_cnddt_subcntnt_list.append("それでも")
    if check_text_start_string(line_msg_txt, "でも"):
         rmv_cnddt_subcntnt_list.append("でも")
    if check_text_start_string(line_msg_txt, "如何せん"):
         rmv_cnddt_subcntnt_list.append("如何せん")
    if check_text_start_string(line_msg_txt, "いかんせん"):
         rmv_cnddt_subcntnt_list.append("いかんせん")
    if check_text_start_string(line_msg_txt, "残念ながら"):
         rmv_cnddt_subcntnt_list.append("残念ながら")
    if check_text_start_string(line_msg_txt, "言い換えれば"):
         rmv_cnddt_subcntnt_list.append("言い換えれば")
    if check_text_start_string(line_msg_txt, "言い換えると"):
         rmv_cnddt_subcntnt_list.append("言い換えると")
    if check_text_start_string(line_msg_txt, "初めに言っておくと"):
         rmv_cnddt_subcntnt_list.append("初めに言っておくと")
    if check_text_start_string(line_msg_txt, "はじめに言っておくと"):
         rmv_cnddt_subcntnt_list.append("はじめに言っておくと")
    if check_text_start_string(line_msg_txt, "先に言っておくと"):
         rmv_cnddt_subcntnt_list.append("先に言っておくと")
    if check_text_start_string(line_msg_txt, "先に言っておくけど"):
         rmv_cnddt_subcntnt_list.append("先に言っておくけど")
    if check_text_start_string(line_msg_txt, "初めに断っておくと"):
         rmv_cnddt_subcntnt_list.append("初めに断っておくと")
    if check_text_start_string(line_msg_txt, "はじめに断っておくと"):
         rmv_cnddt_subcntnt_list.append("はじめに断っておくと")
    if check_text_start_string(line_msg_txt, "初めに断っておくけど"):
         rmv_cnddt_subcntnt_list.append("初めに断っておくけど")
    if check_text_start_string(line_msg_txt, "はじめに断っておくけど"):
         rmv_cnddt_subcntnt_list.append("はじめに断っておくけど")

    #前段で取得した削除候補の中から実際に削除するサブコンテントを決定して、これを呼出し元に引渡しをする
    rmv_cnddt_subcntnt_list_tmp = []
    for subcntnt in rmv_cnddt_subcntnt_list:
        rmv_cnddt_subcntnt_list_tmp.append([len(subcntnt), subcntnt])
    if  len(rmv_cnddt_subcntnt_list_tmp) == 0:
        rmv_subcntnt_rslt = line_msg_txt
        return rmv_subcntnt_rslt
    if  len(rmv_cnddt_subcntnt_list_tmp) == 1:
        tmp_subcntnt      = rmv_cnddt_subcntnt_list_tmp[0][1]
        rmv_subcntnt_rslt = re.sub(tmp_subcntnt, "", line_msg_txt)
        return rmv_subcntnt_rslt
    idx          = 0
    tmp_subcntnt = ""
    while len(rmv_cnddt_subcntnt_list_tmp) > (idx+1):
           if rmv_cnddt_subcntnt_list_tmp[idx+1][0] > rmv_cnddt_subcntnt_list_tmp[idx][0]:
              tmp_subcntnt = rmv_cnddt_subcntnt_list_tmp[idx+1][1]
              idx = idx + 1
           else:
              continue
    rmv_subcntnt_rslt = re.sub(tmp_subcntnt, "", line_msg_txt)
    return rmv_subcntnt_rslt
