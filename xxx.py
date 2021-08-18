data=[]
ganjil=[]
genap=[]
def createlist():
    jumlah_data=int(input("Banyaknya Bilangan = "))
    for i in range (0,jumlah_data):
        input_data = int(input("Masukkan Bilangan ke %s = " %i))
        data.append(input_data)
        print()
    print("Bilangan = ",data)
def ganjil_genap():
    for i in range (0,len(data)):
        if (data[i])%2 == 0:
            genap.append(data[i])
        else:
            ganjil.append(data[i])
    print("Genap = ",genap)
    print("Ganjil = ",ganjil)

createlist()
ganjil_genap()

