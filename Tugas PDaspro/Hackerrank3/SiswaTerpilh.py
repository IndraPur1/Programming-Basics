def IsEmpty(S):
    return S == []
def FirstList(S):
    if S == [] :
        return None
    else:
        return S[0]
def TailList(S):
    if S == [] :
        return None
    else:
        return S[1:]
def LastList(S):
    if S == [] :
        return None
    else:
        return S[-1]
print(LastList(["siri",20]))
#fungsinya
def NilaiSiswa(Si,S):
    if IsEmpty(S):
        return "Siswa itu tidak ada di kelas ini"
    else:
        if FirstList(FirstList(S)) == Si:
            return LastList(FirstList(S))
        else:
            return NilaiSiswa(Si,TailList(S))

print(NilaiSiswa("Antonio",[["siri",20],["Intan",70],["Antonio",100]]))



































