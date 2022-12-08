from diaries.DiarySample import DiarySample
from diaries.KurahashiDiary import KurahashiDiary
from diaries.YamamotoDiary import YamamotoDiary
from diaries.SakaiDiary import SakaiDiary 

diaries = [
  DiarySample(),
  YamamotoDiary(),
  KurahashiDiary(),
  SakaiDiary(),
  ]

for d in diaries:
    print("--------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()