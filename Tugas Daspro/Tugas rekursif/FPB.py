#Nama File  : FPB
#Pembuat    : Indra Purwanto
#Tanggal    : 1 november 2023
#Deskripsi  : mencari pembagi terbesar dari angka masukan

# DEFINISI DAN SPESIFIKASI
# FPB : 2 integer > 0 --> integer
# {FPB(a,b) menemukan nilai FPB dari 2 buah bilangan integer yang dimasukan}

# REALISASI

def FPB(a,b):
    if b == 0:
        return a
    else:
        return FPB(b,a % b)

#APLIKASI
print(FPB(60,10))
print(FPB(11,1))
print(FPB(70,5))