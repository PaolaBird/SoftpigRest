from flask_restful import Resource, request

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