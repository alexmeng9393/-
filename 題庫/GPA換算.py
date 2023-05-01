n=int(input())
if n>=90 and n<=100:
    print("4.3")
    print("A+")
elif n>=85 and n<=89:
    print("4.0")
    print("A")
elif n>=80 and n<=84:
    print("3.7")
    print("A-")
elif n>=77 and n<=79:
    print("3.3")
    print("B+")
elif n>=70 and n<=72:
    print("3.0")
    print("B")
elif n>=67 and n<=69:
    print("2.3")
    print("C+")
elif n>=63 and n<=66:
    print("2.0")
    print("C")
elif n>=60 and n<=62:
    print("1.7")
    print("C-")
else:
    print("0")
    print("F")