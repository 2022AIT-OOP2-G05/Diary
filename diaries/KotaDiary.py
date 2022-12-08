from diaries.AbstractDiary import AbstractDiary

class KotaDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "眠たい１日だった。早く寝たい。"

    def get_author(self):
        return "こーた"