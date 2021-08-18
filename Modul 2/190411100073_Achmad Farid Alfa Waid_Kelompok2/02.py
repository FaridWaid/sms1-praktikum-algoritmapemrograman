TA = int (input("masukkan TA : "))
TK = int (input("masukkan TK : "))
TP = int (input("masukkan TP : "))
rerata = (TA+TK+TP) / 3
if rerata >= 75:
    if TA > TK or TA > TP:
        print ("bagian administrasi")
    elif TK > TA and TK > TP:
        print ("bagian produksi")
    else:
        print ("bagian pemasaran")
else:
    print ("anda tidak lulus")
