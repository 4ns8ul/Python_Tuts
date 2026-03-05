# Loops in Python

# while loop in python

# while True: # infinite loop
#     print("hello")

# count = 1
# while count<5:
#     print("hello")
#     count += 1

# # print a string 10000 times in Python
# count = 1
# while count <= 10000:
#     print("Hello", count)
#     count += 1

# For loops in Python
## Traversing a list in Python without index

# list1 = [1, 2 ,3, 4, 5, 6, 7]
# for element in list1:
#     print("List element:", element)

# # Traversing in tuple
# tuple1 = (1,2, 3, 4, 5, 6, 7, 8, 100)
# for tup_elem in tuple1:
#     print("Tuple element: ", tup_elem)

# # Traversing in string using char

# str1 = "Hello world and bye world are different"
# count = 0
# for char in str1:
#     count += 1
# print("The total count of the characters present in the sentence is:", count)

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

seq2 = range(10)

for i in seq2:
    print(seq2[i])

for i in range(15): # Automatically sets start=0 & step=1
    print(i)
for i in range(2,15): # Automatically sets start=0 & step=1
    print(i)
for i in range(2,100, 2): # Automatically sets start=0 & step=1
    print(i)


for i in range(10):
    pass

print("I am the end. I am the inevitable. I am Th@n0s")