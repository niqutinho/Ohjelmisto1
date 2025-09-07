import random


noppa=int(input("Kuinka monta noppaa?: "))

summa=0

for i in range(noppa):
    heitto=random.randint(1,6)
    print(f"Noppa {i+1}: {heitto}")
    summa+=heitto

print(f"Noppien summa on {summa}")