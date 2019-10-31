from flask_restful import Resource
from Config.DbConfig import DbConfig

class GetRaces(Resource):
    
    connection = DbConfig()
    
    def get(self):
        query = "SELECT * FROM RaceCat"
        return self.connection.read(query)
