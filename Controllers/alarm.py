from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify
from datetime import datetime

class Alarms(Resource):
    
    connection = DbConfig()
    
    def get(self, id):
        query = "SELECT ID_ALARM, date, hour, issue FROM Alarm WHERE employee = {}".format(id)
        alarms = [] 
        result = self.connection.read(query)
        for alarm in result:
            alarms.append({'id': alarm[0],'date': str(alarm[1]),'hour': str(alarm[2]), 'issue': alarm[3]})
        
        return jsonify({'alarms': alarms})
    
    def post(self):
        id_Employee = request.get_json('id_Employee') 
        date = request.get_json('date') 
        hour = request.get_json('hour')
        issue = request.get_json('issue')
        query = "INSERT INTO  Alarm(employee, DATE, hour, issue) VALUES ({}, '{}', '{}', '{}')".format(id_Employee['id_Employee'], date['date'], hour['hour'], issue['issue'])
        
        return self.connection.insert(query)
    
    def delete(self, id):
        query = "DELETE FROM Alarm WHERE ID_ALARM = {}".format(id)
        return self.connection.delete(query)
        