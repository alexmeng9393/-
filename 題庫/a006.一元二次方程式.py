a,b,c=map(int,input().split())
dis=b**2-4*a*c#判斷式
if dis==0:
    x=(-b+((b**2-4*a*c)**0.5))/(2*a)
    print("Two same roots x=",int(x),sep='')#sep中間以"空白"隔開
elif dis<0:
    print("No real root")
else:
    x=(-b+(b**2-4*a*c)**0.5)/(2*a)
    y=(-b-(b**2-4*a*c)**0.5)/(2*a)
    if x>y:
        print("Two different roots x1=",int(x)," , ","x2=",int(y),sep='')
    else:
        print("Two different roots x1=",int(y)," , ","x2=",int(x),sep='')
