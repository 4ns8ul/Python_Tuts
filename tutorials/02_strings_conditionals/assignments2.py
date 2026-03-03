# # Find the length of usr's input name 
# name = input("Enter your name:   ")
# print(name + ", your name has a length of", len(name), "characters")

# # Find occurence of '$'
# counter = "#@$%#$%^$$#@%%$$#$$$#$%%$#$"
# print(counter.count('$'))

# # Evn or odd
# num1 = int(input("Enter a number:   "))
# if(num1%2 == 0):
#     print("The number is even!")
# else:
#     print("The number is odd!")

# # Greatest of 3
# g_num1 = int(input("Enter the first number:  "))
# g_num2 = int(input("Enter the second number:  "))
# g_num3 = int(input("Enter the third number:  "))

# if(g_num1 >= g_num2 and g_num1 >= g_num3):
#     print(g_num1,  "i.e., the first number is the greatest of all 3.")
# elif(g_num2 > g_num1 and g_num2 >= g_num3):
#     print(g_num2,  "i.e., the second number is the greatest of all 3.")
# elif(g_num3 > g_num2 and g_num3 > g_num1):
#     print(g_num3,  "i.e., the third number is the greatest of all 3.")

# # Check multiple of 7
# m_num = 50

# if(m_num%7 == 0):
#     print("The number is a multiple of 7!")
# else:
#     print("The number isn't multiple of 7!")

# Greatest of 4
gr_num1 = int(input("Enter the first number:  "))
gr_num2 = int(input("Enter the second number:  "))
gr_num3 = int(input("Enter the third number:  "))
gr_num4 = int(input("Enter the fourth number:  "))

if(gr_num1 >= gr_num2 and gr_num1 >= gr_num3 and gr_num1 >= gr_num4):
    print(gr_num1,  "i.e., the 'first' number is the greatest of all 4.")
elif(gr_num2 >= gr_num1 and gr_num2 >= gr_num3 and gr_num2 >= gr_num4):
    print(gr_num2,  "i.e., the 'second' number is the greatest of all 4.")
elif(gr_num3 >= gr_num2 and gr_num3 >= gr_num1 and gr_num3 >= gr_num4):
    print(gr_num3,  "i.e., the 'third' number is the greatest of all 4.")
else:
    print(gr_num4,  "i.e., the 'fourth' number is the greatest of all 4.")