import mysql.connector


def get_airport_info(icao_code):
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="0368",
        autocommit=True
    )

    cursor = connection.cursor(dictionary=True)

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao_code,))
    result = cursor.fetchone()

    connection.close()
    return result


icao = input("Enter the ICAO code of an airport: ").strip().upper()

airport = get_airport_info(icao)

if airport is not None:
    print(f"Airport name: {airport['name']}")
    print(f"Location: {airport['municipality']}")
else:
    print(f"No airport found with that ICAO code {icao}")
