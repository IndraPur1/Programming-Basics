#Nama File : mencari nilai tengah.py
#Pembuat   : Indra Purwanto
#Tanggal   : 23 September 2023
#Deskripsi : program untuk yang menghasilkan sebuah nilai tengah dari tiga bilangan integer yang diberikan
#Definisi dan spesifikasi
    # min2 : integer,integer --> integer
    # {min2(a,b) fungsi antara untuk mendapatkan nilai terkecil dari 2 integer berlainan(a dan b)}
#Definisi dan spesifikasi
    # max2 : integer,integer --> integer
    # {max2(a,b) fungsi antara untuk mendapatkan nilai terbesar dari 2 integer berlainan(a dan b)}
#Definisi dan spesifikasi
    # min3 : integer,integer,integer --> integer
    # {min3(a,b,c) fungsi antara untuk mendapatkan nilai terkecil dari 3 integer berlainan(a, b, dan c)}
#Definisi dan spesifikasi
    # median : integer,integer,integer --> integer
    # {median(a,b,c) fungsi untuk mendapatkan nilai tengah dari 3 integer berlainan(a, b, dan c)}
#Realisasi
def min2(a,b):
    return(a+b-abs(a-b))/2
def max2(a,b):
    return(a+b+abs(a-b))/2
def min3(a,b,c):
    return(a+min2(b,c)-abs(a-min2(b,c)))/2
def median(a,b,c):
    return(int(min3(max2(a,b),max2(b,c),max2(a,c))))
#Aplikasi
print(median(3,7,5))
print(median(25,20,40))


    