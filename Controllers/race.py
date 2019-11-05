from flask_restful import Resource
from Config.DbConfig import DbConfig
<<<<<<< HEAD
from flask import jsonify
=======
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a

class GetRaces(Resource):
    
    connection = DbConfig()
    
    def get(self):
<<<<<<< HEAD
                
        query = "SELECT * FROM RaceCat"
        races = [] 
        result = self.connection.read(query)
        for race in result:
            races.append({'id': race[0],'name': race[1],'description': race[2]})
        
        return jsonify({'races': races})
=======
        query = "SELECT * FROM RaceCat"
        return self.connection.read(query)
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
