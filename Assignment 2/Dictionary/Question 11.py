import operator

dict1 = {
    'name': "Aakancha",
    'lastname': "Thapa",
    'section': 'A',
    'std': 'BCA'
}
print(f"Real dictionary {dict1}")
order = input("Enter 'A' for ascending and 'D' For descending: ")
if order == 'A':
    sorted_dict = sorted(dict1.items(), key=operator.itemgetter(0))
    print(f"Ascending sort: {sorted_dict}")
else:
    sorted_dict = sorted(dict1.items(), key=operator.itemgetter(0), reverse=True)
    print(f"Descending sort: {sorted_dict}")
