class PeriodGestation():
    
    _idPeriodGestation = ""
    _idFemale = ""
    _idMale = ""
    _dateStart = ""

    def __init__(self, idPeriodGestation, idFemale, idMale, dateStart):
        self._idPeriodGestation = idPeriodGestation
        self._idFemale = idFemale
        self._idMale = idMale
        self._dateStart = dateStart

    def getIdPeriodGestation (self):
        return self._idPeriodGestation

    def getIdFemale (self):
        return self._idFemale

    def getIdMale (self):
        return self._idMale

    def getDateStart (self):
        return self._dateStart