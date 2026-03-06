# Length of a list
heros = [ "G.One", "Mr India", "Pakshi Raaj"]
super_heros = ["Ra.One", "Mogambo", "Kaal", "2.0"]

def list_len(list1):
    print(len(list1))

list_len(heros)
list_len(super_heros)

# Elements of a length
def list_elem(list2):
    for e in list2:
        print(e, end=' ')

list_elem(heros)
list_elem(super_heros)

# Find factorial of n
def fact(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial

print(fact(5))

# USDT => INR 91.5
def convCurr(usdt_val):
    inr_val = usdt_val * 91.59
    return inr_val

print(convCurr(89))


# Sum of first n natural numbers

def sum_n(num,current_sum=0):
    current_sum = current_sum + num

    # Base case
    if num == 0:
        return current_sum
    
    return sum_n(num - 1, current_sum)

print(sum_n(5))

# Print elements in a list

def print_list(my_list, index=0):
    listLength = len(my_list)

    if index == listLength:
        return 
    print(my_list[index])
    print_list(my_list, index+1)

list1 = [1, 24, 5, 12, 433, 221, 454, 23]
print_list(list1)