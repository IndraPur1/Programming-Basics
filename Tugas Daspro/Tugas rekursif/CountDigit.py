#Nama File  : CountDigit
#Pembuat    : Indra Purwanto
#Tanggal    : 1 november 2023
#Deskripsi  : menghitung jumlah digit dari angka masukan

# DEFINISI DAN SPESIFIKASI
# CountDigit : integer --> integer
# {CountDigit(n) menghitung banyaknya digit dari sebuah bilangan integer 0}

# REALISASI
def CountDigit(n) :
    if n >= 0 and n <= 9 :
        return 1
    else :
        return 1 + CountDigit(n//10)

#APLIKASI
print(CountDigit(0))
print(CountDigit(1234))
print(CountDigit(222))