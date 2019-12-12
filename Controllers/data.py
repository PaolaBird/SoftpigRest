from flask_restful import Resource
from Config.DbConfig import DbConfig
from flask import jsonify
from datetime import datetime

class Dasboard(Resource):
    connection = DbConfig()
    def get (self):
        try:
            dashboardData = [] 
            null_result = 0
            
            administrativos = self.connection.count("SELECT COUNT(*) FROM Person WHERE idRole = 10")
            
            if(administrativos):
                dashboardData.append({'administrativos': administrativos[0]})
            else:
                dashboardData.append({'administrativos': null_result})
    
            operativos = self.connection.count("SELECT COUNT(*) FROM Person WHERE idRole = 11")
            
            if(operativos):
                dashboardData.append({'operativos': operativos[0]})
            else:
                dashboardData.append({'operativos': null_result})
                
            articles = self.connection.count("SELECT COUNT(*) FROM Article WHERE quantity > 0")
            if articles:
                dashboardData.append({'items_inventory':articles[0]})
            else:
                dashboardData.append({'items_inventory':null_result})
                
            article_person = self.connection.count("SELECT COUNT(*) FROM ArticlePerson group by idPerson")
            
            if article_person:
                dashboardData.append({'article_person': article_person[0]})
            else:
                dashboardData.append({'article_person': null_result})
            
            installations = self.connection.count("SELECT COUNT(*) FROM InstalationCat")
            
            if (installations):
                dashboardData.append({'number_installations': installations[0]})
            else:
                dashboardData.append({'number_installations': null_result})
                
            typeInstallation = self.connection.count("SELECT COUNT(*) FROM TypeInstalationCat")
            
            if typeInstallation:
                dashboardData.append({'installations_type': typeInstallation[0]})
            else:
                dashboardData.append({'installations_type': null_result})
           
            return jsonify({'dashboard': dashboardData})
        except:
            return jsonify ({'status': 400})
               
class FemaleData(Resource):
    connection = DbConfig()
    
    def get(self, id):
        data_female = []
        now = datetime.now()
        heat = self.connection.count("SELECT COUNT(*) FROM PeriodHeat WHERE ID_FEMALE = {} AND year(DATE_START)={}".format(id,now.year))
        data_female.append({'heats_year': heat[0]})
        gestation = self.connection.count("SELECT COUNT(*) FROM PeriodGestation WHERE ID_FEMALE = {} AND year(DATE_START)={}".format(id,now.year))
        data_female.append({'gestation_year': gestation[0]})
        birth = self.connection.count("SELECT COUNT(*) FROM Birth WHERE ID_FEMALE = {} AND year(DATE_BIRTH)={}".format(id,now.year))
        data_female.append({'birth_year': birth[0]})
        return jsonify ({'data_female': data_female})
    
class ReportData(Resource):
    
    connection = DbConfig()
    
    def get(self):
        
        now = datetime.now()
        
        #Data reporductora
        result_noBabies  =self.connection.count("SELECT SUM(noBabies) FROM Birth WHERE YEAR(DATE_BIRTH)= {}".format(now.year))
        result_noDead = self.connection.count("SELECT SUM(noDead) FROM Birth WHERE YEAR(DATE_BIRTH)= {}".format(now.year))
        
        data= []
        data.append({'noBabies': int(result_noBabies[0]), 
                     'noDead': int(result_noDead[0])})
        
        result_gestations = self.connection.count("SELECT COUNT(*) FROM PeriodGestation WHERE YEAR(DATE_START)= {}".format(now.year))
        result_birth = self.connection.count("SELECT COUNT(*) FROM Birth WHERE YEAR(DATE_BIRTH)= {}".format(now.year))
        
        data.append({'gestations': result_gestations[0],
                     'births': result_birth[0]})
        
        result_month = self.connection.count("SELECT COUNT(*) FROM Birth WHERE MONTH(DATE_BIRTH)= {}".format(now.month))
        result_females = self.connection.count("SELECT COUNT(*) FROM Female WHERE state='Asignada'")
        
        data.append({'month-births': result_month[0],
                     'females': result_females[0]})
        
        return jsonify({'report-data': data})
    
        