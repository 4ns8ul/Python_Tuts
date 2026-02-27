# Basics
*[NOTE: All the sample code can be found in [sample_code.py](./sample_code.py) while all the assignments solutions can be found in [assignments.py](./assignments.py)]*
## Python Character Sets
- Letters - A-Z a-z
- Digits -> 0-9
- Special Symbols -> !,@,#,$,%,/ etc
- Whitespaces (Tabs, Blank Spaces, newline, carriage return, formfeed)
- Other Characters (ASCII & UNICODE)

---

## Getting Output from Python
- `print("Hello World")`
- `print("Hello ", "Anshul")`
- `print(91 + 92)`
- etc


# Variables in Python
Variables are the containers in memory that hold a certain value. These can be Strings, Numbers, Characters, Boolean etc.

**Identifiers in Python** ~ Identifers can be the name that is used to recognise any variable, class, function etc.

**Strings In Python** ~ In programming language, a sequence of multiple characters forms a string. These characters can be the one supported by Python (mentioned above), including the whitespaces, numbers, special symbols etc as long as they encloswd within `""`.


*[Note: Python is case Sensitive Language]*

Eg:->
- `name = "Akshansh"`
- `age = 22`
- `price = 233`

***Tip ~*** **Assignment:** Assignment in Python works by writing the value to the variable from right to left i.e., in above eg, we should read it as "Akshansh" is stored inside name (right to left) and not name is getting the value "Askhansh". `=` Is the assignment operator

## Rules for Assignment
1. Identifiers can be a combination of different characters, digits and underscore (`_`). Eg, `myvar`, `my_var`, `myVar`, `myVar1` etc.
2. An identifier cannot start with a digit. Eg `1Var` ❌ `Var1` ✅
3. We can't use special symbols in out identifiers like `!, @, #, %` etc.
4. Identifier can be of any length

## Data Types In Python
**TIP:** Use `type(<var_name>)` to see the type of variable
Data types represents vast vareity of data that Python supports by default.

These are divided into 2 types:

1. **Primitive Data types**: These are the basic building blocks that store single values and are generally immutable *(Their values cannot be changed once they are created)*.

    | Type | Description | Example |
    | ---- | ----------- | ------- |
    | `int` | Integers(whole numbers, positive, negative, etc) | `age = 30` |
    | `float` | Floating point (Decimal numbers) | `price = 70.10` |
    | `bool` | Boolean Vales (True or False) | `is_active = False` |
    | `str` | Sequence of characters, Enclosed in quotes | `name = "Alice"` |
    | `None` | Represents a variable where we don't wish to store any value | `dicton = None`|

2. **Non-Primitive Data Types:** These are the built-in data structures or collection types that can store multipe values or are complex and are generally mutable *(Their values can be changed after they are created)*
    | Type | Description | Example |
    | ---- | ----------- | ------- |
    | `list` | An *ordered* collection of items which can be of different data types | `items = [1, "hello", True]` |
    | `tuple` | An *ordered* immutable collection of items | `coordinates = (10.0, 20.0)` |
    | `dict` | A collection of key-value pairs | stud_id = `{"id": 1, "name" : "John"}` |
    | `set` | An unordered collection o funique items | `unique_ids = {1, 2, 3}` |

    *[Note: Here **ordered** doesn't mean ascending or descending but the order in which the data type was created will be preserved!]*

    Some other data types can be referred from the [image](./img/difference-between-primitive-and-non-primitive-data-structures-1.webp)

### Reserved Words in Python
| Keywords | Keywords | Keywords | Keywords |
| -------- | -------- | -------- | -------- |
|`and` | `else` | `in` | `return` |
|`as` | `except` | `is` | `True` |
|`assert` | `finally` | `lambda` | `try` |
|`break` | `False` | `nonlocal` | `with` |
|`class` | `for` | `None` | `while` |
|`break` | `False` | `nonlocal` | `with` |
|`continue` | `from` | `not` | `yield` |
|`def` | `global` | `or` |
|`del` | `if` | `pass` |
|`elif` | `import` | `raise` |

*[Note: Keywords cannot be used as identifers]*

## Calculation in Python

**Q.1:** Print the sum of two numbers in Python

**Sol:** 

    a = 12
    b = 13
    c = a+b
    print(c)

## Comments in Python
Comments are used to define meaning for peice of code. Comments are ignored byt the Interpreter/Compiler and are only meant to be read by humans for better understanding of the code (or snippet)

*Use case Scenarios*
- When many developers are working on a project or code, comments are implemented so that other developers can read and understand the snippets
- Comments are included in many products and open source projects so as to give idea to general users what the code does (they are different from manuals/documentations as they give information about specific piece of code)
- Can be implemented as checkpoints for debugging or development.

Types of comments in Python:
1. **Single Line Comments:** These are simple comments that extends to just a single line providing brief instructions or information. They begin with a `#` and end with next line
2. **Multi Line Comments:** These comments can extend to multiple lines enclosed within `'''` or `"""` and ends with another `'''` or `"""`.

### Operators in Python
An operator is a symbol that performs different operations:
- **Arithmetic Operators: *[Calculation]*** `+` `-` `*` `/` `%` `**`
- **Relational Operators: *[Comparision]*** `==` `!=` `<` `>` `<=` `>=`
- **Assignment Operators: *[Assignment]*** `=` `+=` `-=` `*=` `/=` `%=` `**=`
- **Logical Operators: *[Boolean]*** `and` `or` `not`


## Type Conversion & Casting in Python
- **Type Conversion:** In Python type conversion occurs automatically when the interpreter sees a suitable tyoe for a value. Eg, `num = 12` here num will be int but when we change it's value to something else like `num = 12.1232` Python automatically changes the type of variable as `float`.
- **Type Casting:** It happnes when the programmer explicitly tries to convert a data another data type. Like converting from **float** to **int**.

*[Note: The type conversion depends according to different data tyoes. Eg, float can store more data than int hence can be automatically be converted by Python, but the reverse is not true; we have to explicitly convert the data which means we are losing the digits after the decimal point. Also, **int** or **float** cannot be converted to string data type]*

### How to do type casting?
    a, b = 1, "2"
    c = int(b)
    sum = a + c

## Taking inputs in Python
In Python we make use of `input("<any_text>")` to take user input and store it in a variable. By default it stores the input in `str` data type. To convert to other data types, we use:
    
    int(input()) # To convert input to int data type
    float(input()) # To convert input to float data type

# Practice Questions
**Q1.** Write a program to input 2 numbers and print their sum.

**Q2.** Write a program to input 2 floating point numbers and print their average.

**Q3.** Write a program to input 2 numbers a & b. Print true if a is greater than or equal to b. If not print false.
