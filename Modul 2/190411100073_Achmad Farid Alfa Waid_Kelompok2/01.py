print ("Selamat Datang di Swalayan 'MAJU MUNDUR'")
print("")
barang = str(input("Ingin membeli apa (baju/celana/sepatu)? "))
member = str(input("apakah mempunyai kartu member? ya/tidak "))
baju = 100000
celana = 150000
sepatu = 250000
diskon1 = baju - (baju*0.2)
diskon2 = celana - (celana*0.2)
diskon3 = sepatu - (sepatu*0.2)
if barang == "baju":
    if member == "ya":
        print ("Harga baju = Rp.",diskon1)
    else:
        print ("Rp.",baju)
elif barang == "celana":
    if member == "ya":
        print ("Harga celana = Rp.",diskon2)
    else:
        print ("Rp.",celana)
elif barang == "sepatu":
    if member == "ya":
        print ("Harga sepatu = Rp.",diskon3)
    else:
        print ("Rp.",sepatu)
else:
    print ("Dagangan tidak tersedia")
