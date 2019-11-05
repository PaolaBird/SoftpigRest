from flask_restful import Resource, request
from Config.DbConfig import DbConfig
<<<<<<< HEAD
from flask import jsonify
=======
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a

class GetMale(Resource):
    
    connection = DbConfig()
    
    def get(self):
<<<<<<< HEAD
        update = "UPDATE Male SET state='Asignado' WHERE state IS NULL"
        print(self.connection.update(update))
        query = """SELECT ID_MALE, physicalConformation 
                        FROM Male WHERE state = 'Asignado' OR state is NULL 
                        """
        males = [] 
        result = self.connection.read(query)
        for male in result:
            males.append({'id': male[0],'conformation': male[1]})
        
        return jsonify({'males': males})
        
class RemoveMale(Resource):
    connection = DbConfig()
    
    def put (self, id):
        query = """UPDATE Male SET state='{}' WHERE ID_MALE = {}""".format('Baja',id)
        return self.connection.update(query)
=======
        update = "UPDATE Male SET state='Active' WHERE state IS NULL"
        print(self.connection.update(update))
        query = "SELECT * FROM Male WHERE state = 'Active' OR state is NULL"
        return self.connection.read(query)
        
class SearchMale(Resource):
    def get(self, id):
        respuesta = "{} ok, soy el get de SearchMale". format(id)
        return respuesta, 200
    
    def put (self, id):
        # este tendra al parecido a esto: 
        """ form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400

        return 'ok', 200
        https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
        """
        respuesta = "{} ok, soy el put de SearchMale". format(id)
        return respuesta, 200
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
