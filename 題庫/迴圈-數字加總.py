a=input()
list1=list(a)
print(list1)
list1.replace(",","")
for i in list1:
    if int(i)%2==0:
        print(i)
