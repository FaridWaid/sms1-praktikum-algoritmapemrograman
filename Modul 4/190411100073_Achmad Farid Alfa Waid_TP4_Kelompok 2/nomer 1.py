print ("Penjumlahan dan Pengurangan data dari 2 list angka")
print ()
list1 = []
while True :
    a = float(input("Masukkan list 1 = "))
    list1.append(a)
    b = str(input("Input y to continue = "))
    if not (b == "y"):
        break
print ("list1 == ",list1)
print()
list2 = []
while True :
    a = float(input("Masukkan list 2 = "))
    list2.append(a)
    b = str(input("Input y to continue = "))
    if not (b == "y"):
        break
print ("list 2 = ", list2)
print ()
penambahanlist = []
penguranganlist = []
if len(list1) == len(list2):
    for c in range (len(list2)):
        penambahanlist.append(float(list1[c]) + (list2[c]))
    print ("Penjumlahan list1 + list2 = ", penambahanlist)
    for c in range (len(list2)):
        penguranganlist.append(float(list1[c]) - (list2[c]))
    print ("Pengurangan list1 - list2 = ", penguranganlist)
else:
    print ("Warning!!!! Panjang kedua list tidak sama")
