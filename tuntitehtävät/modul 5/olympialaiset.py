vuosi=int(input("anna vuosiluku: "))

if vuosi==2020:
    print("oli korona, ei olympialaisia")

elif vuosi % 4==0:
    print("oli olympialaiset")

else:
    print("ei olympialaisia")