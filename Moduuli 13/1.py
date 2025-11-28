from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:luku>')
def tarkista_alkuluku(luku):
    return jsonify({
        "Number": luku,
        "isPrime": onko_alkuluku(luku)
    })

@app.route('/')
def info():
    return "<h2>Tehtävä 1: Alkulukupalvelu</h2><p>Kokeile: /alkuluku/31</p>"

if __name__ == '__main__':
    app.run(port=3000, debug=True)