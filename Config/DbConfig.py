import os  
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class DbConfig:
    
    _username = "root"
    _password = "root"
    _hostname = "localhost"
    _database = "softpig"
    app = Flask(__name__) #Para iniciar una app en flask (Debe estar instalado)

    #Pasaremos ahora los datos de conexión a el modulo de flask_sqlalchemy
    def __init__(self):
        
        db =SQLAlchemy(self.app)  #Crear la base de datos
        db.create_all()
        
    def dataBaseConect(self):
        BASE_DIR =  os.path.abspath(os.path.dirname(__file__))  #Nos sirve para acceder a la ruta absoluta de nuestra base de datos
        DB_URI = "mysql+mysqlconnector://{}:{}@{}/{}".format(self._username, self._password, self._hostname, self._database)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  
        