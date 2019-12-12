from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify
from datetime import datetime, timedelta

class Gestation(Resource):
    
    connection = DbConfig()
    
    def get(self, id):
        query = "SELECT ID_PERIOD_GESTATION, idMale, DATE_START FROM PeriodGestation WHERE ID_FEMALE = {}".format(id)
        gestations = [] 
        result = self.connection.read(query)
        for gestation in result:
            gestations.append({'id': gestation[0],'male': gestation[1],'date_start': datetime.strftime(gestation[2], '%d/%m/%Y')})
        
        return jsonify({'gestations': gestations})
    
    def post(self):
        ID_FEMALE = request.get_json('ID_FEMALE')
        idMale = request.get_json('idMale')
        DATE_START = request.get_json('DATE_START')
        
        id_Employee = self.connection.employee("SELECT NO_EMPLOYEE FROM Person WHERE idInstalation = 03")
        
        date = datetime.strptime(DATE_START['DATE_START'], "%Y-%m-%d")
        alarm = date + timedelta(days=113)
        hour = datetime.now()
        hour = datetime.strftime(hour,"%X")
        
        issue = "En aproximadamente 1 dia la reproductora {} tendrá sus bebes, revisala".format(ID_FEMALE['ID_FEMALE'])
        
        alarm = "INSERT INTO  Alarm(employee, DATE, hour, issue) VALUES ({}, '{}', '{}', '{}')".format(id_Employee[0], alarm, hour, issue)
        result_alarm = self.connection.insert(alarm)
        if(result_alarm):
            
            idAlarm = "SELECT MAX(ID_ALARM) FROM Alarm"
            result_idAlarm = self.connection.count(idAlarm)
            query = """INSERT INTO PeriodGestation (ID_FEMALE, idMale, DATE_START, idAlarm) 
                VALUES ({},{},'{}',{})""".format(ID_FEMALE['ID_FEMALE'], idMale['idMale'], DATE_START['DATE_START'], result_idAlarm[0])
            return self.connection.insert(query)
        
        else:
            return jsonify({'status': 400})

