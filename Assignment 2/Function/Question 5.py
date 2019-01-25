Q.Write a function called digit_sum that can take any mumber of intiger argiments takes returns
the sum of all that number's digits.
Solution:
    
def digit_sum(n):
    a = 0
    for each in str(n):
        a = a + int(each)
    return a
print(digit_sum(2468))
