def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Sort the array
    strs.sort()

    # Compare the first and the last strings
    first = strs[0]
    last = strs[-1]
    common_prefix = ""

    # Find the common prefix between the first and last strings
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            common_prefix += first[i]
        else:
            break

    return common_prefix

# Example usage
strs = ["flower", "flow", "floght"]
print(longest_common_prefix(strs))  # Output: "fl"
