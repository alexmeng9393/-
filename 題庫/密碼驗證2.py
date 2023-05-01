cp=int(input())
yp=int(input())
times=0
while True:
    if cp<0 or cp>2000000000:
        exit(print("Wrong Password Setting!"))
    elif cp!=yp:
        yp=int(input())
        times=times+1
    elif cp==yp:
        i=0
        for i in range(0,times,1):
            print("Wrong Password!")
        print("Correct!")
        break