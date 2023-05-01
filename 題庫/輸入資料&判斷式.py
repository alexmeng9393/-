n=input()
while n!="q":
    if n.isdecimal()==True:
        a=int(n)*int(n)
        n=input()
    elif n.isdecimal()==False:
        b=float(n)*float(n)
        n=input()
print(a)
print(b)
if a==b:
    print("Float = Int")
elif a>b:
    print("Float > Int")
elif a<b:
    print("Float < Int")