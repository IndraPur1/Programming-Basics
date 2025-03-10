def konso(e, L : list):
    if L == [] :
        return [e]
    else :
        return [e] + L

def FirstElmt(L : list):
    return L[0]

def Tail(L : list):
    return L[1:]

def IsMember(e,L : list):
    if L == []:
        return False
    elif FirstElmt(L) == e:
        return True
    else :
        return IsMember(e,Tail(L))

def Jumlah(L):
    if L == "" :
        return 0
    elif IsMember(FirstElmt(L), list("1234567890")):
        return int(FirstElmt(L)) + Jumlah(Tail(L))
    else:
        return Jumlah(Tail(L))
 
print(Jumlah('Inv35t4s1'))
