import random


def roll_dice(sides):
    return random.randint(1, sides)

sides=int(input("Anna nopan tahkojen määrä: "))

tulos = 0
while tulos != sides:
    tulos = roll_dice(sides)
    print(f"Heitit: {tulos}")
print("Sait maksimisilmäluvun", sides)