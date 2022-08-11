import math
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

if(a==0):
    print("Not Divisible")
elif((b**2-4*a*c)<0):
    print("The roots are imaginary")
else:
    print("The Roots are: ")
    x1 =(-b + (((b**2)-4*a*c))**0.5)/2*a
    print(x1)
    x2 = x1 =(-b - (((b**2)-4*a*c))**0.5)/2*a
    print(x2)


# x=math.sqrt(16) This both are same
# y=16**0.5