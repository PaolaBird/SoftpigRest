from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify

class Login(Resource):
    
    connection = DbConfig()
    
    def post(self):
        user = request.get_json('user')
        password_form = request.get_json('password')
        query = """SELECT NO_EMPLOYEE, state, contract, hoursWorked, dateAdmission, dateOff, salary, document, 
                        firstName, secondName, fatherLastName, motherLastName, sex, email, phone, celPhone, RoleCat.role AS role, InstalationCat.name AS instalation, password
                        FROM Person
                        INNER JOIN InstalationCat ON ID_INSTALATION = Person.idInstalation
                        INNER JOIN RoleCat ON ID_ROLE = Person.idRole WHERE email = '{}' AND password = MD5({})""".format(user['user'],password_form['password'])
        result = self.connection.employee(query)
        if result:
            data = []
            data.append({'id': result[0],
                                'state': result[1], 
                                'contract':result[2], 
                                'hoursWorked':result[3], 
                                'dateAdmission':result[4], 
                                'dateOff':result[5], 
                                'salary':result[6], 
                                'document': result[7],
                                'firstName': result[8],
                                'secondName': result[9],
                                'fatherLastName': result[10],
                                'motherLastName': result[11],
                                'sex': result[12],
                                'email': result[13],
                                'phone': result[14],
                                'celPhone': result[15],
                                'role': result[16],
                                'instalation': result[17]})
            return jsonify({"employee_data":data})
        else :
            return jsonify({'state': 403})
 