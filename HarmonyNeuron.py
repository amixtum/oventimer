from random import choice

from Neuron import Neuron
from SequenceNeuron import SequenceNeuron
from LSystemNeuron import LSystemNeuron
from RhythmGen import RhythmGen
from HarmonyHelper import *
from Mixer import *

class HarmonyNeuron(Neuron):
    def __init__(self, sequenceNeuron, lsystemNeuron, growthFactor, nEven, nOdd):
        self.sNeuron = sequenceNeuron
        self.lNeuron = lsystemNeuron
        for _ in range(growthFactor):
            self.lNeuron.grow()
        self.pm = sequenceNeuron.pm.copy()
        self.lNeuron.pm.setCarrierFrequency(440)
        self.pm.setCarrierFrequency(440)
        self.rhythm = RhythmGen(nEven, nOdd, self.sNeuron.bpm)

    # return sum of three oscillators as int array
    def getMix(self):
        return mixN([self.pm, self.sNeuron.pm, self.lNeuron.pm])

    def fire(self):
        self.lNeuron.fire()
        makeChord(self.sNeuron.pm, self.lNeuron.pm, self.pm)
        self.sNeuron.fire()

        rFn = choice([self.rhythm.tickSixteenth, self.rhythm.tickEighth, self.rhythm.tickQuarter])
        r = rFn()
        self.pm.setDuration(r[1])
        if r[0]:
            self.pm.queueSamples()
        else:
            self.pm.queueRest()
