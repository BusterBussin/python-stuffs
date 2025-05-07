class SpaceMission:
    def __init__(self, missionName, model, array, comms):
        self.missionName = missionName
        self.model = model
        self.array = array
        self.comms = comms

    def __init__(self, mission):
        self.missionName = mission.missionName
        self.model = mission.model
        self.array = mission.array
        self.comms = mission.comms

    def getName(self):
        return self.missionName
    
    def getModel(self):
        return self.model
    
    def getArray(self):
        return self.array
    
    def getComms(self):
        return self.comms
    
    def setName(self, missionName):
        self.missionName = missionName
    
    def setModel(self, model):
        self.model = model
    
    def setArray(self, array):
        self.array = array
    
    def setComms(self, comms):
        self.comms = comms