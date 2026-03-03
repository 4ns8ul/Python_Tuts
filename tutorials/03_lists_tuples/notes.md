# Lists in Python
List is an ordered collection of data in Python that can store multiple values within single variable. It is like storing multiple values within a single variable. The variable then becomes of the type *'List'*.

SYNTAX:

    list1 = [1,2,3,4,5]
    List is enclosed within square braces.

*[Note: In other programming languages, list is commonly reffered as **arrays**.]*

- **Lists** are similar to **arrays** but with a key difference: Arrays store similar type of data while list stores multiple types of data (even list within list)
- Unlike **strings**, **lists** in Python are mutable, i.e., their values can be changed after their creation.
- Eg:

        list1 = [123, "Gambhir", "Gambhir"]`
        list1[1] = "Gautam"

- Lists can be indexed & traversed the same way **strings** can be.

### List Slicing
Similar to strings slicing, list slicing is also possible. Eg:

- SYNTAX: list[start_index:end_index] end_index is not counted

        marks = [78, 86, 89, 74, 65]
        marks[1:4]
        marks[:4] # Same as marks[0:4]
        marks[1:] # Same as marks[1:len(marks)]
        marks[:] # Gives entire list
        marks[-3:-1] # Equals to [65, 74]

### List Methods
Some of the methods designed to enhance the operations performed on lists are:

    list = [1,2,3]
    list.append(4) # Adds an element (within brackets) at the end of the list
    list.sort() # Sorts the elements in ascending order
    list.sort(reverse = True) # Sorts the list in reverse order
    list.reverse() # reverses the list not sorting in descending order
    list.insert(index, element) # Adds elements on the specified position
    list.remove() # Remove the last element from the list
    list.pop(index) # Rwmoves the element at a particular index and returns

# Tuples in Python
Tuple is a built-in Python data type that creates immutable sequence of values.

SYNTAX:

    tup1 = (1,2,3,4,5)
    List is enclosed within circular brackets.

- To create a tuple with single value, always put a `,` at the end otherwise Python will treat it as an integer surrounded by brackets
        
        tup1 = (1,)

### Slicing in Tuple
Slicing in tuple is similar to slicing in list

### Methods in Tuple

    tup = (2,3,1,2)
    tup.index(el) # Returns index of first occurenece of element el
    tup.count(el) # Counts total number of occurences

## Practice Questions
### Lists
1. WAP to ask users names of their favourite movies and store them in a string.
2. WAP to check if a list contains palindrome of elements?

### Tuples
1. WAP to count the number of students with grade 'A' in the followng tuple:
["C", "D", "A", "A", "B", "B", "A"]

2. Store the above values in the list and sort them from "A" to "D"

### Self-Notes
While doing the palindrome question, I found the importance of .copy() function. If we directly go and create a copy of a list in Python, it does not create a copy (or object) in the memory but just a reference to that variable. So, if any operations performed using the new variable will affect on original objects. That's why we need to create a seperate object at times

- `my_list_rev = my_list2` **Reference**
- `my_list_rev = my_list2.copy()` **New object is created**