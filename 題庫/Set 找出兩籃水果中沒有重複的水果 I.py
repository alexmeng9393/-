itemsA = {"蘋果","香蕉","鳳梨","芭樂"}
itemsB = {"鳳梨","蘋果","水梨","蓮霧"}
a=itemsA.difference(itemsB)
b=itemsB.difference(itemsA)
list1=list(a)+list(b)
list1.sort()
print(list1)