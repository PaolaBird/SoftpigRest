from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'softpig'

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def index():
    if request.method == "GET":
        cur = mysql.connection.cursor()
        query = "SELECT * FROM examcat"
        cur.execute(query)
        data = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        examcat = [
            {
            "idExam": data[0],
            "examName": data[1],
            "examDescription": data[2],
            }
        ]
    return jsonify(examcat)

if __name__ == '__main__':
    app.run(debug=True)