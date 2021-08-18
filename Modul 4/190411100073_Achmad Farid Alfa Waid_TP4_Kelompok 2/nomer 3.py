print ("Searching data in list")
print()
while True:
    x = 0
    list = ['if', 'you', 'rerun', 'the', 'analysis', 'using', 'our', 'algoritms', 'and', 'our', 'data,', 'you', 'will', 'not', 'get', 'the', 'identical', 'result', 'as', 'provided', 'here.', 'the', 'reason', 'is', 'an', 'inherent', 'stochatic', 'component', 'in', 'these', 'result.', 'all', 'test', 'are', 'based', 'on', 'surrogates.', 'surrogates', 'are', 'random', 'signal']
    a = str(input("Masukkan data yang mau di cari : "))
    for i in range (0, (len(list) - 1)):
        if list[i] == a:
            print("Data",list[i], "ada di index ke-", i)
            x = 1
    if x == 0:
        print("Data tidak ditemukan")
    print("Jumlah data ", a, "sebanyak = ",list.count(a))
    b = str(input("Input y to continue "))
    if not (b == "y"):
        print ("Thank you")
        break
