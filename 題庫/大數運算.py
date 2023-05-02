a=list(map(str,input().split(" ")))
if a[1] =="+":
    answer=int(a[0])+int(a[2])
elif a[1] =="-":
    answer=int(a[0])-int(a[2])
elif a[1] =="*":
    answer=int(a[0])*int(a[2])
elif a[1] =="/":
    answer=int(a[0])//int(a[2])
print(answer)