# coding: utf-8




#LINEボットの性格や振舞いを決定づけるためのクラスを宣言・定義する
class BotCharacter:
      #ボットのマインド(＝心の状態)を表す変数
      mindstt = 0

      #ボットのミッション(＝使命の達成状態)を表す変数
      missnstt = 0

      #ボットのミッション実行への到達度を表す変数
      dgr_of_missnexctn = 0

      #コンストラクター
      def __init__(self):
          pass

      #ボットのマインドのセッター
      @classmethod
      def set_mind(cls, mindstt):
          cls.mindstt = mindstt

      #ボットのマインドのゲッター
      @classmethod
      def get_mind(cls):
          return cls.mindstt

      #ボットのマインドを指定された分だけ上昇させるメソッド
      @classmethod
      def add_mind(cls, amnt):
          cls.mindstt += amnt

      #ボットのマインドを指定された分だけ下降させるメソッド
      @classmethod
      def sub_mind(cls, amnt):
          cls.mindstt -= amnt


      @classmethod
      def set_misson_state(cls, missnstt):
          cls.missnstt = missnstt

      @classmethod
      def get_misson_state(cls):
          return cls.missnstt


      @classmethod
      def add_misson_state(cls, amnt):
          cls.missnstt += amnt


      @classmethod
      def sub_misson_state(cls, amnt):
          cls.missnstt -= amnt

      @classmethod
      def set_degree_of_mission_execution(cls, dgr_of_missnexctn):
          cls.dgr_of_missnexctn = dgr_of_missnexctn


      @classmethod
      def get_degree_of_mission_execution(cls):
          return cls.dgr_of_missnexctn

      @classmethod
      def add_degree_of_mission_execution(cls, amnt):
          cls.dgr_of_missnexctn += amnt


      @classmethod
      def sub_degree_of_mission_execution(cls, amnt):
          cls.dgr_of_missnexctn -= amnt

      #ボットのマインドを計算するメソッド
      @classmethod
      def calc_mind(cls, flw_of_uttrnc, cntnt):
          if flw_of_uttrnc == "<挨拶>":
             if cls.get_degree_of_mission_execution() < 100:
                cls.add_degree_of_mission_execution(50)
                return "<挨拶>"
             if cls.get_degree_of_mission_execution() >= 100:
                cls.set_degree_of_mission_execution(0)
                cls.add_misson_state(100)
                return "<聞出し>"
          if (flw_of_uttrnc == "<依頼＆要求>" and "相談" in cntnt):
              cls.set_degree_of_mission_execution(0)
              cls.set_misson_state(0)
              return "<助言>"