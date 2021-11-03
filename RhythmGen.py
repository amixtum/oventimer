from RhythmHelper import RhythmHelper

class RhythmGen(object):
    def __init__(self, nEven, nOdd, bpm=120):
        self.rhythm = RhythmHelper(bpm, 44100)
        self.metronome = 0

        self.nEven = nEven
        self.nOdd = nOdd
        self.evenNext = True 
        self.sinceOdd = 0
        self.sinceEven = 0
    
    def tickSixteenth(self):
        self.metronome = (self.metronome + 1) % 4
        return (self.__computeNote(), self.rhythm.sixteenth())
    
    def tickEighth(self):
        self.metronome = (self.metronome + 2) % 4
        return (self.__computeNote(), self.rhythm.eighth())

    def tickQuarter(self):
        return (self.__computeNote(), self.rhythm.quarter())

    def __computeNote(self):
        if (self.metronome % 2) == 0:
            if self.evenNext:
                self.sinceOdd += 1
                if self.sinceOdd >= self.nEven:
                    self.evenNext = False
                return True
            return False 
        else:
            if self.evenNext:
                return False
            self.sinceEven += 1
            if self.sinceEven >= self.nOdd:
                self.evenNext = True 
            return True