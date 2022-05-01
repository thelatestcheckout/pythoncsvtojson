class outputData():
    def __init__(self, id, issue, stance, argument):
        self.id = id
        self.issue = issue
        self.stance = stance
        self.argumentative = []
        self.quality = []
        self.effectiveness = []
        self.argument = argument

    def setArgumentative(self, argumentative):
        self.argumentative.append(argumentative)

    def setQuality(self, quality):
        self.quality.append(quality)

    def setEffectiveness(self, effectiveness):
        self.effectiveness.append(effectiveness)
