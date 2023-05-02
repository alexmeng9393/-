while True:
    try:
        x=int(input())#
    except:
        break
    if (x%4==0 and x%100!=0) or x%400==0: #!=為不等於
        print("閏年")
    else:
        print("平年")
