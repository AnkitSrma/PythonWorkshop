def char_frequency(str):
    dict = {}
    for x in str:
        keys = dict.keys()
        if x in keys:
            dict[x] += 1
        else:
            dict[x] = 1
    return dict
print(char_frequency('google.com'))
