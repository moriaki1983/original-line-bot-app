# coding: utf-8




import re
from janome.tokenizer import Tokenizer




#ユーザーから送られるLINEメッセージの中に含まれる記号を除去する
def remove_symbol(line_msg_txt):
    #メッセージの中に含まれる各種の記号・空白を除去する
    rmv_symbl_rslt   = re.sub("(’)", "", line_msg_txt)
    rmv_symbl_rslt2  = re.sub("(”)", "", rmv_symbl_rslt)
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
    rmv_symbl_rslt17 = re.sub("( )",  "", rmv_symbl_rslt16)
    rmv_symbl_rslt18 = re.sub("(　)", "", rmv_symbl_rslt17)
    rmv_symbl_rslt19 = re.sub("(,)",  "", rmv_symbl_rslt18)
    rmv_symbl_rslt20 = re.sub("(.)",  "", rmv_symbl_rslt19)

    #メッセージの中に含まれる先頭と末尾の空白と改行を除去する
    rmv_symbl_rslt_end = rmv_symbl_rslt20.strip()
    return rmv_symbl_rslt_end


#ユーザーから送られるLINEメッセージの中に含まれる終助詞等を除去する
def remove_endparticle(rmv_symbl_rslt):
    #終助詞等を表す正規表現パターンを用意・作成する
    pattern   = re.compile("(よお)$")
    pattern2  = re.compile("(よぉ)$")
    pattern3  = re.compile("(よっ)$")
    pattern4  = re.compile("(ねえ)$")
    pattern5  = re.compile("(ねぇ)$")
    pattern6  = re.compile("(ねっ)$")
    pattern7  = re.compile("(なあ)$")
    pattern8  = re.compile("(なぁ)$")
    pattern9  = re.compile("(なっ)$")
    pattern10 = re.compile("(わあ)$")
    pattern11 = re.compile("(わぁ)$")
    pattern12 = re.compile("(わっ)$")
    pattern13 = re.compile("(ぜえ)$")
    pattern14 = re.compile("(ぜぇ)$")
    pattern15 = re.compile("(ぜっ)$")
    pattern16 = re.compile("(っすよ)$")
    pattern17 = re.compile("(っすね)$")
    pattern18 = re.compile("(っす)$")
    pattern19 = re.compile("(わよ)$")
    pattern20 = re.compile("(わね)$")
    pattern21 = re.compile("(ってば)$")
    pattern22 = re.compile("(ってばよ)$")
    pattern23 = re.compile("(爆)$")
    pattern24 = re.compile("(爆笑)$")
    pattern25 = re.compile("(笑)+$")
    pattern26 = re.compile("(わら)+$")
    pattern27 = re.compile("(ワラ)+$")
    pattern28 = re.compile("(草)+$")
    pattern29 = re.compile("(w)+$")
    pattern30 = re.compile("(W)+$")

    #メッセージの中の正規表現パターンに合致するものを除去する
    if pattern.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub(r'よお$', "", rmv_symbl_rslt)
    if pattern2.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub(r'よぉ$', "", rmv_symbl_rslt)
    if pattern3.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub(r'よっ$', "", rmv_symbl_rslt)
    if pattern4.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub(r'ねえ$', "", rmv_symbl_rslt)
    if pattern5.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub(r'ねぇ$', "", rmv_symbl_rslt)
    if pattern6.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub(r'ねっ$', "", rmv_symbl_rslt)
    if pattern7.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub(r'なあ$', "", rmv_symbl_rslt)
    if pattern8.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(わぁ)", "", rmv_symbl_rslt)
    if pattern9.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(わっ)", "", rmv_symbl_rslt)
    if pattern10.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(ぜえ)", "", rmv_symbl_rslt)
    if pattern11.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(ぜぇ)", "", rmv_symbl_rslt)
    if pattern12.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(ぜっ)", "", rmv_symbl_rslt)
    if pattern13.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(よお)", "", rmv_symbl_rslt)
    if pattern14.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(よぉ)", "", rmv_symbl_rslt)
    if pattern15.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(よっ)", "", rmv_symbl_rslt)
    if pattern16.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(っすよ)", "", rmv_symbl_rslt)
    if pattern17.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(っす)", "", rmv_symbl_rslt)
    if pattern18.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(わね)", "", rmv_symbl_rslt)
    if pattern19.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(わよ)", "", rmv_symbl_rslt)
    if pattern20.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(ってば)", "", rmv_symbl_rslt)
    if pattern21.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(笑)", "", rmv_symbl_rslt)
    if pattern22.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(わら)", "", rmv_symbl_rslt)
    if pattern23.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(ワラ)", "", rmv_symbl_rslt)
    if pattern24.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(草)", "", rmv_symbl_rslt)
    if pattern25.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(w)", "", rmv_symbl_rslt)
    if pattern26.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(W)", "", rmv_symbl_rslt)
    if pattern27.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(爆)", "", rmv_symbl_rslt)
    if pattern28.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(爆笑)", "", rmv_symbl_rslt)
    if pattern29.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(爆)", "", rmv_symbl_rslt)
    if pattern30.search(rmv_symbl_rslt) == True:
         rmv_edprtcl_rslt = re.sub("(爆笑)", "", rmv_symbl_rslt)
         
    #メッセージの中に含まれる先頭と末尾の空白と改行を除去する
    #rmv_edprtcl_rslt_end = rmv_edprtcl_rslt.strip()
    #return rmv_edprtcl_rslt_end 
    return rmv_symbl_rslt


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
    #メッセージの中に含まれる日本語固有のインテントの削除候補をリストアップする
    rmv_cnddt_intnt_list = []
    #if check_text_terminated_string(rmv_edprtcl_rslt, "します"):
    #     rmv_cnddt_intnt_list.append("します")


    #前段で取得した削除候補の中から実際に削除するインテントを決定して、これを呼出し元に引渡しをする
    rmv_cnddt_intnt_list_tmp = []
    for intnt in rmv_cnddt_intnt_list:
        rmv_cnddt_intnt_list_tmp.append([len(intnt), intnt])
    if len(rmv_cnddt_intnt_list_tmp) == 0:
       rmv_intnt_rslt = rmv_edprtcl_rslt
       return rmv_intnt_rslt
    if len(rmv_cnddt_intnt_list_tmp) == 1:
       tmp_intnt      = rmv_cnddt_intnt_list_tmp[0][1]
       rmv_intnt_rslt = re.sub(tmp_intnt, "", rmv_edprtcl_rslt)
       return rmv_intnt_rslt
    idx       = 0
    tmp_intnt = ""
    while len(rmv_cnddt_intnt_list_tmp) > (idx+1):
          if rmv_cnddt_intnt_list_tmp[idx+1][0] > rmv_cnddt_intnt_list_tmp[idx][0]:
             tmp_intnt = rmv_cnddt_intnt_list_tmp[idx+1][1]
             idx = idx + 1
          else:
             continue
    rmv_intnt_rslt = re.sub(tmp_intnt, "", rmv_edprtcl_rslt)
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


