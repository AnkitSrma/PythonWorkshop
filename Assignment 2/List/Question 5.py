list1 = ["Black", "Red", "Maroon", "Yellow"]
list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
newlist = []
dict1 = {}
for each in range(len(list1)):
    dict1['color_name'] = list1[each]
    dict1['color_code'] = list2[each]
    newlist.append(dict1)
    dict1 = {}

print(newlist)



