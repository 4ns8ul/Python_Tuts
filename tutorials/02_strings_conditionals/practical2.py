# str1 = "Hello there!"
# str2 = 'Null is good'
# str3 = """Hello
# You're Welcome to this program
# How about some tutorials and a nice cup of coffee?"""

# print(str1)
# print(str2)
# print(str3)


# str4 = 'Hello welcome to the course And I am using Apna College\'s Tutorials for this path'


# print(str4)


# # Concatenation
# str1 = "Python"
# str2 = " is a great"
# str3 = " language"
# final_str = str1 + str2 + str3
# print(final_str)

# print(len(str1))
# print(len(final_str))

# # Indexing in Python
# str1 = "Python is great"
# print(str1[5])


# str2 = "Python"
# slice = str2[-1:-5]
# print(slice)

# str3 = "Hello World!"
# str3 = str3.replace("World", "Developer")
# print(str3)

# print(str3.find("l"))
# print(str3.count("o"))

# Conditionals in Python
age = 21
if (age >= 18):
    print("Eligible for vote")
else:
    print("Not eligible for vote")

# Simple marks-grade mapper

marks = 100
grade = ''
if(marks > 100):
    print("Program broken. Please input correct value")
else:
    if(marks >= 90 and marks <= 100):
        grade = 'A'
    elif (marks >= 80 and marks < 90):
        grade = 'B+'
    elif (marks >= 60 and marks < 70):
        grade = 'B'
    elif (marks >= 45 and marks < 60):
        grade = 'C'
    elif (marks >= 35 and marks < 45):
        grade = 'D'
    elif (marks >= 28 and marks < 35):
        grade = 'E'
    else:
        grade = 'F'

    print("Based on your marks, your current grade is:  ", grade)

    if(grade == 'A' or grade == 'B+'):
        print("Well done! Keep it up")
    elif(grade == 'B' or grade == 'C'):
        print("You did great! Just aim a little high next time")
    elif(grade == 'D' or grade == 'E'):
        print("Your performance is below average. Please improve your grades to avoid suspension")
    else:
        print("You are suspended due to low grades!")