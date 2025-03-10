# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt : list --> elemen
# FirstElmt(L) menghasilkan elemen pertama list L, L tidak kosong
# I.S. L terdefinisi tidak kosong
def FirstElmt(L : list):
    return L[0]

# Tail : list --> list
# Tail(L) menghasilkan list L tanpa elemen pertamanya, L tidak kosong
# I.S. L terdefinisi tidak kosong
def Tail(L : list):
    return L[1:]

# Alice : List --> integer
# Alice(L) menentukan berapa elemen yang kurang dari 0
def Alice(L):
    if L == [] :
        return 0
    else :
        if FirstElmt(L) < 0 :
            return 1 + Alice(Tail(L))
        else :
            return Alice(Tail(L))

print(Alice([1, 2 , 0, -1, -2]))