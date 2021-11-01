from math import pow

class NoteHelper(object):
    def __init__(self, center=220):
        self.center = center
        self.frequency = self.center
    
    def transpose(self, semitones):
        self.frequency *= (semitones * pow(2, 1 / 12))
        return self.frequency

    def transposeFromCenter(self, semitones):
        return self.center * (semitones * pow(2, 1 / 12))