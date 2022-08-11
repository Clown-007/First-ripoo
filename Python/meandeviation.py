
# x | x - mean(x) | |x-mean(x)|
#-----------------------------------
#   |               |    
#Find mean devaition s

x = [5, 8, 9, 10, 6, 0, 11,1]
mean = 0
total = 0
sum = sum(x)
mean = sum/len(x)

for i in range(0, len(x)):
    a = x[i]
    b = a - mean
    if (b<0):
        c = b*-1
      
    else:
        c = b * 1
    print(a ," \t",b,"\t", c )
    total=total+c  
print(" ")
print ("Summation = ", total)
print(total/len(x))