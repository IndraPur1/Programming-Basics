#Nama File  : primabukan
#Pembuat    : Indra Purwanto
#Tanggal    : 1 november 2023
#Deskripsi  : menentukan apakah angka masukan adalah prima atau bukan

# DEFINISI DAN SPESIFIKASI
# Isprima : 2 integer > 0 --> boolean
# {Isprima(n,div=2) mengembalikan nilai true jika bilangan prima dan false jika bukan bilangan prima}
 
# REALSASI
def Isprima(n, div=2):
    if n == 1 :
        return False
    elif n == 2 :
        return True 
    elif n % div == 0 :
        return False
    elif div * div > n :
        return True
    else :
        return Isprima(n, div + 1)

#APLIKASI
print(Isprima(7))
print(Isprima(10))