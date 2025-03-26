class Payroll:
    def __init__(self):
        FINAL_NUM_ASTRONAUTS = 7
        self.astronautId = [5658845, 4520125, 7895122, 8777541, 8451277, 1302850, 7580489]
        self.hours = [0] * FINAL_NUM_ASTRONAUTS
        self.payRate = [0] * FINAL_NUM_ASTRONAUTS
        self.grossPay = [0] * FINAL_NUM_ASTRONAUTS
    
    def getGrossPay(self, i):
        return self.payRate[i] * self.hours[i]
    def setAstronautIdAt(self, i, id):
        self.astronautId[i] = id
    def setHoursAt(self, i, h):
        self.hours[i] = h
    def setPayRate(self, i, p):
        self.payRate[i] = p
    def getAstronautIDAt(self, i):
        return self.astronautId[i]
    def getHoursAt(self, i):
        return self.hours[i]
    def getPayRateAt(self, i):
        return self.payRate[i]
    def getFinal(self):
        return 7