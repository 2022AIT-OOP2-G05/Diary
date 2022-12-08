from diaries.DiarySample import DiarySample
from diaries.Shimadadiary import Shimadadiary
diaries = [
    DiarySample(), 
    Shimadadiary(),
    ]

for d in diaries:
    print("--------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()