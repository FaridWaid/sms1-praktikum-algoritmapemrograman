x=int(input("Masukkan urutan trianguler : "))
def tri(n):
    if n==0:
        return 0
    else:
        return n +tri(n-1)
print(tri(x))
