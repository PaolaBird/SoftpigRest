from flask_restful import Resource
from Config.DbConfig import DbConfig
from flask import jsonify

class Dasboard(Resource):
    connection = DbConfig()
    def get (self):
        administrativos = "SELECT COUNT(*) FROM Person WHERE idRole = 10"
        numAdministrativos = self.connection.count(administrativos)
        dashboardData = [] 
        for admin in numAdministrativos:
            dashboardData.append({'administrativos': admin})
            
        operativos = "SELECT COUNT(*) FROM Person WHERE idRole = 11"
        numOperativos = self.connection.count(operativos)
        
        for opera in numOperativos:
            dashboardData.append({'operativos': opera})
        
        articles = "SELECT COUNT(*) FROM Article"
        numArticles = self.connection.count(articles)
        article_person = "SELECT COUNT(*) FROM ArticlePerson"
        num_article_person = self.connection.count(article_person)
        
        for person in num_article_person:
            dashboardData.append({'article_person': person})
            for article in numArticles:
                article =article-person
                dashboardData.append({'items_inventory':article})
        
        installation = "SELECT COUNT(*) FROM InstalationCat"
        numInstallations = self.connection.count(installation)
    
        for installa in numInstallations:
            dashboardData.append({'number_installations': installa})
            
        typeInstallation = "SELECT COUNT(*) FROM TypeInstalationCat"
        numTypeInstallations = self.connection.count(typeInstallation)
        for typeInstalla in numTypeInstallations:
            dashboardData.append({'installations_type': typeInstalla})
        
        return jsonify ({'dashboard': dashboardData})
    
