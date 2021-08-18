UMR = 3000000
inti = str(input("Apakah anda sudah memiliki gaji ? (ya/tidak): "))
gaji = int(input("Berapakah gaji anda :"))
nikah = str(input("Apakah anda sudah menikah ? (ya/tidak): "))
rumah = str(input("Apakah anda sudah memiliki rumah ? (ya/tidak) : "))
if inti == "ya":
    if gaji > UMR:
        print ("Anda wajib mengikuti asuransi")
    else:
        print ("Anda tidak wajib mengikuti asuransi")
    if nikah == "ya":
        print ("Anda sudah bisa menabung")
    else:
        print ("Anda tidak wajib menabung")
    if rumah == "ya":
        print ("Anda wajib membayar pajak rumah")
    else:
        print ("Anda tidak wajib membaayar pajak rumah")
else:
    print ("Sebaiknya anda bekerja terlbih dahulu")
        
