# Functions in Python

def calc_sum(a, b): # Parameters
    return a + b

calc_sum(1, 2) # Function calls
print(calc_sum(1, 2)) # 1, 2 are arguments

# Average of 3 numbers

def avg_num(n1, n2, n3):
    return (n1 + n2 + n3)/3

print(avg_num(1, 2, 3))

# Default Parameters

def cal_prod(a, b):
    print(a*b)
    return a*b

cal_prod() # This will result in error as there is no value passed or exist to which the function can process
# TypeError: cal_prod() missing 2 required positional arguments: 'a' and 'b'

def cal_prod(a=1, b=1):
    print(a*b)
    return a*b

cal_prod()

# Recursion

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("END")

show(5)

# Recusion through factorial
# logic => We can say that, n! = (n-1)! * n
# Like 5! = (5-1)! * 5 = 4! * 5
# Like 4! = (4-1)! * 4 = 3! * 4
# Like 3! = (3-1)! * 3 = 2! * 3
# Like 2! = (2-1)! * 2 = 1! * 2
def fact(n):
    if(n == 0 or n == 1):
        return 1 # First returns 1 and then gives control back to previous block
    else:
        return n * fact(n-1)
    
print(fact(5))