def edt_list(n_list):
    fnl_list = []
    for i, value in enumerate(n_list):
        if i != 0 and i != 4 and i != 5:
            fnl_list.append(value)
    return fnl_list

n = int(input("Enter number of items in the list: "))
listn = []
for each in range(n):
    item = input("Enter item: ")
    listn.append(item)
print(f"new list: {edt_list(listn)}")
