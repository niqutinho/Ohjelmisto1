import random


def roll_dice():
    return random.randint(1, 6)


tulos = 0
while tulos != 6:
    tulos = roll_dice()
    print(tulos)