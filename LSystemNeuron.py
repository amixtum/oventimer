from random import choice

from GLSystem import GLSystem
from Neuron import Neuron
from RhythmGen import RhythmGen

class LSystemNeuron(Neuron):
    """
        pmBase = PMNeuron to copy initial frequencies and state of scales
    """
    def __init__(self, pmBase, axiom, expandRules, trimRules, bpm, nEven, nOdd) -> None:
        super().__init__()
        self.pm = pmBase.copy()
        self.lsystem = GLSystem(axiom, expandRules, trimRules)
        self.rhythm = RhythmGen(bpm, nEven, nOdd)
        self.idx = 0    
    
    def interval(self):
        return self.pm.interval()
    
    def grow(self):
        self.pm.resetQueue()
        self.idx = 0
        self.lsystem.expand()
        self.lsystem.trim()

        nowIdx = 0
        while nowIdx < len(self.lsystem.now):
            rFn = choice([self.rhythm.tickQuarter, self.rhythm.tickEighth, self.rhythm.tickSixteenth])
            r = rFn()
            self.pm.setDuration(r[1])
            if r[0]:
                self.pm.transpose(self.lsystem.now[nowIdx])
                nowIdx += 1
                self.pm.queueSamples()
            else:
                self.pm.queueRest()

    def fire(self):
        i = self.idx
        self.idx = (self.idx + 1) % len(self.lsystem.now)
        return self.lsystem.now[i]