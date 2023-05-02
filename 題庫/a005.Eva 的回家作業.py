x=int(input())
while True:
    try:
        for i in range(x):
            a,b,c,d=map(int,input().split())
            if (b-a)==(c-b):
                e=d+(c-b)
                print(a,b,c,d,e)
            else:
                n=d/c
                e=int(d*n)
                print(a,b,c,d,e)
    except:
        break
