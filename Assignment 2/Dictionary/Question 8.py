dict_1 = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
    
}
dict2 = {
    'Mohit': {'Family': 'Father', 'Number': 4567532521},
    'Deepa': {'Family': 'Mother', 'Number': 2637263476}
    
}
sumval = 0

for val in dict_1.values():
    sumval += val
print(f"The sum of all the values is : {sumval}")

sumval = ""
for val in dict2.values():
    sumval += val
print(f"The sum of all the values is : {sumval}")
