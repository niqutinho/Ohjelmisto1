import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='0368',
         autocommit=True
        )



def hae_lentokentät():
    sql=f"SELECT ident, name FROM airport LIMIT 5"
    print(sql)
    kursori=yhteys.cursor()
    kursori.execute(sql)

    kaikki=kursori.fetchall()
    print(kaikki)

hae_lentokentät()



