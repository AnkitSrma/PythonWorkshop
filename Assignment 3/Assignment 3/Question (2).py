def nested_sum(a):
    sum_ = 0
    for each in a:
        sum_ += sum(each)
    return sum_

t = [[1, 2], [3], [4, 5, 6]]
print(f"Sum is {nested_sum(t)}")
