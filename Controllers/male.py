from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify

class GetMale(Resource):
    
    connection = DbConfig()
    
    def get(self):
        update = "UPDATE Male SET state='Asignado' WHERE state IS NULL"
        print(self.connection.update(update))
        query = """SELECT ID_MALE, physicalConformation 
                        FROM Male WHERE state = 'Asignado' OR state is NULL 
                        """
        males = [] 
        result = self.connection.read(query)
        for male in result:
            males.append({'id': male[0],'conformation': male[1]})
        
        return jsonify({'males': males})
        
class RemoveMale(Resource):
    connection = DbConfig()
    
    def put (self, id):
        query = """UPDATE Male SET state='{}' WHERE ID_MALE = {}""".format('Baja',id)
        return self.connection.update(query)
