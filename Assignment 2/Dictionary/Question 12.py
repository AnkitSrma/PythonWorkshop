dict1 = {
    'mother': 53,
    'father': 62,
    'sister': 35,
    'brother': 26,
    'me': 20,
    'uncle': 43
}
'''
maxval = max(dict1.keys(), key=lambda x: dict1[x])
minval = min(dict1.keys(), key=lambda x: dict1[x])
print(f"Minimum value: {dict1[minval]}")
print(f"Maximum value: {dict1[maxval]}")
'''
minval = list(dict1.values())[0]
maxval = 0
print(dict1)
for each in dict1.values():
    if each > maxval:
        maxval = each
    if each < minval:
        minval = each
print(f"Minimum value: {minval}")
print(f"Maximum value: {maxval}")
