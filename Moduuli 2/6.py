import random


koodi1 = "".join(str(random.randint(0, 9)) for _ in range(3))


koodi2 = "".join(str(random.randint(1, 6)) for _ in range(4))


print(f"Kolminumeroinen koodi (0–9): {koodi1}")
print(f"Nelinumeroinen koodi (1–6): {koodi2}")