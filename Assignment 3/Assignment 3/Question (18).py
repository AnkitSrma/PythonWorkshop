def sum_(x):
    sum_1 = 0
    while x != 0:

        sum_1 += (x % 10) * (x % 10)
        x = int(x / 10)
    return sum_1


n = int(input("Enter a number: "))
n_= n

while sum_(n) != 1:
    n = sum_(n)
    if sum_(n) == 1:
        print(f"{n_} is a Happy number")
        break
