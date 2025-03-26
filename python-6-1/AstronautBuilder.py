class AstronautBuilder:
    def __init__(self, name=None, age=None, address=None, phone=None):
        self.name = name if name is not None else "Unknown"
        self.age = age if age is not None else 0
        self.address = address if address is not None else "Not Provided"
        self.phone = phone if phone is not None else "Not Provided"

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setAddress(self, address):
        self.address = address

    def setPhone(self, phone):
        self.phone = phone

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone
