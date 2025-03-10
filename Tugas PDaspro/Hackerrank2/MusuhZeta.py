def FirstElmt(L : list):
    return L[0]

def IsEmpty(L):
    return L==[]

def LastElmt(L : list):
    return L[-1]

def JumlahElement(L : list):
    if L == []:
        return 0
    else:
        return 1 + JumlahElement(Tail(L))

def konso(e, L : list):
    if L == [] :
        return [e]
    else :
        return [e] + L

def IsOneElmt(L : list):
    return JumlahElement(L) == 1

def Head(S):
    return S[:-1]

def Tail(L : list):
    return L[1:]

def IsMember(e,L):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == e:
        return True
    else:
        return IsMember(e,Tail(L))

def Rember(x,L):
    if IsEmpty(L):
        return []
    else :
        if FirstElmt(L) == x :
            return Tail(L)
        else :
           return konso (FirstElmt(L),Rember(x,Tail(L)))

def max2(a,b):
    if a > b:
        return a
    else :
        return b
    
def MaxList(L):
    if IsOneElmt(L):
        return LastElmt(L)
    else :
        return max2(LastElmt(L),MaxList(Head(L)))

print(MaxList([1,2,3,4]))

def CleanList(L):
    if L == []:
        return L
    else :
        if IsMember(FirstElmt(L),Tail(L)):
            return CleanList(Tail(L))
        else :
           return konso(FirstElmt(L),CleanList(Tail(L)))
print(CleanList([999, 901, 900, 621, 620, 567, 330, 297, 900]))

def Musuh(L):
    if L == []:
        return []
    else:
        return CleanList(konso(MaxList(L),Musuh(Rember(MaxList(L),L))))
print(Musuh([999, 901, 900, 621, 620, 567, 330, 297, 900]))