#ユーザーから送られるLINEメッセージがギャグ＆声帯模写＆その他だったとして、これからインテントを抽出する
def extract_intent_from_gag_vocalcordcopy_and_etc(line_msg_txt):
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
            extrct_intnt_from_gag_vclcrdcpy_and_etc_rslt = "(モノマネ＆ギャグ＆一発芸)(人物・キャラクターに基づいて)"
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
            extrct_intnt_from_gag_vclcrdcpy_and_etc_rslt = "(モノマネ＆声帯模写)(モノ・動物に基づいて)"
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
            extrct_intnt_from_gag_vclcrdcpy_and_etc_rslt = "(生理現象に伴う音)"
    elif (line_msg_txt == "おい" or
          line_msg_txt == "ねぇ" or
          line_msg_txt == "なあ" or
          line_msg_txt == "なぁ" or
          line_msg_txt == "なあ？" or
          line_msg_txt == "なぁ？" or
          line_msg_txt == "なあ！" or
          line_msg_txt == "なぁ！"):
            extrct_intnt_from_gag_vclcrdcpy_and_etc_rslt = "(呼掛け＆問掛け)"      
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
            extrct_intnt_from_gag_vclcrdcpy_and_etc_rslt = "(フィラー)(間の引き延ばし)"
    elif (line_msg_txt == "ブー ブー" or
          line_msg_txt == "ブーブー" or
          line_msg_txt == "ブー！ ブー！" or
          line_msg_txt == "ブー！ブー！"):
            extrct_intnt_from_gag_vclcrdcpy_and_etc_rslt = "(ブーイング)"
    elif (line_msg_txt == "海" or
          line_msg_txt == "うみ" or
          line_msg_txt == "海！" or
          line_msg_txt == "うみ！" or
          line_msg_txt == "セイ イェーイ" or
          line_msg_txt == "セイイェーイ" or
          line_msg_txt == "セイ イェーイ！" or
          line_msg_txt == "セイイェーイ！"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(掛合い＆コールアンドレスポンス)"
    else:
            extrct_intnt_from_gag_vclcrdcpy_and_etc_rslt = "(その他・不明)"
    return extrct_intnt_from_gag_vclcrdcpy_and_etc_rslt


#LINEメッセージが短文＆定型文だったとして、これからインテントを抽出する
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(挨拶)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(称賛＆礼賛)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(罵詈＆罵倒)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(人格・存在否定)"
    elif (line_msg_txt == "大天才ですか" or
          line_msg_txt == "天才ですか" or
          line_msg_txt == "大秀才ですか" or
          line_msg_txt == "秀才ですか" or
          line_msg_txt == "優秀ですか"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(称賛＆礼賛)(半疑問)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(罵詈＆罵倒)(半疑問)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(現在)(状態・状況について)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(過去)(状態・状況について)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(現在)(願望・欲求について)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(過去)(願望・欲求について)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(未来)(願望・欲求について)"
    elif (line_msg_txt == "どうしたいのですか" or
          line_msg_txt == "どうしたいんですか" or
          line_msg_txt == "どうしたいですか" or
          line_msg_txt == "どうしたいのかな" or
          line_msg_txt == "どうしたいの" or
          line_msg_txt == "どうしたい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(現在)(願望・欲求について)(漠然とした様子・様相)"
    elif (line_msg_txt == "どうしたかったのですか" or
          line_msg_txt == "どうしたかったんですか" or
          line_msg_txt == "どうしたかったの" or
          line_msg_txt == "どうしたかった"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(過去)(願望・欲求について)(漠然とした様子・様相)"
    elif (line_msg_txt == "どうしていきたいのですか" or
          line_msg_txt == "どうしていきたいんですか" or
          line_msg_txt == "どうしていきたいの" or
          line_msg_txt == "どうしていきたい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(未来)(願望・欲求について)(漠然とした様子・様相)"
    elif (line_msg_txt == "どうなのですか" or
          line_msg_txt == "どうなんですか" or
          line_msg_txt == "どうなの" or
          line_msg_txt == "どうなん"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(意図・目的について)"
    elif line_msg_txt == "どう":
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(感想・感慨について)"
    elif (line_msg_txt == "どうしてなのですか" or
          line_msg_txt == "どうしてなんですか" or
          line_msg_txt == "どうしてですか" or
          line_msg_txt == "どうして"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(理由・事情について)"      
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(理由・事情について)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(許容＆許可)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(賛意＆賛同)" 
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(依頼＆要求)"
    elif (line_msg_txt == "行きます" or
          line_msg_txt == "いきます" or
          line_msg_txt == "遣ります" or
          line_msg_txt == "やります" or
          line_msg_txt == "遊びます" or
          line_msg_txt == "あそびます" or
          line_msg_txt == "休みます" or
          line_msg_txt == "やすみます"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(宣言＆表明)(現在＆未来)(行為・行動について)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(訴求＆表現)(心理・感情について)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(訴求＆表現)(精神・肉体について)"
    elif (line_msg_txt == "最初は グー" or
          line_msg_txt == "最初はグー" or
          line_msg_txt == "じゃんけんぽん" or
          line_msg_txt == "じゃんけん" or
          line_msg_txt == "ジャンケンポン" or
          line_msg_txt == "ジャンケン"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(児戯＆遊戯)"
    elif (line_msg_txt == "お願い致します" or
          line_msg_txt == "お願いいたします" or
          line_msg_txt == "お願いします" or
          line_msg_txt == "お願いです" or
          line_msg_txt == "お願い"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(依願＆依頼)"
    elif (line_msg_txt == "御免なさい" or
          line_msg_txt == "ごめんなさい" or
          line_msg_txt == "ゴメンなさい" or
          line_msg_txt == "御免" or
          line_msg_txt == "ごめん" or
          line_msg_txt == "ゴメン" or
          line_msg_txt == "メンゴ メンゴ" or
          line_msg_txt == "メンゴメンゴ" or
          line_msg_txt == "メンゴ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(陳謝＆謝罪)"
    elif (line_msg_txt == "承知致しました" or
          line_msg_txt == "承知いたしました" or
          line_msg_txt == "承知しました" or
          line_msg_txt == "承知した" or
          line_msg_txt == "承知" or
          line_msg_txt == "かしこまりました" or
          line_msg_txt == "かしこまり"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(承知＆承諾)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(了承＆了解)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(訴求＆表現)(求愛・発情している)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆確認＆質問)(単純)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆確認＆質問)(やや反発している・やや反感を抱いている)"
    elif (line_msg_txt == "大丈夫でしょうか" or
          line_msg_txt == "大丈夫ですか" or
          line_msg_txt == "大丈夫"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(安否・健康状態について)"
    elif (line_msg_txt == "うむ" or
          line_msg_txt == "うん"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(了承＆承諾)(納得)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(慰労＆労い)"
    elif (line_msg_txt == "分かった" or
          line_msg_txt == "わかった"):
            extrct_intnt_from_gag_vclcrdcpy_and_etc_rslt = "(理解＆認識)"
    elif (line_msg_txt == "きざったらしい" or
          line_msg_txt == "キザったらしい" or
          line_msg_txt == "きざっぽい" or
          line_msg_txt == "キザっぽい" or
          line_msg_txt == "嫌味ったらしい" or
          line_msg_txt == "イヤミったらしい" or
          line_msg_txt == "嫌味っぽい" or
          line_msg_txt == "イヤミっぽい"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(訴求＆表現)(反発している・反感を抱いている)(強い嫌悪)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(許容・許可を求める)(肯定形)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(許容・許可を求める)(否定形)"
    elif (line_msg_txt == "お伺いします" or
          line_msg_txt == "お聞きします"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(聴取＆傾聴)(用件を尋ねる)"
    elif (line_msg_txt == "お聞かせ下さい" or
          line_msg_txt == "お聞かせください"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(聴取＆傾聴)(意見・感想を求める)"
    elif (line_msg_txt == "お考えになって下さい" or
          line_msg_txt == "お考え下さい" or
          line_msg_txt == "考えて下さい" or
          line_msg_txt == "考えてください" or
          line_msg_txt == "考えてくれ" or
          line_msg_txt == "考えて"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(要求＆要請)(思慮・思考を求める)"
    elif (line_msg_txt == "考え直して下さい" or
          line_msg_txt == "考え直してください" or
          line_msg_txt == "考え直してくれ" or
          line_msg_txt == "考え直して" or
          line_msg_txt == "思い直して下さい" or
          line_msg_txt == "思い直してください" or
          line_msg_txt == "思い直してくれ" or
          line_msg_txt == "思い直して"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(要求＆要請)(再度の思慮・思考を求める)"
    elif (line_msg_txt == "良きに計らえ" or
          line_msg_txt == "よきに計らえ" or
          line_msg_txt == "良しなに" or
          line_msg_txt == "よしなに" or
          line_msg_txt == "どうぞ良しなに" or
          line_msg_txt == "どうぞよしなに"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(要求＆要請)(善処を求める)"
    elif (line_msg_txt == "うむ" or
          line_msg_txt == "ウム" or
          line_msg_txt == "うん" or
          line_msg_txt == "ウン"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(了承＆承諾)(納得する様子)"
    elif (line_msg_txt == "そう言っているのです" or
          line_msg_txt == "そういっているのです" or
          line_msg_txt == "そう言っているんです" or
          line_msg_txt == "そういっているんです" or
          line_msg_txt == "そう言っている" or
          line_msg_txt == "そういっている" or
          line_msg_txt == "そう言ってる" or
          line_msg_txt == "そういってる"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(問答)(肯定)"
    elif (line_msg_txt == "そうは言っていないよ" or
          line_msg_txt == "そうはいっていないよ" or
          line_msg_txt == "そうは言っていない" or
          line_msg_txt == "そうはいっていない" or
          line_msg_txt == "そうは言ってないよ" or
          line_msg_txt == "そうはいってないよ" or
          line_msg_txt == "そうは言ってない" or
          line_msg_txt == "そうはいってない"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(問答)(否定)"
    elif (line_msg_txt == "しますよね" or
          line_msg_txt == "するよね" or
          line_msg_txt == "やるよね"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(行為・行動について)(肯定)"
    elif (line_msg_txt == "しませんよね" or
          line_msg_txt == "しないよね" or
          line_msg_txt == "やらないよね"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(行為・行動について)(否定)"
    elif (line_msg_txt == "するよな" or
          line_msg_txt == "やるよな"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(行為・行動について)(肯定)(半強制)"
    elif (line_msg_txt == "しないよな" or
          line_msg_txt == "せんよな" or
          line_msg_txt == "やらないよな" or
          line_msg_txt == "やらんよな"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(行為・行動について)(否定)(半強制)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(同意)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(不同意)"
    elif (line_msg_txt == "そうなのですね" or
          line_msg_txt == "そうなんですね" or
          line_msg_txt == "なのですね" or
          line_msg_txt == "なんですね"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(理解＆納得)(肯定)"
    elif (line_msg_txt == "そうではないのですね" or
          line_msg_txt == "そうではないんですね" or
          line_msg_txt == "そうじゃないんですね" or
          line_msg_txt == "ではないのですね" or
          line_msg_txt == "ではないんですね" or
          line_msg_txt == "じゃないんですね"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(理解＆納得)(否定)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(追求)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(歓迎＆歓待)"
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
          line_msg_txt == "よろしく"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(依願＆依頼)(挨拶に近い)"
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
            extrct_intnt_from_shrt_and_blrplt_rslt = "(推奨＆勧告)(誘いに近い)"
    elif (line_msg_txt == "本当ですよ" or
          line_msg_txt == "ホントですよ" or
          line_msg_txt == "本当だよ" or
          line_msg_txt == "ホントだよ" or
          line_msg_txt == "本当よ" or
          line_msg_txt == "ホントよ" or
          line_msg_txt == "ホント ホント" or
          line_msg_txt == "ホントホント"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(宣告)(真実であることを告げる)"
    elif (line_msg_txt == "嘘ですよ" or
          line_msg_txt == "ウソですよ" or
          line_msg_txt == "嘘だよ" or
          line_msg_txt == "ウソですよ" or
          line_msg_txt == "嘘よ" or
          line_msg_txt == "ウソよ" or
          line_msg_txt == "ウソ ウソ" or
          line_msg_txt == "ウソウソ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(宣告)(虚偽であることを告げる)"
    elif (line_msg_txt == "本当ですか" or
          line_msg_txt == "ホントですか" or
          line_msg_txt == "本当か" or
          line_msg_txt == "ホントか" or
          line_msg_txt == "ホント"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(真実であるかどうか)"
    elif (line_msg_txt == "嘘ですか" or
          line_msg_txt == "ウソですか" or
          line_msg_txt == "嘘か" or
          line_msg_txt == "ウソか" or
          line_msg_txt == "嘘" or
          line_msg_txt == "ウソ"):
            extrct_intnt_from_shrt_and_blrplt_rslt = "(疑義＆質問＆確認)(虚偽であるかどうか)"
    else:
            extrct_intnt_from_shrt_and_blrplt_rslt = "(その他・不明)"
    return extrct_intnt_from_shrt_and_blrplt_rslt


#ユーザーから送られるLINEメッセージの中からインテントを抽出する
def extract_intent(rmv_edprtcl_rslt):
    #メッセージの末尾部分からインテントを抽出して、これを呼出し元に引渡しをする
    if   (check_text_terminated_string(rmv_edprtcl_rslt, "を行います") or
          check_text_terminated_string(rmv_edprtcl_rslt, "を行う") or
          check_text_terminated_string(rmv_edprtcl_rslt, "します") or
          check_text_terminated_string(rmv_edprtcl_rslt, "する")):
           extrct_intnt_rslt = "(宣言＆表明)(現在＆未来＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "を行いません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "を行わない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しない")):
           extrct_intnt_rslt = "(宣言＆表明)(現在＆未来＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "行っています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "行っている") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "している") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してる")):
           extrct_intnt_rslt = "(宣言＆表明)(現在進行＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "行っていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "行ってません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "していません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "していない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してない")):
            extrct_intnt_rslt = "(宣言＆表明)(現在進行＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ができている") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ができてる") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できている") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてる")):
            extrct_intnt_rslt = "(宣言＆表明)(現在進行＆能動＆可能＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ができていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ができてません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ができていない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ができてない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できていない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてない")):
            extrct_intnt_rslt = "(宣言＆表明)(現在進行＆能動＆可能＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できた")):
            extrct_intnt_rslt = "(宣言＆表明)(過去＆可能＆完了)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてない")):
            extrct_intnt_rslt = "(宣言＆表明)(過去＆不可能＆未完了)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できる")):
            extrct_intnt_rslt = "(宣言＆表明)(現在＆能動＆可能)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できない")):
            extrct_intnt_rslt = "(宣言＆表明)(現在＆能動＆不可能)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しない")):
            extrct_intnt_rslt = "(宣言＆表明)(未来)(能動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "した") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやりました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやった")):
            extrct_intnt_rslt = "(宣言＆表明)(過去)(能動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してない")):
            extrct_intnt_rslt = "(宣言＆表明)(過去進行)(能動)(否定)"    
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてます")):
            extrct_intnt_rslt = "(宣言＆表明)(過去進行)(受動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されていない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてない")):
            extrct_intnt_rslt = "(宣言＆表明)(過去進行)(受動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "された")):
            extrct_intnt_rslt = "(宣言＆表明)(過去完了)(受動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "でした") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だったです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だった")):
            extrct_intnt_rslt = "(宣言＆表明)(過去完了)(能受不明)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でなかった")):
            extrct_intnt_rslt = "(宣言＆表明)(過去完了)(能受不明)(否定)"
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
            extrct_intnt_rslt = "(宣言＆表明)(現在＆未来)(持続)(能動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でなかった")):
            extrct_intnt_rslt = "(宣言＆表明)(現在＆未来)(持続)(能動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ですから") or
          check_text_terminated_string(rmv_edprtcl_rslt, "です") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ます")):
            extrct_intnt_rslt = "(紹介＆説明＆提示)(宣言＆表明)(能受不明)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "っていました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってた")):
            extrct_intnt_rslt = "(報告＆連絡)(過去＆能動)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しません")):
            extrct_intnt_rslt = "(誘導＆勧誘)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "したい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "たい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "やりたい")):
            extrct_intnt_rslt = "(願望・欲求について)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "いです")):
            extrct_intnt_rslt = "(紹介＆説明＆提示)"
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
            extrct_intnt_rslt = "(制止＆禁止)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしないように") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしないよう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がするな") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃ駄目") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃだめ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃダメ")):
            extrct_intnt_rslt = "(制止＆禁止)(特定個人)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "をしてください") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をして") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてください") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はして") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してください") or
          check_text_terminated_string(rmv_edprtcl_rslt, "して")):
            extrct_intnt_rslt = "(依頼＆要求)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしてください") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がして")):
            extrct_intnt_rslt = "(依頼＆要求)(特定個人)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しなさい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しろ")):
            extrct_intnt_rslt = "(指示＆命令)"
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
            extrct_intnt_rslt = "(勧告)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしなければならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなければ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしないといけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしないといけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がせにゃならん")):
            extrct_intnt_rslt = "(勧告)(肯定)(特定個人)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はしてはならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてはいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしたらいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃならん") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてはならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてはいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしたらいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃならん") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してはならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してはいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "したらいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃならん"):
            extrct_intnt_rslt = "(勧告)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしてはならない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしてはいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしたらいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃいけない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃならん")):
            extrct_intnt_rslt = "(勧告)(否定)(特定個人)"
    elif check_text_terminated_string(rmv_edprtcl_rslt, "だ"):
            extrct_intnt_rslt = "(紹介＆説明＆提示)(宣言＆表明)(誇示＆顕示)(強調)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "でしょう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だろう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だろ")):
            extrct_intnt_rslt = "(推定＆推測＆推量)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "だそうです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だろう")):
            extrct_intnt_rslt = "(推定＆推測＆推量)(報告＆連絡)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はいます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はいる")):
            extrct_intnt_rslt = "(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がいます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がいる")):
            extrct_intnt_rslt = "(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(個人・個物特定)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はいません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はいない")):
            extrct_intnt_rslt = "(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がいません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がいない")):
            extrct_intnt_rslt = "(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(個人・個物特定)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "にいます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "にいる")):
            extrct_intnt_rslt = "(報告＆連絡)(所在＆場所)(人間＆動物＆その他)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "にいません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "にいない")):
            extrct_intnt_rslt = "(報告＆連絡)(所在＆場所)(人間＆動物＆その他)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はあります") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はある")):
            extrct_intnt_rslt = "(報告＆連絡)(存在＆有無)(物体＆モノ全般)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "があります") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がある")):
            extrct_intnt_rslt = "(報告＆連絡)(存在＆有無)(物体＆モノ全般)(個人・個物特定)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はありません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はない")):
            extrct_intnt_rslt = "(報告＆連絡)(存在＆有無)(物体＆モノ全般)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がありません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がない")):
            extrct_intnt_rslt = "(報告＆連絡)(存在＆有無)(物体＆モノ全般)(個人・個物特定)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "するか")):
           extrct_intnt_rslt = "(疑義＆質問＆確認)(現在＆未来＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないか")):
           extrct_intnt_rslt = "(疑義＆質問＆確認)(現在＆未来＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しているか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してるか")):
           extrct_intnt_rslt = "(疑義＆質問＆確認)(現在進行＆能動＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "していないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(現在進行＆能動＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できているか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてるか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(現在進行＆能動＆可能＆肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できていないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できていませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてませんか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(現在進行＆能動＆可能＆否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できましたか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できたか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(過去＆能受不明＆可能＝完了)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できていませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できてないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(過去＆能受不明＆不可能＝未完了)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できるか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(現在＆能動＆可能)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "できませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "できないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(現在＆能動＆不可能)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(未来)(能動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "しましたか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "したか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやりましたか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやったか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(過去)(能動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "していませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(過去進行)(能動)(否定)"    
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされていますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされていますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されていますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてますか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(過去進行)(受動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされていませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされていませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されていませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されていないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されてないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(過去進行)(受動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がされましたか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はされましたか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されましたか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "されたか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(過去完了)(受動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "でしたか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だったですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だったか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(過去完了)(能受不明)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でなかったか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(過去完了)(能受不明)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "をしていきたいですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしていきたいか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてたいですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてたいか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたいですか")
          check_text_terminated_string(rmv_edprtcl_rslt, "をやってたいですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやってたいか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "していきたいか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してたいか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "いたいか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(現在＆未来)(持続)(能動)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はしていきたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "していきたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしていきたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやっていきたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやってたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやっていきたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやってたくないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやっていかないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやっていかないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやってかないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はやってかないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(現在＆未来)(持続)(能動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではなかったか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でなかったか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(現在＆未来)(持続)(能動)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ますか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(紹介＆説明＆提示)(能受不明)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "っていましたか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってましたか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってたか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(過去＆能動)"
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
            extrct_intnt_rslt = "(疑義＆質問＆確認)(叙述内容)(単純)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "をしませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しませんか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(誘導＆勧誘)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "したいか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "たいか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "やりたいか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "たいですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "たいか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(願望・欲求について)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "いですか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(様子＆様相)(能受不明)")
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃ駄目ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃだめですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃダメですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてはいけませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃ駄目ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃだめですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃダメですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてはいけませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃ駄目か") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃだめか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃダメか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃ駄目か") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃだめか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃダメか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃ駄目か") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃだめか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃダメか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(制止＆禁止)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃ駄目か") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃだめか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃダメか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(制止＆禁止)(特定個人)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "をしてくれますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してくれますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてくれるか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してくれるか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてくださいますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してくださいますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてくれますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してくれますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してくれるか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやってくれますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をやってくれるか")):
            extrct_intnt_rslt = "(依頼＆要求)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしてくださいますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしてくれますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がやってくれますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がやってくれるか")):
            extrct_intnt_rslt = "(依頼＆要求)(特定個人)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はしなければならないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなければいけないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしないといけないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃいけないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしなきゃいけませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃいけませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はせにゃならんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "せにゃならんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなければならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしないといけないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしないといけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃいけませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしなきゃならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をせにゃならんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなければならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなければいけませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないといけないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しないといけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃいけないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しなきゃならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "せにゃならんか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(勧告)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしなければならないのですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなければならないんですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなければならないのかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなければならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしないといけないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしないといけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけないかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけませんかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしなきゃいけませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がせにゃならんかのかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がせにゃならんかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がせにゃならんか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(勧告)(肯定)(特定個人)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はしてはならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしてはいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしたらいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はしちゃならんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてはならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしてはいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしたらいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をしちゃならんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してはならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "してはいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "したらいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "しちゃならんか"):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(勧告)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がしてはならないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしてはいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしたらいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃいけないか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がしちゃならんか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(勧告)(否定)(特定個人)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だろうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "だろか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(推定＆推測＆推量)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はいますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はいるか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がいますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がいるか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(個人・個物特定)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はいませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はいないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がいませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がいないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(存在＆有無)(人間＆動物＆その他)(個人・個物特定)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "にいますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "にいるか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(所在＆場所)(人間＆動物＆その他)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "にいませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "にいないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(所在＆場所)(人間＆動物＆その他)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はありますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はあるか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(存在＆有無)(物体＆モノ全般)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がありますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "があるか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(存在＆有無)(物体＆モノ全般)(個人・個物特定)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はありませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(存在＆有無)(物体＆モノ全般)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "がありませんか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "がないか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(報告＆連絡)(存在＆有無)(物体＆モノ全般)(個人・個物特定)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はだね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をだね")):
            extrct_intnt_rslt = "(紹介＆説明＆提示)(継続)(前段)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "をお願い致します") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をお願いいたします") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をお願いします") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をお願い") or
          check_text_terminated_string(rmv_edprtcl_rslt, "お願い致します") or
          check_text_terminated_string(rmv_edprtcl_rslt, "お願いいたします") or
          check_text_terminated_string(rmv_edprtcl_rslt, "お願いします") or
          check_text_terminated_string(rmv_edprtcl_rslt, "お願い")):
            extrct_intnt_rslt = "(依願＆依頼)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "大丈夫でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "大丈夫ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "大丈夫")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(安否)(健康状態)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫ではないのでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫ではないんですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "大丈夫ではないのでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "大丈夫ではないんですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫じゃないんですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "大丈夫じゃないんですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫じゃない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "大丈夫じゃない")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(安否)(健康状態)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "は必要でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は必要ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "必要ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "必要") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要りますでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要りますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "要りますでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "要りますか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "要る")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(要否)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "は要らないでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "要らないでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要らないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "要らないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要らないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要らない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "要らない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は不要でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "不要でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は不要ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "不要ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は不要") or
          check_text_terminated_string(rmv_edprtcl_rslt, "不要")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(要否)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はするべきでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をするべきでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はすべきでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をすべきでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "するべきでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "すべきでしょうか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(是非)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はするべきではないということでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をするべきではないということでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はすべきではないということでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をすべきではないということでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "するべきではないということでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "すべきではないということでしょうか")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(是非)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫です") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫")):
            extrct_intnt_rslt = "(宣言＆表明)(安否)(健康状態)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫ではない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は大丈夫でない")):
            extrct_intnt_rslt = "(宣言＆表明)(安否)(健康状態)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "は必要です") or
          check_text_terminated_string(rmv_edprtcl_rslt, "が必要です") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は必要") or
          check_text_terminated_string(rmv_edprtcl_rslt, "が必要") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要ります") or
          check_text_terminated_string(rmv_edprtcl_rslt, "が要ります") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要る") or
          check_text_terminated_string(rmv_edprtcl_rslt, "が要る")):
            extrct_intnt_rslt = "(宣言＆表明)(要否)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "は要らないでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "要らないでしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要らないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "要らないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要らないですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は要らない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "要らない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は不要でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "不要でしょうか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は不要ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "不要ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "は不要") or
          check_text_terminated_string(rmv_edprtcl_rslt, "不要")):
            extrct_intnt_rslt = "(宣言＆表明)(要否)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はするべきです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をするべきです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はすべきです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をすべきです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "するべきです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "すべきです")):
            extrct_intnt_rslt = "(宣言＆表明)(是非)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "はするべきではないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をするべきではないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はすべきではないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をすべきではないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "すべきではないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はするべきではない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をするべきではない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はすべきではない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をすべきではない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "するべきではない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "すべきではない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はするべきでない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をするべきでない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "するべきでない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "はすべきでない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "をすべきでない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "すべきでない")):
            extrct_intnt_rslt = "(宣言＆表明)(是非)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "という事でしょう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でいうことでしょう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "という事でしょうね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということでしょうね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でしょう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でしょうね")):
            extrct_intnt_rslt = "(推定＆推測＆推量)(進言＆提言)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "という事ではないでしょう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということではないでしょう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "という事ではないでしょうね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということではないでしょうね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではないでしょう") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではないでしょうね")):
            extrct_intnt_rslt = "(推定＆推測＆推量)(進言＆提言)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "かも知れないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "かも知れない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "かもしれないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "かもしれない"):
            extrct_intnt_rslt = "(推定＆推測＆推量)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではないかも知れないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではないかも知れない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではないかもしれないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではないかもしれない" or
          check_text_terminated_string(rmv_edprtcl_rslt, "でないかも知れないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でないかも知れない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でないかもしれないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "でないかもしれない"):
            extrct_intnt_rslt = "(推定＆推測＆推量)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "ではと思っています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではと思ってます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではと思っている") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ではと思ってる") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っている") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思ってる") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思っています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思ってます") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思っている") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思ってる") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っています") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っている") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思ってる") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思う"):
            extrct_intnt_rslt = "(思慮＆考慮)(現在)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "とは思っていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思ってません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思っていない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思ってない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っていません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思ってません") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っていない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思ってない")):
            extrct_intnt_rslt = "(思慮＆考慮)(現在)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "とは思っていました") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思っていた") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思ってた") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っていました" or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っていた" or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思ってた")):
            extrct_intnt_rslt = "(思慮＆考慮)(過去)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "とは思っていませんでした") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思っていなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思っていなかったな") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思ってなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "とは思ってなかったな" or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っていませんでした") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っていなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思っていなかったな") or                             
          check_text_terminated_string(rmv_edprtcl_rslt, "と思ってなかった") or
          check_text_terminated_string(rmv_edprtcl_rslt, "と思ってなかったな")):
            extrct_intnt_rslt = "(思慮＆考慮)(過去)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "らしい") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしいです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしいですよ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしいですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしいね")):
            extrct_intnt_rslt = "(感想＆感慨)(形容)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "らしくない") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしくないです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしくないですよ") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしくないですね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしくないね")):
            extrct_intnt_rslt = "(感想＆感慨)(形容)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "らしいですよね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしいよね")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(感想＆感慨)(形容)(肯定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "らしくないですよね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "らしくないよね")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(感想＆感慨)(形容)(否定)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "という事です") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "っていう事です") or
          check_text_terminated_string(rmv_edprtcl_rslt, "っていうことです") or
          check_text_terminated_string(rmv_edprtcl_rslt, "って事です") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってことです")):
            extrct_intnt_rslt = "(紹介＆説明＆提示)(叙述)"
    elif (check_text_terminated_string(rmv_edprtcl_rslt, "という事ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "っていう事ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "っていうことですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "って事ですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってことですか") or
          check_text_terminated_string(rmv_edprtcl_rslt, "という事ですかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ということですかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "っていう事ですかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "っていうことですかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "って事ですかね") or
          check_text_terminated_string(rmv_edprtcl_rslt, "ってことですかね")):
            extrct_intnt_rslt = "(疑義＆質問＆確認)(叙述)"
    else:
            extrct_intnt_rslt = "(その他・不明)"
    return extrct_intnt_rslt


#ユーザーから送られるLINEメッセージの中からサブコンテント(＝副詞＆前置詞＆接続詞)を抽出する
def extract_subcontent(rmv_edprtcl_rslt):
    #メッセージの先頭部分からサブコンテントを抽出して、これを呼出し元に引渡しをする
    if   (check_text_start_string(rmv_edprtcl_rslt, "さて") or
          check_text_start_string(rmv_edprtcl_rslt, "ところで")):
            extrct_subcntnt_rslt = "(転換＆切替)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "そして") or
          check_text_start_string(rmv_edprtcl_rslt, "それで") or
          check_text_start_string(rmv_edprtcl_rslt, "そんで")):
            extrct_subcntnt_rslt = "(結論＆結末)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "加えて") or
          check_text_start_string(rmv_edprtcl_rslt, "更に") or
          check_text_start_string(rmv_edprtcl_rslt, "さらに") or
          check_text_start_string(rmv_edprtcl_rslt, "又") or
          check_text_start_string(rmv_edprtcl_rslt, "また")):
            extrct_subcntnt_rslt = "(添加＆追加)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "多分") or
          check_text_start_string(rmv_edprtcl_rslt, "たぶん") or
          check_text_start_string(rmv_edprtcl_rslt, "恐らくは") or
          check_text_start_string(rmv_edprtcl_rslt, "おそらくは") or
          check_text_start_string(rmv_edprtcl_rslt, "恐らく") or
          check_text_start_string(rmv_edprtcl_rslt, "おそらく")):
            extrct_subcntnt_rslt = "(推定＆推測＆推量)(揣摩＆憶測)(理知・理性的に言う)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "又は") or
          check_text_start_string(rmv_edprtcl_rslt, "または")):
            extrct_subcntnt_rslt = "(論理和)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "且つ") or
          check_text_start_string(rmv_edprtcl_rslt, "かつ")):
            extrct_subcntnt_rslt = "(論理積)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "得てして") or
          check_text_start_string(rmv_edprtcl_rslt, "えてして") or
          check_text_start_string(rmv_edprtcl_rslt, "概して") or
          check_text_start_string(rmv_edprtcl_rslt, "大抵は") or
          check_text_start_string(rmv_edprtcl_rslt, "大抵") or
          check_text_start_string(rmv_edprtcl_rslt, "大概は") or
          check_text_start_string(rmv_edprtcl_rslt, "大概")): 
            extrct_subcntnt_rslt = "(概要＆概略)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "確実に") or
          check_text_start_string(rmv_edprtcl_rslt, "明らかに") or
          check_text_start_string(rmv_edprtcl_rslt, "多くの場合には") or
          check_text_start_string(rmv_edprtcl_rslt, "多くの場合は") or
          check_text_start_string(rmv_edprtcl_rslt, "多くの場合") or
          check_text_start_string(rmv_edprtcl_rslt, "多くは") or
          check_text_start_string(rmv_edprtcl_rslt, "多く") or
          check_text_start_string(rmv_edprtcl_rslt, "少なくとも") or
          check_text_start_string(rmv_edprtcl_rslt, "少なくても")):
            extrct_subcntnt_rslt = "(断定＆確定)"
    elif  check_text_start_string(rmv_edprtcl_rslt, "(大層"):
            extrct_subcntnt_rslt = "(程度強調)(情緒・感情的に言う)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "なので") or
          check_text_start_string(rmv_edprtcl_rslt, "ですから")):
            extrct_subcntnt_rslt = "(説得＆説明)(事由＆理由＆事情＆状況)"
    elif check_text_start_string(rmv_edprtcl_rslt, "さては"):
            extrct_subcntnt_rslt = "(推定＆推測＆推量)(確定＆断定)(事実)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "もしや"):
            extrct_subcntnt_rslt = "(推定＆推測＆推量)(揣摩＆憶測)(仮定＆仮説)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "もしも") or
          check_text_start_string(rmv_edprtcl_rslt, "もし")):
            extrct_subcntnt_rslt = "(仮定＆仮説)(原因＆要因＆事情＆状況＆状態的)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "例えば") or
          check_text_start_string(rmv_edprtcl_rslt, "たとえば") or
          check_text_start_string(rmv_edprtcl_rslt, "例すれば") or
          check_text_start_string(rmv_edprtcl_rslt, "例せば")):
            extrct_subcntnt_rslt = "(比喩＆類例)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "類すれば") or
          check_text_start_string(rmv_edprtcl_rslt, "類せば")):
            extrct_subcntnt_rslt = "(仮定＆仮説)(比較＆類似)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "譬え") or
          check_text_start_string(rmv_edprtcl_rslt, "たとえ") or
          check_text_start_string(rmv_edprtcl_rslt, "仮に")):
            extrct_subcntnt_rslt = "(仮定＆仮説)(特別・特例言及)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "或いは") or
          check_text_start_string(rmv_edprtcl_rslt, "あるいは")):
            extrct_subcntnt_rslt = "(選択＆追求)(可能性)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "若しくは") or
          check_text_start_string(rmv_edprtcl_rslt, "もしくは") or
          check_text_start_string(rmv_edprtcl_rslt, "もしか")):
            extrct_subcntnt_rslt = "(選択＆追求)(可能性)(代理＆代替)(対名詞・存在)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "乃至は") or
          check_text_start_string(rmv_edprtcl_rslt, "ないしは") or
          check_text_start_string(rmv_edprtcl_rslt, "ないし")):
            extrct_subcntnt_rslt = "(選択＆追求)(可能性)(代理＆代替)(対動詞・行為)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "さぞかし") or
          check_text_start_string(rmv_edprtcl_rslt, "さぞ")):
            extrct_subcntnt_rslt = "(推定＆推測＆推量)(揣摩＆憶測)(感情＆感性)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "決して") or
          check_text_start_string(rmv_edprtcl_rslt, "決まって"):
            extrct_subcntnt_rslt = "(断定＆確定)(限定)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "ひょっとして") or
          check_text_start_string(rmv_edprtcl_rslt, "もしかして"):
            extrct_subcntnt_rslt = "(推定＆推測＆推量)(揣摩＆憶測)(中立＆中性)"
    elif  check_text_start_string(rmv_edprtcl_rslt, "もしかしたら"):
            extrct_subcntnt_rslt = "(推定＆推測＆推量)(揣摩＆憶測)(場合分け)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "必ずしも") or
          check_text_start_string(rmv_edprtcl_rslt, "必ずしも")):
            extrct_subcntnt_rslt = "(確信・約束に至らない場合)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "必ずや") or
          check_text_start_string(rmv_edprtcl_rslt, "必ず")):
            extrct_subcntnt_rslt = "(確信＆約束)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "もっと言えば") or
          check_text_start_string(rmv_edprtcl_rslt, "もっといえば") or
          check_text_start_string(rmv_edprtcl_rslt, "更に言えば") or
          check_text_start_string(rmv_edprtcl_rslt, "さらに言えば")):
            extrct_subcntnt_rslt = "(添加＆追加)(条件付け)(補足)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "欲を言えば") or
          check_text_start_string(rmv_edprtcl_rslt, "欲をいえば")):
            extrct_subcntnt_rslt = "(添加＆追加)(条件付け)(願望・欲求について)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "強ち") or
          check_text_start_string(rmv_edprtcl_rslt, "あながち")):
            extrct_subcntnt_rslt = "(推定＆推測＆推量)(揣摩＆憶測)(意外なことにも考えを巡らす)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "最も") or
          check_text_start_string(rmv_edprtcl_rslt, "もっとも")):
            extrct_subcntnt_rslt = "(結果＆結論)(皮相＆皮肉)"
    elif  check_text_start_string(rmv_edprtcl_rslt, "実に"):
            extrct_subcntnt_rslt = "(認知・認識強調)(事実＆現実)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "畢竟") or
          check_text_start_string(rmv_edprtcl_rslt, "詮ずる所") or
          check_text_start_string(rmv_edprtcl_rslt, "詮ずるところ") or
          check_text_start_string(rmv_edprtcl_rslt, "詮ずると") or
          check_text_start_string(rmv_edprtcl_rslt, "詰まる所") or
          check_text_start_string(rmv_edprtcl_rslt, "詰まるところ") or
          check_text_start_string(rmv_edprtcl_rslt, "詰まりは") or
          check_text_start_string(rmv_edprtcl_rslt, "つまりは") or
          check_text_start_string(rmv_edprtcl_rslt, "詰まり") or
          check_text_start_string(rmv_edprtcl_rslt, "つまり")):
            extrct_subcntnt_rslt = "(結果＆結論)"
    elif (check_text_start_string(rmv_edprtcl_rslt,"まさか") or
          check_text_start_string(rmv_edprtcl_rslt,"よもや")):
            extrct_subcntnt_rslt = "(臆見＆憶測)(思惑＆感情)"
    elif (check_text_start_string(rmv_edprtcl_rslt,"当然にして") or
          check_text_start_string(rmv_edprtcl_rslt, "当然")):
            extrct_subcntnt_rslt = "(推理＆推論)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "非常に") or
          check_text_start_string(rmv_edprtcl_rslt,"とても")):
            extrct_subcntnt_rslt = "(程度強調)"
    elif (check_text_start_string(rmv_edprtcl_rslt,"極めて") or
          check_text_start_string(rmv_edprtcl_rslt,"かなり")):
            extrct_subcntnt_rslt = "(程度強調)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "纏めると") or
          check_text_start_string(rmv_edprtcl_rslt, "まとめると")):
            extrct_subcntnt_rslt = "(総括＆概括)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "初めに") or
          check_text_start_string(rmv_edprtcl_rslt, "はじめに"):
            extrct_subcntnt_rslt = "(前置き)(最初)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "終わりに") or
          check_text_start_string(rmv_edprtcl_rslt, "おわりに"):
            extrct_subcntnt_rslt = "(前置き)(最後)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "だけども") or
          check_text_start_string(rmv_edprtcl_rslt, "だけど") or
          check_text_start_string(rmv_edprtcl_rslt, "それでも") or
          check_text_start_string(rmv_edprtcl_rslt, "でも")):
            extrct_subcntnt_rslt = "(反駁＆反論)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "言い換えれば") or
          check_text_start_string(rmv_edprtcl_rslt, "言い換えると")):
            extrct_subcntnt_rslt = "(換言＆言換え)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "初めに言っておくと") or
          check_text_start_string(rmv_edprtcl_rslt, "はじめに言っておくと") or
          check_text_start_string(rmv_edprtcl_rslt, "先に言っておくと") or
          check_text_start_string(rmv_edprtcl_rslt, "先に言っておくけど")):
            extrct_subcntnt_rslt = "(前置き＆先述)"
    elif (check_text_start_string(rmv_edprtcl_rslt, "初めに断っておくと") or
          check_text_start_string(rmv_edprtcl_rslt, "はじめに断っておくと") or
          check_text_start_string(rmv_edprtcl_rslt, "初めに断っておくけど") or
          check_text_start_string(rmv_edprtcl_rslt, "はじめに断っておくけど")):
            extrct_subcntnt_rslt = "(断り＆先述)"
    else:
            extrct_subcntnt_rslt = "(その他・不明)"
    return extrct_subcntnt_rslt


