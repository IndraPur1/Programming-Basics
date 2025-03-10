def MakePoint(x,y):
    return[x,y]

def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

import math
from math import sqrt
def Gradien(P1,P2):
    return ((ordinat(P2)-ordinat(P1))/(absis(P2)-absis(P1)))

def jarak0(P) :
    return math.sqrt((absis(P)-0)**2 + (ordinat(P)-0)**2)

def Jarak02(a,b) :
    if a < b :
        return a
    elif a == b :
        return "Sama"
    else :
        return b

P1 = MakePoint(3,2)
P2 = MakePoint(6,8)
P3 = MakePoint(6,2)
P4 = MakePoint(8,3)
#Aplikasi
print(Gradien(P1,P2))
print(Jarak02(P1,P2))
print(Gradien(P3,P4))
print(Jarak02(P1,P1))

from math import sqrt
def MakePoint(x,y):
    return[x,y]

def MakeGaris(p1,p2):
    return(p1,p2)

def Gradien(X):
    point1,point2 = X
    x1, y1 = point1
    x2, y2 = point2
    gradient =  (y2-y1)/(x2-x1)
    return gradient

def Jarak02(X):
    point1,point2 = X
    x1,y1 = point1
    x2,y2 = point2
    jarak1 = sqrt((x1**2)+(y1**2))
    jarak2 = sqrt((x2**2)+(y2**2))
    if jarak1 < jarak2 :
        return point1
    elif jarak1 == jarak2 :
        return "Sama"
    else :
        return point2
    
#Aplikasi
import sys
exec(''.join(sys.stdin.readlines()))
