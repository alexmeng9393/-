a=int(input())
#score=int(input())
if a!=1 and a!=2:
    exit(print("roll error"))
score=int(input())
if score<0 or score>100:
    print("score error")
elif a==1 :
    if score>=60:
        print("pass")
    else:
        print("fail")
elif a==2 :
    if score>=70:
        print("pass")
    else:
        print("fail")