from collections import Counter
X = int(input()) # Number of shoes
shoe_size_list = map(int, input().split(" ")) # list of all shoe sizes

N = int(input()) # Number of customers

shoe_size_count = Counter(shoe_size_list)

final_price = 0
for i in range (0, N):
    shoe_size, price = map(int, input().split(" "))
    if shoe_size_count[shoe_size] < 1:
        price = 0
    final_price = final_price + price
    shoe_size_count[shoe_size] -= 1

print(final_price)