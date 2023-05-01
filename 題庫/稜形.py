y=int(input())
x=int(y/2)
for i in range(0,y-x,1):
    print((" "*((y-x) - (i+1))) + ('*' * ((2 * i)+1) ))
for i in range(y-x-2,-1,-1):
    print((" "*((y-x) - (i+1))) + ('*' * ((2 * i)+1) ))

