from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify

class GetFemale(Resource):
    
    connection = DbConfig()
    
    def get(self):
        update = "UPDATE Female SET state='Asignada' WHERE state IS NULL"
        self.connection.update(update)
        query = "SELECT ID_FEMALE, virgin, gestation, state FROM Female WHERE state = 'Asignada' OR state is NULL"
        females = [] 
        result = self.connection.read(query)
        for female in result:
            females.append({'id': female[0],'virgin': female[1],'gestation': female[2], 'state': female[3]})
        
        return jsonify({'females': females})
        #return result
    
class RemoveFemale(Resource):
    connection = DbConfig()
    
    def put (self, id):
        query = """UPDATE Female SET state='{}' WHERE ID_FEMALE = {}""".format('Baja',id)
        #return self.connection.update(query)
