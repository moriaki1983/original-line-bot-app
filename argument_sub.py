import re
from janome.tokenizer import Tokenizer




#ユーザーから送られるLINEメッセージが指定された文字列で開始するかを判定する
def check_text_start_string(line_msg_txt, str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で開始するかを判定する
    is_strt
    if str in line_msg_txt:
       is_strt = line_msg_txt.startswith(str)
    else:
       is_strt = False
    return is_strt


#ユーザーから送られるLINEメッセージが指定された文字列で終結するかを判定する
def check_text_terminated_string(line_msg_txt, str):
    #メッセージの中に指定された文字列が含まれている場合に、メッセージがこの文字列で終結するかを判定する
    is_trmntd
    if str in line_msg_txt:
       is_trmntd = line_msg_txt.endswith(str)
    else:
       is_trmntd = False
    return is_trmntd


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


#LINEメッセージが短文＆定型文だったとして、これからインテント(＝意図するもの)を抽出する
def extract_intent_from_short_and_boilerplate(line_msg_text):
    #短文＆定型文からインテントを抽出して、これを呼出し元に引渡しをする
    intnt_rslt
    if   line_msg_text == "おはよう" or
         line_msg_text == "こんにちは" or
         line_msg_text == "こんばんは" or
         line_msg_text == "やあ" or
         line_msg_text == "どうも":
         intnt_rslt = "挨拶"
    elif line_msg_text == "さすがですね" or
         line_msg_text == "さすが" or
         line_msg_text == "素晴らしい" or
         line_msg_text == "すばらしい":
         intnt_rslt = "称賛"
    elif line_msg_text == "最低" or
         line_msg_text == "バカ":
         intnt_rslt = "罵倒"
    elif line_msg_text == "天才ですか" or
         line_msg_text == "秀才ですか":
         intnt_rslt = "称賛(半疑問)"
    elif line_msg_text == "バカですか" or
         line_msg_text == "アホですか":
         intnt_rslt = "罵倒(半疑問)"
    elif line_msg_text == "何をしますか" or
         line_msg_text == "どうしますか":
         intnt_rslt = "確認(意図＆目的)(現在)"
    elif line_msg_text == "何をしていますか" or
         line_msg_text == "どうしていますか":
         intnt_rslt = "確認(意図＆目的)(現在進行)"
    elif line_msg_text == "何をしてきましたか" or
         line_msg_text == "どうしてきましたか":
         intnt_rslt = "確認(意図＆目的)(過去)"
    elif line_msg_text == "何をしていきたいですか" or
         line_msg_text == "どうしていきたいですか":
         intnt_rslt = "確認(意図＆目的)(未来)"
    elif line_msg_txt == "いいですよ" or
         line_msg_txt == "いいよ":
         intnt_rslt = "許可"
    elif line_msg_text == "おい" or
         line_msg_text == "ねぇ" or
         line_msg_text == "なぁ":
         intnt_rslt = "呼掛け"
    elif line_msg_text == "海":
         intnt_rslt = "掛合い"
    else:
         intnt_rslt = "その他・不明"
    return intnt_rslt


#LINEメッセージの末尾部分からインテント(＝意図するもの)を抽出する
def extract_intent_from_endnotes(tknz_rslt):
    #メッセージの末尾部分からインテントを抽出して、これを呼出し元に引渡しをする
    intnt_rslt
    if   check_text_terminated_string(line_msg_txt, "する"):
           intnt_rslt = "表明(現在＆肯定)"
    elif check_text_terminated_string"しない":
           intnt_rslt = "表明(現在＆否定)"
    elif check_text_terminated_string(line_msg_txt, "している"):
           intnt_rslt = "表明(現在進行＆肯定)"
    elif check_text_terminated_string(line_msg_txt, "してる"):
           intnt_rslt = "表明(現在進行＆肯定)"
    elif check_text_terminated_string(line_msg_txt, "しています"):
           intnt_rslt = "表明(現在進行＆肯定)"
    elif check_text_terminated_string(line_msg_txt, "してます"):
           intnt_rslt = "表明(現在進行＆肯定)"
    elif check_text_terminated_string(line_msg_txt, "していない") or
         check_text_terminated_string(line_msg_txt, "してない") or
         check_text_terminated_string(line_msg_txt, "していません") or
         check_text_terminated_string(line_msg_txt, "してません":
           intnt_rslt = "表明(現在進行＆否定)"
    elif check_text_terminated_string(line_msg_txt, "できている") or
         check_text_terminated_string(line_msg_txt, "できてる"):
           intnt_rslt = "表明(現在進行＆可能＆肯定)"
    elif check_text_terminated_string(line_msg_txt, "できていない") or
         check_text_terminated_string(line_msg_txt, "できてない") or
         check_text_terminated_string(line_msg_txt, "できていません") or
         check_text_terminated_string(line_msg_txt, "できてません":
           intnt_rslt = "表明(現在進行＆可能＆否定)"
    elif check_text_terminated_string(line_msg_txt, "できました") or
         check_text_terminated_string(line_msg_txt, "できた":
           intnt_rslt = "表明(過去＆可能＝完了)"
    elif check_text_terminated_string(line_msg_txt, "できていません") or
         check_text_terminated_string(line_msg_txt, "できてません") or
         check_text_terminated_string(line_msg_txt, "できてない":
           intnt_rslt = "表明(過去＆不可能＝未完了)"
    elif check_text_terminated_string(line_msg_txt, "できます") or
         check_text_terminated_string(line_msg_txt, "できると思います") or
         check_text_terminated_string(line_msg_txt, "できると思う":
           intnt_rslt = "表明(現在＆可能)"
    elif check_text_terminated_string(line_msg_txt, "できません") or
         check_text_terminated_string(line_msg_txt, "できない":
           intnt_rslt = "表明(現在＆不可能)"
    elif check_text_terminated_string(line_msg_txt, "しよう") or
         check_text_terminated_string(line_msg_txt, "しようと思います") or
         check_text_terminated_string(line_msg_txt, "しようと思う":
           intnt_rslt = "表明(未来＆肯定)"
    elif check_text_terminated_string(line_msg_txt, "しない") or
         check_text_terminated_string(line_msg_txt, "しないと思う":
           intnt_rslt = "表明(未来＆否定)"
    elif check_text_terminated_string(line_msg_txt, "しました") or
         check_text_terminated_string(line_msg_txt, "した":
           intnt_rslt = "表明(過去＆肯定)"
    elif check_text_terminated_string(line_msg_txt, "していません") or
         check_text_terminated_string(line_msg_txt, "してません") or
         check_text_terminated_string(line_msg_txt, "してない":
           intnt_rslt = "表明(過去＆否定)"
    elif check_text_terminated_string(line_msg_txt, "です") or
         check_text_terminated_string(line_msg_txt, "でした":
           intnt_rslt = "紹介＆説明＆提示"
    elif check_text_terminated_string(line_msg_txt, "でしょうか") or
         check_text_terminated_string(line_msg_txt, "ですか":
           intnt_rslt = "疑義＆質問"
    elif check_text_terminated_string(line_msg_txt, "しませんか") or
         check_text_terminated_string(line_msg_txt, "しません":
           intnt_rslt = "誘導＆勧誘"
    elif check_text_terminated_string(line_msg_txt, "したいな") or
         check_text_terminated_string(line_msg_txt, "したい") or
         check_text_terminated_string(line_msg_txt, "やりたいな") or
         check_text_terminated_string(line_msg_txt, "やりたい:
           intnt_rslt = "欲求＆欲動"
    elif check_text_terminated_string(line_msg_txt, "いいですよ") or
         check_text_terminated_string(line_msg_txt, "いいよ":
           intnt_rslt = "許可＆認可" 
    elif check_text_terminated_string(line_msg_txt, "しないように") or
         check_text_terminated_string(line_msg_txt, "しないよう") or
         check_text_terminated_string(line_msg_txt, "するなよ") or
         check_text_terminated_string(line_msg_txt, "するな":
           intnt_rslt = "制止＆禁止"
    elif check_text_terminated_string(line_msg_txt, "してください") or
         check_text_terminated_string(line_msg_txt, "して":
           intnt_rslt = "依頼"
    elif check_text_terminated_string(line_msg_txt, "しなさい") or
         check_text_terminated_string(line_msg_txt, "しろ":
           intnt_rslt = "命令"
    else:
           intnt_rslt = "その他・不明"
    return intnt_rslt


#LINEメッセージの先頭・中間部分からコンテント(＝意図されるもの)を抽出する
def extract_content_from_top_and_middle(line_msg_text):
    #メッセージの先頭・中間部分部分からコンテントを抽出して、これを呼出し元に引渡しをする
    cntnt_rslt
    if   check_text_terminated_string(line_msg_txt, "する"):
           cntnt_rslt = re.sub(r"する", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しない"):
           cntnt_rslt = re.sub(r"しない", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "している"):
           cntnt_rslt = re.sub(r"している", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "してる"):
           cntnt_rslt = re.sub(r"してる", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しています"):
           cntnt_rslt = re.sub(r"しています", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "してます"):
           cntnt_rslt = re.sub(r"してます", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "していない"):
           cntnt_rslt = re.sub(r"していない", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "してない"):
           cntnt_rslt = re.sub(r"してない", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "していません"):
           cntnt_rslt = re.sub(r"していません", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "してません"):
           cntnt_rslt = re.sub(r"してません", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できている"):
           cntnt_rslt = re.sub(r"できている", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できてる"):
           cntnt_rslt = re.sub(r"できてる", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できていない"):
           cntnt_rslt = re.sub(r"できていない", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できてない"):
           cntnt_rslt = re.sub(r"できてない", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できていません"):
           cntnt_rslt = re.sub(r"できていません", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できてません"):
           cntnt_rslt = re.sub(r"できてません", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できました"):
           cntnt_rslt = re.sub(r"できました", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できた":
           cntnt_rslt = re.sub(r"できた", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できていません"):
           cntnt_rslt = re.sub(r"できていません", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できてません"):
           cntnt_rslt = re.sub(r"してます", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できてない"):
           cntnt_rslt = re.sub(r"できてない", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できます"):
           cntnt_rslt = re.sub(r"できます", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できると思います"):
           cntnt_rslt = re.sub(r"できると思います", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できると思う"):
           cntnt_rslt = re.sub(r"できると思う", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できません"):
           cntnt_rslt = re.sub(r"できません", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "できない"):
           cntnt_rslt = re.sub(r"できない", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しよう"):
           cntnt_rslt = re.sub(r"しよう", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しようと思います"):
           cntnt_rslt = re.sub(r"しようと思います", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しようと思う"):
           cntnt_rslt = re.sub(r"しようと思う", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しない"):
           cntnt_rslt = re.sub(r"しない", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しないと思う"):
           cntnt_rslt = re.sub(r"しないと思う", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しました"):
           cntnt_rslt = re.sub(r"しました", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "した"):
           cntnt_rslt = re.sub(r"した", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "していません"):
           cntnt_rslt = re.sub(r"していません", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "してません"):
           cntnt_rslt = re.sub(r"してません", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "してない"):
           cntnt_rslt = re.sub(r"してない", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "です"):
           cntnt_rslt = re.sub(r"です", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "でした"):
           cntnt_rslt = re.sub(r"でした", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "でしょうか"):
           cntnt_rslt = re.sub(r"でしょうか", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "ですか"):
           cntnt_rslt = re.sub(r"ですか", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しませんか"):
           cntnt_rslt = re.sub(r"しませんか", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しません"):
           cntnt_rslt = re.sub(r"しません", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "したいな"):
           cntnt_rslt = re.sub(r"したいな", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "したい"):
           cntnt_rslt = re.sub(r"したい", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "やりたいな"):
           cntnt_rslt = re.sub(r"やりたいな", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "やりたい):
           cntnt_rslt = re.sub(r"やりたい", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しないように"):
           cntnt_rslt = re.sub(r"しないように", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しないよう"):
           cntnt_rslt = re.sub(r"しないよう", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "するなよ"):
           cntnt_rslt = re.sub(r"するなよ", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "するな"):
           cntnt_rslt = re.sub(r"するな", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "してください"):
          cntnt_rslt = re.sub(r"してください", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "して"):
           cntnt_rslt = re.sub(r"して", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しなさい"):
           cntnt_rslt = re.sub(r"しなさい", "", line_msg_txt)
    elif check_text_terminated_string(line_msg_txt, "しろ"):
           cntnt_rslt = re.sub(r"しろ", "", line_msg_txt)
    else:
           cntnt_rslt = ""
    return cntnt_rslt