def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

nth = int(input("Enter the term of the series: "))
print(fib(nth))
