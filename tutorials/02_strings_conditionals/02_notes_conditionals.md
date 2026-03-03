# Coonditionals in Python

In real world, there are situations where we can have multiple choices or conditions to follow. For eg, going to the market, if the usual route is not available, we have to move to another one. In programming, this case is similar, hence we make use of conditionals.

SYNTAX:
- `if(condition)`: The first contition on which we want to do a task
- `elif(condition2)`: If the 1st condition fails, Python checks for this condition and performs tasks accordingly
- `else`: If neither of the conditions are met, we got to else block.

*[Note: `if` always comes first. If there are multiple `if` statements in a program then it is similar to **checkboxes** [] Condition 1, [] Condition 2 etc.]*

*[Note: `elif` can be written multiple times but should be preceeded by `if` block first. `else` is **optional** if `elif` is present and can only be written once for an if block. Useful when program has to deal woth just 2 conditions]*

    if(condition1):
        Statement1
    elif(condition2):
        Statement2
    else:
        StatementN

## Indentation in Python
Unlike other programming language, which incorporates usage of enclosing the code within `{}`, indentation in Python is a replacement for these `{}`. Normally, in C++ or JAVA, we can write a piece of code as:

    if(condition1)
    {
        Statement1
    }
    elif(condition2)
    {
        Statement2
    }
    else
    {
        StatementN
    }

Here the spaces doesn't matter as long as the statements are under `{}`. Although recommended to make code cleaner.

---

Python uses different approach. Each time we are inside a **block** or **function**, we need to give a 4-character space (or a tab space) to indicate we are inside the function. If we want to join the previous block, we can remove the 4 tabular space to jump out of the current code block.

### Nesting in Python
Nesting in Python refers to writing a block of code within a block of code. For eg,

    if(condition1 == True):
        if(condition2 == True):
            if(condition3 == True):
                Statement3
            else:
                Statement03

# Practice Hub
1. WAP to check if a number printed by the user is even or odd.
2. WAP to find the greatest of 3 numbers entered by the user.
3. WAP to check if a number is a multiple of 7 or not.
4. **[Bonus]** WAP to find the greatest of 4 in numbers entered by the user.