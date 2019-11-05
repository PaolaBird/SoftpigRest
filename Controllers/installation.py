<<<<<<< HEAD
from flask_restful import Resource
from Config.DbConfig import DbConfig
from flask import jsonify
=======
from flask_restful import Resource, request
from Config.DbConfig import DbConfig
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a

class GetInstallation(Resource):
    
    connection = DbConfig()
    
    def get(self):
<<<<<<< HEAD
        query = "SELECT ID_INSTALATION, TypeInstalationCat.typeInstalation AS typeInstalation, name, capacity FROM InstalationCat INNER JOIN TypeInstalationCat ON ID_TYPE_INSTALATION = InstalationCat.idtypeInstalation"
        installations = [] 
        result = self.connection.read(query)
        for installation in result:
            installations.append({'id': installation[0],'type': installation[1],'name': installation[2],'capacity': installation[3]})
        
        return jsonify({'installations': installations})
=======
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
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
