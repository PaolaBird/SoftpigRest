from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify

class Medicine(Resource):
    
    connection = DbConfig()
    
    def get(self, id):
        query = "SELECT ID_MEDICINE, DATE, applied FROM MedicinePig WHERE ID_PIG = {}".format(id)
        medicines = [] 
        result = self.connection.read(query)
        for medicine in result:
            medicines.append({'id': medicine[0],'date': medicine[1],'applied': medicine[2]})
        
        return jsonify({'medicines': medicines})
    
    def post(self):
        ID_MEDICINE = request.get_json('ID_MEDICINE')
        ID_PIG = request.get_json('ID_PIG') 
        date = request.get_json('date')
        applied = request.get_json('applied')
        query = "INSERT INTO  MedicinePig(ID_MEDICINE,ID_PIG, DATE, applied) VALUES ({},{},'{}','{}')".format(ID_MEDICINE['ID_MEDICINE'],ID_PIG['ID_PIG'], date['date'], applied['applied'])
        return self.connection.insert(query)
    
class GetInventoryMedicine(Resource):
    connection = DbConfig()
    
    def get(self):
        query = """SELECT ID_MEDICINE, TypeMedicineCat.typeMedicine AS typeMedicine, name, quantity FROM MedicineCat
                    INNER JOIN TypeMedicineCat ON ID_TYPE_MEDICINE = MedicineCat.idTypeMedicine
                    WHERE quantity > 0"""
                    
        inventary = []
        result = self.connection.read(query)
        for medicine in result:
            inventary.append({'id': medicine[0], 'type': medicine[1], 'name': medicine[2], 'quantity': medicine[3]})
        return jsonify({'medicines': inventary})
    
    def put(self, id): 
        query = "UPDATE MedicineCat SET quantity=0 WHERE ID_MEDICINE = {}".format(id)
        return self.connection.update(query)