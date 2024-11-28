def roman_to_int(s):
    # Dictionary to map Roman numerals to integers
    roman_to_value = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    # Initialize result
    total = 0
    
    # Loop through the string
    for i in range(len(s)):
        # If the current value is less than the next value, subtract it
        if i < len(s) - 1 and roman_to_value[s[i]] < roman_to_value[s[i + 1]]:
            total -= roman_to_value[s[i]]
        else:
            # Otherwise, add it
            total += roman_to_value[s[i]]
    
    return total

# Example usage
s = "XIII"
print(roman_to_int(s))  # Output: 3