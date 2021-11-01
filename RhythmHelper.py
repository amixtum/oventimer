class RhythmHelper(object):
    def __init__(self, bpm=120, sampleRate=44100):
        self.bpm = bpm
        self.sampleRate = sampleRate
        self.spb = (60 * sampleRate) / bpm

    def setBPM(self, bpm):
        self.bpm = bpm
        self.spb = (60 * self.sampleRate) / bpm   

    def quarter(self):
        return int(self.spb)
    
    def eighth(self):
        return int(self.spb / 2)
    
    def sixteenth(self):
        return int(self.spb / 4)