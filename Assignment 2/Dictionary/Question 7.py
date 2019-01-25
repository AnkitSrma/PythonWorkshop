def merge_dict(*args):
    newdict = {}
    for each in args:
        newdict.update(each)

    return newdict


dict1 = {
    'name': "Aakancha",
    'age': 18,
    'section': 'A',
    'std': 'BCA'
}
dict2 = {
     'Mohit': {'Family': 'Father', 'Number': 4567532521},
    'Deepa': {'Family': 'Mother', 'Number': 2637263476}
    
}
dict3 = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
print("Merging dict1 and dict2:")
print(merge_dict(dict1, dict2))

print("Merging dict2 and dict3:")
print(merge_dict(dict2, dict3))

print("Merging dict1 and dict3:")
print(merge_dict(dict1, dict3))

