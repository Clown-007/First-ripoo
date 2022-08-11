#wrtite a function smallest integer not in the list
# triangle where middle is hollow






def longest(n):
    b = ""
    while(n>0):
        r = n % 2
        n = n//2
        b = str(r) + b
    return b

def bin_gap(N):
    