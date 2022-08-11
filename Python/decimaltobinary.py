n = int(input("Enter a Decimal Number"))
l =[]
while (n != 0):
    temp = n % 2
    l.append (temp)
    n = n // 2
l.reverse()
print (l)
