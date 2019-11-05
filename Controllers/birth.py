from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify

class GetBirth(Resource):
    
    connection = DbConfig()
    
    def get(self, id):
        query = "SELECT ID_BIRTH, idMale, DATE_BIRTH, noBabies, noMummy, noDead FROM Birth WHERE ID_FEMALE = {}".format(id)
        births = [] 
        result = self.connection.read(query) #La alarma sirve para poner las vacunas a los cerdos
        for birth in result:
            births.append({'id': birth[0],'male': birth[1],'date': birth[2],'babies': birth[3],'mummy': birth[4],'dead': birth[5]})
        
        return jsonify({'births': births})