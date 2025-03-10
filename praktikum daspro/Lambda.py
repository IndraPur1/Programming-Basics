def SigI(a,b):
    if a > b :
        return 0
    else:
        return a + SigI(a+1,b)

def SigI3(a,b):
    if a > b :
        return 0
    else:
        return a**3 + SigI3(a+1,b)

print(SigI(3,10))
print(SigI3(1,10))