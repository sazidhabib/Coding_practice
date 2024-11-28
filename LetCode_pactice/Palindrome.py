# def is_palindrome(x):
#     # Negative numbers are not palindromes
#     if x < 0:
#         return False
    
#     # Convert the number to a string and check if it's equal to its reverse
#     str_x = str(x)
#     return str_x == str_x[::-1]

# # Example usage
# x1 = 121
# x2 = -121
# x3 = 10

# print(is_palindrome(x1))  # Output: True
# print(is_palindrome(x2))  # Output: False
# print(is_palindrome(x3))  # Output: False

def isPalindrom(s):
    return s== s[::-1]

s1 = "hello"

print(isPalindrom(s1))