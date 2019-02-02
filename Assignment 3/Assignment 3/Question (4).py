def middle(a):
    del a[0]
    if len(a) >= 1:
        del a[-1]
    return a


t = [1, 2, 3, 4]
print(f"The new list is: {middle(t)}")
