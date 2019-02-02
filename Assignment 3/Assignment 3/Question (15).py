def squarelist(list):
    list1 = []
    for each in list:
        list1.append(each**2)
    return list1


n = int(input("enter the number of items in list: "))
list1 = []
for a in range(n):
    item = int(input("Enter item: "))
    list1.append(item)
new_list = squarelist(list1)
print(f"Square list: {new_list}")
