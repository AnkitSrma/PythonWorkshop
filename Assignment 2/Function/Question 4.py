Q.Define a function is_even that will take a number x as input.If x is even, then return True.
Otherwise, return False.
Solution:
  
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
print(is_even(7))
print(is_even(8))
