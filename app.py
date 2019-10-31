from flask import Flask
from flask_restful import Api
from Controllers.pig import *
from Controllers.race import *
from Controllers.alarm import *
from Controllers.article import *
from Controllers.birth import *
from Controllers.employee import *
from Controllers.female import *
from Controllers.heat import *
from Controllers.installation import *
from Controllers.male import *
from Controllers.medicine import *
from Controllers.periodGestation import *


app = Flask(__name__)
api = Api(app)

#Routes 
#Pig
api.add_resource(GetPigs, '/api/pig_list')
api.add_resource(InactivatePig, '/api/inactivate_pig/<int:id>', methods=['PUT']) #Sin funcionar aun

#Races
api.add_resource(GetRaces, '/api/race_list')

#Articles
api.add_resource(GetArticle, '/api/article_list') #Para la visualización de los empleados administrativos, y administrador
api.add_resource(GetArticlesPerson, '/api/article-person_list/<int:id>')
api.add_resource(AddArticle, '/api/add_aritcle-employee')

#Terceraa nota, partos
api.add_resource(GetBirth, '/api/birth_list/<int:id>')
api.add_resource(SearchBirth, '/api/search_birth/<int:id>')

#Persons
api.add_resource(GetEmployee, '/api/employee_list')
api.add_resource(SearchEmployee, '/api/search_employee/<int:id>')

#Female
api.add_resource(GetFemale, '/api/female_list')
api.add_resource(SearchFemale, '/api/search_female/<int:id>')

#Tercera entrega
api.add_resource(GetHeat, '/api/heat_list/<int:id>')
api.add_resource(SearchHeat, '/api/search_heat/<int:id>')

#Installations
api.add_resource(GetInstallation, '/api/installation_list')
api.add_resource(SearchInstallation, '/api/search_installation/<int:id>')

#Males
api.add_resource(GetMale, '/api/male_list')
api.add_resource(SearchMale, '/api/search_male/<int:id>')

api.add_resource(GetMedicine, '/api/medicine_list/<int:id>')
api.add_resource(SearchMedicine, '/api/search_medicine/<int:id>')

api.add_resource(GetPeriodGestation, '/api/period_gestation_list/<int:id>')
api.add_resource(SearchPeriodGestation, '/api/search_period_gestation/<int:id>')

#Alarms  (Ultima entrega)
api.add_resource(GetAlarms, '/api/alarm_list/<int:id>')
api.add_resource(SearchAlarms, '/api/search_alarm/<int:id>')
api.add_resource(AddAlarm, '/api/add_alarm')


if __name__ == '__main__':
    app.run(debug=True)