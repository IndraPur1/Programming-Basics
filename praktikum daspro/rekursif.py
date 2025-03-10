#pengurangan
def pengurangan(x,y):
    if y==0:
        return x
    else:
        return pengurangan(x,y-1)-1
    
print(pengurangan(10,2))


#penjumlahann
def penjumlahan(x,y):
    if y==0:
        return x
    return penjumlahan(x+1,y-1)
    
print(penjumlahan(10,3))


#perkalian
def perkalian(x,y):
    if y==1:
        return x
    return x + perkalian(x,y-1)
    
print(perkalian(10,5))


#pembagian
def pembagian(x,y):
    if x < y:
        return 0
    return 1 + pembagian(x-y,y)
    
print(pembagian(10,2))


#pangkat
def pangkat(x,y):
    if y==0:
        return 1
    return x*pangkat(x,(y-1))
    
print(pangkat(10,2))

