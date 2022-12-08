from diaries.DiarySample import DiarySample
from diaries.YamamotoDiary import YamamotoDiary

diaries = [DiarySample(), YamamotoDiary(),]

for d in diaries:
    print("--------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()