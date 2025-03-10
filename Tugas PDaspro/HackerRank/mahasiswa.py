# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# make_mhs: string, 2 integer --> mahasiswa
# make_mhs(nama,nilai_uts,nilai_uas) membentuk sebuah tipe bentukan mahasiswa yang berisikan nama, nim, dan ipk.
# REALISASI
def make_mhs(nama,nim,ipk):
    return [nama,nim,ipk]

def nama(m):
    return m[0]

def nim(m):
    return m[1]

def ipk(m):
    return m[2]

def cek_ipk(m):
    if ipk(m)>3.5:
        return True 
    else :
        return False

def banyak_sks_mhs(m):
    if m[2]<2.0:
        return "18 sks"
    elif 2.0<=m[2]<=2.49:
        return "20 sks"
    elif 2.5<=m[2]<=2.99:
        return "22 sks"
    elif m[2]>3.0:
        return "24 sks"
        

m = make_mhs('Dengklek', '123456', 4.0 )

print(cek_ipk(m))
print(nama(m))
print(banyak_sks_mhs(m))