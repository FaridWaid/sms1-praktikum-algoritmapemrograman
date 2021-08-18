def buatmatriks(bar,kol):
    matrixln2=[]
    for i in range (bar):
        data=[]
        for j in range (kol):
            data.append(int(input("Matriks[{0},{1}] = ".format(i,j))))
        matrixln2.append(data)
        return matrixln2

def perkalianmat(mat1,mat2):
    matrikskali=[]
    for a in range (0, len(mat1)):
        var=[]
        for b in range (0, len(mat1[0])):
            kali=0
            for c in range (0, len(mat1[0])):
                kali=kali+(mat1[a][c]*mat2[c][b])
            var.append(kali)
        matrikskali.append(var)
    return matrikskali

m1=buatmatriks(2,2)
print ("Matriks 1 adalah ", m1)
m2=buatmatriks(2,2)
print ("Matriks 2 adalah ", m2)
print (perkalianmat(m1,m2))
