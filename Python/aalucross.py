for i in range(5):
    for j in range(8):
        if (i % 3 == 2 or j % 3 ==2 ):
            print("*", end =' ')
        else:
            print(" ", end = ' ')
    print (" ")

for i in range(10):
    for j in range(10):
        if (i % 3 == 0 or j % 3 == 0 ):
            print("*", end =' ')
        else:
            print(" ", end = ' ')
    print (" ")
