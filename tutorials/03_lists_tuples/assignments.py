# # 3 fav movies
# # Since loops are not covered till now, I'll be using the available methods
# movies_list = []
# movie1 = input("Enter the 1st fav movie:    ")
# movies_list.append(movie1)
# movie2 = input("Enter the 2nd fav movie:    ")
# movies_list.append(movie2)
# movie3 = input("Enter the 3rd fav movie:    ")
# movies_list.append(movie3)

# print(movies_list)

# OR we can save our memory (reduce variable)
# movies_list2 = []
# mov = input("Enter your fav movie:    ")
# movies_list2.append(mov)
# mov = input("Enter your fav movie:    ")
# movies_list2.append(mov)
# mov = input("Enter your fav movie:    ")
# movies_list2.append(mov)
# print(movies_list2)

# # OR EVEN A BETTER APPROACH

# movies_list3 = []
# movies_list3.append(input("Enter your fav movie:    "))
# movies_list3.append(input("Enter your fav movie:    "))
# movies_list3.append(input("Enter your fav movie:    "))

# print(movies_list3)

# # Check if a list contains palindrome elements or not
# my_list1 = ["item1", 1, 2, 3, "item4"]
# my_list2 = ["item2", 1, 2, 1, "item2"]

# my_list_rev = my_list2.copy()

# my_list_rev.reverse()

# print(my_list_rev)

# if(my_list_rev == my_list2):
#     print("The list is a palindrome")
# else:
#     print("The list is not a palindrome")

# Grade
my_tup = ("C", "D", "A", "A", "B", "B", "A")

print("There are", my_tup.count("A"), "students with grade 'A'")

# sort
the_list = ["C", "D", "A", "A", "B", "B", "A"]
the_list.sort()
print(the_list)