from diaries.AbstractDiary import AbstractDiary

class YamamotoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-08"

    def get_summary(self):
        return "今日は朝起きれなくて、焦っちゃった"

    def get_author(self):
        return "Yamamoto"