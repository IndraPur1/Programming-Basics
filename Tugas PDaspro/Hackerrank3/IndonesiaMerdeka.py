#LOL
def IsEmpty(S):
    return S == []
def FirstList(S):
    if S == [] :
        return None
    else:
        return S[0]
def TailList(S):
    if S == [] :
        return None
    else:
        return S[1:]

#List
def LastElmt(L):
    if  L == []:
        return None
    else:
        return L[-1]
def Head(L):
    if L == []:
        return []
    else:
        return L[:-1]

#fungsi tambahan
def IsOneElmt(L):
    return Head(L) == []
def max2(a,b):
    if a > b:
        return a
    else :
        return b
def MaxElmtL(L):
    if IsOneElmt(L):
        return LastElmt(L)
    else :
        return max2(LastElmt(L),MaxElmtL(Head(L)))

#fungsinya
def HargaNinja(S):
    if IsEmpty(S):
        return 0
    else:
        if FirstList(S):
            return MaxElmtL(FirstList(S))*1000000 + HargaNinja(TailList(S))
        else:
            HargaNinja(TailList(S))

print(HargaNinja([[2,3,4,6],[1,1,3,9,2,7],[2,1],[4,4,6],[3,3]]))