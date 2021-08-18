a = int(input("masukkan nilai : "))
if a >= 40:
    if a%5 == 0:
        print ("Pembulatan :",a)
    elif a%5 == 1:
        b = a - 1
        print ("Pembulatan :",b)
    elif a%5 == 2:
        c = a - 2
        print ("Pembulatan :",c)
    elif a%5 == 3:
        d = a + 2
        print ("Pembulatan :",d)
    elif a%5 == 4:
        e = a + 1
        print ("Pembulatan :",e)
elif a < 40:
    print (a)
else:
    print ("ERROR")
