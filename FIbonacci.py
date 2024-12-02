def fibonaccci(n):
    if n <= 1:
        return n
    return fibonaccci(n -1) + fibonaccci(n-2)

n = 10
fibonaccci_sequence = [fibonaccci(i) for i in range(n)]
print(fibonaccci_sequence)