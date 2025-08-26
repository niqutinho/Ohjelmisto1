leiviskat=int(input("Anna leiviskät: "))
naulat=int(input("Anna naulat: "))
luodit=int(input("Anna luodit: "))

naulaa_per_leiviska=20
luotia_per_naula=32
grammaa_per_luoti=13.3

luotien_maara=(leiviskat*naulaa_per_leiviska*luotia_per_naula+naulat+luotia_per_naula+luodit)

kokonaisgrammat=luotien_maara*grammaa_per_luoti
kilot=int(kokonaisgrammat/1000)
grammat=kokonaisgrammat % 1000

print(f"Massa on nykymittojen mukaan: {kilot} kilogrammaa ja {grammat:.3} grammaa.")