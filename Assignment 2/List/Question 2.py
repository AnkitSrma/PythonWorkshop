n = int(input("Enter number of items: "))
listn = []
for each in range(n):
    i = input("Enter item: ")
    listn.append(i)
cnt = 0
for each in listn:
    if len(each) >= 2 and each[0] == each[len(each)-1]:
        cnt += 1
print(f"{cnt}")
