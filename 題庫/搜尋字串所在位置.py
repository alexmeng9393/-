a=input()
b=input()
pos=a.find(b)
while pos!=-1:
    print(pos)
    pos=a.find(b,pos+1)