class Race ():
    
    _idRace = ""
    _race = ""
    _description = ""

    def __init__(self, idRace, race, description):
        self._idRace = idRace
        self._race = race
        self._description = description

    def getIdRace (self):
        return self._idRace

    def getRace (self):
        return self._race

    def getDescription (self):
        return self._description