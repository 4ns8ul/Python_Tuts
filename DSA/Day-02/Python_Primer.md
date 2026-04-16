# Python Overview

## The Interpreted Language
- Python is an interpreted language. This means that it executes each statement line by line and gives the error at runtime (if any).

- The statements in Python can be executed in 2 different ways:

    1. **Interpreted mode**: User enters each statement and Python immediately executes it (**REPL**: *Read-Eval-Print-Loop*).
    2. **Scripted mode**: Stores all the statements in a `.py` file and the whole file is passed on to the interpreter

- On most Operating Systems, Python can be run using `python` command in the shell. To run a script, use `python script.py` or use `-i` flag to enter interactive after running the script `python -i script.py`.

- **IDEs (Integrated Development Enviornments)** provide richer software development platforms for Python like VS code, IDLE, a Python native IDE with syntax highlighting and basic debugging features.

### Python Program preview
    print("Welcome to the GPA calculator.")
    print("Please enter all your letter grades, one per line.")
    print("Enter a blank line to designate the end.")
    # map from letter grade to point value
    points = { A+ :4.0, A :4.0, A- :3.67, B+ :3.33, B :3.0, B- :2.67, C+ :2.33, C :2.0, C :1.67, D+ :1.33, D :1.0, F :0.0}
    num courses = 0
    total points = 0
    done = False
    while not done:
        grade = input() # read line from user
        if grade == '': # empty line was entered
            done = True
        elif grade not in points: # unrecognized grade entered
            print("Unknown grade '{0}' being ignored".format(grade))
        else:
            num courses += 1
            total points += points[grade]
    if num courses > 0:# avoid division by zero
        print( 'Your GPA is {0:.3}'.format(total points / num courses))


Python's code heavily relies on **whitespaces** or **indentation**. Individual statements are typically ended with new line either with concluding backslash `\`

## Objects in Python

### Object assignment
In Python, assignment of an object to an identifer is the most important part as we need data to perform actions, it helps us take data from user (or define it) and store it in the memory.

    Eg, temperature = 98.6
    # Here temperature is an identifier, which is associated with the object on the right hand side of the assignment operator =

### Objects in Python
The semantics of Python is similar to Programming languages like Java, C++. Each identifier is associated with the ***memory address*** of the object it is pointing.

A special identifier can be assigned to a reference variable named `None` which is similar to `null` in Java/C++. Basically the reference variable points to nothing.

Unlike Java/C++, Python is **dynamically typed** i.e. it recognises the type of the variable automatically through the object it is pointing. it doesn't have any predefined declaration associating with the identifier.

An identifier can be associated with any type of object and it can later be reassigned to same or other type since, the variable is just pointing the object (value) so the reference for that object in memory changes not the variable entirely.

**Instance of a class**: An instance is an object, created from a class

When you write something like:

    class Car:
        def drive(self):
            print("Driving")

    c = Car()

Here’s what actually happens:

**Car()** creates an object → that object is immediately an instance of Car.

**c** is just a reference (variable) that points to that object.


## Python $v/s$ Java
In Python, everything is treated in the form of Object Oriented Programming. 

Everything is trated in the form of objects and references. The identifiers becomes the references and the value that are assigned to them are called objects. Thus, when we see something like:

    x = 10

It means that, **x** is the reference for an int class object **10**
Here, unlike most programming languages, it doesn't store the value 10 in a container (variable) **x**. Not even for the **primary data types**

Java on the other hand stores data in 2 different ways, one of which is similar to Python:

1. **Primary Data Types**: For primary data types (classes), it stores data in the variable-value fashion, i.e., the variable doesn't act as the reference here. That is why, in Java we have to define the variable first and we can store limited data with respect to the data types (eg, 32 bits for int).

        Eg, int x = 10 // Here, x behaves as an actual container to store x in it

2. **Reference-Object**: For custom or user defined classes and object instances, Java stores data similar to Python by creating reference to the real-world object (value).

        Eg, class People{.....}
        People person = new People()
        // Here we are creating a new object of the class People, where person is the reference