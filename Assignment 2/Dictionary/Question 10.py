dict1 = {
    'name': "Aakancha",
    'lastname': "Thapa",
    'section': 'A',
    'std': 'BCA'
}

print(dict1)
k = input("Enter a key: ")
if k in dict1:
    del dict1[k]
    print(dict1)
else:
    print("Key not found.")
