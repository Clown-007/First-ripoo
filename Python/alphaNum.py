# if a string is aplha numeric or not

def alphanum(s):
    x = s.isalnum()
    if (x == True):
        print ("It is a AlphaNumeric")
        exit()
    else :
        print ("It is not a alpha numeric")
        exit()

print(alphanum(input("Enter a string : ")))