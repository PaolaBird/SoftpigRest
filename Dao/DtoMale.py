from DtoPig import Pig

class Male(Pig):
    _idMale = ""
    _conformacionFisica =""

    def __init__ (self, idMale, conformacionFisica, sex, weigth, idRace, growthPhase, pigState, health, idInstalation, birthDate, acquisitionDate):
        Pig.__init__(self, idMale, sex, weigth,idRace,growthPhase,pigState,health,idInstalation,birthDate,acquisitionDate)
        self._idMale = idMale
        self._conformacionFisica = conformacionFisica

    def getIdMale (self):
        return self._idMale

    def getConformacionFisica (self):
        return self._conformacionFisica
