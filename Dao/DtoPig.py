class Pig():
    _idPig = ""
    _sex = ""
    _weigth = ""
    _idRace = ""
    _growthPhase = ""
    _pigState = ""
    _health = ""
    _idInstalation = ""
    _birthDate = ""
    _acquisitionDate = ""

    def __init__(self, idPig, sex, weigth, idRace, growthPhase, pigState, health, idInstalation, birthDate, acquisitionDate):
        self._idPig = idPig
        self._sex = sex
        self._weigth = weigth
        self._idRace = idRace
        self._growthPhase = growthPhase
        self._pigState = pigState
        self._health = health
        self._idInstalation = idInstalation
        self._birth= birthDate
        self._acquisition= acquisitionDate
 
    def getIdPig (self):
        return self._idPig
 
    def getSex (self):
        return self._sex
 
    def getWeigth (self):
        return self._weigth
 
    def getIdRace (self):
        return self._idRace
 
    def getGrowthPhase (self):
        return self._growthPhase
 
    def getPigState (self):
        return self._pigState
 
    def getHealth (self):
        return self._health
 
    def getIdInstalation (self):
        return self._idInstalation
 
    def getBirthDate (self):
        return self._birthDate
 
    def getAcquisitionDate (self):
        return self._acquisitionDate
         