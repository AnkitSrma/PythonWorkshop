list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
sum1 = 0
greater = 0
for i, list3 in enumerate(list1):
    sum2 = 0
    for each in list3:
        sum2 += each
    if sum2 > sum1:
        sum1 = sum2
        greater = i
print(f"The list in a list of lists whose sum of elements is the highest is : {list1[greater]}")
