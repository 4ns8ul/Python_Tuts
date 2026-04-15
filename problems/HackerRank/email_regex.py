import re
import email.utils

N = int(input())
email_adds = []
for _ in range(0, N):
    inp = input()
    name, email_add = email.utils.parseaddr(inp)
    result = re.fullmatch(r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email_add)
    if result:
        email_adds.append(inp)

for emails in email_adds:
    print(emails)