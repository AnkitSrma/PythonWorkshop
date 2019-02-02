def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)


n = input("Enter number: ")
sum_ = 0
for each in n:
    sum_ += fact(int(each))

if sum_ == int(n):
    print(f"{n} is a strong number.")
else:
    print(f"{n} is not a strong number.")
