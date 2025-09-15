def get_season(month):
    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"
    return None

s = input("Enter the number of a month (1-12): ")
try:
    month = int(s)
    print("You entered:", month)
    season = get_season(month)
    if season:
        print("The season is", season + ".")
    else:
        print("Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input! Please enter an integer between 1 and 12.")
