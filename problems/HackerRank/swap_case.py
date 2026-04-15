# def swap_case(s):
#     char_list = list(s)
#     s1=""
#     for c in char_list:
#         if c.isupper():
#             c = c.lower()
#             s1 += c
#         else:
#             c = c.upper()
#             s1 += c
            
#     return s1


# Faster method:
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)