# TO DO:
# 1. Phone "number": The number is int!
# 2. Length of the number should be 10 digits
# 3. Starts with 7, 8, 9.
# Method 1
# N = int(input())
# # ph_num = []
# flag = 0
# for i in range(0, N):
#     ph_num = input()

#     if len(ph_num) == 10:
#         if ph_num.isdigit():
#             if int(int(ph_num)/1000000000) == 9 or int(int(ph_num)/1000000000) == 8 or int(int(ph_num)/1000000000) == 7:
#                 print("YES")
#             else:
#                 print("NO")
#         else:
#             print("NO")
#     else:
#         print("NO")


# Method 2
import re

N = int(input())

for i in range(0, N):
    ph_num = input()
    result = re.search(r'^[789]\d{9}$', ph_num)

    if result:
        print('YES')
    else:
        print('NO')