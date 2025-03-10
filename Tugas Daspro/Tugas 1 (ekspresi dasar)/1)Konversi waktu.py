# Nama File : Konversi Waktu
# Pembuat : Indra Purwanto
# Tanggal : 5 September 2023
# Deskripsi : mengkonversi sebuah waktu ke dalam satuan dettik dari 3 integer

#Definisi dan spesifikasi
# konversi_total_detik(jj,mm,dd) : 3 integer --> integer
# konversi_total_detik(jj,mm,dd) msngkonversi 3 bilangan integer berlainan yaitu jam(0<=jj), menit(0<=mm), detik(0<=dd) menjadi detik(dd)
    
# Realisasi
def konversi_total_detik(jj,mm,dd):
    return (jj*3600)+(mm*60)+(dd)

# Aplikasi
print(konversi_total_detik(1,1,1),"detik")
print(konversi_total_detik(24,60,60),"detik")