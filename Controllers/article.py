from flask_restful import Resource
from Config.DbConfig import DbConfig

class GetArticle(Resource):
    
    connection = DbConfig()
    
    def get(self):
        query = "SELECT ID_ARTICLE, typearticlecat.typeArticle AS typeArticle, quantity, available, loan FROM Article INNER JOIN typearticlecat ON ID_TYPE_ARTICLE = article.idType"
        return self.connection.read(query)
        
class GetArticlesPerson(Resource):
    connection = DbConfig()
    
    def get(self, id):
        query = "SELECT ID_ARTICLE_PERSON, borrowedCopies, article.name AS name FROM articleperson INNER JOIN article ON ID_ARTICLE = articleperson.idArticle WHERE idPerson = {}".format(id)
        return self.connection.read(query) 
    
class AddArticle(Resource):
     def get(self):
        return "INSERT INTO  articleperson (ID_ARTICLE_PERSON, idArticle, idPerson, borrowedCopies, lastUpdate) VALUES ({},{},{})". format("01",id_employee,issue)