
k="P","M","H"
v="Pikachu","Mickey Mouse","Hello kitty"
dc=dict(zip(k,v))





while True:
    qkey=input()
    if qkey=="-1":
        break
    if qkey in dc:
        print(dc[qkey])
    else:
        print( qkey,"does not exist. Enter a new one:")
        dc[qkey]=input()