#for given n, the sum of first n prime nos






# Program to check if a number is prime or not



# num = int(input("Enter a number: "))
# flag = False
# add = 0
# if num > 1:
#     for i in range(2, num+1):
#         if (num % i == 0):  
#             add = add + i        
#             flag = False 
#             break
#         else:
#             flag = True 
#             break
# for i in range(2, num+1):
#     if flag:
#         print (add ,"Is not a prime num ")
#     else: 
#         print (add, "It is a prime num")

# num = int(input("Enter a number: "))
# flag = False
# add = 0
# if num > 1:
#     for i in range (2, num+1):
#         for j in range(2,num+1):
#             if (num % i != 0):
#                 add = add + num 
#                 flag = True
#                 break 
#             else:
#                 flag = False
#                 break
# if flag:
#     print (add, "is the sum of the prime number...")




def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    dc = 0
    for i in range(1, n+1):
        if n % i == 0:
            dc += 1
    if dc == 2:
        return True


def primeSumUptoN(n):
    if n < 1 and n >= 0:
        return 0;
    sum = 0
    for i in range(2,n+1):
        if isPrime(i):
            sum += i
    return sum
def nPrimeSum(n):
    if n < 1:
        return 0
    sum = 0
    pc = 0
    x = 2
    while (pc<n):
        if isPrime(x):
            sum += x
            pc += 1
        x += 1
    return sum
print (nPrimeSum(10))

# print(isPrime(7))
        
        
