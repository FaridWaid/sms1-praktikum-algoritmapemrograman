while True:
    a = int(input("How many stars row: "))
    a = a+1
    for b in range (0,a,1):
        for j in range (0,b,1):
            print ("*", end= ' ')
        print ("")
    c = str(input("Want to insert print star again? (input y or n)"))
    if c == "n":
        print ("Thank you")
        break


