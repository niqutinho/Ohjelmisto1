limit = 42.0
zander = (float(input("Enter the length of the zander in centimeters: ")))

if zander < limit:

    difference = limit - zander

    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {difference:.1f} centimeters below the size limit.")

else:
    print("The zander meets the size limit.")
