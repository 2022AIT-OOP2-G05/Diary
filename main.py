from diaries.DiarySample import DiarySample
from diaries.KotaDiary import KotaDiary
from diaries.KurahashiDiary import KurahashiDiary
from diaries.YamamotoDiary import YamamotoDiary
from diaries.SakaiDiary import SakaiDiary 
from diaries.Shimadadiary import Shimadadiary
from diaries.nakamuraDiary import nakamuraDiary

diaries = [
  DiarySample(),
  YamamotoDiary(),
  KurahashiDiary(),
  SakaiDiary(),
  KotaDiary(),
  Shimadadiary(),
  nakamuraDiary(),
  ]
  
for d in diaries:
    print("--------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()