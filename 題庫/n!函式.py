def fact(n):
    total=1
    for i in range(1,n+1):
        total=total*i
    return total
num=int(input())
ans=fact(num)
print(ans)