n = int(input("Enter number of items: "))
listn = []
for each in range(n):
    item = input("Enter item: ")
    listn.append(item)
newlist = []
num = int(input("Enter a number: "))
for each in range(1, num+1):
    for new in listn:
        newlist.append(new + str(each))
print(f"New list: {newlist}")
