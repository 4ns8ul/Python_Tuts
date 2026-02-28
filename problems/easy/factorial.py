# A simple program to take user input and get factorial of that number!
num = int(input("Enter a number:   "))
fact = 1

if num == 0 or num == 1:
    fact = 1

while num > 1:
    fact = fact * num
    num -= 1

print("The factorial of the number is: ", fact)

