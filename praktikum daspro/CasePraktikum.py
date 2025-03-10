def segitiga(a,b,c) :
    if (a==b and b==c and a==c) :
        return "segitiga sama sisi"
    elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a) :
        return "segitiga sama kaki"
    else :
        return "segitiga sembarang"
print (segitiga(4,3,4))



def konversisuhu(suhu, char) :
    if (char=="R"):
        return((4/5)*suhu)
    elif (char=="k"):
       return(273+suhu)
    elif char=="f":
        return((9/5)*suhu)+32
print(konversisuhu(32,"R"))
