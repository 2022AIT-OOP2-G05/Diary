from diaries.DiarySample import DiarySample
from diaries.KotaDiary import KotaDiary
diaries = [
    DiarySample(), 
    KotaDiary(),
]

for d in diaries:
    print("--------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()