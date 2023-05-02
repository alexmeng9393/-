while True:#建表
    try:
        x=int(input())
        a=2
        start=("")
    except:
        break
    for i in range(x-2):
        n=int(x%a)#餘數
        a=a+1
        if n==0:
            start=(start+"非質數")
        elif n!=0:
            start=(start+"質數")
    if "非" in start:
        print("非質數")
    else:
        print("質數")


