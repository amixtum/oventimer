from random import choice

from GLSystem import GLSystem
from Neuron import Neuron
from PMNeuron import PMNeuron
from RhythmGen import RhythmGen
from HarmonyHelper import *

class LSystemNeuron(Neuron):
    """
        pmBase = PMNeuron to copy initial frequencies and state of scales
    """
    def __init__(self, pmBase, axiom, expandRules, trimRules, bpm, nEven, nOdd) -> None:
        super().__init__()
        self.pm = pmBase.copy()
        self.lsystem = GLSystem(axiom, expandRules, trimRules)
        self.rhythm = RhythmGen(bpm, nEven, nOdd)
    
    def fire(self):
        self.pm.resetQueue()
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
