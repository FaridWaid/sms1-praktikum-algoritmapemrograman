x=int(input("Masukkan Suku Awal = "))
y=int(input("Masukkan Banyak Suku = "))
z=int(input("Masukkan Beda = "))
listarit=[]
def arit(x,y,z):
    listarit.append(x)
    for i in range (1,y):
        x=x+z
        listarit.append(x)
    return listarit
def jumlah(x,y,z):
    sn=int((y/2)*(2*x+((y-1)*z)))
    return sn

print ("Isi listnya adalah ",arit(x,y,z))
print ("Jumlah Data = ",jumlah(x,y,z))
