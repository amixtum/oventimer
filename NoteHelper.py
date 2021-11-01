from math import pow

class NoteHelper(object):
    def __init__(self, center=220):
        self.center = center
        self.frequency = self.center
    
    def setCenter(self, center):
        self.center = center
        self.frequency = center

    def transpose(self, semitones):
        if semitones < 0:
            s = int(abs(semitones))
            self.frequency *= ((1 / s) * pow(2, 1 / 12))
        else:
            self.frequency *= (semitones * pow(2, 1 / 12))
        return self.frequency

    def transposeFromCenter(self, semitones):
        if semitones < 0:
            s = int(abs(semitones))
            return self.center * ((1 / s) * pow(2, 1 / 12))
        else:
            return self.center * (semitones * pow(2, 1 / 12))