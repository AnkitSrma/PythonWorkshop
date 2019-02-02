def is_anagram(x, y):

    for each in x:
        flag = False
        for val in y:
            if each == val:
                flag = True
        if not flag:
            return False
    return True


str_ = input("Enter first string: ")
str_0 = input("Enter second string: ")
print(is_anagram(str_, str_0))
