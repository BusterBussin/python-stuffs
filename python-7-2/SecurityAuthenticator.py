class SecurityAuthenticator:
    def __init__(self):
        self.valid = int[5658845, 4520125, 7895122, 8777541, 8451277, 1302850, 8080152, 4562555, 5552012, 5050552, 7825877, 1250255, 1005231, 6545231, 3852085, 7576651, 7881200, 4581002]
    def isValid(self, number):
            for indexNumber in range(len(self.valid)):
                 if number == self.valid[indexNumber]:
                      return True
            return False