jumlah=int(input("Masukkan suku trianguler : "))
def x(n):
    if n==1:
        return n
    else:
        return n+x(n-1)
print("Hasil dari trianguler Numbers = ",x(jumlah))
