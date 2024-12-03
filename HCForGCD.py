# num1 = int(input("Enter First number: \n"))
# num2 = int(input("Enter Second number: \n"))

# if num1<num2:
#     minNum = num1
# else:
#     minNum = num2

# for i in range(1, minNum+1):
#     if num1%i == 0 and num2%i == 0:
#         GCD = i

# print(f"The HCF/GCD of these two number is {GCD}")


def find_gcd(num1, num2):
    # Determine the smaller of the two numbers
    if num1 < num2:
        min_num = num1
    else:
        min_num = num2

    # Initialize GCD
    gcd = 1

    # Iterate to find the largest divisor that divides both numbers
    for i in range(1, min_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

    return gcd

# Example usage
num1 = 48
num2 = 18
result = find_gcd(num1, num2)
print(f"The HCF/GCD of {num1} and {num2} is {result}")
