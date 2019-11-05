from flask_restful import Resource, request
<<<<<<< HEAD
from Config.DbConfig import DbConfig
from flask import jsonify
import datetime

class GetPeriodGestation(Resource):
    
    connection = DbConfig()
    
    def get(self, id, person):
        hoy = datetime.datetime.utcnow()
        fecha = hoy + datetime.timedelta(days=112)
        #fecha = alarm.strftime("%x")
        #hora = alarm.strftime("%X")
        query = "SELECT ID_PERIOD_GESTATION, idMale, DATE_START FROM PeriodGestation WHERE ID_FEMALE = {}".format(id)
        issue = "En aproximadamente 2 dias la reproductora {} estará en parto, revisa su estado".format(id)
        alarm= "INSERT INTO  Alarm (date_start, issue, id_employee) VALUES ({},{},{})".format(fecha,issue, person)
        # heats = [] 
        # result = self.connection.read(query)
        # for heat in result:
        #     heats.append({'id': heat[0],'type': heat[1],'sincrony': heat[2],'dateStart': heat[3],'dateEnd': heat[4]})
        
        #return jsonify({'heats': heats})
        #print (alarm)
        return query

=======

class GetPeriodGestation(Resource):
    
    def get(self):
        return "ok, soy el get de PeriodGestation", 200
    
class SearchPeriodGestation(Resource):
    def get(self, id):
        respuesta = "{} ok, soy el get de SearchPeriodGestation". format(id)
        return respuesta, 200
    
    def put (self, id):
        # este tendra al parecido a esto: 
        """ form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400

        return 'ok', 200
        https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
        """
        respuesta = "{} ok, soy el put de SearchPeriodGestation". format(id)
        return respuesta, 200
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
