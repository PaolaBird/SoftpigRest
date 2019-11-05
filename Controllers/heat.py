from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify

class GetHeat(Resource):
    
    connection = DbConfig()
    
    def get(self, id):
        query = "SELECT ID_PERIOD_HEAT, typeMating, sincrony, DATE_START, dateEnd FROM PeriodHeat WHERE ID_FEMALE = {}".format(id)
        heats = [] 
        result = self.connection.read(query)
        for heat in result:
            heats.append({'id': heat[0],'type': heat[1],'sincrony': heat[2],'dateStart': heat[3],'dateEnd': heat[4]})
        
        return jsonify({'heats': heats})
    
