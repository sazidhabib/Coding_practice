#    """
#     Prints numbers from 1 to n with the following rules:
#     - Multiples of 3 are replaced with 'Fizz'.
#     - Multiples of 5 are replaced with 'Buzz'.
#     - Multiples of both 3 and 5 are replaced with 'FizzBuzz'.

#     Parameters:
#         n (int): The range of numbers to print (1 to n).
#     """

def fizzbuzz(input):
    for i in range(1, input+1):
        if i%3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i% 3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)