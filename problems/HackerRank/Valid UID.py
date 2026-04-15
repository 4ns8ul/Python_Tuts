# ToDo:
# 1. Atelast 2 uppercases
# 2. Must contain atleast 3 digits
# 3. Only alphanumeric characters a-zA-Z0-9
# 4. No character repetition
# 5. Max chars 10
import re
T = int(input())
for _ in range(T):

    regex = (r'^(?=(?:.*[A-Z]){2,}).+$')
    exp = input()
    match = re.search(r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[a-zA-Z0-9]{10}$', exp)

    if match:
        print("Valid")
    else:
        print("Invalid")