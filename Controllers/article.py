<<<<<<< HEAD
from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify, json
=======
from flask_restful import Resource
from Config.DbConfig import DbConfig
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a

class GetArticle(Resource):
    
    connection = DbConfig()
    
    def get(self):
<<<<<<< HEAD
        query = "SELECT ID_ARTICLE, TypeArticleCat.typeArticle AS typeArticle, quantity, available, loan FROM Article INNER JOIN TypeArticleCat ON ID_TYPE_ARTICLE = Article.idType"
        articles = [] 
        result = self.connection.read(query)
        for article in result:
            articles.append({'id': article[0],'name': article[1],'type': article[2],'quantity': article[3],'available': article[4],'loan': article[5]})
        
        return jsonify({'articles': articles})
=======
        query = "SELECT ID_ARTICLE, typearticlecat.typeArticle AS typeArticle, quantity, available, loan FROM Article INNER JOIN typearticlecat ON ID_TYPE_ARTICLE = article.idType"
        return self.connection.read(query)
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
        
class GetArticlesPerson(Resource):
    connection = DbConfig()
    
    def get(self, id):
<<<<<<< HEAD
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
        
=======
        query = "SELECT ID_ARTICLE_PERSON, borrowedCopies, article.name AS name FROM articleperson INNER JOIN article ON ID_ARTICLE = articleperson.idArticle WHERE idPerson = {}".format(id)
        return self.connection.read(query) 
    
class AddArticle(Resource):
     def get(self):
        return "INSERT INTO  articleperson (ID_ARTICLE_PERSON, idArticle, idPerson, borrowedCopies, lastUpdate) VALUES ({},{},{})". format("01",id_employee,issue)
>>>>>>> 23320b92dd5462b0fe807ff61d229ab756c0c17a
