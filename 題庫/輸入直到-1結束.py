sum1=0
ct=0

MaxVal=0
MaxPos=0
n=int(input())
while n!=-1:
    sum1+=n
    ct+=1
    if n>MaxVal:
        MaxVal=n
        MaxPos=ct
    n=int(input())
else:
    print(sum1)
    print(sum1/ct)
    print(MaxVal)
    print(MaxPos)
