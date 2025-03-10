def make_layang(a,t):
    return[a,t]

def alas(L):
    return L[0]

def tinggi(L):
    return L[1]

def luas(L):
    return(alas(L))*(tinggi(L))/2

L1 = make_layang(4.0,6.0)
L2 = make_layang(4.3,7.2)
L3 = make_layang(3.9,6)

print(luas(L1))
print(luas(L2))
print(luas(L3))