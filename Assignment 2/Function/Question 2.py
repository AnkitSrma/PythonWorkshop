Q.Function to sum all the numbers in a list.
Solution:
    
def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(sum((10, 2, 8, 4, 6)))
