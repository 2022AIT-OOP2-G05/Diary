from diaries.AbstractDiary import AbstractDiary

class SakaiDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-15"

    def get_summary(self):
        return "課題をなんとか出し終えた"

    def get_author(self):
        return "さかい"