class Employee():
    
    _idEmployee = ""
    _role = ""
    _status = ""
    _admissionDate = ""
    _document = ""
    _gender = ""
    _firstName = ""
    _secondName = ""
    _lastName = ""
    _motherLastName = ""
    _email = ""
    _telephone = ""
    _mobile = ""

    def __init__ (self, idEmployee, role, status, admissionDate, document, gender, firstName, secondName, lastName, motherLastName, email, telephone, mobile):
        
        self._idEmployee = idEmployee
        self._role = role
        self._status = status
        self._admissionDate = admissionDate
        self._document = document
        self._gender = gender
        self._firstName = firstName
        self._secondName = secondName
        self._lastName = lastName
        self._motherLastName = motherLastName
        self._email = email
        self._telephone = telephone
        self._mobile = mobile

    def getIdEmployee (self):
        return self._idEmployee

    def getRole (self):
        return self._role
    
    def getStatus (self):
        return self._status
    
    def getAdmissionDate (self):
        return self._admissionDate
    
    def getDocument (self):
        return self._document
    
    def getGender (self):
        return self._gender
    
    def getFirstName (self):
        return self._firstName
    
    def getSecondName (self):
        return self._secondName
    
    def getLastName (self):
        return self._lastName

    def getMotherLastName (self):
        return self._motherLastName
    
    def getEmail (self):
        return self._email
    

    def getTelephone(self):
        return self._telephone
    

    def getMobile (self):
        return self._mobile
    