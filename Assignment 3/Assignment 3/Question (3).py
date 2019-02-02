def cum_sum(a):
    cumsum = []
    sum_1 = 0
    for each in a:
        sum_1 += each
        cumsum.append(sum_1)
    return cumsum


t = [1, 2, 3]
print(f"original list: {t}")
print(f"Cummulative sum list: {cum_sum(t)}")
