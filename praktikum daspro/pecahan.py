'''
Nama File : tipedatapecahan.py
Deskripsi : Membuat tipe bentukan Pecahan beserta selektornya
Pembuat   : Indra Purwanto
Tanggal   : 29 September 2023
'''

#DEFINISI TYPE
#type pecahan : <n:integer >=0, d:integer>0 >
#   {<n:integer >=0, d:integer>0 > n adalah pembilang (numerator) dan d adalah penyebut (denumerator). Penyebut sebuah pecahan tidak boleh nol}

#DEFINISI  DAN SPESIFIKASI KONSTRUKTOR
#make_pecahan : integer>=0, integer>0 => pecahan
#   {make_pecahan(n,d) membentuk sebuah pecahan dari pembilang x dan penyebut y, dengan x dan y integer}
def make_pecahan(a,b):
    return[a,b]

#DEFINISI DAN SPESIFIKASI SELEKTOR
#pemb : pecahan => integer>=0
#   {pemb(p) memberikan numerator pembilang n dari pecahan tsb}
def pemb(P):
    return P[0]

#peny : pecahan => integer>0
#   {peny(p) memberikan denumerator penyebut d dari pecahan tsb}
def peny(P):
    return P[1]

#DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI
#AddP : 2 pecahan => pecahan
#   {AddP(P1,P2) : Menambahkan dua buah pecahan P1 dan P2 : n1/d1 + n2/d2 = (n1*d2 + n2*d1)/d1*d2}
#Realisasi dalam Python
def AddP(P1,P2):
    return ((pemb(P1)*peny(P2)+pemb(P2)*peny(P1)),(peny(P1)*peny(P2)))

#RealP : pecahan => real
#   {Menuliskan bilangan pecahan dalam notasi desimal}
#Realisasi dalam Python
def RealP(P):
    return pemb(P)/peny(P)

#SubP : 2 pecahan => pecahan
#   {SubP(P1,P2) : Mengurangkan dua buah pecahan P1 dan P2 : n1/d1 - n2/d2 = (n1*d2 - n2*d1)/d1*d2}
#Realisasi dalam Python
def SubP(P1,P2):
    return (pemb(P1)*peny(P2)-pemb(P2)*peny(P1)),(peny(P1)*peny(P2))

#MulP : 2 pecahan => pecahan
#   {MulP(P1,P2) : Mengalikan dua buah pecahan P1 dan P2 : n1/d1 * n2/d2 = (n1*n2/d1*d2}
#Realisasi dalam Python
def MulP(P1,P2):
    return ((pemb(P1)*pemb(P2))),(peny(P1)*peny(P2))

#DivP : 2 pecahan => pecahan
#   {DivP(P1,P2) : Membagi dua buah pecahan P1 dan P2 : (n1/d1) / (n2/d2) = (n1*d2)/(d1*n2)}
#Realisasi dalam Python
def DivP(P1,P2):
    return(pemb(P1)*peny(P2)),(peny(P1)*pemb(P2))

#DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqP?: 2 pecahan => boolean
#   {IsEqP?(P1,P2) true jika P1 = P2, membandingkan apakah dua buah pecahan sama nilainya : n1/d1 = n2/d2 jika dan hanya jika n1*d2 = n2*d1}
# Realisasi dalam Python
def IsEqP(P1,P2):
    return pemb(P1)*peny(P2) == peny(P1)*pemb(P2)

# IsLtP?: 2 pecahan => boolean
#   {IsLtP?(P1,P2) true jika P1 < P2, membandingkan dua buah pecahan, apakah P1 lebih kecil nilainya dari P2 : n1/d1 < n2/d2 jika dan hanya jika n1*d2 < n2*d1}
# Realisasi dalam Python
def IsLtP(P1,P2):
    return pemb(P1)*peny(P2) < peny(P1)*pemb(P2)

# IsGtP?: 2 pecahan => boolean
#   {IsGtP?(P1,P2) true jika P1 > P2, membandingkan dua buah pecahan, apakah P1 lebih besar nilainya dari P2 : n1/d1 > n2/d2 jika dan hanya jika n1*d2 > n2*d1}
# Realisasi dalam Python
def IsGtP(P1,P2):
    return pemb(P1)*peny(P2) > peny(P1)*pemb(P2)


P1 = make_pecahan(12,6)
P2 = make_pecahan(6,3)
print(pemb(P1))
print(peny(P2))
print(AddP(P1,P2))
print(RealP(P1))
print(IsGtP(P1,P2))
print(IsLtP(P1,P2))
print(IsEqP(P1,P2))
print(DivP(P1,P2))
print(MulP(P1,P2))
print(SubP(P1,P2))
