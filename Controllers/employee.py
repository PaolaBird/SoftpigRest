from flask_restful import Resource, request, reqparse
from Config.DbConfig import DbConfig
from flask import jsonify
import datetime as time
from datetime import datetime

class GetEmployee(Resource):
    
    connection = DbConfig()
    
    def get(self):
        hoy = time.date.today()
        update = "UPDATE Person SET dateAdmission='{}' WHERE dateAdmission IS NULL".format(hoy)
        self.connection.update(update)
        query = """SELECT NO_EMPLOYEE, state, contract, hoursWorked, dateAdmission, dateOff, salary, document, 
        firstName, secondName, fatherLastName, motherLastName, sex, email, phone, celPhone, RoleCat.role AS role, InstalationCat.name AS instalation 
        FROM Person
        INNER JOIN InstalationCat ON ID_INSTALATION = Person.idInstalation
        INNER JOIN RoleCat ON ID_ROLE = Person.idRole"""
        
        employees = []
        result = self.connection.read(query)
        for employee in result:
            if (employee[5] is None):
                employees.append({'id': employee[0],
                              'state': employee[1], 
                              'contract':employee[2], 
                              'hoursWorked':employee[3], 
                              'dateAdmission': datetime.strftime(employee[4], '%d/%m/%Y'), 
                              'dateOff':"00/00/0000", 
                              'salary':employee[6], 
                              'document': employee[7],
                              'firstName': employee[8],
                              'secondName': employee[9],
                              'fatherLastName': employee[10],
                              'motherLastName': employee[11],
                              'sex': employee[12],
                              'email': employee[13],
                              'phone': employee[14],
                              'celPhone': employee[15],
                              'role': employee[16],
                              'instalation': employee[17]})
            else:
                employees.append({'id': employee[0],
                              'state': employee[1], 
                              'contract':employee[2], 
                              'hoursWorked':employee[3], 
                              'dateAdmission': datetime.strftime(employee[4], '%d/%m/%Y'), 
                              'dateOff':datetime.strftime(employee[5], '%d/%m/%Y'), 
                              'salary':employee[6], 
                              'document': employee[7],
                              'firstName': employee[8],
                              'secondName': employee[9],
                              'fatherLastName': employee[10],
                              'motherLastName': employee[11],
                              'sex': employee[12],
                              'email': employee[13],
                              'phone': employee[14],
                              'celPhone': employee[15],
                              'role': employee[16],
                              'instalation': employee[17]})
        
        return jsonify({'employees': employees})
    
class AddHoursWorked(Resource):
    connection = DbConfig()
    
    def put (self):
        person = request.get_json('person') 
        hours = request.get_json('hours')
        salary = int (hours['hours']) * 3450
        query = """UPDATE Person SET hoursWorked={}, salary={} WHERE NO_EMPLOYEE = {}""".format(hours['hours'],salary, person['person'])
        return self.connection.update(query)
    
class ChangeState(Resource):
    connection = DbConfig()
    def put (self):
        person = request.get_json('id') 
        state = request.get_json('state')
        if(state['state'] == "Despedido"):
            hoy = time.date.today()
            update = "UPDATE Person SET dateOff='{}', state='{}' WHERE NO_EMPLOYEE = {}".format(hoy, state['state'], person['id'])
            return self.connection.update(update)
        else:
            query = """ UPDATE Person SET state='{}' WHERE NO_EMPLOYEE = {}""".format(state['state'], person['id'])
            return self.connection.update(query)
       

        
    