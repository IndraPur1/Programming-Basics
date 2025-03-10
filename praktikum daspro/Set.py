def Konso(e,L):
    if L == []:
        return [e]
    else:
        return [e] + L

def Konsi(L,e):
    if L == []:
        return [e]
    else:
        return L + [e] 

def FirstElmt(L):
    if L == [] :
        return None
    else:
        return L[0]

def LastElmt(L):
    if  L == []:
        return None
    else:
        return L[-1]

def Tail(L):
    if L == []:
        return []
    else:
        return L[1:]

def Head(L):
    if L == []:
        return []
    else:
        return L[:-1]

def IsEmpty(L):
    return L == []

def IsOneElmt(L):
    if L == []:
        return False
    else:
        return Head(L) == []    # Tail(L) == [] ini juga bisa

def IsEqual(L1,L2):
    if(IsEmpty(L1) and IsEmpty(L2)):
        return True 
    else:
        if(FirstElmt(L1) == FirstElmt(L2)):
            return IsEqual(Tail(L1),Tail(L2))
        else:
            return False

def NbElmt(L):
    if IsEmpty(L) :
        return 0
    else:
        return 1 + NbElmt(Tail(L))
    
def ElmtkeN(N,L):
    if N == 1:
        return FirstElmt(L)
    else:
        return ElmtkeN(N-1,Tail(L))
    
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L),Copy(Tail(L))) #L[|:|]

def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(LastElmt(L),Inverse(Head(L)))

def Konkat(L1,L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konkat(Konsi(L1,FirstElmt(L2)),Tail(L2))

def IsMember(X,L):
    if IsEmpty(L):
        return False
    elif X == FirstElmt(L):
        return True
    else:
        return IsMember(X,Tail(L))

#Set
def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L),Tail(L)):
            return False
        else:
            return IsSet(Tail(L))

print(IsSet([1,2,3]))