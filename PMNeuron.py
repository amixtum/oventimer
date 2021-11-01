from array import array

from math import pi, sin, cos

import simpleaudio as sa

from Neuron import Neuron
from RhythmHelper import RhythmHelper


class PMNeuron(Neuron):
    cPhase = 0.0
    mPhase = 0.0
    duration = 44100
    queue = []

    def __init__(self, cf, mf, mi, duration, bpm):
        self.setCarrierFrequency(cf)
        self.setModulationFrequency(mf)
        self.setModulationIndex(mi)
        self.duration = duration

        self.rhythm = RhythmHelper(bpm, 44100)

    def setCarrierFrequency(self, cf):
        self.cf = cf
        self.cIncrement = (cf * 2.0 * pi) / 44100.0

    def setModulationFrequency(self, mf):
        self.mf = mf
        self.mIncrement = (mf * 2.0 * pi) / 44100.0

    def setModulationIndex(self, mi):
        self.mi = mi

    def setDuration(self, duration):
        self.duration = duration

    def setQuarter(self):
        self.duration = self.rhythm.quarter()

    def setEighth(self):
        self.duration = self.rhythm.eighth()

    def setSixteenth(self):
        self.duration = self.rhythm.sixteenth()

    def next(self):
        s = 0.5 * sin(self.cPhase + (self.mi * cos(self.mPhase)))
        self.cPhase += self.cIncrement
        self.mPhase += self.mIncrement

        if self.cPhase >= 2.0 * pi:
            self.cPhase = 0.0
        elif self.cPhase < 0.0:
            self.cPhase = 2.0 * pi

        if self.mPhase >= 2.0 * pi:
            self.mPhase = 0.0
        elif self.mPhase < 0.0:
            self.mPhase = 2.0 * pi

        return s

    # t = time in samples
    def samples(self, t):
        return sa.WaveObject(array('i', [int(32767 * self.next()) for _ in range(int(t))]), 1, 2, 44100)
    
    # t = time in samples
    def rest(self, t):
        return sa.WaveObject(array('i', [0 for _ in range(int(t))]), 1, 2, 44100)

    def queueSamples(self):
        self.queue.append(self.samples(self.duration))
    
    def queueRest(self):
        self.queue.append(self.rest(self.duration))

    def fire(self):
        if len(self.queue) > 0:
            return self.queue.pop(0).play()