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
def KonsLi(S,L):
    if L == []:
        return [L]
    else:
        return S + [L]
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

#fungsi tambahan
def IsPrima(n,i=2) :
  if n < 2 :
    return False
  elif n == 2 :
    return True
  elif n % i == 0 :
    return False
  elif i*i > n :
    return True
  else :
    return IsPrima(n,i+1)

def Konkat(L1, L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konkat(KonsLi(L1,FirstList(L2)),TailList(L2))

def ConcatS(S):
    if IsEmpty(S):
        return []
    else:
        if IsList(FirstList(S)):
            return ConcatS(Konkat(FirstList(S),TailList(S)))
        else:
            return Konkat(KonsLo(FirstList(S),[]), ConcatS(TailList(S)))

#fungsinya
def JumlahPrima(S):
    if IsEmpty(ConcatS(S)):
        return 0
    else:
        if IsPrima(FirstList(ConcatS(S))):
            return FirstList((ConcatS(S))) + JumlahPrima(TailList(ConcatS(S)))
        else:
            return JumlahPrima(TailList(ConcatS(S)))
print(JumlahPrima([5,5,5,[10,5,10,5,[3,[3,[3,[2]]]]]]))
