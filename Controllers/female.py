from flask_restful import Resource, request
from Config.DbConfig import DbConfig
<<<<<<< HEAD
from flask import jsonify
=======
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a

class GetFemale(Resource):
    
    connection = DbConfig()
    
    def get(self):
<<<<<<< HEAD
        update = "UPDATE Female SET state='Asignada' WHERE state IS NULL"
        #self.connection.update(update)
        query = "SELECT ID_FEMALE, virgin, gestation FROM Female WHERE state = 'Asignada' OR state is NULL"
        females = [] 
        result = self.connection.read(query)
        for female in result:
            females.append({'id': female[0],'virgin': female[1],'gestation': female[2]})
        
        return jsonify({'females': females})
        #return result
    
class RemoveFemale(Resource):
    connection = DbConfig()
    
    def put (self, id):
        query = """UPDATE Female SET state='{}' WHERE ID_FEMALE = {}""".format('Baja',id)
        #return self.connection.update(query)
=======
        update = "UPDATE Female SET state='Active' WHERE state IS NULL"
        self.connection.update(update)
        query = "SELECT * FROM Female WHERE state = 'Active' OR state is NULL"
        return self.connection.read(query)
    
class SearchFemale(Resource):
    def get(self, id):
        respuesta = "{} ok, soy el get de SearchFemale". format(id)
        return respuesta, 200
    
    def put (self, id):
        # este tendra al parecido a esto: 
        """ form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400

        return 'ok', 200
        https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
        """
        respuesta = "{} ok, soy el put de SearchFemale". format(id)
        return respuesta, 200
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
