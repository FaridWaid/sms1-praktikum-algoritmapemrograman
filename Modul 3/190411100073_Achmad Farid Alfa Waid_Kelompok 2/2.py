print (" 3 angka terakhir di NIM saya adalah 073 ")
a = int(input("Masukkan size yang anda inginkan: "))
b=a
#angka 0
print ("*" * a)
for i in range (a-2):
    print ("*" + " "*(a-2) + "*")
print ("*" * a)
#angka 7
print ("*"*a)
while a>0 :
    print (' '*(a-1)+'*')
    a=a-1
print (" "+"*"*a)
#angka 3
print ("*" * b)
for i in range (b-5):
    print (" " * (b-1)+"*")
print ("*" * b)
for i in range (b-5):
    print (" " * (b-1) + "*")
print ("*" * b)

