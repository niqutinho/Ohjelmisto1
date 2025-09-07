luvut=[]

while True:
    syöte=(input("Anna numero (tai paina eneter lopettaaksesi): "))
    if syöte=="":
        break

    luvut.append(float(syöte))

luvut.sort(reverse=True)

print("Viisi suurinta lukua on: ")
for luku in luvut[:5]:
    print(luku)