# Nama file : Status Kelulusan
# Pembuat : Indra Purwanto
# Tanggal : 6 September 2023
# Deskripsi : program untuk mengecek apakah seorang mahasiswa cumluade berdasarkan masa studi yang dinyatakan dalam bulan dan nilai IPK dengan range [0..4].

#Definisi dan spesifikasi
# status_kelulusan(mm,ipk) : integer, float --> boolean
# status_kelulusan(mm,ipk) menentukan nilai kebenaran dari bilangan integer(mm) dan bilangan float(ipk)

# Realisasi
def status_kelulusan(mm,ipk):
    return (0<=mm<=12*4.5) and (3.5<=ipk)
     
# Aplikasi
print(status_kelulusan(45,3.7))
print(status_kelulusan(54,3.4))