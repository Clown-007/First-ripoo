#This is just printing stars
# for i in range (1,5):
#     for j in range(1,5):
#         print("*",end='')
#     print('')


# for i in range(1, 5):
#     print("*"*5)

#This is printing in line form
# for i in range(5):
#     for j in range(i+1):
#         print("*", end='')
#     print ('')

#This is printing in line form while giving the spacing      
for i in range(5):
    for sp in range(4-i):
        print(' ',end='')
    
    for j in range(2*i+1):
        print("*", end = '')
    print (' ')

# THis is Hollow Pyramid
# n = 10
# for i in range(n):
#     for sp in range(n-1-i):
#         print(' ',end='')
    
#     for j in range(2*i+1):
#         if (j == 0 or i == n - 1 or j == 2 * i):
#             print('*',end = '')
#         else:
#             print(' ', end = '')
#     print ('')


#Create Inverted hollow Pyramid and normal pyramid
