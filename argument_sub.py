from janome.tokenizer import Tokenizer




#ユーザーから送られるLINEメッセージをJanomeで形態素解析する(見出しのみをリストにして出力する)
def tokenize(line_msg_text):
    #メッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr = Tokenizer()
    tkns  = tknzr.tokenize(line_msg_text)

    #分解後のメッセージをリストに格納して呼出し元に引渡しをする
    tknz_rslt = []
    for tkn in tkns:
        tknz_rslt.append(tkn.surface)
    return tknz_rslt


#ユーザーから送られるLINEメッセージをJanomeで形態素解析する(見出しと品詞のセットをリストにして出力する)
def tokenize2(line_msg_text):
    #メッセージの内容を品詞や単語を単位として分解する(＝文節に分ける)
    tknzr = Tokenizer()
    tkns = tknzr.tokenize(line_msg_text)
    tknz_rslt = []

    #分解後のメッセージをリストに格納して呼出し元に引渡しをする
    for tkn in tkns:
        tknz_rslt.append([tkn.surface, tkn.part_of_speech])
    return (tknz_rslt)


#LINEメッセージが短文＆定型文だったとして、これからインテントを抽出する
def extract_intent_from_short_and_boilerplate(line_msg_text):
    #短文＆定型文からインテントを抽出して、これを呼出し元に引渡しをする
    intnt_rslt
    if   line_msg_text == line_msg_text == "おはよう" or line_msg_text == "こんにちは" or line_msg_text == "こんばんは" or line_msg_text == "やあ" or line_msg_text == "どうも":
         intnt_rslt = "挨拶"
    elif line_msg_text == "さすがですね" or line_msg_text == "さすが" or line_msg_text == "素晴らしい" or line_msg_text == "すばらしい":
         intnt_rslt = "称賛"
    elif line_msg_text == "最低" or line_msg_text == "バカ":
         intnt_rslt = "罵倒"
    elif line_msg_text == "天才ですか" or line_msg_text == "秀才ですか":
         intnt_rslt = "称賛(半疑問)"
    elif line_msg_text == "バカですか" or line_msg_text == "アホですか":
         intnt_rslt = "罵倒(半疑問)"
    elif line_msg_text == "何をしますか" or line_msg_text == "どうしますか":
         intnt_rslt = "確認(意図＆目的)(現在)"
    elif line_msg_text == "何をしていますか" or line_msg_text == "どうしていますか":
         intnt_rslt = "確認(意図＆目的)(現在進行)"
    elif line_msg_text == "何をしてきましたか" or line_msg_text == "どうしてきましたか":
         intnt_rslt = "確認(意図＆目的)(過去)"
    elif line_msg_text == "何をしていきたいですか" or line_msg_text == "どうしていきたいですか":
         intnt_rslt = "確認(意図＆目的)(未来)"
    elif line_msg_text == "おい" or line_msg_text == "ねぇ" or line_msg_text == "なぁ":
         intnt_rslt = "呼掛け"
    elif line_msg_text == "海":
         intnt_rslt = "掛合い"
    else:
         intnt_rslt = "その他・不明"
    return intnt_rslt


#janomeで解析した後のLINEメッセージの末尾部分からインテントを抽出する
def extract_intent_from_endnotes(tknz_rslt):
    #解析した後のメッセージの末尾部分からインテントを抽出して、これを呼出し元に引渡しをする
    intnt_rslt
    if tknz_rslt[-1] == "する":
         intnt_rslt = "表明(現在＆肯定)"
    elif tknz_rslt[-1] == "しない":
         intnt_rslt = "表明(現在＆否定)"
    elif tknz_rslt[-1] == "している" or tknz_rslt[-1] == "してる" or tknz_rslt[-1] == "しています" or tknz_rslt[-1] == "してます":
         intnt_rslt = "表明(現在進行＆肯定)"
    elif tknz_rslt[-1] == "していない" or tknz_rslt[-1] == "してない" or tknz_rslt[-1] == "していません" or tknz_rslt[-1] == "してません":
         intnt_rslt = "表明(現在進行＆否定)"
    elif tknz_rslt[-1] == "できている" or tknz_rslt[-1] == "できてる":
         intnt_rslt = "表明(現在進行＆可能＆肯定)"
    elif tknz_rslt[-1] == "できていない" or tknz_rslt[-1] == "できてない" or tknz_rslt[-1] == "できていません" or tknz_rslt[-1] == "できてません":
         intnt_rslt = "表明(現在進行＆可能＆否定)"
    elif tknz_rslt[-1] == "できました"or tknz_rslt[-1] == "できた":
         intnt_rslt = "表明(過去＆可能＝完了)"
    elif tknz_rslt[-1] == "できていません" or tknz_rslt[-1] == "できてません" or tknz_rslt[-1] == "できてない":
         intnt_rslt = "表明(過去＆不可能＝未完了)"
    elif tknz_rslt[-1] == "できます" or tknz_rslt[-1] == "できると思います" or tknz_rslt[-1] == "できると思う":
         intnt_rslt = "表明(現在＆可能)"
    elif tknz_rslt[-1] == "できません" or tknz_rslt[-1] == "できない":
         intnt_rslt = "表明(現在＆不可能)"
    elif tknz_rslt[-1] == "しよう" or tknz_rslt[-1] == "しようと思います" or tknz_rslt[-1] == "しようと思う":
         intnt_rslt = "表明(未来＆肯定)"
    elif tknz_rslt[-1] == "しない" or tknz_rslt[-1] == "しないと思う":
         intnt_rslt = "表明(未来＆否定)"
    elif tknz_rslt[-1] == "しました" or tknz_rslt[-1] == "した":
         intnt_rslt = "表明(過去＆肯定)"
    elif tknz_rslt[-1] == "していません" or tknz_rslt[-1] == "してません" or tknz_rslt[-1] == "してない":
         intnt_rslt = "表明(過去＆否定)"
    elif tknz_rslt[-1] == "です" or tknz_rslt[-1] == "でした":
         intnt_rslt = "紹介＆説明＆提示"
    elif tknz_rslt[-1] == "でしょうか" or tknz_rslt[-1] == "ですか":
         intnt_rslt = "疑義＆質問"
    elif tknz_rslt[-1] == "しませんか" or tknz_rslt[-1] == "しません":
         intnt_rslt = "誘導＆勧誘"
    elif tknz_rslt[-1] == "したいな" or tknz_rslt[-1] == "したい" or tknz_rslt[-1] == "やりたいな" or tknz_rslt[-1] == "やりたい:
         intnt_rslt = "欲求＆欲動"
    elif tknz_rslt[-1] == "いいですよ" or tknz_rslt[-1] == "いいよ":
         intnt_rslt = "許可＆認可" 
    elif tknz_rslt[-1] == "しないように" or tknz_rslt[-1] == "しないよう" or tknz_rslt[-1] == "するなよ" or tknz_rslt[-1] == "するな":
         intnt_rslt = "制止＆禁止"
    elif tknz_rslt[-1] == "してください" or tknz_rslt[-1] == "して":
         intnt_rslt = "依頼"
    elif tknz_rslt[-1] == "しなさい" or tknz_rslt[-1] == "しろ":
         intnt_rslt = "命令"
    else:
         intnt_rslt = "その他・不明"
    return intnt_rslt