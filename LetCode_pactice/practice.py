
# Integer
x = 10

# Float
y = 3.14

# String
name = "Python"

# Boolean
is_active = True

print("bool: ",is_active," String: ", name," Float: ", y," Integer: ", x);

# Example
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")

# Example
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))

# Control Flow
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


# For Loop:

for i in range(5):
    print("ForLoop: ",i)


# While Loop:

count = 0
while count < 5:
    print("While loop: ",count)
    count += 1

# 4. Functions
# Functions encapsulate reusable blocks of code.

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Lambda Functions: One-liner anonymous functions.


square = lambda x: x**2
print(square(5))

# class
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy")
dog.bark()