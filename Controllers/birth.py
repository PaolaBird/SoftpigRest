from flask_restful import Resource, request
<<<<<<< HEAD
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
=======

class GetBirth(Resource):
    
    def get(self):
        return "ok, soy el get de birth", 200
    
class SearchBirth(Resource):
    def get(self, id):
        respuesta = "{} ok, soy el get de SearchBirth". format(id)
        return respuesta, 200
    
    def put (self, id):
        # este tendra al parecido a esto: 
        """ form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400

        return 'ok', 200
        https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
        """
        respuesta = "{} ok, soy el put de Searchbirth". format(id)
        return respuesta, 200
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
