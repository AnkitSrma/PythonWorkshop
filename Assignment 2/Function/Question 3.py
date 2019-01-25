Q.Function to calculate the factorial of a number (a non-negative integer). The
function accepts the number as an argument.
Solution:
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to calculate the factiorial : "))
print(factorial(n))
