from DtoPig import Pig

class Female (Pig):
    _idFemale = ""
    _virgin = ""
    _gestation = ""

    def __init__ (self, idFemale, virgin, gestation, sex, weigth, idRace, growthPhase, pigState, health, idInstalation,  birth,  acquisition):
        Pig.__init__(self, idFemale, sex, weigth, idRace, growthPhase, pigState,  health, idInstalation,  birth,  acquisition)
        self._idFemale = idFemale
        self._virgin = virgin
        self._gestation = gestation

    def getIdFemale (self):
        return self._idFemale

    def isVirgin (self): 
        return self._virgin

    def isGestation (self):
        return self._gestation