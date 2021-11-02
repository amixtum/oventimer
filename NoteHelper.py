from math import pow

class NoteHelper(object):
    def __init__(self, center=220):
        self.center = center
        self.frequency = self.center
    
    def setCenter(self, center):
        self.center = center
        self.frequency = center

    def transpose(self, semitones):
        self.frequency *= pow(2, semitones / 12)
        return self.frequency

    def transposeFromCenter(self, semitones):
            return self.center * pow(2, semitones / 12)