def gallon_to_leters(gallons):
    return gallons*3.785

while True:
    gallons=float(input("Anna bensiinimäärä: "))
    if gallons<0:
        print("Ohjelma päättyy")
        break
    liters = gallon_to_leters(gallons)
    print(f"{gallons} galloonaa on {liters:.2f} litraa")
