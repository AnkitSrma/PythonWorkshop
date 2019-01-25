r_m = int(input("Number of rows: "))
c_n = int(input("Number of columns: "))
_list = [[0 for col in range(c_n)] for row in range(r_m)]

for row in range(r_m):
    for col in range(c_n):
        _list[row][col]= row*col

print(_list)