#ユーザーから送られるLINEメッセージの中に含まれるコンテントを解析する
def analyze_content(rmv_intnt_rslt):
    anlyz_cntnt_rslt = ""
    return anlyz_cntnt_rslt


#ユーザーから送られるLINEメッセージの中に含まれるサブコンテント(＝副詞＆前置詞＆接続詞)を除去する
def remove_subcontent(rmv_edprtcl_rslt):
    #メッセージの中に含まれる日本語固有のサブコンテントの削除候補をリストアップする
    rmv_cnddt_subcntnt_list = []
    if check_text_start_string(rmv_edprtcl_rslt, "さて"):
         rmv_cnddt_subcntnt_list.append("さて")
    if check_text_start_string(rmv_edprtcl_rslt, "ところで"):
         rmv_cnddt_subcntnt_list.append("ところで")
    if check_text_start_string(rmv_edprtcl_rslt, "そして"):
         rmv_cnddt_subcntnt_list.append("そして")
    if check_text_start_string(rmv_edprtcl_rslt, "それで"):
         rmv_cnddt_subcntnt_list.append("それで")
    if check_text_start_string(rmv_edprtcl_rslt, "そんで"):
         rmv_cnddt_subcntnt_list.append("そんで")
    if check_text_start_string(rmv_edprtcl_rslt, "加えて"):
         rmv_cnddt_subcntnt_list.append("加えて")
    if check_text_start_string(rmv_edprtcl_rslt, "更に"):
         rmv_cnddt_subcntnt_list.append("更に")
    if check_text_start_string(rmv_edprtcl_rslt, "さらに"):
         rmv_cnddt_subcntnt_list.append("さらに")
    if check_text_start_string(rmv_edprtcl_rslt, "又"):
         rmv_cnddt_subcntnt_list.append("又")
    if check_text_start_string(rmv_edprtcl_rslt, "また"):
         rmv_cnddt_subcntnt_list.append("また")
    if check_text_start_string(rmv_edprtcl_rslt, "多分"):
         rmv_cnddt_subcntnt_list.append("多分")
    if check_text_start_string(rmv_edprtcl_rslt, "たぶん"):
         rmv_cnddt_subcntnt_list.append("たぶん")
    if check_text_start_string(rmv_edprtcl_rslt, "恐らくは"):
         rmv_cnddt_subcntnt_list.append("恐らくは")
    if check_text_start_string(rmv_edprtcl_rslt, "おそらくは"):
         rmv_cnddt_subcntnt_list.append("おそらくは")
    if check_text_start_string(rmv_edprtcl_rslt, "恐らく"):
         rmv_cnddt_subcntnt_list.append("恐らく")
    if check_text_start_string(rmv_edprtcl_rslt, "おそらく"):
       rmv_cnddt_subcntnt_list.append("おそらく")
    if check_text_start_string(rmv_edprtcl_rslt, "又は"):
         rmv_cnddt_subcntnt_list.append("又は")
    if check_text_start_string(rmv_edprtcl_rslt, "または"):
         rmv_cnddt_subcntnt_list.append("または")
    if check_text_start_string(rmv_edprtcl_rslt, "且つ"):
         rmv_cnddt_subcntnt_list.append("且つ")
    if check_text_start_string(rmv_edprtcl_rslt, "かつ")):
         rmv_cnddt_subcntnt_list.append("かつ")
    if check_text_start_string(rmv_edprtcl_rslt, "得てして"):
         rmv_cnddt_subcntnt_list.append("得てして")
    if check_text_start_string(rmv_edprtcl_rslt, "えてして"):
         rmv_cnddt_subcntnt_list.append("えてして")
    if check_text_start_string(rmv_edprtcl_rslt, "概して"):
         rmv_cnddt_subcntnt_list.append("概して")
    if check_text_start_string(rmv_edprtcl_rslt, "大抵は"):
         rmv_cnddt_subcntnt_list.append("大抵は")
    if check_text_start_string(rmv_edprtcl_rslt, "大抵"):
         rmv_cnddt_subcntnt_list.append("大抵")
    if check_text_start_string(rmv_edprtcl_rslt, "大概は"):
         rmv_cnddt_subcntnt_list.append("大概は")
    if check_text_start_string(rmv_edprtcl_rslt, "大概"):
         rmv_cnddt_subcntnt_list.append("大概")
    if check_text_start_string(rmv_edprtcl_rslt, "確実に"):
         rmv_cnddt_subcntnt_list.append("確実に")
    if check_text_start_string(rmv_edprtcl_rslt, "明らかに"):
         rmv_cnddt_subcntnt_list.append("明らかに")
    if check_text_start_string(rmv_edprtcl_rslt, "多くの場合には"):
         rmv_cnddt_subcntnt_list.append("多くの場合には")
    if check_text_start_string(rmv_edprtcl_rslt, "多くの場合は"):
         rmv_cnddt_subcntnt_list.append("多くの場合は")
    if check_text_start_string(rmv_edprtcl_rslt, "多くの場合"):
         rmv_cnddt_subcntnt_list.append("多くの場合")
    if check_text_start_string(rmv_edprtcl_rslt, "多くは"):
         rmv_cnddt_subcntnt_list.append("多くは")
    if check_text_start_string(rmv_edprtcl_rslt, "多く"):
         rmv_cnddt_subcntnt_list.append("多く")
    if check_text_start_string(rmv_edprtcl_rslt, "少なくとも"):
         rmv_cnddt_subcntnt_list.append("少なくとも")
    if check_text_start_string(rmv_edprtcl_rslt, "少なくても"):
         rmv_cnddt_subcntnt_list.append("少なくても")
    if check_text_start_string(rmv_edprtcl_rslt, "大層"):
         rmv_cnddt_subcntnt_list.append("大層")
    if check_text_start_string(rmv_edprtcl_rslt, "なので"):
         rmv_cnddt_subcntnt_list.append("なので")
    if check_text_start_string(rmv_edprtcl_rslt, "ですから"):
         rmv_cnddt_subcntnt_list.append("ですから")
    if check_text_start_string(rmv_edprtcl_rslt, "さては"):
         rmv_cnddt_subcntnt_list.append("さては")
    if check_text_start_string(rmv_edprtcl_rslt, "もしや"):
         rmv_cnddt_subcntnt_list.append("もしや")
    if check_text_start_string(rmv_edprtcl_rslt, "もしも"):
         rmv_cnddt_subcntnt_list.append("もしも")
    if check_text_start_string(rmv_edprtcl_rslt, "もし"):
         rmv_cnddt_subcntnt_list.append("もし")
    if check_text_start_string(rmv_edprtcl_rslt, "例えば"):
         rmv_cnddt_subcntnt_list.append("例えば")
    if check_text_start_string(rmv_edprtcl_rslt, "たとえば"):
         rmv_cnddt_subcntnt_list.append("たとえば")
    if check_text_start_string(rmv_edprtcl_rslt, "例すれば"):
         rmv_cnddt_subcntnt_list.append("例すれば")
    if check_text_start_string(rmv_edprtcl_rslt, "例せば"):
         rmv_cnddt_subcntnt_list.append("例せば")
    if check_text_start_string(rmv_edprtcl_rslt, "類すれば"):
         rmv_cnddt_subcntnt_list.append("類すれば")
    if check_text_start_string(rmv_edprtcl_rslt, "類せば"):
         rmv_cnddt_subcntnt_list.append("類せば")
    if check_text_start_string(rmv_edprtcl_rslt, "譬え"):
         rmv_cnddt_subcntnt_list.append("譬え")
    if check_text_start_string(rmv_edprtcl_rslt, "たとえ"):
         rmv_cnddt_subcntnt_list.append("たとえ")
    if check_text_start_string(rmv_edprtcl_rslt, "仮に"):
         rmv_cnddt_subcntnt_list.append("仮に")
    if check_text_start_string(rmv_edprtcl_rslt, "或いは"):
         rmv_cnddt_subcntnt_list.append("或いは")
    if check_text_start_string(rmv_edprtcl_rslt, "あるいは"):
         rmv_cnddt_subcntnt_list.append("あるいは")
    if check_text_start_string(rmv_edprtcl_rslt, "若しくは"):
         rmv_cnddt_subcntnt_list.append("若しくは")
    if check_text_start_string(rmv_edprtcl_rslt, "もしくは"):
         rmv_cnddt_subcntnt_list.append("もしくは")
    if check_text_start_string(rmv_edprtcl_rslt, "もしか"):
         rmv_cnddt_subcntnt_list.append("もしか")
    if check_text_start_string(rmv_edprtcl_rslt, "乃至は"):
         rmv_cnddt_subcntnt_list.append("乃至は")
    if check_text_start_string(rmv_edprtcl_rslt, "ないしは"):
         rmv_cnddt_subcntnt_list.append("ないしは")
    if check_text_start_string(rmv_edprtcl_rslt, "ないし"):
         rmv_cnddt_subcntnt_list.append("ないし")
    if check_text_start_string(rmv_edprtcl_rslt, "さぞかし"):
         rmv_cnddt_subcntnt_list.append("さぞかし")
    if check_text_start_string(rmv_edprtcl_rslt, "さぞ"):
         rmv_cnddt_subcntnt_list.append("さぞ")
    if check_text_start_string(rmv_edprtcl_rslt, "決して"):
         rmv_cnddt_subcntnt_list.append("決して")
    if check_text_start_string(rmv_edprtcl_rslt, "決まって"):
         rmv_cnddt_subcntnt_list.append("決まって")
    if check_text_start_string(rmv_edprtcl_rslt, "ひょっとして"):
         rmv_cnddt_subcntnt_list.append("ひょっとして")
    if check_text_start_string(rmv_edprtcl_rslt, "もしかして"):
         rmv_cnddt_subcntnt_list.append("もしかして")
    if check_text_start_string(rmv_edprtcl_rslt, "もしかしたら"):
         rmv_cnddt_subcntnt_list.append("もしかしたら")
    if check_text_start_string(rmv_edprtcl_rslt, "必ずしも"):
         rmv_cnddt_subcntnt_list.append("必ずしも")
    if check_text_start_string(rmv_edprtcl_rslt, "必ずや"):
         rmv_cnddt_subcntnt_list.append("必ずや")
    if check_text_start_string(rmv_edprtcl_rslt, "必ず"):
         rmv_cnddt_subcntnt_list.append("必ず")
    if check_text_start_string(rmv_edprtcl_rslt, "もっと言えば"):
         rmv_cnddt_subcntnt_list.append("もっと言えば")
    if check_text_start_string(rmv_edprtcl_rslt, "もっといえば"):
         rmv_cnddt_subcntnt_list.append("もっといえば")
    if check_text_start_string(rmv_edprtcl_rslt, "更に言えば"):
         rmv_cnddt_subcntnt_list.append("更に言えば")
    if check_text_start_string(rmv_edprtcl_rslt, "さらに言えば"):
         rmv_cnddt_subcntnt_list.append("さらに言えば")
    if check_text_start_string(rmv_edprtcl_rslt, "欲を言えば"):
         rmv_cnddt_subcntnt_list.append("欲を言えば")
    if check_text_start_string(rmv_edprtcl_rslt, "欲をいえば"):
         rmv_cnddt_subcntnt_list.append("欲をいえば")
    if check_text_start_string(rmv_edprtcl_rslt, "強ち"):
         rmv_cnddt_subcntnt_list.append("強ち")
    if check_text_start_string(rmv_edprtcl_rslt, "あながち"):
         rmv_cnddt_subcntnt_list.append("あながち")
    if check_text_start_string(rmv_edprtcl_rslt, "最も"):
         rmv_cnddt_subcntnt_list.append("最も")
    if check_text_start_string(rmv_edprtcl_rslt, "もっとも"):
         rmv_cnddt_subcntnt_list.append("もっとも")
    if check_text_start_string(rmv_edprtcl_rslt, "実に"):
         rmv_cnddt_subcntnt_list.append("実に")
    if check_text_start_string(rmv_edprtcl_rslt, "畢竟"):
         rmv_cnddt_subcntnt_list.append("畢竟")
    if check_text_start_string(rmv_edprtcl_rslt, "詮ずる所"):
         rmv_cnddt_subcntnt_list.append("詮ずる所")
    if check_text_start_string(rmv_edprtcl_rslt, "詮ずるところ"):
         rmv_cnddt_subcntnt_list.append("詮ずるところ")
    if check_text_start_string(rmv_edprtcl_rslt, "詮ずると"):
         rmv_cnddt_subcntnt_list.append("詮ずると")
    if check_text_start_string(rmv_edprtcl_rslt, "詰まる所"):
         rmv_cnddt_subcntnt_list.append("詰まる所")
    if check_text_start_string(rmv_edprtcl_rslt, "詰まるところ"):
         rmv_cnddt_subcntnt_list.append("詰まるところ")
    if check_text_start_string(rmv_edprtcl_rslt, "詰まりは"):
         rmv_cnddt_subcntnt_list.append("つまりは")
    if check_text_start_string(rmv_edprtcl_rslt, "つまりは"):
         rmv_cnddt_subcntnt_list.append("つまりは")
    if check_text_start_string(rmv_edprtcl_rslt, "詰まり"):
         rmv_cnddt_subcntnt_list.append("詰まり")
    if check_text_start_string(rmv_edprtcl_rslt, "つまり"):
         rmv_cnddt_subcntnt_list.append("つまり")
    if check_text_start_string(rmv_edprtcl_rslt, "まさか"):
         rmv_cnddt_subcntnt_list.append("まさか")
    if check_text_start_string(rmv_edprtcl_rslt, "よもや"):
         rmv_cnddt_subcntnt_list.append("よもや")
    if check_text_start_string(rmv_edprtcl_rslt, "当然にして"):
         rmv_cnddt_subcntnt_list.append("当然にして")
    if check_text_start_string(rmv_edprtcl_rslt, "当然"):
         rmv_cnddt_subcntnt_list.append("当然")
    if check_text_start_string(rmv_edprtcl_rslt, "非常に"):
         rmv_cnddt_subcntnt_list.append("非常に")
    if check_text_start_string(rmv_edprtcl_rslt, "とても"):
         rmv_cnddt_subcntnt_list.append("とても")
    if check_text_start_string(rmv_edprtcl_rslt, "極めて"):
         rmv_cnddt_subcntnt_list.append("極めて")
    if check_text_start_string(rmv_edprtcl_rslt, "かなり"):
         rmv_cnddt_subcntnt_list.append("かなり")
    if check_text_start_string(rmv_edprtcl_rslt, "纏めると"):
         rmv_cnddt_subcntnt_list.append("纏めると")
    if check_text_start_string(rmv_edprtcl_rslt, "まとめると"):
         rmv_cnddt_subcntnt_list.append("まとめると")
    if check_text_start_string(rmv_edprtcl_rslt, "初めに"):
         rmv_cnddt_subcntnt_list.append("初めに")
    if check_text_start_string(rmv_edprtcl_rslt, "はじめに"):
         rmv_cnddt_subcntnt_list.append("はじめに")
    if check_text_start_string(rmv_edprtcl_rslt, "終わりに"):
         rmv_cnddt_subcntnt_list.append("終わりに")
    if check_text_start_string(rmv_edprtcl_rslt, "おわりに"):
         rmv_cnddt_subcntnt_list.append("おわりに")
    if check_text_start_string(rmv_edprtcl_rslt, "だけども"):
         rmv_cnddt_subcntnt_list.append("だけども")
    if check_text_start_string(rmv_edprtcl_rslt, "だけど"):
         rmv_cnddt_subcntnt_list.append("だけど")
    if check_text_start_string(rmv_edprtcl_rslt, "それでも"):
         rmv_cnddt_subcntnt_list.append("それでも")
    if check_text_start_string(rmv_edprtcl_rslt, "でも"):
         rmv_cnddt_subcntnt_list.append("でも")
    if check_text_start_string(rmv_edprtcl_rslt, "言い換えれば"):
         rmv_cnddt_subcntnt_list.append("言い換えれば")
    if check_text_start_string(rmv_edprtcl_rslt, "言い換えると"):
         rmv_cnddt_subcntnt_list.append("言い換えると")
    if check_text_start_string(rmv_edprtcl_rslt, "初めに言っておくと"):
         rmv_cnddt_subcntnt_list.append("初めに言っておくと")
    if check_text_start_string(rmv_edprtcl_rslt, "はじめに言っておくと"):
         rmv_cnddt_subcntnt_list.append("はじめに言っておくと")
    if check_text_start_string(rmv_edprtcl_rslt, "先に言っておくと"):
         rmv_cnddt_subcntnt_list.append("先に言っておくと")
    if check_text_start_string(rmv_edprtcl_rslt, "先に言っておくけど"):
         rmv_cnddt_subcntnt_list.append("先に言っておくけど")
    if check_text_start_string(rmv_edprtcl_rslt, "初めに断っておくと"):
         rmv_cnddt_subcntnt_list.append("初めに断っておくと")
    if check_text_start_string(rmv_edprtcl_rslt, "はじめに断っておくと"):
         rmv_cnddt_subcntnt_list.append("はじめに断っておくと")
    if check_text_start_string(rmv_edprtcl_rslt, "初めに断っておくけど"):
         rmv_cnddt_subcntnt_list.append("初めに断っておくけど")
    if check_text_start_string(rmv_edprtcl_rslt, "はじめに断っておくけど"):
         rmv_cnddt_subcntnt_list.append("はじめに断っておくけど")

    #前段で取得した削除候補の中から実際に削除するサブコンテントを決定して、これを呼出し元に引渡しをする
    rmv_cnddt_subcntnt_list_tmp = []
    for subcntnt in rmv_cnddt_subcntnt_list:
        rmv_cnddt_subcntnt_list_tmp.append([len(subcntnt), subcntnt])
    if  len(rmv_cnddt_subcntnt_list_tmp) == 0:
        rmv_subcntnt_rslt = rmv_edprtcl_rslt
        return rmv_subcntnt_rslt
    if  len(rmv_cnddt_subcntnt_list_tmp) == 1:
        tmp_subcntnt      = rmv_cnddt_subcntnt_list_tmp[0][1]
        rmv_subcntnt_rslt = re.sub(tmp_subcntnt, "", rmv_edprtcl_rslt)
        return rmv_subcntnt_rslt
    idx          = 0
    tmp_subcntnt = ""
    while len(rmv_cnddt_subcntnt_list_tmp) > (idx+1):
           if rmv_cnddt_subcntnt_list_tmp[idx+1][0] > rmv_cnddt_subcntnt_list_tmp[idx][0]:
              tmp_subcntnt = rmv_cnddt_subcntnt_list_tmp[idx+1][1]
              idx = idx + 1
           else:
              continue
    rmv_subcntnt_rslt = re.sub(tmp_subcntnt, "", rmv_edprtcl_rslt)
    return rmv_subcntnt_rslt
