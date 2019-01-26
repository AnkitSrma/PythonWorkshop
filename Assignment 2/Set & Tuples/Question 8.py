p = [('item1','12.20'), ('item2','15.10'), ('item3','24.5')]
print( sorted(p, key=lambda a: float(a[1]), reverse=True))
