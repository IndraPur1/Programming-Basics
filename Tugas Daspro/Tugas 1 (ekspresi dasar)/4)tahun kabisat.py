# Nama file : Penentuan Tahun Kabisat
# Pembuat : Indra Purwanto
# Tanggal : 7 September 2023
# Deskripsi : sebuah program untuk mengecek apakah sebuah tahun merupakan tahun kabisat

#Definisi dan spesifikasi
# Jenis_Tahun : integer --> boolean
# Jenis_Tahun(yyyy) menentukan nilai kebenaran dari bilangan integer(yyyy)

# Realisasi
def Jenis_Tahun(yyyy):
    return (yyyy%400==0) or (((yyyy%4==0) and (yyyy%100!=0)))

# Aplikasi
print (Jenis_Tahun(2000))
print(Jenis_Tahun(2019))