#Nama File : dapat beasiswa atau tidak+
#Pembuat   : Indra Purwanto
#Tanggal   : 23 September 2023
#Deskripsi : program untuk menentukan seoarang mahasiswa mendapatkan beasiswa atau tidak dengan beberapa syarat
#Definisi dan spesifikasi
    # conv : char --> integer
    # {conv(x) fungsi untuk merubah grade nilai berupa character menjadi suatu nilai integer yang sudah ditentukan}
#Definisi dan spesifikasi
    # IP : 5 char --> float
    # {IP(a,b,c,d,e) fungsi untuk mendapatkan nilai rata rata dari 5 grade nilai (character) yang sudah diubah menjadi integer 
    #  dan dikali 3(karena jumlah sks 3) dan dibagi 15(karena jumlah sks(3) dikali jumlah grade nilai(5))}
#Definisi dan spesifikasi
    # dapatbeasiswa : integer,string, 5 char --> string
    # {dapatbeasiswa(se,st,a,b,c,d,e) fungsi untuk mengecek apakah mahasiswa mendapatkan beasiswa 
    #  atau tidak dengan syarat semester saat ini(3 <= se and 8 >= se), status mahasiswa(st=="Aktif"), nilai rata rata IP(IP(a,b,c,d,e))>3.3),
    #  dan 5 grade nilai(a,b,c,d,e=='A' or a,b,c,d,e=='B') dengan keluaran string jika true "Dapat Beassiwa", 
    # dan jika  false "Tidak Dapat Beasiswa"}
#Realisasi
def conv(x):
    if x == 'A':
        return 4
    elif x == 'B':
        return 3
    elif x == 'C':
        return 2
    elif x == 'D':
        return 1
    elif x == 'E':
        return 0
    else :
        return "eror"
def IP(a,b,c,d,e):
    return((conv(a)*3)+(conv(b)*3)+(conv(c)*3)+(conv(d)*3)+(conv(e)*3))/15
def dapatbeasiswa(se,st,a,b,c,d,e):
    if (3 <= se and 8 >= se) and (st=="Aktif") and (a=='A' or a=='B') and (b=='A' or b=='B') and (c=='A' or c=='B') and (d=='A' or d=='B')and (e=='A' or e=='B') and ((IP(a,b,c,d,e))>3.3):
        return "Dapat Beasiswa"
    else :
        return "Tidak Dapat Beasiswa"
#Aplikasi
print(dapatbeasiswa(5,"Aktif",'A','B','A','A','B'))
print(dapatbeasiswa(9,"Aktif",'B','A','A','A','B'))
print(dapatbeasiswa(3,"Cuti",'A','A','A','A','B'))
print(dapatbeasiswa(4,"Aktif",'A','A','A','A','C'))