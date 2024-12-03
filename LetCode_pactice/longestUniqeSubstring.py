def longest_unique_substring(s):
   
    start = 0  
    max_length = 0  
    char_index_map = {} 

    
    for i in range(len(s)):
        char = s[i]

        
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        
        char_index_map[char] = i

       
        max_length = max(max_length, i - start + 1)

    return max_length


s = "abcabcbb"
result = longest_unique_substring(s)
print("The length of the longest substring without repeating characters is:", result)




# def longest_unique_substring(s):
#     """
#     Finds the length of the longest substring without repeating characters.

#     Parameters:
#         s (str): The input string.

#     Returns:
#         int: The length of the longest substring without repeating characters.
#     """
#     # Initialize variables
#     start = 0  # Start index of the current substring
#     max_length = 0  # Maximum length of substring found so far
#     char_index_map = {}  # Dictionary to store the last seen index of each character

#     # Iterate through the string
#     for i in range(len(s)):
#         char = s[i]

#         # If the character is already in the substring, move the start index
#         if char in char_index_map and char_index_map[char] >= start:
#             start = char_index_map[char] + 1

#         # Update the last seen index of the character
#         char_index_map[char] = i

#         # Update the maximum length
#         max_length = max(max_length, i - start + 1)

#     return max_length

# # Example usage
# s = "abcabcbb"
# result = longest_unique_substring(s)
# print("The length of the longest substring without repeating characters is:", result)
