# Nama File : Jumlah Akar
# Pembuat : Indra Purwanto
# Tanggal : 6 September 2023
# Deskripsi : program untuk menghitung jumlahan kuadrat dari akar-akar persamaan kuadrat (x1^2 + x2^2) tersebut jika diberikan nilai a, b, dan c

#Definisi dan spesifikasi
# Jumlahan_Akar(x,y,z) : 3 integer --> float
# Jumlahan_Akar(x,y,z) menghitung jumlahan akar dari(X1**2+X2**2) bilangan integer yang berlainan x,y,z

# Realisasi
def Jumlahan_Akar(x,y,z):
    return (((-y/x)**2)-2*(z/x))

# Aplikasi
print (Jumlahan_Akar(2,8,4))
print (Jumlahan_Akar(3,18,9))