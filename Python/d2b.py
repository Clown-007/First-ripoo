from audioop import reverse


def D2B(n):
    b = ""
    while(n>0):
        r = n % 2
        n = n//2
        b = b + str(r)
    return b


print(D2B(22))