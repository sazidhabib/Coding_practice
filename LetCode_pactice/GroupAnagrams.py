def group_anagrams(words):
    anagram_groups = {}

    for word in words:
        
        frequency = [0] * 26  
        for char in word:
            frequency[ord(char) - ord('a')] += 1
       
        frequency_key = tuple(frequency)

        if frequency_key not in anagram_groups:
            anagram_groups[frequency_key] = []
        anagram_groups[frequency_key].append(word)
   
    return anagram_groups.values()

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print("Grouped Anagrams: %s" % result)

# def group_anagrams(words):

#     # Dictionary to hold groups of anagrams
#     anagram_groups = {}

#     for word in words:
#         # Create a frequency tuple for the word
#         frequency = [0] * 26  # Assuming only lowercase English letters
#         for char in word:
#             frequency[ord(char) - ord('a')] += 1
#         # Convert list to tuple for dictionary key
#         frequency_key = tuple(frequency)

#         # Add the word to the appropriate group
#         if frequency_key not in anagram_groups:
#             anagram_groups[frequency_key] = []
#         anagram_groups[frequency_key].append(word)

#     # Return the values of the dictionary as a list of anagram groups
#     return anagram_groups.values()

# # Example usage
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = group_anagrams(words)
# print("Grouped Anagrams: %s" % result)

