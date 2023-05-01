n=input()
intab="173540"
outtab="ITESAO"
trantab=str.maketrans(intab,outtab)
n1=n.translate(trantab)
print(n1)