#Nama File : quality check air
#Pembuat   : Indra Purwanto
#Tanggal   : 10 September 2023
#Deskripsi : mengecheck apakah air higienis atau tidak dengan 3 bilangan integer

#Definisi dan spesifikasi
# AirHigienis : 3 integer --> string
# AirHigienis(air,bakteri,parasite) menentukan jenis air dari 3 bilangan integer yang berlainan air, bakteri, parasite

#Realisasi
def AirHigienis(air,bakteri,parasite):
    if air>500 and ((air)/(bakteri+parasite)**2)<1:
        return("Air Steril")
    elif air>250 and ((air)/(bakteri+parasite)**2)<25:
        return("Air bersih")
    elif air>100 and ((air)/(bakteri+parasite)**2)<50:
        return("Air Kotor")
    elif air<100 and ((air)/(bakteri+parasite)**2)>50:
        return("Air Toxic")
    else :
        return("Unknown")

#Aplikasi
print(AirHigienis(150,50,70))
print(AirHigienis(1000,50,70))