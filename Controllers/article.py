from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify, json

class GetArticle(Resource):
    
    connection = DbConfig()
    
    def get(self):
        query = "SELECT ID_ARTICLE, TypeArticleCat.typeArticle AS typeArticle, quantity, available, loan FROM Article INNER JOIN TypeArticleCat ON ID_TYPE_ARTICLE = Article.idType"
        articles = [] 
        result = self.connection.read(query)
        for article in result:
            articles.append({'id': article[0],'name': article[1],'type': article[2],'quantity': article[3],'available': article[4],'loan': article[5]})
        
        return jsonify({'articles': articles})
        
class GetArticlesPerson(Resource):
    connection = DbConfig()
    
    def get(self, id):
        query = "SELECT ID_ARTICLE_PERSON, borrowedCopies, Article.name AS name FROM ArticlePerson INNER JOIN Article ON ID_ARTICLE = ArticlePerson.idArticle WHERE idPerson = {}".format(id)
        articles = [] 
        result = self.connection.read(query)
        for article in result:
            articles.append({'id': article[0],'borrowedCopies': article[1],'name': article[2]})
        
        return jsonify({'articles': articles})

class AddArticle(Resource):
    connection = DbConfig()
    
    def post(self, id, person, copies):
        query = "INSERT INTO  ArticlePerson (idArticle, idPerson, borrowedCopies) VALUES ({},{},{})". format(id,person,copies)
        return self.connection.insert(query)
        
