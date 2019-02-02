def generate_dic(name):
    dict_ = {}
    f = open(name, 'r')
    for a in f:
        list_ = a.split()
        for each in list_:
            dict_[each] = len(each)
        list_ = []
    return dict_


filename = input("Enter file name: ")
print(f"{generate_dic(filename)}")
