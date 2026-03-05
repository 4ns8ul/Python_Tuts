# my_dict1 = {
#     "name" : "Johhny",
#     "age" : 24,
#     "cgpa" : 8.11,
#     "marks" : [88, 85, 79, 80]
# }

# print(my_dict1["age"])

# my_dict2 = {} # Initializing a null dictonary
# my_dict2["name"] = "Baba yaga" # Assigning value in dict after it's creation
# print(my_dict2)
# my_dict2["name"] = "John Wick" # Changing the above value
# print(my_dict2)

# # Nested Dictonary
# student_details = {
#     "name" : "Anarth",
#     "age" : 24,
#     # Here, supposing we need to store the subjects alongwith the marks of the students
#     "subjects" : {
#         "physics" : 81,
#         "Chemistry" : 65,
#         "Mathematics" : 91,
#         "Computer Science" : 98
#     }   
# }

# # Accessing items in a nested dictonary
# print(student_details["subjects"]["physics"])
# print(student_details["subjects"].keys())
# print(tuple(student_details.keys()))

# # update method

# myDict = {"greet" : "hello", "name" : "chintu"}
# new_dict = {"interests" : ["singing", "cricket", "cooking", "reading"]}
# myDict.update(new_dict)

# print(myDict)

# # Sets in Python
# collection = {1, 2, 3, 4, 5, "hello", "world", "hello", 4, 4, 3, 8}
# print(collection)
# print(type(collection))
# print(len(collection)) # Prints total number of items

# collection2 = {} # Empty dictonary
# collection3 = set() # Empty set

set1 = {1,2 ,3, 4, 5}
set2 = {3, 4, 6, 7, 8, 9}
# set1.add(44)
# set1.remove(44)
# print(set1)

print(set1.union(set2))
print(set1.intersection(set2))