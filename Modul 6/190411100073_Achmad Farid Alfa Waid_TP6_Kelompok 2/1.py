data=[]
batas=int(input("Berapa banyak data yang anda inginkan : "))
bil=int(input("Masukkan Data Bilangan : "))
batas=batas-2
def jumlah(b):
    if len(data)>batas:
        data.append(b)
        return b
    else:
        data.append(b)
        bil=int(input("Masukkan Data Bilangan : "))
        return b+jumlah(bil)
print("Hasil penjumlahan dari", data, "adalah = ",jumlah(bil))
