from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'softpig'

mysql = MySQL(app)


@app.route('/')
def index():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        return jsonify({"message": "Conexión a la Bd correcta"})

if __name__ == '__main__':
    app.run(debug=True)