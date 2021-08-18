print ("Selamat datang di program kelulusan Beasiswa, isi data dibawah ini")
print("")
Nama = str(input("Masukan Nama anda :"))
IPK = float(input("Masukan IPK anda :"))
Skor = int(input("Masukan Skor anda :"))
print ("")
print ("Nama :" +Nama)
if IPK >= 3.00 and Skor > 1100:
    print ("Selamat anda dinyatakan lulus Beasiswa!")
else :
    print ("Maaf anda belum lulus! Tetap semangat ya!")
