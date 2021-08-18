angka=int(input("Masukkan Angka : "))
pangkat=int(input("Masukkan Pangkat : "))
def x(angka,pangkat):
    if pangkat==1:
        return angka
    else:
        return angka*x(angka,pangkat-1)
print("Hasilnya adalah",x(angka,pangkat))
