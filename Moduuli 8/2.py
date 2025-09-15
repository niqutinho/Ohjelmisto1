import mysql.connector


def get_airports_by_country(country_code):
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="root",
        autocommit=True
    )

    cursor = connection.cursor()

    sql = "SELECT type FROM airport WHERE iso_country = %s"
    cursor.execute(sql, (country_code,))
    results = cursor.fetchall()

    connection.close()

    airport_counts = {}
    for row in results:
        airport_type = row[0]  # tuple, ensimmäinen sarake on type
        if airport_type in airport_counts:
            airport_counts[airport_type] += 1
        else:
            airport_counts[airport_type] = 1

    return airport_counts


def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ").strip().upper()

    airport_counts = get_airports_by_country(country_code)
    print()
    print(f"\nAirports in {country_code}:")
    for airport_type, count in airport_counts.items():
        print(f"{count} {airport_type} airports")


run_country_program()
