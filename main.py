from diaries.DiarySample import DiarySample
from diaries.nakamuraDiary import nakamuraDiary

diaries = [
    DiarySample(),
    nakamuraDiary(),
    ]

for d in diaries:
    print("--------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()