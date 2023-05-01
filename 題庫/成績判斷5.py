a=int(input())
if  a>=60:
    print("pass")
    b=input()
    if b=="y":
        a=int(input())
else:
    print("fail")
    b=input()
    if b=="y":
        a=int(input())

while b=="y":
    if  a>=60:
        print("pass")
        b=input()
        if b=="y":
            a=int(input())
    else:
        print("fail")
        b=input()
        if b=="y":
            a=int(input())
else:
    exit()





