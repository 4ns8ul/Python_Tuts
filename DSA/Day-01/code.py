# This code is an experiment to prove the difference between linear search (list) (O(n)) and Hash Table Lookup (O(1)) (sets).
import timeit

# This code only runs once before actual tst starts
setup_code = """
import random
list_data = list(range(10000)) # Creates a list of number from 0 to 9999
set_data = set(range(10000)) # Creates a set of number from 0 to 9999
target = 9999
"""

list_test = "target in list_data" # Python starts at 0 and traverses through 9999 elements
set_test = "target in set_data" # Python passes the data through a hash function and gets a specific address for that data. Then it jumps to the required one thus performs one check only.

# The actual magic:
# stmt: The code you want to time.
# setup: The environment preparation we defined earlier.
# number=10000: This tells Python to run the test $10,000$ times
# If we only ran it once, the time would be so small (nanoseconds) that your computer's clock couldn't measure it accurately. By running it $10,000$ times, we accumulate enough time to see a clear difference.
t_list = timeit.timeit(stmt=list_test, setup=setup_code, number=10000)
t_set = timeit.timeit(stmt=set_test, setup=setup_code, number=10000)

print(f"List search time: {t_list:.5f}s")
print(f"Set search time: {t_set:.5f}s")

# Sample OUTPUT:
# List search time: 1.10059s
# Set search time: 0.00045s