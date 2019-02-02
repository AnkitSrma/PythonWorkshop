import random


class DiceRoll:

    @staticmethod
    def dice_r():
        return int(random.random()*6)+1


exit_ = False
while not exit_:
    select = input("Do you want to Roll the dice? (Y/N)\n")
    if select == "Y" or select == "y":
        print(DiceRoll.dice_r())
    else:
        exit_ = True
