first_home = list(map(int,input().split(" ")))
first_away = list(map(int,input().split(" ")))
second_home = list(map(int,input().split(" ")))
second_away = list(map(int,input().split(" ")))
h = 0
a = 0
print(sum(first_home),':',sum(first_away ),sep='')
print(sum(second_home ),':',sum(second_away),sep='')
if sum(first_home) > sum(first_away):
    h += 1
else:
    a += 1
if sum(second_home) > sum(second_away):
    h += 1
else:
    a += 1
if h > a:
    print("Win")
elif h == a:
    print("Tie")
else:
    print("Lose")