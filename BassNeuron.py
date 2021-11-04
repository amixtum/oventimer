from random import choice
from math import abs

from Neuron import Neuron
from PMNeuron import PMNeuron
from RhythmGen import RhythmGen

class BassNeuron(Neuron):
    def __init__(self, rootFrequency, bpm, mode):
        self.bpm = bpm
        self.mode = mode

        self.pm = PMNeuron(rootFrequency, 0, 0, 0, bpm, mode, None)
        self.rhythm = RhythmGen(1, 1, bpm)
            
        self.sequence = (3, -4, 5, -4)
        self.sidx = 0
    
    def fire(self):
        nxtFn = [self.rhythm.tickEighth, self.rhythm.tickSixteenth, self.rhythm.tickQuarter]
        nxtIdx = choice([0, 1, 2])
        nxt = nxtFn[nxtIdx]()
        if nxt[0]:
            if nxtIdx == 0:
                self.pm.setEighth()
            elif nxtIdx == 1:
                self.pm.setSixteenth()
            elif nxtIdx == 2:
                self.pm.setQuarter()

            self.pm.queueSamples()
            self.pm.transpose(self.sequence[self.sidx])
            self.sidx = (self.sidx + 1) % 4
            if abs(self.pm.intervalFull()) >= 16:
                self.pm.resetTranspose()
        else:
            if nxtIdx == 0:
                self.pm.setEighth()
            elif nxtIdx == 1:
                self.pm.setSixteenth()
            elif nxtIdx == 2:
                self.pm.setQuarter()
            
            self.pm.queueRest()
