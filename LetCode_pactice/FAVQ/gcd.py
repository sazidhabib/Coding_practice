
def gcd(num1,num2):
    if num1<num2:
        min = num1
    else:
        min = num2

    gcd = 1
    
    for i in range(1, min+1):

        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd

num1 = 48
num2 = 18
print("GCD: ", gcd(num1,num2))
