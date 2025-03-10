def DNA (a,b,c,d,e,f,g,h):
  return([a,b,c,d,e,g,h])

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

def FirstElmt(L):
    return L[0]

def IsEmpty(L):
    return L == []

def konso(e,L):
    if L == [] :
        return [e]
    else :
        return [e] + L

def Tail(L):
    return L[1:]

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

def ToString(L):
    return ''.join(L)

def StringDNAtoRNA (DNA):
    return ToString(DNAtoRNA(DNA))

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

def StringDNAtoBinary(DNA):
    return ToString(DNAtoBinary(DNA))

def IsMember(e,L : list):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == e:
        return True
    else:
        return IsMember(e,Tail(L))

def NbNeuclotide(DNA):
    if IsEmpty(DNA) :
      return 1
    elif IsMember(FirstElmt(DNA),['']) :
        return NbNeuclotide((Tail(DNA)))
    else :
      return 1 + NbNeuclotide(Tail(DNA))

def ManyX(DNA,X):
    if DNA == []:
        return 0
    elif FirstElmt(DNA) != X:
        return 1 + ManyX(Tail(DNA),X)
    else:
        return 1 + ManyX(Tail(DNA),X)

def FrekuensiX(DNA,X):
    return NbNeuclotide(DNA) / ManyX(DNA,X)

def konsi(L : list, e):
    if L == [] :
        return [e]
    else :
        return L + [e]

def InversRNA(DNA):
    if IsEmpty(DNA):
        return []
    else:
        return konsi(InversRNA(Tail(DNAtoRNA(DNA))),FirstElmt(DNAtoRNA(DNA)))

def InversBinary(DNA):
    if IsEmpty(DNA):
        return []
    else:
        return konsi(InversBinary(Tail(DNAtoBinary(DNA))),FirstElmt(DNAtoBinary(DNA)))

def UpdateXtoY(DNA,X,Y):
    if IsEmpty(DNA):
      return []
    else:
      if FirstElmt(DNA) == X:
        return konso(Y,UpdateXtoY(Tail(DNA),X,Y))
      else :
        return konso(FirstElmt(DNA),UpdateXtoY(Tail(DNA),X,Y))


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