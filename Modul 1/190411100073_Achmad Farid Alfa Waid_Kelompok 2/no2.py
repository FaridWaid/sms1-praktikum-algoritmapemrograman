print (" Selamat datang! isi data berikut ini ")
print ("")
Nama = str(input("Masukan Nama :"))
NIM = int(input("Masukan NIM :"))
UTS = int(input("Masukan nilai UTS :"))
UAS = int(input("Masukan nilai UAS :"))
Rerata =(UTS+UAS)/2
print ("")
print ("Nama anda :" +Nama)
print ("NIM anda :",NIM)
print ("Nilai Rata-rata anda :",Rerata)
if 100 >= Rerata >= 80:
    print ("Anda mendapatkan nilai A")
elif 80 > Rerata >= 70:
    print ("Anda mendapatkan nilai B")
elif 70 > Rerata >= 60:
    print ("Anda mendapatkan nilai C")
elif 60 > Rerata >= 40:
    print ("Anda mendapatkan nilai D")
else :
    print ("Anda mendapatkan nilai E")

                 
