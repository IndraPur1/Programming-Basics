def ganjil(n, i):
    if n >= i:
        return 0
    else :
        if n % 15 != 0 and n % 13 != 0:
            return ganjil(n+1, i)
        else:
            print(n, ganjil(n+1, i))


def cari_dan_cetak_ganjil():
    for n in range(10001, 50000):  # Mulai dari 10001 untuk memastikan angka ganjil
        if n % 13 == 0 and n % 15 == 0:  # Memeriksa apakah habis dibagi 13 dan 15
            print(n)

print(cari_dan_cetak_ganjil())