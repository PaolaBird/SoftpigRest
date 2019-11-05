from flask_restful import Resource
from Config.DbConfig import DbConfig
<<<<<<< HEAD
from flask import jsonify
=======
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a

class GetAlarms(Resource):
    
    connection = DbConfig()
    
<<<<<<< HEAD
    def get(self, id):
        query = "SELECT ID_ALARM, date_start, issue FROM Alarm WHERE id_employee = {}".format(id)
        alarms = [] 
        result = self.connection.read(query)
        for alarm in result:
            alarms.append({'id': alarm[0],'date_start': alarm[1],'issue': alarm[2]})
        
        return jsonify({'alarms': alarms})
=======
    def put(self, idUser):
        query = "SELECT * FROM Alarm WHERE id_employee = {}".format(idUser)
        return self.connection.read(query)
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
    
class SearchAlarms(Resource):
    def get(self, id):
        respuesta = "{} ok, soy el get de Searchalarm". format(id)
        return respuesta, 200
    
    def put (self, id):
        # este tendra al parecido a esto: 
        """ form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400

        return 'ok', 200
        https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
        """
        respuesta = "{} ok, soy el put de SearchPig". format(id)
        return respuesta, 200
    
class AddAlarm(Resource):
    def get(self):
        id_employee = "01" #"""request.form['idEmployee']"""
        dateStart = time.strftime('%c') #request.form['dateStart']
        issue = "Esto es un asunto" #"""request.form['issue']"""
        lastUpdate = time.strftime("%c")
        
        
        return "INSERT INTO  Alarm(ID_ALARM, id_Employee, date_start, issue, lastUpdate) VALUES ({},{},{}, {}, {})". format("01",id_employee, dateStart,issue, lastUpdate)
        