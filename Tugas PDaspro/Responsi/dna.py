#Nama File : dna.py
#Pembuat   : NAMA-NIM
#Tanggal   : TGL-BLN-THN

# ==== DEFINISI ====
# Modul dna.py adalah bentuk realisasi dari soal-soal DNA

# ====ALGORTIMA ====

#FUNGSI LOKAL
#DEFINISI DAN SPESIFIKASI FUNGSI LOKAL
#Konso(e,L): menambahkan elemen e kepada list sebagai first elemen list
#output : List
def konso(e,L):
    if L == [] :
        return [e]
    else :
        return [e] + L

#Konsi(e,L): menambahkan elemen e kepada list sebagai last elemen list
#output : List
def konsi(e,L):
    if L == [] :
        return [e]
    else :
        return L + [e]

#FirstElmt(L): mengembalikan elemen pertama dari sebuah list
#output : character
def FirstElmt(L):
    return L[0]
#tail(L): mengembalikan list selain first elemen list
#output : list
def Tail(L):
    return L[1:]

#ToString(L): mengembalikan list ke dalam bentuk string
#output : string
def ToString(L):
    return ''.join(L)

def IsMember(e,L : list):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == e:
        return True
    else:
        return IsMember(e,Tail(L))

def IsEmpty(L):
    return L == []

def konsi(L : list, e):
    if L == [] :
        return [e]
    else :
        return L + [e]

#TIPE DATA BENTUKAN DNA
#DEFINISI DAN SPESIFIKASI TIPE DATA DNA
#type DNA <a,b,c,d,e,f,g,h> merupakan type data yang terbentuk dari character entah 
# 'A', 'T', 'C', dan 'G' dimana setiap character menunjukkan sebuah neuclotide

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#MakeDNA: 8 char --> DNA
#MakeDNA (a,b,c,d,e,f,g,h) membentuk sebuah DNA dari a sampai h dengan a sampai
# h sebagai neuclotide
def DNA (a,b,c,d,e,f,g,h):
  return([a,b,c,d,e,g,h])
  
#DEFINISI DAN SPESIFIKASI SELEKTOR
#nucleotideX: DNA,integer --> char
#nucleotideX(DNA,X) memberikan nucleotide DNA ke X
def nucleotideX (DNA,X):
    if X == 1 :
      return DNA[0]
    elif X == 2 :
      return DNA[1]
    elif X == 3 :
      return DNA[2]
    elif X == 4 :
      return DNA[3]
    elif X == 5 :
      return DNA[4]
    elif X == 6 :
      return DNA[5]
    elif X == 7 :
      return DNA[6]
    else :
      return DNA[7]

def IsEmpty(L):
    return L == []
  
#DEFINISI DAN SPESIFIKASI FUNGSI
#DNAtoRNA: DNA --> list
#DNATORNA(DNA) mengembalikan bentuk RNA dari DNA input dengan A = U, G = C, 
# C = G, dan T = A
def DNAtoRNA (DNA):
    if IsEmpty(DNA):
      return []
    else:
      if FirstElmt(DNA) == 'A' :
        return konso('U',DNAtoRNA(Tail(DNA)))
      elif FirstElmt(DNA) == 'G':
        return konso('C',DNAtoRNA(Tail(DNA)))
      elif FirstElmt(DNA) == 'C' :
        return konso('G',DNAtoRNA(Tail(DNA)))
      elif FirstElmt(DNA) == 'U' :
        return konso('A',DNAtoRNA(Tail(DNA)))
      else:
        return konso(FirstElmt(DNA),DNAtoRNA(Tail(DNA)))
  
#StringDNAtoRNA (DNA) mengembalikan bentuk string dari DNAtoRNA(DNA)
def StringDNAtoRNA (DNA):
    return ToString(DNAtoRNA(DNA))
  
