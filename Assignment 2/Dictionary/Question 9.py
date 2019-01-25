dict1 = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
product = 1
for each in dict1.values():
    product *= each
print(f"The product of all the values of the dictionary is : {product}")
