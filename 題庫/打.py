a=int(input())
b=int(a//12)
c=a%12
if a%12 ==0:
    print(b,"dozen")
else:
    print(b,"dozen","and",c)