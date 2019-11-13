from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify
from datetime import datetime

class GetPigs(Resource):
    
    connection = DbConfig()
    
    def get(self):
        query = """SELECT ID_PIG, state, sex, weigth, RaceCat.race AS race, growthPhase, pigStage, health, InstalationCat.name AS instalation, birthDate, acquisitionDate 
     				FROM Pig
     				INNER JOIN RaceCat 	   ON ID_RACE = Pig.idRace
     				INNER JOIN InstalationCat ON ID_INSTALATION = Pig.idInstalation"""
        pigs = []
        result = self.connection.read(query)
        for pig in result:
            pigs.append({'id': pig[0],
                         'state': pig[1],
                         'sex': pig[2],
                         'weigth': pig[3],
                         'race': pig[4],
                         'growthPhase': pig[5],
                         'pigStage': pig[6],
                         'health': pig[7],
                         'installation': pig[8],
                         'birthDate': datetime.strftime(pig[9], '%d/%m/%Y'),
                         'acquisitionDate': datetime.strftime(pig[10], '%d/%m/%Y')})
            
        return jsonify({'pigs': pigs})
    
class InactivatePig(Resource): 
    
    connection = DbConfig()
       
    def put (self, id):
        query = """UPDATE Pig SET state='{}' WHERE ID_PIG = {}""".format('Baja',id)
        return self.connection.update(query)