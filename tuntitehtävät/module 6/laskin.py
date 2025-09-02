def laskin(operaatio, num1, num2):
    if operaatio=="*":
        return num1*num2
    if operaatio=="+":
        return num1+num2
    if operaatio=="/":
        return num1/num2
    if operaatio=="potenssi" or operaatio=="**":
        return num1**num2

    return "fuckooff"


kertolaskun_tulos=laskin("*", 3, 5)
print(kertolaskun_tulos)

tulos=laskin("+",3,5)
print(tulos)
jakojäänös=laskin("/",3,5)
print(jakojäänös)
potenssssi=laskin("potenssi",3,5)
print(potenssssi)
tähti=laskin("**",3,5)
print(tähti)