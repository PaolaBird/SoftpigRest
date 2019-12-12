from flask_restful import Resource, request
from Config.DbConfig import DbConfig
from flask import jsonify, json

class GetArticle(Resource):
    
    connection = DbConfig()
    
    def get(self):
        query = "SELECT ID_ARTICLE, name, TypeArticleCat.typeArticle AS typeArticle, quantity, loan FROM Article INNER JOIN TypeArticleCat ON ID_TYPE_ARTICLE = Article.idType"
        articles = [] 
        result = self.connection.read(query)
        for article in result:
            articles.append({'id': article[0],'name': article[1],'type': article[2],'quantity': article[3], 'loan': article[4]})
        
        return jsonify({'articles': articles})
        
class GetArticlesPerson(Resource):
    connection = DbConfig()
    
    def get(self, id):
        query = """SELECT idArticle, ArticlePerson.loan, Article.name AS name, TypeArticleCat.typeArticle AS type FROM ArticlePerson 
                    INNER JOIN Article ON ID_ARTICLE = ArticlePerson.idArticle 
                    INNER JOIN TypeArticleCat ON ID_TYPE_ARTICLE = Article.idType
                    WHERE idPerson = {}""".format(id)

        articles = [] 
        result = self.connection.read(query)
        for article in result:
            articles.append({'id': article[0], 'loan': article[1], 'name': article[2], 'type': article[3]})
        
        return jsonify({'articles': articles})

class AddArticle(Resource):
    connection = DbConfig()
    
    def post(self):
        person = request.get_json('person') 
        article = request.get_json('article')
        loan = request.get_json('copies')
        query = "INSERT INTO  ArticlePerson (idArticle, idPerson, loan) VALUES ({},{},{})". format(article['article'],person['person'], loan['copies'])
        add_article_person = self.connection.insert(query)
        if(add_article_person):
            query_quantity = "SELECT quantity FROM Article WHERE ID_ARTICLE = {}".format(article['article'])
            result = self.connection.read(query_quantity)
            for quantity in result:
                new_quantity = quantity[0] - int (article['copies']) 
                articles = "UPDATE Article SET quantity={} WHERE ID_ARTICLE = {}".format(new_quantity,article['article'])
            return self.connection.update(articles)
        else:
            return jsonify({'status': 400})
    
class RemoveArticle(Resource):

    connection = DbConfig()
    
    def post(self):
        article = request.get_json('article')
        table = request.get_json('table')
        if(table['table'] == "Article"):
            query = "UPDATE Article SET quantity=0 WHERE ID_ARTICLE = {}".format(article['article'])
            self.connection.delete(query)
        else:
            result = self.connection.read("SELECT loan FROM ArticlePerson WHERE idArticle = {}".format(article['article']))
            global l
            for loan in result:
                l = loan[0]
            query = "DELETE FROM ArticlePerson WHERE idArticle = {}".format(article['article'])
            delete_article_person = self.connection.delete(query)
            if (delete_article_person):
                query_quantity = "SELECT quantity FROM Article WHERE ID_ARTICLE = {}".format(article['article'])
                result_quantity = self.connection.read(query_quantity)
                for result_quantity in result:
                    q = result_quantity[0]
                quantity_db = l + q
                articles = "UPDATE Article SET quantity={} WHERE ID_ARTICLE = {}".format(quantity_db,article['article'])
                return self.connection.update(articles)    
            else:
                return jsonify({'status': 400})
    
class TypeArticle(Resource):
    connection = DbConfig()
    
    def get(self):
        query = "SELECT ID_TYPE_ARTICLE, typeArticle FROM TypeArticleCat"
        articles = []
        result = self.connection.read(query)
        for article in result:
           articles .append({'id': article[0], 'type':article[1]})
        
        return jsonify({'articles_Type': articles})