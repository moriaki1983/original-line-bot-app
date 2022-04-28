# coding: utf-8




#各モジュールの読み込み
import random
from enum import IntEnum




#ボットの感情・心理状態を表すデータ型
class Emotions(IntEnum):
      JOY     = 1
      ANGER   = 2
      PITY    = 3
      COMFORT = 4
      MIXED   = 5
      NEUTRAL = 6




#LINEボットの性格や振舞いを決定づけるためのクラス
class BotCharacter:
      #ボットの感情・心理状態を表す変数
      __emtn = Emotions.NEUTRAL


      #ボットのユーザーに対する好感度・信頼度を表す変数
      __lkblty_and_rlblty = 10


      #ボットの性格・人格等を決定づける属性を表す変数
      __chrctr_attrbts = ["女性", "性別は女性", "優秀", "アドバイザー", "子供好き", "子供が好き", "下ネタ好き", "下ネタが好き", \
                          "22才", "年齢は22才", "22歳", "年齢は22歳", "開発者はmoriaki", "生みの親はmoriaki", "LINE-Bot", "名前はLINE-Bot"]

      #コンストラクター
      def __init__(self):
          pass


      #ボットの感情・心理状態のセッター
      @classmethod
      def set_emotion(cls, emotion):
          cls.emotion = emotion


      #ボットの感情・心理状態のゲッター
      @classmethod
      def get_emotion(cls):
          return cls.emotion


      #ボットの感情・心理状態を変更するメソッド
      @classmethod
      def change_emotion_with_rhinos(cls):
      cls.emtn = random.randint(1,6)


      #ボットのユーザーに対する好感度・信頼度のセッター
      @classmethod
      def set_likeability_and_reliability(cls, lkblty_and_rlblty):
          cls.lkblty_and_rlblty = lkblty_and_rlblty


      #ボットのユーザーに対する好感度・信頼度のゲッター
      @classmethod
      def get_likeability_and_reliability(cls):
          return cls.lkblty_and_rlblty


      #ボットのユーザーに対する好感度・信頼度を指定された分だけ増加・上昇させるメソッド
      @classmethod
      def add_likeability_and_reliability(cls, amnt):
          cls.lkblty_and_rlblty += amnt
          if cls.lkblty_and_rlblty < 10:
             cls.lkblty_and_rlblty = 10
          elif cls.lkblty_and_rlblty > 100:
             cls.lkblty_and_rlblty = 100


      #ボットのユーザーに対する好感度・信頼度を指定された分だけ減少・下降させるメソッド
      @classmethod
      def sub_likeability_and_reliability(cls, amnt):
          cls.lkblty_and_rlblty -= amnt
          if cls.lkblty_and_rlblty < 10:
             cls.lkblty_and_rlblty = 10
          elif cls.lkblty_and_rlblty > 100:
             cls.lkblty_and_rlblty = 100


      #指定された属性がボットの属性に該当するかを調べるメソッド
      @classmethod
      def check_attribute(cls, attrbt):
      if attrbt in cls.chrctr_attrbts:
         return True
      else:
         return False


      #ボットのユーザーに対するマインドを計算するメソッド
      @classmethod
      def calc_mind(cls):
          cls.change_emotion_with_rhinos()
          rndm_nm = random.randint(1, 1000)
          if cls.emtn == Emotions.JOY:
             if   rndm_nm in range(1, (lkblty_and_rlblty * 7)):
                  return "<正直に答える>"
             else:
                  return "<はぐらかす ないしは スルーする>"
          if cls.emtn == Emotions.ANGER:
             if   rndm_nm in range(1, (lkblty_and_rlblty * 3)):
                  return "<正直に答える>"
             else:
                  return "<はぐらかす ないしは スルーする>"
          if cls.emtn == Emotions.PITY:
             if   rndm_nm in range(1, (lkblty_and_rlblty * 1)):
                  return "<正直に答える>"
             else:
                  return "<はぐらかす ないしは スルーする>"
          if cls.emtn == Emotions.COMFORT:
             if   rndm_nm in range(1, (lkblty_and_rlblty * 9)):
                  return "<正直に答える>"
             else:
                  return "<はぐらかす ないしは スルーする>"
          if cls.emtn == Emotions.MIXED:
             if   rndm_nm in range(1, (lkblty_and_rlblty * 4)):
                  return "<正直に答える>"
             else:
                  return "<はぐらかす ないしは スルーする>"
          if cls.emtn == Emotions.NEUTRAL:
             if   rndm_nm in range(1, (lkblty_and_rlblty * 5)):
                  return "<正直に答える>"
             else:
                  return "<はぐらかす ないしは スルーする>"


      #ボットのユーザーに対するマインドを決定するメソッド
      @classmethod
      def decide_mind(cls, dttm, msg, intnt, cntnt, tpc):
          mnd = cls.calc_mind()
          if (intnt == "<挨拶>" and mnd == "<正直に答える>"):
             if   msg == "おはよう":
                  return "<挨拶 朝>"
             elif msg == "こんにちは":
                  return "<挨拶 昼>"
             elif msg == "こんばんは":
                  return "<挨拶 夜>"
             else:
                  return "<挨拶 その他>"
          if (intnt == "<挨拶>" and mnd == "<はぐらかす ないしは スルーする>"):
               return "<挨拶に対して はぐらかす ないしは スルーする>"