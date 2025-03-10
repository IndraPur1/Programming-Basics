#Nama File  : nextday
#Pembuat    : Indra Purwanto
#Tanggal    : 1 november 2023
#Deskripsi  : Menentukan hari setelah angka tanggal masukan

# DEFINISI TYPE 
# type date : <d: integer [1..31], m: integer [1..12], y: integer > 0>  
#   <d,m,y> adalah sebuah date, dengan d adalah hari, m adalah bulan dan y adalah tahun

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeDate: integer [1..31], integer [1..12], integer > 0 --> date
#   {MakeDate(d,m,y) membentuk sebuah date dari d,m,y dimana d adalah hari, m adalah bulan dan y adalah tahun}
def date(d,m,y):
    return [d,m,y]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Day: date --> integer
#   {Day(D) memberikan hari dari date D}
def Day(D):
    return D[0]

# Month: date --> integer
#   {Month(D) memberikan bulan dari date D}
def Month(D):
    return D[1]

# Year: date --> integer
#   {Year(D) memberikan tahun dari date D}
def Year(D):
    return D[2]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsKabisat?: integer --> Boolean
#   {IsKabisat?(y) true jika y % 4 = 0 dan y % 100 != 0 atau y % 400 = 0}
def IsKabisat(y):
     return (((y % 4 == 0) and  (y % 100 != 0) or (y % 400 == 0)))

# DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN
# NextNDay: date, integer >= 0 --> date
#   {NextNDay(D,n) menghitung date yang merupakan n hari(n adalah nilai integer sesudah dari date D yang diberikan)}
def NextNday(D,n):
    if n == 0:
        return D
    else:
        d = Day(D)
        m = Month(D)
        y = Year(D)
        if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10) :
            if d == 31:
                m = m + 1
                d = 1
            else:
                d = d + 1
        elif (m == 4 or m == 6 or m == 9 or m == 11):
            if d == 30:
                m = m + 1
                d = 1
            else:
                d = d + 1
        elif (m == 12):
            if d == 31:
                y = y + 1
                d = 1
                m = 1
            else:
                d = d + 1
        else:
            if (IsKabisat(y)):
                if d == 29:
                    m = m + 1
                    d = 1
                else:
                    d = d + 1
            else:
                if d == 28:
                    m = m + 1
                    d = 1
                else:
                    d = d + 1
    return NextNday(date(d,m,y),n-1)

# APLIKASI
print(NextNday(date(22,10,2023),3))
print(NextNday(date(1,11,2023),5))
