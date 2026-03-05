# # Print numbers from 1 to 100

# i = 1
# while i<= 100:
#     print(i)
#     i += 1

# # Print numbers from 100 to 1
# j = 100
# while j >= 1:
#     print(j)
#     j -= 1

# # Print multiplication table of a number

# num = int(input("Enter the number:   "))
# i = 1
# while i <= 10:
#     print(num,"x", i, "=", num*i)
#     i += 1

# # Elements of the list
# my_list = [1, 4, 9, 16, 25, 36, 49, 63, 81, 100]

# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i+=1

# # Search for x in tuple
# inp = int(input("Enter a valid number:   "))
# my_tuple = (1, 4, 9, 16, 25, 36, 49, 63, 81, 100)

# found = 0
# i = 0
# while i < len(my_tuple):
#     if inp == my_tuple[i]:
#         print("Element", inp, "found at the index", i)
#         found = 1
#         break
#     i += 1

# if found == 0:
#     print("Element does not exists in the tuple")

# for loop

# # Elements of the list
# my_list2 = [1, 4, 9, 16, 25, 36, 49, 63, 81, 100]
# for i in my_list2:
#     print(i)

# # Search for x in tuple
# my_tuple2 = (1, 4, 9, 16, 25, 36, 49, 63, 81, 100)
# elem = int(input("Enter the element to be searched: "))
# count = 0
# found = 0
# for x in my_tuple2:
#     count += 1
#     if x == elem:
#         print("Element found at position:", count)
#         found = 1
#         break

# if found == 0:
#     print("The element is not present in the tuple")

# # 1-100
# for i in range(101):
#     print(i)

# # 100-1
# for i in range(100,0,-1):
#     print(i)

# # Multiplication
# table = int(input("Enter a valid number:  "))
# for i in range(1, 11):
#     print(table, "x", i, "=", i*table)

# Sum of first n numbers
num01 = int(input("Enter the number: "))
i = 1
sum = 0
while i <= num01:
    sum += i
    i += 1

print(sum)

# Factorial of number
num02 = int(input("Enter the number: "))
fact = 1
if num02 <= 1:
    print("Factorial of the number is: 1")
else:
    for i in range(1, num02+1):
        fact = fact * i
        i+=1

print("Factorial of the number", num02, "is", fact)