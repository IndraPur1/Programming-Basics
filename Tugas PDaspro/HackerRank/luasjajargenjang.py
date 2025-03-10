def make_jajargenjang(a,t):
    return [a,t]

def alas(j):
    return j[0]

def tinggi(j):
    return j[1]

def luas(j):
    return(alas(j))*(tinggi(j))

j1 = make_jajargenjang(5.0, 6.0)
j2 = make_jajargenjang(3.3, 8.2)
j3 = make_jajargenjang(4.9, 5)

print(luas(j1))
print(luas(j2))
print(luas(j3))
