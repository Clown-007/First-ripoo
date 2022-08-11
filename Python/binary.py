from unicodedata import decimal


b  = "10011"
s = 0 
l = len(b)
def Decimal1() :
    for i in range(l):
        p = (l -1) - i 
        s += int(b[i])*2**p
    return s


print(Decimal1())