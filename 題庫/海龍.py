from math import sqrt
ax,ay=map(float,input().split())
bx,by=map(float,input().split())
cx,cy=map(float,input().split())
aside=float(sqrt((bx-cx)**2+(by-cy)**2))
bside=float(sqrt((ax-cx)**2+(ay-cy)**2))
cside=float(sqrt((ax-bx)**2+(ay-by)**2))
s=float(aside+bside+cside)
area=(round,sqrt(s(s-aside)(s-bside)(s-cside)),2)
