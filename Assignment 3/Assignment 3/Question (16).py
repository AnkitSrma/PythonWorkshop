n = int(input("Enter a number: "))
proper_divisors = []

for a in range(1, n):
    if n % a == 0:
        proper_divisors.append(a)

sum_ = 0

for each in proper_divisors:
    sum_ += each

if sum_ == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
