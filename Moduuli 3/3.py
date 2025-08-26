sex=input("Sex? (male, female): ").strip().lower()

try:
    homovalue = float(input("Enter hemoglobin value (g/l): "))
except ValueError:
    print("Invalid hemoglobinvalue.")
    exit()

if sex=="female":
    if homovalue < 117:
        print("Your hemoglobin is low.")
    elif homovalue <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

elif sex == "male":
    if homovalue < 134:
        print("Your hemoglobin is low.")
    elif homovalue <= 167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is high.")

else:
    print("Invalid gender.")
