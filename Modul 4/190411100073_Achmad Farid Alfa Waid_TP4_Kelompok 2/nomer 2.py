print ("Input data dalam list")
print()
data=[]
b="y"
while b=="y":
    a=str(input("Masukkan data ke dalam list : "))
    data.append(a)
    for i in range (0, (len(data)-1)):
        if data [i]==a:
            print ("Duplikasi Terdektedi")
            print ("Data", data[i] ,"ada di indeks ke- ", i)
            print ("Data ",a, " Sudah Terhapus")
            del data[i]
            data.remove(a)
            break
    b=str(input("Masukkan y untuk melanjutkan = "))

print ()
print ("My List = ",data)
