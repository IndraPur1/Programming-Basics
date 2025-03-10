#LOL
def IsEmpty(S):
    return S == []

def IsList(S):
    return isinstance(S, list)
def KonsLo(L,S):
    if L == []:
        return [L]
    else:
        return [L] + S

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
    
#fungsi
def jumlah(S):
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return jumlah(FirstList(S)) + jumlah(TailList(S))
    else:
        return FirstList(S) + jumlah(TailList(S))

def total(S) :
    if IsEmpty(S):
        return 0
    elif IsList(FirstList(S)):
        return total(FirstList(S)) + total(TailList(S))
    else :
        return 1 + total(TailList(S))

def avg(S):
    return jumlah(S)//total(S)
print(avg([[8,9,10,12],[90,5,7,3],[86,78,40,32]]))


def Pasukan(S,Avg):
    if IsEmpty(S):
        return S
    else:
        if IsList(FirstList(S)):
            return KonsLo(Pasukan(FirstList(S),Avg),Pasukan(TailList(S),Avg))
        else:
            if FirstList(S) > Avg:
                return Pasukan(TailList(S),Avg)
            else:
                return KonsLo(FirstList(S),Pasukan(TailList(S),Avg))
            
print(Pasukan([[8,9,10,12],[90,5,7,3],[86,78,40,32]],avg([[8,9,10,12],[90,5,7,3],[86,78,40,32]])))
