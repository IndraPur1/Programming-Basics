#Nama File  : angkakebiner
#Pembuat    : Indra Purwanto
#Tanggal    : 1 november 2023
# Deskripsi : Mengubah angka menjadi biner

# DEFINISI DAN SPESIFIKASI
# biner : integer >= 0 --> string
# {biner(n) mengkonversi bilangan integer >= 0 menjadi string bilangan biner menggunakan fungsi rekursif}

# REALISASI
def biner(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else :
        return biner(n // 2) + biner(n % 2)

#APLIKASI
print(biner(10))
print(biner(8))