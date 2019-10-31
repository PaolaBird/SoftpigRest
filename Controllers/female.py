from flask_restful import Resource, request
from Config.DbConfig import DbConfig

class GetFemale(Resource):
    
    connection = DbConfig()
    
    def get(self):
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