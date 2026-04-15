from collections import defaultdict

# d = defaultdict(list)
# d['python'].append('awesome')
# d['something-else'].append('not-relevant')
# d['python'].append('language')
# for i in d.items():
#     print(i)


# items: list[tuple[str, int]] = [('a', 1), ('b', 2), ('c', 3),('d', 4)]

n, m = map(int, input().split(' '))
# m = int(input())

d = defaultdict(list)
for i in range(0, n):
    d['A'].append(input())
for j in range(0, m):
    d['B'].append(input())

found = 0
for i in range(0, m):
    elem = d['B'][i]
    for j in range(0, n):
        if elem == d['A'][j]:
            print(j+1, end="")
            found = 1
        print("")

if found == 0:
    print(-1)
