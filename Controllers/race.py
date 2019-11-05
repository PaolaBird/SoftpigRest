from flask_restful import Resource
from Config.DbConfig import DbConfig
from flask import jsonify

class GetRaces(Resource):
    
    connection = DbConfig()
    
    def get(self):
                
        query = "SELECT * FROM RaceCat"
        races = [] 
        result = self.connection.read(query)
        for race in result:
            races.append({'id': race[0],'name': race[1],'description': race[2]})
        
        return jsonify({'races': races})
