# def palindrom(n):

#     if n < 0:
#         return False
    
#     x = str(n)
#     return x == x[::-1]


# n = 12121
# print(palindrom(n))

def strpalindrom(s):
    return s==s[::-1]

s="helleh"
print(strpalindrom(s))