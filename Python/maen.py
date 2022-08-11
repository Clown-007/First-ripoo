
#mean


#program to print mean
x = [5, 3, 2, 6, 1]
y = sum(x)/ len(x)
print (y)

#this is program using loop to print mean
sum = 0
mean = 0
for i in range(0, len(x)):
    z = x[i]
    mean = mean+z
print(mean/len(x))

