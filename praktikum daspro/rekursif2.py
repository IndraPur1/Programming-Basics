# Nama File : rekursif.py
# Deskripsi : Membuat modul terkait fungsi rekursif
# Pembuat   : Indra Purwanto

#Plus:integer --> integer
#{Plus(x,y) mengembalikan nilai x dijumlahkan dengan
#y dengan fungsi rekursif}
#Realisasi dalam python
def Plus(x,y):
    if y == 0 :
        return x
    else :
        return Plus(x+1,y-1)
print(Plus(3,4))

#Min:integer --> integer
#{Min(x,y) mengembalikan nilai x dikurangi dengan
# y dengan fungsi rekursif}
#Realisasi dalam python
def Min(x,y):
    if y == 0 :
        return x
    return Min(x-1,y-1)
print(Min(4,3))
#Mul:integer --> integer
#{Mul(x,y) mengembalikan nilai x dikali dengan 
# y dengan fungsi rekursif}
#Realisasi dalam python
def Mul(x,y):
    if y==1:
        return x
    elif y==0:
        return 0
    return x + Mul(x,y-1)
print(Mul(2,3))

#Dis:integer --> integer
#{Dis(x,y) mengembalikan nilai x dibagi dengan
# y dengan fungsi rekursif}
#Realisasi dalam python
def Dis(x,y):
    if x < y :
        return 0
    return 1 + Dis(x-y,y)
print(Dis(6,3))

#Exp:integer --> integer
#{Exp(x,y) mengembalikan nilai x dipangkat dengan
# y dengan fungsi rekursif}
#Realisasi dalam python
def Exp(x,y):
    if y == 0 :
        return 1
    return Exp(x,y-1)*x
print(Exp(4,5))

#Deretint:integer --> integer
#{Deretint(n) mengembalikan jumlah deret integer
# Deretint(6) = 1+2+3+4+5+6 , output 21}
#Realisasi dalam python
def Deretint(n):
    if n <= 1 :
        return n
    return n + Deretint(n-1)
print(Deretint(5))

#Deretbeda3:integer --> integer
#{Deretbeda3(n) mengembalikan jumlah deret 
# aritmatika beda 3 dengan Deretbeda3(2) = 3+6, output 9}
#Realisasi dalam python
def Deretbeda3(n):
    if n == 0 :
        return 3
    return 3 + Deretbeda3(n-1)
print(Deretbeda3(2))

#Deretgeo3:integer --> integer
#{Deretgeo3(n) mengembalikan jumlah deret 
# geometri r=3 dengan Deretgeo3(2) = 1+3, output 4}
#Realisasi dalam python
def Deretgeo3(n):
    if n == 0 :
        return 0
    return 3**(n-1) + Deretgeo3(n-1)
print(Deretgeo3(2))

#Deretkubik:integer --> integer
#{Deretkubik(n) mengembalikan jumlah deret 
# dengan Deretkubik(3) = 1+4+9, output 14}
#Realisasi dalam python
def Deretkubik(n):
    if n == 1 :
        return 1
    return n**2 + Deretkubik(n-1)
print(Deretkubik(3))