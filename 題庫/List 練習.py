st=[]
a=int(input())
while a!=-1:
    st.append(a)
    a=int(input())
st.sort()
print(st)
st.insert(3,10)
print(st)
a=st.count(10)
print(a)
st.sort()
st.reverse()
print(st)
