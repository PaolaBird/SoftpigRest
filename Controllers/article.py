from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify, json

class GetArticle(Resource):
    
    connection = DbConfig()
    
    def get(self):
        query = "SELECT ID_ARTICLE, name, TypeArticleCat.typeArticle AS typeArticle, quantity FROM Article INNER JOIN TypeArticleCat ON ID_TYPE_ARTICLE = Article.idType"
        articles = [] 
        result = self.connection.read(query)
        for article in result:
            articles.append({'id': article[0],'name': article[1],'type': article[2],'quantity': article[3]})
        
        return jsonify({'articles': articles})
        
class GetArticlesPerson(Resource):
    connection = DbConfig()
    
    def get(self, id):
        query = """SELECT idArticle, Article.name AS name, TypeArticleCat.typeArticle AS type FROM ArticlePerson 
                    INNER JOIN Article ON ID_ARTICLE = ArticlePerson.idArticle 
                    INNER JOIN TypeArticleCat ON ID_TYPE_ARTICLE = Article.idType
                    WHERE idPerson = {}""".format(id)

        articles = [] 
        result = self.connection.read(query)
        for article in result:
            articles.append({'id': article[0], 'name': article[1], 'type': article[2]})
        
        return jsonify({'articles': articles})

class AddArticle(Resource):
    connection = DbConfig()
    
    def post(self):
        person = request.get_json('person') 
        article = request.get_json('article')
        query = "INSERT INTO  ArticlePerson (idArticle, idPerson) VALUES ({},{})". format(article['article'],person['person'])
        return self.connection.insert(query)
    
class RemoveArticle(Resource):
    connection = DbConfig()
    
    def post(self):
        article = request.get_json('article')
        table = request.get_json('table')
        if(table['table'] == "Article"):
            query = "UPDATE Article SET quantity=0 WHERE ID_ARTICLE = {}".format(article['article'])
        else:
            query = "DELETE FROM ArticlePerson WHERE idArticle = {}".format(article['article'])
        return self.connection.delete(query)