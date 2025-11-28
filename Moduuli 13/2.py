from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/kenttä/<icao>')
def lentokentta(icao):
    try:
        conn = sqlite3.connect('airports.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        for taulu in ['airport', 'airports', 'Airport', 'AIRPORTS']:
            try:
                cur.execute(f"SELECT ident, name, municipality FROM {taulu} WHERE ident = ? OR icao = ?",
                            (icao.upper(), icao.upper()))
                row = cur.fetchone()
                if row:
                    conn.close()
                    return jsonify({
                        "ICAO": row["ident"] if "ident" in row.keys() else row["icao"],
                        "Name": row["name"],
                        "Municipality": row["municipality"] if "municipality" in row.keys() else "Ei tietoa"
                    })
            except sqlite3.OperationalError:
                continue

        conn.close()
        return jsonify({"error": "Lentokenttää ei löydy"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/')
def info():
    return "<h1>Tehtävä 2 – toimii nyt KAIKILLA airports.db-tiedostoilla!</h1><p>Testaa: /kenttä/EFHK</p>"


if __name__ == '__main__':
    app.run(port=3001, debug=True)