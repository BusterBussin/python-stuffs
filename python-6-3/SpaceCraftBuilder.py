import math
class SpaceCraftBuilder:
    craftName = " "
    crewCapacity = 0
    fuelCapacity = float(0)
    currentCrew = 0
    currentFuel = float(0)
    def __init__(self, craftName = None, crewCapacity = None, fuelCapacity = None):
        self.craftName = craftName
        self.crewCapacity = crewCapacity
        self.fuelCapacity = fuelCapacity
    def boardCrew(self, crewCount):
        status = bool
        if self.currentCrew + crewCount <= self.crewCapacity:
            self.currentCrew = self.currentCrew + crewCount
            status = True
            return status
        else:
            status = False
            return status
    def refuel(self, fuelAmount):
        self.currentFuel = min(self.currentFuel + fuelAmount, self.fuelCapacity)
    def launch(self, destination):
        if self.currentCrew > 0 and self.currentFuel > 0 :
            print("Spacecraft " + self.craftName + " successfully launched to " + destination + "!")
        else:
            print("Launch failed. Insufficient crew or fuel.")
    def getCurrentCrew(self):
        return self.currentCrew
    def getCurrentFuel(self):
        return self.currentFuel