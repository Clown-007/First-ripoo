#smallest positive that is missing 
# def s(num_list):
#     n = len(num_list)

#     for i in range(1,n+2):
#         if i not in num_list:
#             return i
# num_list=[1,2,3,4,5,7]
# print(s(num_list))

def small(num_list):
    n = len(num_list)

    for i in range(1, n+2):
        if i not in num_list:
            return i
num_list = [1, 3, 4, 6, 7]
print(small(num_list))
