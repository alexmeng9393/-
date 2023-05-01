def sum1(n):
    total=0
    for i in range(1,n+1):
        total=total+i
    return total
num=int(input())
ans=sum1(num)
print(ans)