list1=['甲','乙','丙','丁','戊','已','庚','辛','壬','癸']
list2=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
list3=['鼠','牛','虎','兔','龍','蛇','馬','羊','猴','雞','狗','豬']
n=int(input())
a=(n-3)%10
b=(n-3)%12
c=(n-3)%12
print((list1[(a-1)]),(list2[(b-1)]),sep="")
print(list3[(c-1)])