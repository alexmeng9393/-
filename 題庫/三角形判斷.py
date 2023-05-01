a=int(input())
b=int(input())
c=int(input())
if a+b>c and b+c>a and a+c>b:
    print("True")
else:
    exit(print("False"))
if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2 :
    print("Right Triangle")
else:
    print("Non-Right Triangle")