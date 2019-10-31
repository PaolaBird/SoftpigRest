from flask_restful import Resource, request
from Config.DbConfig import DbConfig

class GetPigs(Resource):
    
    connection = DbConfig()
    
    def get(self):
        query = """SELECT ID_PIG, sex, weigth, RaceCat.race AS race, growthPhase, pigStage, health, InstalationCat.name AS instalation, birthDate, acquisitionDate 
     				FROM Pig
     				INNER JOIN RaceCat 	   ON ID_RACE = Pig.idRace
     				INNER JOIN InstalationCat ON ID_INSTALATION = Pig.idInstalation"""
        return self.connection.read(query)
    
class InactivatePig(Resource): 
    
    connection = DbConfig()
       
    def put (self, id):
        query = """UPDATE Pig SET state='{}' WHERE ID_PIG = {}""".format('De Baja',id)
        return self.connection.update(query)