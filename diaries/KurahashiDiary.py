from diaries.AbstractDiary import AbstractDiary

class KurahashiDiary(AbstractDiary):

    def get_date(self):
        return "2122-12-08"

    def get_summary(self):
        return "眠たい"

    def get_author(self):
        return "Kurahashi"