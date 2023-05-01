x = int(input())
for j in range(x, 0, -1):
    print(" " * (x - j) + "*" * j)