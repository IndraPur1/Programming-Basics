# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# konso : elemen, list --> list
# konso(e,L) menghasilkan sebuah list dari L dengan tambahan e sebagai elemen pertamanya
# I.S. e, L terdefinisi
def konso(e, L : list):
    if L == [] :
        return [e]
    else :
        return [e] + L

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt : list --> elemen
# FirstElmt(L) menghasilkan elemen pertama list L, L tidak kosong
# I.S. L terdefinisi tidak kosong
def FirstElmt(L : list):
    return L[0]

# LastElmt : list --> elemen
# LastElmt(L) menghasilkan elemen terakhir list L, L tidak kosong
# I.S. L terdefinisi tidak kosong
def LastElmt(L : list):
    return L[-1]

# Tail : list --> list
# Tail(L) menghasilkan list L tanpa elemen pertamanya, L tidak kosong
# I.S. L terdefinisi tidak kosong
def Tail(L : list):
    return L[1:]

# Head : list --> list
# Head(L) menghasilkan list L tanpa elemen terakhirnya, L tidak kosong
# I.S. L terdefinisi tidak kosong
def Head(L : list):
    return L[:-1]

# NbElmt : list --> int
# NbElmt(L) menghasilkan banyaknya elemen list L
# I.S. L terdefinisi
def NbElmt(L : list):
    if L == []:
        return 0
    else:
        return 1 + NbElmt(Tail(L))

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty : list --> boolean
# IsEmpty(L) true jika list kosong
def IsEmpty(L : list):
    return L == []

# IsOneElmt : list --> boolean
# IsOneElmt(L) true jika list L hanya berisi satu elemen
def IsOneElmt(L : list):
    return NbElmt(L) == 1

# IsMember : elemen, list --> boolean
# IsMember(e,L) true jika e adalah elemen dari list L
def IsMember(e,L : list):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == e:
        return True
    else:
        return IsMember(e,Tail(L))

# Rember : elemen, list --> list
# Rember(x,L) menghapus sebuah elemen bernilai x dari lis L, list baru berkurang satu elemnya yaitu bernilai e
def Rember(x,L):
    if IsEmpty(L):
        return []
    else :
        if FirstElmt(L) == x :
            return Tail(L)
        else :
           return konso (FirstElmt(L),Rember(x,Tail(L)))

# MaxList : List --> integer
# MaxList(L) menghasikan elemen L yang bernilai maksimum menggunakan fungsi rekursif
def MaxList(L):
    if IsOneElmt(L):
        if FirstElmt(L):
            return FirstElmt(L)
        else:
            return MaxList(FirstElmt(L))
    else:
        if FirstElmt(L):
            return Max(FirstElmt(L),MaxList(Tail(L)))
        else:
            return Max(FirstElmt(L, MaxList(Tail(L))))
def Max(a,b):
    if a >= b:
        return a
    else:
        return b

#Nama File  : MaxList2
#Pembuat    : Indra Purwanto
#Tanggal    : 15 november 2023
# Deskripsi : fungsi untuk mencari maximum kedua dari list

# DEFINISI DAN SPESIFIKASI
# MaxList2 : list  --> intteger
# {MaxList2(L) menghasilkan elemen L yang bernilai maximum kedua menggunakan fungsi rekursif}
def MaxList2(L):
    return MaxList(Rember(MaxList(L),L))

print(MaxList2([1,2,3,4,3,2,4,5,4,4,6,76,5,7,9,765,5,9,8,432,22]))
#print(MaxList2([2, 6, 10, 99, 100, 20]))
#print(MaxList2([70, 67, 13, 98, 10, 20]))

#Nama File  : KaliList
#Pembuat    : Indra Purwanto
#Tanggal    : 15 november 2023
# Deskripsi : fungsi untuk perkalian elemen dari dua list

# DEFINISI DAN SPESIFIKASI
# KaliList : List, List  --> List
# {KaliList(L) menghasilkan List dari hasil perkalian setiap elemen di list pertama dan list kedua menggunakan fungsi rekursif}
def KaliList(L1,L2):
    if IsEmpty(L1):
        return []
    else :
        return konso(FirstElmt(L1)*FirstElmt(L2),KaliList(Tail(L1),Tail(L2)))
#print(KaliList([2,4,6],[1,2,3]))
#print(KaliList([1,2,3,4],[1,2,3,4]))

#Nama File  : MunculBerapaKali
#Pembuat    : Indra Purwanto
#Tanggal    : 15 november 2023
# Deskripsi : fungsi untuk menentukan jumlah munculkya sutau elemen dalam list

# DEFINISI DAN SPESIFIKASI
# NBElmtX : elemen, List  --> integer
# {NBElmtX(e,L) menghasilkan jumlah dari elemen yang ada pada list menggunakan fungsi rekursif}
def NBElmtX(e,L):
    if L == '':
        return 0
    else :
        if FirstElmt(L) == e :
            return 1 + NBElmtX(e,Tail(L))
        else :
            return NBElmtX(e,Tail(L))
