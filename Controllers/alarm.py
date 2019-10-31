from flask_restful import Resource
from Config.DbConfig import DbConfig

class GetAlarms(Resource):
    
    connection = DbConfig()
    
    def put(self, idUser):
        query = "SELECT * FROM Alarm WHERE id_employee = {}".format(idUser)
        return self.connection.read(query)
    
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
        