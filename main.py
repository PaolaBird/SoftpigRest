from flask import Flask
import os
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
from Controllers.data import *
from Controllers.login import *

app = Flask(__name__)
api = Api(app)


#Routes 

#login
api.add_resource(Login, '/api')

#Data bashboard
api.add_resource(Dasboard, '/api/dasboard')

#Pig
api.add_resource(GetPigs, '/api/pig_list')
api.add_resource(InactivatePig, '/api/inactivate_pig/<int:id>')

#Races
api.add_resource(GetRaces, '/api/race_list')

#Articles
api.add_resource(GetArticle, '/api/article_list') #Para la visualización de los empleados administrativos, y administrador
api.add_resource(GetArticlesPerson, '/api/article-person_list/<int:id>')
api.add_resource(AddArticle, '/api/add_aritcle-employee')
api.add_resource(RemoveArticle, '/api/remove_article')

#Persons
api.add_resource(GetEmployee, '/api/employee_list')
api.add_resource(AddHoursWorked, '/api/hours_employee')
api.add_resource(ChangeState, '/api/change_state')

#Female
api.add_resource(GetFemale, '/api/female_list')
api.add_resource(RemoveFemale, '/api/remove_female/<int:id>')

#Installations
api.add_resource(GetInstallation, '/api/installation_list')

#Males
api.add_resource(GetMale, '/api/male_list')
api.add_resource(RemoveMale, '/api/remove_male/<int:id>')

#Terceraa nota, partos
api.add_resource(GetBirth, '/api/birth_list/<int:id>')

#Tercera entrega
api.add_resource(GetHeat, '/api/heat_list/<int:id>')


api.add_resource(GetMedicine, '/api/medicine_list/<int:id>')
api.add_resource(SearchMedicine, '/api/search_medicine/<int:id>')

api.add_resource(GetPeriodGestation, '/api/period_gestation_list/<int:id>/<int:person>')

#Alarms  (Ultima entrega)
api.add_resource(GetAlarms, '/api/alarm_list/<int:id>')
api.add_resource(SearchAlarms, '/api/search_alarm/<int:id>')
api.add_resource(AddAlarm, '/api/add_alarm')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)