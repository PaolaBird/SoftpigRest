from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify
from datetime import datetime, timedelta

class Heat(Resource):
    
    connection = DbConfig()
    
    def get(self, id):
        query = "SELECT ID_PERIOD_HEAT, typeMating, sincrony, DATE_START, dateEnd FROM PeriodHeat WHERE ID_FEMALE = {}".format(id)
        heats = [] 
        result = self.connection.read(query)
        for heat in result:
            heats.append({'id': heat[0],'type': heat[1],'sincrony': heat[2],'dateStart': datetime.strftime(heat[3], '%d/%m/%Y'),'dateEnd': datetime.strftime(heat[4], '%d/%m/%Y')})
        
        return jsonify({'heats': heats})
    
    def post(self):
        ID_FEMALE = request.get_json('ID_FEMALE') 
        typeMating = request.get_json('typeMating')
        sincrony = request.get_json('sincrony')
        DATE_START = request.get_json('DATE_START')
        dateEnd = request.get_json('dateEnd')
        
        id_Employee = self.connection.employee("SELECT NO_EMPLOYEE FROM Person WHERE idInstalation = 09")
        
        date = datetime.strptime(DATE_START['DATE_START'], "%Y-%m-%d")
        
        issue = "La hembra {} esta en periodo de celo, han pasado 12 horas desde su ultima revisión".format(ID_FEMALE['ID_FEMALE'])
        
        if(typeMating['typeMating'] == 'Inseminacion'):
            hour = datetime.now()
            hour = datetime.strftime(hour,"%X")
            alarm = date + timedelta(days=1)  
            query_alarm = "INSERT INTO  Alarm(employee, date, hour, issue) VALUES ({},'{}', '{}', '{}')".format(id_Employee[0], alarm, hour, issue)
        else:
            alarm = date + timedelta(hours=12)
            hours_obj = datetime.now()
            hours_obj = hours_obj + timedelta(hours=12)
            hours = datetime.strftime(hours_obj,"%X")
            query_alarm = "INSERT INTO  Alarm(employee, date, hour, issue) VALUES ({},'{}', '{}', '{}')".format(id_Employee[0], alarm, hours, issue)
        
        result_alarm = self.connection.insert(query_alarm)
        if(result_alarm):
            idAlarm = "SELECT MAX(ID_ALARM) FROM Alarm"
            result_idAlarm = self.connection.count(idAlarm)
            query = """INSERT INTO  PeriodHeat(ID_FEMALE, typeMating, sincrony, DATE_START, dateEnd, idAlarm) VALUES ({},'{}','{}','{}','{}', {})""".format(ID_FEMALE['ID_FEMALE'],typeMating['typeMating'],sincrony['sincrony'],DATE_START['DATE_START'],dateEnd['dateEnd'], result_idAlarm[0])
            return self.connection.insert(query)
            
        else:
            return jsonify({'status': 400})