#DNAtoBinary: DNA --> list
#DNAtoBinary(DNA) mengembalikan bentuk Binary dari DNA input dengan A = 00, G = 01, 
# C = 10, dan T = 11  
def DNAtoBinary (DNA):
    if IsEmpty(DNA):
      return []
    else:
      if FirstElmt(DNA) == 'A' :
        return konso('00',DNAtoBinary(Tail(DNA)))
      elif FirstElmt(DNA) == 'G':
        return konso('10',DNAtoBinary(Tail(DNA)))
      elif FirstElmt(DNA) == 'C' :
        return konso('01',DNAtoBinary(Tail(DNA)))
      elif FirstElmt(DNA) == 'T' :
        return konso('11',DNAtoBinary(Tail(DNA)))
      else:
        return konso(FirstElmt(DNA),DNAtoBinary(Tail(DNA)))
  
#StringDNAtoBinary (DNA) mengembalikan bentuk string dari DNAtoBinary(DNA)
def StringDNAtoBinary(DNA):
    return ToString(DNAtoBinary(DNA))

#NbNeuclotide : DNA --> integer
# NbNeuclotide(DNA) mengembalikan banyaknya neuclotide yang ada
# dan menghiraukan elemen kosong  
def NbNeuclotide(DNA):
    if IsEmpty(DNA) :
      return 1
    elif IsMember(FirstElmt(DNA),['']) :
        return NbNeuclotide((Tail(DNA)))
    else :
      return 1 + NbNeuclotide(Tail(DNA))
  
def IsMember(e,L : list):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == e:
        return True
    else:
        return IsMember(e,Tail(L))

#ManyX : DNA,char --> integer
# ManyX(DNA,X) mengembalikan banyaknya neuclotide dengan char X  
def ManyX(DNA,X):
    if DNA == []:
        return 0
    elif FirstElmt(DNA) != X:
        return 1 + ManyX(Tail(DNA),X)
    else:
        return 1 + ManyX(Tail(DNA),X)
  
#FrekuensiX :DNA,X --> real
# FrekuensiX(DNA,X) mengembalikan frekuensi dari banyaknya neuclotide dengan char X
# per banyaknya elemen neuclotide
def FrekuensiX(DNA,X):
    return NbNeuclotide(DNA) / ManyX(DNA,X)
  
#InversRNA : DNA --> list
# InversRNA(DNA) mengembalikan invers dari rna  
def InversRNA(DNA):
    if IsEmpty(DNA):
        return []
    else:
        return konsi(InversRNA(Tail(DNAtoRNA(DNA))),FirstElmt(DNAtoRNA(DNA)))
  
#InversBinary : DNA --> list
# InversBinary(DNA) mengembalikan invers dari binary 
def InversBinary(DNA):
    if IsEmpty(DNA):
        return []
    else:
        return konsi(InversBinary(Tail(DNAtoBinary(DNA))),FirstElmt(DNAtoBinary(DNA)))
  
#UpdateXtoY : DNA,X,Y --> DNA
# UpdateXtoY(DNA,X,Y) menggantikan elemen X dengan Y  
def UpdateXtoY(DNA,X,Y):
    if IsEmpty(DNA):
      return []
    else:
      if FirstElmt(DNA) == X:
        return konso(Y,UpdateXtoY(Tail(DNA),X,Y))
      else :
        return konso(FirstElmt(DNA),UpdateXtoY(Tail(DNA),X,Y))
  
# ====APLIKASI ====
print(DNA('A','C','G','T','T','C','G','T'))
print(nucleotideX(DNA('A','C','G','T','T','C','G','T'),1))
print(DNAtoRNA(DNA('A','C','G','T','T','C','G','T')))
print(StringDNAtoRNA(DNA('A','C','G','T','T','C','G','T')))
print(DNAtoBinary(DNA('A','C','G','T','T','C','G','T')))
print(StringDNAtoBinary(DNA('A','C','G','T','T','C','G','T')))
print(NbNeuclotide((DNA('','C','','T','T','C','G','T'))))
print(ManyX((DNA('A','C','C','T','T','C','G','T')),'T'))
print(FrekuensiX((DNA('A','C','C','T','T','C','G','T')),'T'))
print(InversRNA(DNA('A','C','G','T','T','C','G','T')))
print(InversBinary(DNA('A','C','G','T','T','C','G','T')))
print(UpdateXtoY(DNA('A','C','G','T','T','C','G','T'),'T','B'))

# ==== SOAL BONUS ====
