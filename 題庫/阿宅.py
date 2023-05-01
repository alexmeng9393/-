l,s=map(int,input().split())
times=0
while True:
    if s>l:
        if s<2:
            times=times+0
        else:
            s=s-2
            times=times+1
    elif s<l:
        s=s+5
        times=times+1
    else:
        break
print(times)

