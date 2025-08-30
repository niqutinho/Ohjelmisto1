import random


salainen_luku = random.randint(1, 10)

while True:
    try:
        arvaus = int(input("Arvaa luku (1-10): "))
    except ValueError:
        print("Anna kokonaisluku!")
        continue

    if arvaus < salainen_luku:
        print("Liian pieni arvaus.")
    elif arvaus > salainen_luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein!")
        break
