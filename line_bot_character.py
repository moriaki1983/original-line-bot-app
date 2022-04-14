# coding: utf-8




#LINEボットの性格や振舞いを決定づけるためのクラスを宣言・定義する
class BotCharacter:
      #ボットのマインド(＝心の状態)を表す変数を宣言する
      mind_state = 0

      #コンストラクター
      def __init__(self):
          pass

      #ボットのマインドのセッター
      @classmethod
      def set_mind(self, mind_state):
          self.mind_state = mind_state

      #ボットのマインドのゲッター
      @classmethod
      def get_mind(self):
          return self.mind_state

      #ボットのマインドを指定された分だけ上昇させるメソッド
      @classmethod
      def add_mind(self, amnt):
          self.mind_state += amnt

      #ボットのマインドを指定された分だけ下降させるメソッド
      @classmethod
      def sub_mind(self, amnt):
          self.mind_state -= amnt

      #ボットのマインドを計算するメソッド
      @classmethod
      def calc_mind(self, flw_of_uttrnc):
          if flw_of_uttrnc == "<称賛＆礼賛>":
             return "<謝意＆感謝>"
