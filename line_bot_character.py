# coding: utf-8




#LINEボットの性格や振舞いを決定づけるためのクラスを宣言・定義する
class BotCharacter:
      #ボットのマインド(＝心の状態)を表す変数
      __mindstt = 0

      #ボットのミッション(＝使命の達成状態)を表す変数
      __missnstt = 0

      #ボットのミッション実行への到達度を表す変数
      __dgr_of_missnexctn = 0

      #コンストラクター
      def __init__(self):
          pass

      #ボットのマインドのセッター
      @classmethod
      def __set_mind(self, mindstt):
          self.mindstt = mindstt

      #ボットのマインドのゲッター
      @classmethod
      def __get_mind(self):
          return self.mindstt

      #ボットのマインドを指定された分だけ上昇させるメソッド
      @classmethod
      def __add_mind(self, amnt):
          self.mindstt += amnt

      #ボットのマインドを指定された分だけ下降させるメソッド
      @classmethod
      def __sub_mind(self, amnt):
          self.mindstt -= amnt

      #ボットのマインドを計算するメソッド
      @classmethod
      def calc_mind(self, flw_of_uttrnc):
          if flw_of_uttrnc == "<挨拶>":
             if (missnstt == 0 and dgr_of_missnexctn < 100):
                dgr_of_missnexctn += 50
                return "<挨拶>"
             if (missnstt < 100 and dgr_of_missnexctn >= 100):
                dgr_of_missnexctn = 0
                missnstt = 100
                return "<聞出し>"
             if missnstt >= 100:
                dgr_of_missnexctn = 0
                missnstt = 0
                return "<助言>"