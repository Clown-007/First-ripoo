y = int(input ("Please enter a year : "))

if ( y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
    print ("Leap Year")

else:

    print ("Not Leap Year")

