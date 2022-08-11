# def print_stars(n,h=False,inv=False):
#     for i in range(n):
#         if inv:
#             tsp =i 
#             tj = 2 *(n0




# h = eval(input("Enter diamond's height: "))
# for x in range(h):
#     print(" " * (h - x), "*" * (2*x + 1))
# for x in range(h - 2, -1, -1):
#     print(" " * (h - x), "*" * (2*x + 1))


# Reading number of row
row = int(input('Enter number of row: '))

# Upper part of hollow diamond
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part of hollow diamond
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()