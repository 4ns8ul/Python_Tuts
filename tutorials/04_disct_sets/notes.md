# Dictonary in Python

Dictonaries in Python are used to store data in `"key":"value"` pairs.

They are **unordered** and mutable and don't allow **duplicate keys**.

    dictonary = {
        "name" : "Anshul",
        "cgpa" : 9.6,
        "marks" : [98, 97, 95],
    }

To access data inside dictonary, we can search using "key" of the dictonary

    dictonary["name"] # Outputs Anshul
    dictonary["cgpa"] # Outputs 9.6
    my_dict1["marks"] # Outputs [88, 85, 79, 80]

## Nested Dictonary
Just like conditionals, we can create a nested ist inside a list according our requirements. This means that a dictonary can contain another dictonary.

## Methods in Dictonary

1. `myDict.keys()` # Returns all the keys inside a dictonary
2. `myDict.values()` # Returns all the values inside a dictonary
3. `myDict.items()` # Returns all the keys and values as tuples
4. `myDict.get(key)` # Returns the value corrosponding to the key. It is similar to `print(myDict["key"])` except that .get() method returns **no erros** if it doesn't find the key instead it retun **None** in the dictonary while the conventional method does.
5. `myDict.update(newDict/key-value pairs)` # Using this method we can add a new dictonary or a new key-value pair to the current dictonary

*[Note: If we want to convert the keys in a list or tuple, we can use type casting]*

- `list(my_dict.keys())` # Returns a list of keys
- `tuple(my_dict.keys())` # Returns a tuple of keys

*[Note: If we want to get the total number of keys in the list we can use the **len()** method]*

- `len(myDict)` Returns the length of the dictonary by returning the total number of keys in myDict
- `len(list(myDict.keys()))` By getting the list of keys first and then getting it's length.


# Sets in Python
Just like **sets** in Mathematics, Python has sets, which is an unordered collection of immutable & unique objects. Thus, an element cannot be repeated in a set unline list or tuple. Any item, repeated, is automatically resolved to it's single value at it's first occurence.

- SYNTAX

        nums = {1, 2, 3, 4, 5, 6} # General syntax
        set2 = {1, 2, 3, 2, 4, 5, 3} # set2 will become {1, 2, 3, 4, 5}
        null_set = set() # Empty set

*[NOTE: Only immutable data types can be stored inside a set like tuple, string, int etc. but not list, dict]*

## Methods in Sets
Let `set1 = {0, 1, 2, 3}`

    1. set1.add(elem) # Adds new elements inside the set
    2. set1.remove(elem) # Removes the specific element from the set
    3. set1.clear() # Empties the current set
    4. set1.pop() # Removes an element in random order
    5. set1.union(set2) # Combines both set values and returns new
    5. set1.union(set2) # Combines common values & returns new set
*[NOTE: Sets itself are mutable but the elements inside them are immutable.]*

### Unhashable Data Types
- These are the data types whose elements have a spcific hash stored as soon as they are created, for eg, dictonary, sets
- These hashes once created in memory cannot be modified as even if a slight chnage occurs, the entire hash for the object/element also changes.

## Practice Questions
1. Store following word meanings in a Python dictonary.
    
    - `"table": "A piece of furniture", "list of facts and figures"`
    - `"cat": "A small animal"`

2. You are given a list of subject for students. Assume one classroom is required for 1 subject. How many classrooms are required by all the students.

    - `"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"`

3. WAP to enter marks of 3 subjects from user and store them in a dictonary. Start with an empty dictonary & add one by one. Use subject name as key and marks as value.

4. Figure out a way to store 9 & 9.0 as seperate values in a set.
*[Can take help of in-built data types]*