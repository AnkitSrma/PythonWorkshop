Sample_Data = [{"V": "S001"},
               {"V": "S002"},
               {"VI": "S001"},
               {"VI": "S005"},
               {"VII": "S005"},
               {"V": "S009"},
               {"VIII": "S007"}]

val = set()
for each in Sample_Data:
    for value in each.values():
        val.add(value)
print(val)
