set1 = set()
print(set1)
a = set([1, 2, 4, 8, 16])
print(a)

num = set([1, 2, 4, 8, 22])
for i in num:
  print(num)

set1 = set()
set1.add("14")
print(set1)

set1 = set(["22", "44"])
set2 = set(["44", "59"])
seta = set1 | set2
print (seta)

setb = set1 & set2
print (setb)

setc = set1 - set2
print (setc)

setd = set2 - set1
print (setd)

set1.update(["55", "66"])
print(set1)