#print(NBElmtX('a','alamat'))
#print(NBElmtX('o','ilmu komputer dan informatika'))

#Nama File  : Palindrom
#Pembuat    : Indra Purwanto
#Tanggal    : 15 november 2023
# Deskripsi : fungsi untuk mengecek apakah teks menghasilkan bunyi yang sama saat dibaca dari kiri atau kanan

# DEFINISI DAN SPESIFIKASI
# CekPalindrom : List  --> integer
# {CekPalindrom(L) menentukan apakah teks menghasilkan bunyi yang sama saat dibaca dari kiri atau kanan menggunakan fungsi rekursif}
def CekPalindrom(L):
    if L == '':
        return True
    else :
        if FirstElmt(L) == LastElmt(L):
            return CekPalindrom(Tail((Head(L))))
        else :
            return False
#print(CekPalindrom('kodok'))
#print(CekPalindrom('daspro'))

#Nama File  : TerdekatPointList
#Pembuat    : Indra Purwanto
#Tanggal    : 15 november 2023
# Deskripsi : fungsi untuk menentukan point dari list point yang terdekat dari point inputan

# DEFINISI DAN SPESIFIKASI
# NearestPoint : List --> point
# {NearestPoint(P,LP) mengahasilkan point terdekat dari point inputan menggunakan fungsi rekursif}
def point(a,b):
    return [a,b]

def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

def Jarak(P1,P2):
    return ((absis(P1) - absis(P2))**2 + (ordinat(P1) - ordinat(P2))**2)**0.5

def NearestPoint(P, LP):
    if LP == []:
        return None
    else:        
        if NearestPoint(P,Tail(LP)) != None and Jarak(P, NearestPoint(P,Tail(LP))) < Jarak(P,FirstElmt(LP)):
            return NearestPoint(P,Tail(LP))
        else:
            return FirstElmt(LP)

#print(NearestPoint(point(1,2),[point(0,0), point(3,4), point(6,7), point(1,1), point(2,1)]))

#Nama File  : minimumLOL
#Pembuat    : Indra Purwanto
#Tanggal    : 15 november 2023
# Deskripsi : fungsi untuk menentukan elemen atau elemen atom paling minimum dari list of list

# DEFINISI DAN SPESIFIKASI
# MinList : list of list --> integer
# {MinList(L) menghasilkan elemen atau eemen atom paling minimum dari list of list menggunakan fungsi rekursif}
def IsAtom(L):
    return type(L) != list

def Min2(a,b):
    if a > b:
        return b
    else :
        return a

def MinList(L) :
    if IsOneElmt(L):
        if IsAtom(FirstElmt(L)):
            return FirstElmt(L)
        else :
            return MinList(FirstElmt(L))
    else:
        if IsAtom(FirstElmt(L)):
            return Min2(FirstElmt(L),MinList(Tail(L)))
        else :
            return Min2(MinList(FirstElmt(L)),MinList(Tail(L)))

#print(MinList([3, [2, 4, 5], [6, 3], [6, 4, 1, 2], 7, [2]]))

#Nama File  : BerapaGanjilLOL
#Pembuat    : Indra Purwanto
#Tanggal    : 15 november 2023
# Deskripsi : fungsi untuk menentukan jumlah elemen ganjil dalam list if list

# DEFINISI DAN SPESIFIKASI
# NBOdds : list of list --> integer
# {NBOdds(L) menghasilkan jumlah elemen dan elemen atom yang ganjil yang ada pada list of list menggunakan fungsi rekursif}
def NBOdds(L):
    if IsEmpty(L):
        return 0
    else:
        if IsAtom(FirstElmt(L)):
            if FirstElmt(L) % 2 == 0 :
                return NBOdds(Tail(L))
            else:
                return 1 + NBOdds(Tail(L))
        else :
            return NBOdds(FirstElmt(L)) + NBOdds(Tail(L))
#print(NBOdds([3,[2,4,5],[6,3],[6,4,1,2],7,[2]]))
#print(NBOdds([3,[2,4,5],[6,3],[6,4,1,2],7,[21]]))

#Nama File  : PenjumlahanElemenLOL
#Pembuat    : Indra Purwanto
#Tanggal    : 15 november 2023
# Deskripsi : fungsi untuk menjumlahkan list yang menjadi elemen dari list of list

# DEFINISI DAN SPESIFIKASI
# MakeListAtom : list of list --> list
# {MakeListAtom(L) menghasilkan list biasa yang elemen atomnya merupakan penjumlahan dari semua elemen di list tersebut menggunakan fungsi rekursif}
def JumlahList(L):
    if IsEmpty(L):
        return 0
    else :
        return FirstElmt(L) + JumlahList(Tail(L))

def MakeListAtom(L):
    if IsEmpty(L):
        return []
    else:
        if IsAtom(FirstElmt(L)):
            return konso(FirstElmt(L),MakeListAtom(Tail(L)))
        else :
            return konso(JumlahList(FirstElmt(L)),MakeListAtom(Tail(L)))

print(MakeListAtom(([3, [2, 4, 5], [1, 3], [6, 4, 1, 2], 7, [2]])))