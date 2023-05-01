n=int(input())
if n>12:
    print("Month doesn't exist!")
elif n<=5 and n>=3:
    print("Spring")
elif n<=8 and n>=6:
    print("Summer")
elif n<=11 and n>=9:
    print("Autumn")
else:
    print("Winter")

