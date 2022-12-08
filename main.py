from diaries.DiarySample import DiarySample
from diaries.KurahashiDiary import KurahashiDiary
from diaries.YamamotoDiary import YamamotoDiary

diaries = [DiarySample(),
          YamamotoDiary(),
           KurahashiDiary() ]

for d in diaries:
    print("--------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()