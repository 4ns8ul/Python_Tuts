# Loops in Python
Loops in Python can be described as reptition of a set of instructions. They are used for sequential traversal. Eg, traversing a list, tuple or dictonary or as simple as counting till 1000.

## `while` loops
SYNTAX:

    while <condition>:
        #some instructions

- The variable through which we control out loop is called **iterators**. Eg:
- The number of times the stataments inside the loop block is executed is called **iterations**.

        count = 1 # count is the iterator
        while count<5:
            print("hello")
            count += 1

## `for` loops in Python
SYNTAX:

    # Method I
    for <element> in <some_range>:
        # instructions
    

    # Method II (not used much)
    for <element> in <some_range>:
        # instructions
    else:
        # executed when loop ends
        # This block never executes after a 'break' statement

### `break` & `continue` Keywords
- `break` keyword in Python is used in loops inside a conditional statement to terminate a loop immediately after a condition is satisfied. Eg:

        counter = 1
        while True:
            print("hello world", i)
            counter += 1
            if counter == 5:
                break

- `continue` keyword is primarily used in cases when a condition needs to be skipped.

        counter = 1
        while True:
            print("hello world", i)
            counter += 1
            if counter == 5:
                continue # Will skip the 5th iteration
            if counter == 8:
                break # Will stop at 8th iteration
    
### `range` function in `for` loops
Range function returns a sequence of numbers by default, starting from 0 by default and incrememnts by 1 and stops before a specified number.

SYNTAX: `range(start?<default=0>, stop, step?)` # steps after which next iteration runs


    for i in range(15): # Automatically sets start=0 & step=1
        print(i)

    
    for i in range(2,15): # Automatically sets step=1 & starts from 2
        print(i)

    for i in range(2,15,2): # starts from 2 and executes after every 2 steps
        print(i)

### `pass` function in Python
The pass function in Python is primarily used for skipping an empty loop block. In **continue** we execute some condition first but in case of pass we simply skip the whole loop block.

    for i in range(10):
        pass
    
    print("I am the end. I am the inevitable. I am Th@n0s")

- Useful when a developer is working on some functionality and want to implement the block later

## Practice Hub

### While loop (Do last 2 ques with for loop)
1. Print numbers from 1 to 100.
2. Print numbers from 100 to 1.
3. Print the multiplication table of a number.
4. Print the elements of the following list using a loop: `[1, 4, 9, 16, 25, 36, 49, 63, 81, 100]`.
5. Search for the number x in the tuple using the loop: `(1, 4, 9, 16, 25, 36, 49, 63, 81, 100)`.

### use for loop with range()
1. Print numbers from 1 to 100.
2. Print numbers from 100 to 1.
3. Print the multiplication table of a number n.

### Mixed
1. Find the sum of first n numbers (using while)
2. WAP to find the factorial of first na numbers (using for)