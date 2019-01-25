dict1 = {
    'Name': "Aakancha",
    'Age': 18,
    'Std': 'BCA'
}
for k, value in dict1.items():
    print(f"{k} : {value}")


dict2 = {
    'Mohit': {'Family': 'Father', 'Number': 4567532521},
    'Deepa': {'Family': 'Mother', 'Number': 2637263476}
}
for w, info in dict2.items():
    print(f"{w}")
    for k, value in info.items():
        print(f"{k} : {value}")
       
