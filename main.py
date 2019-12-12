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
from Controllers.reports import *

app = Flask(__name__)
api = Api(app)


#Routes 

#login
api.add_resource(Login, '/api')

#Data bashboards
api.add_resource(Dasboard, '/api/dasboard')
api.add_resource(FemaleData, '/api/female_data/<int:id>')
api.add_resource(ReportData, '/api/report_data')

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
api.add_resource(TypeArticle, '/api/tool_type')

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
api.add_resource(ExamsMale, '/api/male_exam_list/<int:id>', '/api/report_exam')

#Heat
api.add_resource(Heat, '/api/heat_list/<int:id>', '/api/add_heat')

#birth
api.add_resource(Birth, '/api/birth_list/<int:id>','/api/add_birth')

#Medicine
api.add_resource(Medicine, '/api/medicine_list/<int:id>', '/api/add_medicine')
api.add_resource(GetInventoryMedicine, '/api/inventary_medicine', '/api/remove_medicine/<int:id>')

#gestation
api.add_resource(Gestation, '/api/period_gestation_list/<int:id>', '/api/add_gestation')

#Alarms
api.add_resource(Alarms, '/api/alarm_list/<int:id>','/api/add_alarm', '/api/remove_alarm/<int:id>')

#Reports
api.add_resource(GetGeneralReport, '/api/general_report')
api.add_resource(GetFertilityReport, '/api/fertility_report')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)