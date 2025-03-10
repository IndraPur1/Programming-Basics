# TYPE LIST-OF-LIST
# DEFINSI DAN SPESIFIKASI PREDIKAT KHUSUS UNTUK LIST OF LIST 
# IsEmpty : list of list -> boolean
# {IsEmpty(S) benar jika S adalah list of list kosong}
def IsEmpty(S):
    return S == []

# IsAtom : list of list -> boolean
# {IsAtom(S) menghasilkan true jika list adalah atom, yaitu terdiri dari sebuah atom}
def IsAtom(S):
    return isinstance(S, list) and len(S) == 1 and not isinstance(S[0], list)
print(IsAtom([]))
# IsList : list of list -> boolean
# {IsList(S) menghasilkan true jika S adalah sebuah list (bukan atom)}
def IsList(S):
    return isinstance(S, list)
print(IsList([]))

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: List, List of list -> List of list
# {KonsLo(L,S) diberikan sebuah List L dan sebuah List of List S. membentuk list baru 
# dengan List yang diberikan sebagai elemen pertama List of list: L o S → S'}
def KonsLo(L,S):
    if L == []:
        return [L]
    else:
        return [L] + S
    
# KonsLi : List of list, List -> List of list
# {KonsLi(S,L) diberikan sebuah List of list S dan sebuah list L, membentuk list baru 
# dengan List yang diberikan sebagai elemen terakhir list of List: S i(.) L -> S']
def KonsLi(S,L):
    if L == []:
        return [L]
    else:
        return S + [L]
    
# DEFINISI DAN SPESIFIKASI SELEKTOR 
# FirstList: List of list tidak kosong -> List 
# {FirstList(S) Menghasilkan elemen pertama list, mungkin sebuah list atau atom}
def FirstList(S):
    if S == [] :
        return None
    else:
        return S[0]
    
# TailList: List of list tidak kosong -> List of list 
# {TailList(S) Menghasilkan "sisa" list of list S tanpa elemen pertama list S}
def TailList(S):
    if S == [] :
        return None
    else:
        return S[1:]
    
# LastList: List of list tidak kosong -> List of list
# {LastList(S) Menghasilkan elemen terakhir list of list S. mungkin list atau atom}
def LastList(S):
    if S == [] :
        return None
    else:
        return S[-1]
    
# HeadList List of list tidak kosong -> List of list
# {HeadList(S) Menghasilkan "sisa" list of list tanpa elemen terakhir list}
def HeadList(S):
    if S == [] :
        return None
    else:
        return S[:-1]

# DEFINISI PREDIKAT
# IsEqs : 2 List of list -> boolean       MASIH GABISA
# {IsEqs(S1,S2) true jika S1 identik dengan S2 : semua elemennya sama}
def IsEqs(S1, S2):
    if IsEmpty(S1) and IsEmpty(S2):
        return True
    elif not IsEmpty(S1) and IsEmpty(S2):
        return False
    elif IsEmpty(S1) and not IsEmpty(S2):
        return False
    elif not IsEmpty(S1) and not IsEmpty(S2):
        if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)):
            return FirstList(S1) == FirstList(S2) and IsEqs(TailList(S1), TailList(S2))
        elif IsList(FirstList(S1)) and IsList(FirstList(S2)):
            return FirstList(S1) == FirstList(S2) and IsEqs(TailList(S1), TailList(S2))
        else:
            return False
print(IsEqs([1,2,3,[4]],[1,2,3,[4]]))

# IsMemberS : elemen, List of list -> boolean    MASIH GABISA
# {IsMemberS(A,S) true jika A adalah anggota S}
def IsMember(X,L):
    if IsEmpty(L):
        return False
    elif X == FirstElmt(L):
        return True
    else:
        return IsMember(X,Tail(L))

def IsMemberS(A, S):
    if IsEmpty(S):
        return False
    elif IsAtom(FirstList(S)):
        return A == FirstList(S)
    elif IsList(FirstList(S)):
        return IsMember(A, FirstList(S)) or IsMemberS(A, TailList(S))
print(IsMemberS(2,[2,3,4,5,[1]]))

# IsMemberLS : List, List of list -> boolean
# {IsMemberLS(L,S) true jika L adalah anggota S}
def IsMemberLS(L,S):
    if IsEmpty(L) and IsEmpty(S):
        return False
    elif not IsEmpty(L) and IsEmpty(S):
        return False
    elif IsEmpty(L) and not IsEmpty(S):
        return False
    elif not IsEmpty(L) and not IsEmpty(S):
        if (IsAtom(FirstList(S))) :
            return IsMemberLS(L,TailList(S))
        elif (IsList(FirstList(S))) :
            if IsEqual(L,FirstList(S)):
                return True
            else:
                return IsMemberLS(L,TailList(S))

def IsMemberLS(L, S):
    if IsEmpty(L) or IsEmpty(S):
        return False
    elif IsAtom(FirstList(S)):
        return IsEqual(L, FirstList(S)) or IsMemberLS(L, TailList(S))
    elif IsList(FirstList(S)):
        return IsMemberLS(L, FirstList(S)) or IsMemberLS(L, TailList(S))

# DEFINISI DAN SPESIFIKASI OPERATOR TERAHADAP LIST OS LIST
# Rember : elemen, List of list -> List of list
# {Rember(a,S) menghapus sebuah elemen bernilai a dari semua list S}
def Rember(a,S):
    if IsEmpty(S):
        return S
    elif IsList(FirstList(S)):
        return KonsLo(Rember(a,FirstList(S)), Rember(a,TailList(S)))
    else:
        if FirstElmt(S) == a :
            return Rember(a,TailList(S))
        else:
            return KonsLo(FirstElmt(S), Rember(a,TailList(S)))
        
# Max : List of list tidak kosong -> integer
# {Max(S) menghasilkan nilai elemen (atom) yang maksimum dari S}
def Max(S):
    if IsOneElmt(S):
        if IsAtom(FirstList(S)):
            return FirstList(S)
        else:
            return Max(FirstList(S))
    else:
        if IsAtom(FirstList(S)):
            return Max2(FirstList(S),Max(TailList(S)))
        else:
            return Max2(Max(FirstList(S)),Max(TailList(S)))

# Fungsi Perantara
# Max2 : 2 integer -> integer
# {Max2(a,b) menghasilkan nilai maksimum dari a dan b}
def Max2(a,b):
    if a >= b :
        return a
    else:
        return b
