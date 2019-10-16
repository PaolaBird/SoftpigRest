from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

class DbConfig():
    
    app =Flask(__name__)

    _server = 'localhost'
    _database = 'flaskcontacts'
    _user = 'root'
    _pass = 'root'
    _port = '3000'
    
    def __init__():
          conectBD()
    
    
    def conectBD():
        app.config['MYSQL_HOST'] = _server
        app.config['MYSQL_USER'] = _user
        app.config['MYSQL_PASSWORD'] = _pass
        app.config['MYSQL_DB'] = _database
        mysql= MySQL(app)

#if __name__ =="__main__":
    #app.run(port=3000, debug=True)