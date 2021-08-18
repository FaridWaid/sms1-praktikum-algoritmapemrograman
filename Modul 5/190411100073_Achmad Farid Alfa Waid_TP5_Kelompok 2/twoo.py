def buatrik (x,y):
    matriks=[]
    for i in range(x):
        kol=[]
        for j in range(y):
            i=str(i)
            j=str(j)
            data=int(input("Matriks ["+i+","+j+"]="))
            kol.append(data)
        matriks.append(kol)
    return matriks
def kalitrik(a,b):
    matrik=[]
    for i in range(len(a)):
        kol=[]
        for j in range(len(b)):
            tambah=0
            for k in range(len(a)):
                tambah=tambah+(a[i][k]*b[k][j])
            kol.append(tambah)
        matrik.append(kol)
    return matrik
mat1=buatrik(2,2)
print("Matriks 1 = ",mat1)
mat2=buatrik(2,2)
print("Matriks 2 = ",mat2)
kali=kalitrik(mat1,mat2)
print("Matriks 1 * Matriks 2 = ",kali)
