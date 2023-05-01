
def return2num(n=0):
    total=1
    for i in range(1,n+1):
        total*=i
    return total,(1+n)*n//2
num=int(input())
ans=return2num(num)
print(ans[0])
print(ans[1])