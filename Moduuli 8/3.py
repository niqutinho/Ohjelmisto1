import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="root",
        autocommit=True
    )

    cursor = connection.cursor()

    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    connection.close()

    if result is not None:
        latitude = result[0]
        longitude = result[1]
        return (latitude, longitude)
    else:
        return None


def run_airport_distance():
    icao1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if coords1 is None:
        print(f"No airport found with ICAO code {icao1}")
        return
    if coords2 is None:
        print(f"No airport found with ICAO code {icao2}")
        return

    distance_km = geodesic(coords1, coords2).kilometers
    print()
    print(f"\nDistance between {icao1} and {icao2}: {distance_km:.2f} kilometers")


run_airport_distance()
