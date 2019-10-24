class Heat():
    
    _idHeat = ""
    _idFemale = ""
    _typeMating = ""
    _sincrony = ""
    _dateStart = ""
    _dateEnd = ""

    def __init__ (self, idHeat, idFemale, typeMating, sincrony, dateStart, dateEnd):
        
        self._idHeat = idHeat
        self._idFemale = idFemale
        self._typeMating = typeMating
        self._sincrony = sincrony
        self._dateStart = dateStart
        self._dateEnd = dateEnd
        

    def getIdHeat (self):
        return self._idHeat
    

    def getIdFemale (self):
        return self._idFemale

    def  getTypeMating (self):
        return self._typeMating

    def isSincrony (self):
        return self._sincrony

    def getDateStart (self):
        return self._dateStart

    def getDateEnd (self):
        return self._dateEnd