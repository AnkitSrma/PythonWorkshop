n = int(input("Enter the number of items in the list: "))
listn = []
for each in range(n):
    i = int(input("Enter the item: "))
    listn.append(i)
s_item = 0
for each in listn:
    s_item += each
print(f"the sum of all the items in the list {listn} is : {s_item}")
