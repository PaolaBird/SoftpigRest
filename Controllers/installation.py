from flask_restful import Resource, request
from Config.DbConfig import DbConfig

class GetInstallation(Resource):
    
    connection = DbConfig()
    
    def get(self):
        query = "SELECT * FROM instalationcat"
        return self.connection.read(query)
    
class SearchInstallation(Resource):
    def get(self, id):
        respuesta = "{} ok, soy el get de SearchInstallation". format(id)
        return respuesta, 200
    
    def put (self, id):
        # este tendra al parecido a esto: 
        """ form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400

        return 'ok', 200
        https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
        """
        respuesta = "{} ok, soy el put de SearchInstallation". format(id)
        return respuesta, 200