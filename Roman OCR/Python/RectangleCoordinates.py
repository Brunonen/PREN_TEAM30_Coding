class RectangleCoordinates:
    xPos = 0
    yPos = 0

    def __init__(self):
        self.xPos = 0
        self.yPos = 0

    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def getXPos(self):
        # type: () -> object
        # type: () -> object
        return self.xPos

    def getYPos(self):
        return self.yPos

    def setXPos(self, xPos):
        self.xPos = xPos

    def setYPos(self, yPos):
        self.yPos = yPos
