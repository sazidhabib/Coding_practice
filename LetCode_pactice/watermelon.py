def can_divide_watermelon(w):
    # Check if the weight is even and greater than 2
    if w > 2 and w % 2 == 0:
        return "YES"
    else:
        return "NO"

# Input the weight of the watermelon
w = int(input("Enter the weight of the watermelon: "))

# Output the result
print(can_divide_watermelon(w))