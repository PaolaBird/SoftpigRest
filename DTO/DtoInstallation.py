class Insallation (self):    
    _idInstalation = ""
    _typeInstalation = ""
    _name = ""
    _capacity = ""
    
    def __init__ (self, idInstalation, typeInstalation, name, capacity):
        
       self._idInstalation = idInstalation
       self._typeInstalation = typeInstalation
       self._name = name
       self._capacity = capacity

    def getIdInstalation (self):
        return self._idInstalation

    def getTypeInstalation (self):
        return self._typeInstalation

    def getName (self):
        return self._name

    def getCapacity (self):
        return self._capacity