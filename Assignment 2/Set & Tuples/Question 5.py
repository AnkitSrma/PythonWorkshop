tuple1 = "w", 5, "a", "s", "o", "u", "r", "c", "e"
print(tuple1)
tuple1 = tuple1[:3] + tuple1[5:]
print(tuple1)
list1 = list(tuple1) 
list1.remove("r") 
tuple1 = tuple(list1)
print(tuple1)
