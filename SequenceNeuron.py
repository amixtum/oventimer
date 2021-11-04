from random import choice
from math import abs

from Neuron import Neuron
from PMNeuron import PMNeuron
from RhythmGen import RhythmGen

class SequenceNeuron(Neuron):
    def __init__(self, rootFrequency, bpm, mode, sequence, even=1, odd=1):
        self.bpm = bpm
        self.mode = mode

        self.pm = PMNeuron(rootFrequency, 0, 0, 0, bpm, mode, None)
        self.rhythm = RhythmGen(even, odd, bpm)
            
        self.sequence = sequence
        self.sidx = 0
    
    def fire(self):
        nxtFn = choice([self.rhythm.tickEighth, self.rhythm.tickSixteenth, self.rhythm.tickQuarter])
        nxt = nxtFn()
        self.pm.setDuration(nxt[1])
        if nxt[0]:
            self.pm.queueSamples()
            self.pm.transpose(self.sequence[self.sidx])
            self.sidx = (self.sidx + 1) % len(self.sequence)
            if abs(self.pm.intervalFull()) >= 16:
                self.pm.resetTranspose()
        else:
            self.pm.queueRest()
