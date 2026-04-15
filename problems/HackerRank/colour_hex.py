import re

N = int(input())
for _ in range(0, N):
    line = input()

    if ':' in line:
        matches = re.findall(r'#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})', line)
        for e in matches:
            print(e)