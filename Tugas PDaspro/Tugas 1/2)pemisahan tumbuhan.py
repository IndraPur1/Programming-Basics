#Nama File : Pemisahan kelompok tumbuhan
#Pembuat   : Indra Purwanto
#Tanggal   : 10 September 2023
#Deskripsi : program untuk memisahkan tumbuhan monokotil dan dikotil berdasarkan ciri-ciri fisiknya

#Definisi dan spesifikasi
# MonoDiko : 3 String --> String
# MonoDiko(a,b,k) menentukan Kelompok tumbuhan dari 3 data string yang berlainan a(akar),b(batang),k(kambium)

#Realisasi
def MonoDiko(a,b,k):
    if a=="tunggang" and b=="bercabang" and k=="berkambium" :
        return("Dikotil")
    elif a=="berserabut" and b=="beruas" and k=="tidak berkambium":
        return("Monokotil")
    else :
        return("Unknown")
#Aplikasi
print(MonoDiko("tunggang","bercabang","berkambium"))
print(MonoDiko("Berserabut","beruas","tidak berkambium"))