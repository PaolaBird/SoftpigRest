from flask_restful import Resource
from Config.DbConfig import DbConfig
from flask import jsonify

class GetInstallation(Resource):
    
    connection = DbConfig()
    
    def get(self):
        query = "SELECT ID_INSTALATION, TypeInstalationCat.typeInstalation AS typeInstalation, name, capacity FROM InstalationCat INNER JOIN TypeInstalationCat ON ID_TYPE_INSTALATION = InstalationCat.idtypeInstalation"
        installations = [] 
        result = self.connection.read(query)
        for installation in result:
            installations.append({'id': installation[0],'type': installation[1],'name': installation[2],'capacity': installation[3]})
        
        return jsonify({'installations': installations})
