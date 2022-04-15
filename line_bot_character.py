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

      @classmethod
      def __set_degree_of_mission_execution(self, dgr_of_missnexctn):
          self.dgr_of_missnexctn = dgr_of_missnexctn

      @classmethod
      def __get_degree_of_mission_execution(self):
          return self.dgr_of_missnexctn

      @classmethod
      def __add_degree_of_mission_execution(self, amnt):
          self.dgr_of_missnexctn += amnt

      @classmethod
      def __sub_degree_of_mission_execution(self, amnt):
          self.dgr_of_missnexctn -= amnt

      #ボットのマインドを計算するメソッド
      @classmethod
      def calc_mind(self, flw_of_uttrnc):
          if flw_of_uttrnc == "<挨拶>":
             if __get_degree_of_mission_execution() < 100:
                __add_degree_of_mission_execution(self, 50)
                return "<挨拶>"
             if __get_degree_of_mission_execution() >= 100:
                __set_degree_of_mission_execution(0)
                return "<聞出し>"