x=int(input("Banyaknya Bilangan : "))
Bilangan=[]
Genap=[]
Ganjil=[]
def bil(x):
    for i in range (x):
        y=int(input("Masukkan Bilangan ke- {0} =".format(i)))
        Bilangan.append(y)
    a=Bilangan
    return a
def bilgen(Bilangan):
    for i in range (len(Bilangan)):
        if Bilangan[i]%2==0:
            Genap.append(Bilangan[i])
    return Genap
def bilgan(Bilangan):
    for i in range (len(Bilangan)):
        if Bilangan[i]%2==1:
            Ganjil.append(Bilangan[i])
    return Ganjil
    
print ("Bilangan = ",bil(x))
print ("Genap = ",bilgen(Bilangan))
print ("Ganjil = ",bilgan(Bilangan))
