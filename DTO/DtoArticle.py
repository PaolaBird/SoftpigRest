class Article():
    
    _idArticle = ""
    _typeArticle = ""
    _name = ""
    _quantity = 0

    def __init__ (self,idArticle, typeArticle, name, quantity):
        
        self._idArticle = idArticle
        self._typeArticle = typeArticle
        self._name = name
        self._quantity = quantity
        
    def getIdArticle (self):
        return self._idArticle
    
    def getTypeArticle (self):
        return self._typeArticle
    
    def getName (self):
        return self._name
    
    def getQuantity (self):
        return self._quantity