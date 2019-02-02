import random


class PasswordGenerator:

    @staticmethod
    def password_generator(intlen):
        characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5',
                      '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*', '(', ')']
        password = []
        for a in range(intlen):
            password.append(characters[random.randint(1,70)])
        password = "".join(password)
        return password


len_ = int(input("Enter length of password: "))
print(f"Your password is : {PasswordGenerator.password_generator(len_)}")
