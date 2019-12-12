from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify
from datetime import datetime, timedelta

class Birth(Resource):
    
    connection = DbConfig()
    
    def get(self, id):
        query = "SELECT ID_BIRTH, idMale, DATE_BIRTH, noBabies, noMummy, noDead FROM Birth WHERE ID_FEMALE = {}".format(id)
        births = [] 
        result = self.connection.read(query)
        for birth in result:
            births.append({'id': birth[0],'male': birth[1],'date': datetime.strftime(birth[2], '%d/%m/%Y'),'babies': birth[3],'mummy': birth[4],'dead': birth[5]})
        
        return jsonify({'births': births})
    
    def post(self):
        ID_FEMALE = request.get_json('ID_FEMALE')
        idMale = request.get_json('idMale')
        DATE_BIRTH = request.get_json('DATE_BIRTH')
        noBabies = request.get_json('noBabies')
        noMummy = request.get_json('noMummy')
        noDead = request.get_json('noDead')
        
        id_Employee = self.connection.employee("SELECT NO_EMPLOYEE FROM Person WHERE idInstalation = 04")
        
        date = datetime.strptime(DATE_BIRTH['DATE_BIRTH'], "%Y-%m-%d")
        alarm = date + timedelta(days=2)
        hour = datetime.now()
        hour = datetime.strftime(hour,"%X")
        
        issue = "La reproductora {} acaba de tener sus bebes, recuerda vacunar con hierro sus lechones".format(ID_FEMALE['ID_FEMALE'])
        
        alarm = "INSERT INTO  Alarm(employee, DATE, hour, issue) VALUES ({}, '{}', '{}', '{}')".format(id_Employee[0], alarm, hour, issue)
        result_alarm = self.connection.insert(alarm)
        if(result_alarm):
            
            idAlarm = "SELECT MAX(ID_ALARM) FROM Alarm"
            result_idAlarm = self.connection.count(idAlarm)
            query = """INSERT INTO  Birth(ID_FEMALE,idMale,DATE_BIRTH, noBabies, noMummy, noDead, idAlarm) VALUES 
                ({}, {},'{}', {}, {}, {}, {})""".format(ID_FEMALE['ID_FEMALE'], idMale['idMale'], DATE_BIRTH['DATE_BIRTH'], noBabies['noBabies'], noMummy['noMummy'], noDead['noDead'], result_idAlarm[0])
            return self.connection.insert(query)
        else:
            return jsonify({'status': 400})