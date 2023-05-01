from math import sqrt
score=float(input())
score_1=('%.2f' % score)
ad=sqrt(score)*10
ad1=('%.2f' % ad)
gap=int(round(ad-score,0))
print("Original:" , score_1)
print("Adjusted:" , ad1,end=''"(+")
print(gap,end=')')