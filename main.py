from diaries.DiarySample import DiarySample
from diaries.KurahashiDiary import KurahashiDiary

diaries = [DiarySample(),
           KurahashiDiary() ]

for d in diaries:
    print("--------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()