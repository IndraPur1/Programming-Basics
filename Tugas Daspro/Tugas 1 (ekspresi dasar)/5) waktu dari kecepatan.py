# Nama File : Menghitung Waktu Kecepatan
# Pembuat : Indra Purwanto
# Tanggal : 7 september 2023
# Deskripsi : menghitung waktu suatu gerak berkecepatan tetap(km/j) dan berjarak(km) dalam satuan menit

# Definisi dan Spesifikasi
# waktu(j,k) : 2 integer --> float
# waktu(j,k) : menghitung waktu dari 2 integer yaitu jarak(j)km dan kecepatan(k)km/jam
#j = jarak(km)
#k = kecepatan(km/jam)

# Realisasi
def waktu(j,k):
    return(j/k)*60

# Aplikasi
print(waktu(12,40))
print(waktu(30,60))