class Birth():
    
    _idBirth = ""
    _idFemale = ""
    _idMale = ""
    _dataBirth = ""
    _noBabies = ""
    _noMummy = ""
    _noDead = ""

    def __init__(self,idBirth, idFemale, idMale, dataBirth, noBabies, noMummy, noDead):
       self._idBirth = idBirth
       self._idFemale = idFemale
       self._idMale = idFemale
       self._dataBirth = dataBirth
       self._noBabies = noBabies
       self._noMummy = noMummy
       self._noDead = noDead
    
    def getIdBirth (self):
        return self._idBirth

    def getIdFemale (self): 
        return self._idFemale

    def getIdMale (self):
        return self._idMale

    def getDataBirth (self):
        return self._dataBirth

    def getNoBabies (self):
        return self._noBabies

    def getNoMummy (self):
        return self._noMummy
    
    def getNoDead (self):
        return self._noDead