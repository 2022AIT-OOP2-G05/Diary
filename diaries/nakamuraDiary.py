from diaries.AbstractDiary import AbstractDiary

class nakamuraDiary(AbstractDiary):
    def get_date(self):
        return "2022-12-8"

    def get_summary(self):
        return "今日はオブジェクト指向プログラミングの授業を受けた。難しかったのでチームメンバーに迷惑をかけないように復習する。"

    def get_author(self):
        return "Nakamura"