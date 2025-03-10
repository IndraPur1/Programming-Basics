#Nama File : Gaya angkat sayap pesawat terbang
#Pembuat   : Indra Purwanto
#Tanggal   : 10 September 2023
#Deskripsi : program untuk menghitung gaya angkat sayap pesawat terbang dari 3 bilangan integer
#Definisi dan spesifikasi
# Leana : 3 integer --> float
# Leana(A,V1,V2) menghitung gaya angkat pesawat dari 3 bilangan integer yang berlainan A, V1, V2
# A = luas penampang sayap pesawat(m**2)
# V1 = kecepatan udara dibagian bawah(m/s)
# v2 = kecepatan udara dibagian atas (m/s)
#Realisasi
def Leana(A,V1,V2):
    return(((1.3)*((V1**2)-(V2**2))*A)/2)
#Aplikasi
print (Leana(150,320,160))
print (Leana(50,320,160))
