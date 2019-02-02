def func(a):
    Digits = 0
    Letter = 0
    for each in a:
        if 'A' <= each <= 'z':
            Letter += 1
        elif '0' <= each <= '9':
            Digits += 1
    print(f"LETTERS: {Letter}")
    print(f"DIGITS: {Digits}")


str_1 = input("Enter a string: ")
func(str_1)
