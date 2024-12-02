num1 = int(input("Enter First number: \n"))
num2 = int(input("Enter Second number: \n"))

if num1<num2:
    minNum = num1
else:
    minNum = num2

for i in range(1, minNum+1):
    if num1%i == 0 and num2%i == 0:
        GCD = i

print(f"The HCF/GCD of these two number is {GCD}")

