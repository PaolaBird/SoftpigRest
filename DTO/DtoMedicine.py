class Medicine():
    
    _idMedicine = ""
    _typeMedicine = ""
    _name = ""
    _quantity = 0

    def __init__(self, idMedicine, typeMedicine, name, quantity):
        self._idMedicine = idMedicine
        self._typeMedicine = typeMedicine
        self._name = name
        self._quantity = quantity

    def getIdMedicine (self):
        return self._idMedicine

    def getTypeMedicine (self):
        return self._typeMedicine

    def getName (self):
        return self._name

    def getQuantity (self):
        return self._quantity