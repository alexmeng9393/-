st=[]
n=input()
while n!="-1":
    st.append(n)
    n=input()
tst=['T00_'+s.capitalize() for s in st if s.endswith('.txt')]
print(tst)
pst=['P00_'+s.upper().rsplit('.',1)[0]+'.py' for s in st if s.endswith('.py')]
print(pst)