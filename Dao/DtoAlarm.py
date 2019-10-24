class Alarm():
    
    _idAlarm = ""
    _idEmployee = ""
    _dateStart = ""
    _issue = ""

    def __init__(self, idAlarm, idEmployee, dateStart, issue):
        self._idAlarm = idAlarm
        self._idEmployee = idEmployee
        self._dateStart = dateStart
        self._issue = issue
        
    def getIdAlarm (self):
        return self._idAlarm
    
    def getIdEmployee (self):
        return self._idEmployee

    def getDateStart (self):
        return self._dateStart
    
    def getIssue (self):
        return self._issue
    
    def newAlarm():