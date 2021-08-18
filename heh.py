print ("Penjumlahan dan pengurangan data dari 2 list angka")
list1=[]
list2=[]
jumlahlist=[]
jumlahlist=[]
al="y"
while al == "y":
    a = int(input("Masukkan data kedalam list 1 : "))
    list1.append(a)
    a1= input("Input y untuk melanjutkan = ")
    if al == "t":
        print (list1)
        break     
print (list1)
print ()
al="y"
while al =="y":
    a= int(input("Masukkan data kedalam list 2 : "))
    list2.append(a)
    al= input("Input y untuk melanjutkan = ")
    if al=="y":
        print()
        continue
    else:
        print()
        break
print (list2)
print()
if len(list1)==len(list2):
    for i in range (len(list1)):
        jumlahlist.append(int(list1[i])+int(kist2[i]))
    print ("Penjumlahan list1 + list 2 = ",jumlahlisy)
    for i in range (len(list1)):
        kuranglist.append(int(list[i]) - int(list2[i]))
    print ("Penjumlahan list1 - list2 = ",kuranglist)
else:
    print("Warning!!!!!! PAnjang list 1 dan list 2 tidak sama")
