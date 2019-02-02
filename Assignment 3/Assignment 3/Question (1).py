def magic(a):
    sum_ = 0
    while a != 0:
        sum_ += (a % 10)
        a = int(a/10)
    reverse = 0
    sum_0 = sum_
    while sum_ != 0:
        reverse = reverse * 10 + (sum_% 10)
        sum_ = int(sum_ / 10)
    return sum_0 * reverse



number = int(input("What is the magic number?: "))
a1 = magic(number)

if a1 == number:
    print(f"{number} is magic number.")
else:
    print(f"{number} is not a magic number.")
