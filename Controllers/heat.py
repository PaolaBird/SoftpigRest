from flask_restful import Resource, request
<<<<<<< HEAD
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
    
=======

class GetHeat(Resource):
    
    def get(self):
        return "ok, soy el get de Heat", 200
    
class SearchHeat(Resource):
    def get(self, id):
        respuesta = "{} ok, soy el get de SearchHeat". format(id)
        return respuesta, 200
    
    def put (self, id):
        # este tendra al parecido a esto: 
        """ form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400

        return 'ok', 200
        https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
        """
        respuesta = "{} ok, soy el put de SearchHeat". format(id)
        return respuesta, 200
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
