# coding: utf-8




#各モジュールの読み込み
from enum import Enum




#ボットの感情・心理状態を表すデータ型
class Emotions(Enum):
      JOY     = 1
      ANGER   = 2
      PITY    = 3
      COMFORT = 4
      NEUTRAL = 5




#LINEボットの性格や振舞いを決定づけるためのクラス
class BotCharacter:
      #ボットの感情・心理状態を表す変数
      __emtn = Emotions.NEUTRAL

      #ボットのユーザーに対する好感度・信頼度を表す変数
      __lkablty_and_rlblty = 0

      #ボットの性格・人格等を決定づける属性を表す変数
      __chrctr_attrbts = ["女性", "優秀", "アドバイザー", "子供好き", "子供が好き", "下ネタ好き", "下ネタが好き", \
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


      #ボットのユーザーに対する好感度・信頼度のセッター
      @classmethod
      def set_likeability_and_reliability(cls, lkablty_and_rlblty):
          cls.lkablty_and_rlblty = lkablty_and_rlblty

      #ボットのユーザーに対する好感度・信頼度のゲッター
      @classmethod
      def get_likeability_and_reliability(cls):
          return cls.lkablty_and_rlblty

      #ボットのユーザーに対する好感度・信頼度を指定された分だけ増加・上昇させるメソッド
      @classmethod
      def add_likeability_and_reliability(cls, amnt):
          cls.lkablty_and_rlblty += amnt

      #ボットのユーザーに対する好感度・信頼度を指定された分だけ減少・下降させるメソッド
      @classmethod
      def sub_likeability_and_reliability(cls, amnt):
          cls.lkablty_and_rlblty -= amnt

      #指定された属性がボットの属性に該当するかを調べるメソッド
      @classmethod
      def check_attribute(cls, attrbt):
      if attrbt in cls.chrctr_attrbts:
         return True
      else:
         return False

      #ボットのマインドを計算するメソッド
      @classmethod
      def calc_mind(cls, flw_of_cnvrstn, msg, cntnt, tpc):
          if flw_of_cnvrstn == "<挨拶>":
             if   msg == "おはよう":
                  return "<挨拶 朝>"
             elif msg == "こんにちは":
                  return "<挨拶 昼>"
             elif msg == "こんばんは":
                  return "<挨拶 夜>"
             else:
                  return "<挨拶 その他>"