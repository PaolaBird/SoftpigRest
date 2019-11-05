<<<<<<< HEAD
from flask_restful import Resource, request, reqparse
from Config.DbConfig import DbConfig
from flask import jsonify
=======
from flask_restful import Resource, request
from Config.DbConfig import DbConfig
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a

class GetEmployee(Resource):
    
    connection = DbConfig()
    
    def get(self):
<<<<<<< HEAD
        query = """SELECT NO_EMPLOYEE, state, contract, hoursWorked, dateAdmission, dateOff, salary, document, 
        firstName, secondName, fatherLastName, motherLastName, sex, email, phone, celPhone, RoleCat.role AS role, InstalationCat.name AS instalation 
        FROM Person
        INNER JOIN InstalationCat ON ID_INSTALATION = Person.idInstalation
        INNER JOIN RoleCat ON ID_ROLE = Person.idRole"""
        
        employees = [] 
        result = self.connection.read(query)
        for employee in result:
            employees.append({'id': employee[0],
                              'state': employee[1], 
                              'contract':employee[2], 
                              'hoursWorked':employee[3], 
                              'dateAdmission':employee[4], 
                              'dateOff':employee[5], 
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
        #return result
    
class AddHoursWorked(Resource):
    connection = DbConfig()
    
    def put (self, person, hours):
        
        salary = hours * 27604
        query = """UPDATE Person SET hoursWorked={}, salary={} WHERE NO_EMPLOYEE = {}""".format(hours,salary, person)
        return self.connection.update(query)
=======
        query = "SELECT *FROM person"
        return self.connection.read(query)
    
class SearchEmployee(Resource):
    
    def put (self, id):
        # este tendra al parecido a esto: 
        """ form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400

        return 'ok', 200
        https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
        """
        respuesta = "{} ok, soy el put de SearchEmployee". format(id)
        return respuesta, 200
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
