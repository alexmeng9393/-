a=int(input())
b=a//100000%10
c=a//10000%10
d=a//1000%10
e=a//100%10
f=a//10%10
g=a//1%10
if a%7==0 or b==7 or c==7 or d==7 or e==7 or f==7 or g==7:
    print("YES")
else:
    print("NO")