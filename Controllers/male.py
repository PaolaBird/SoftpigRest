from flask_restful import Resource, request
from Config.DbConfig import DbConfig

class GetMale(Resource):
    
    connection = DbConfig()
    
    def get(self):
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
