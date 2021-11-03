from array import array

from math import pi, sin, cos

from random import choice
from random import random

from Neuron import Neuron
from RhythmHelper import RhythmHelper
from ScaleHelper import ScaleHelper


class PMNeuron(Neuron):
    # transpose from major I
    def __init__(self, cf, mf, mi, duration, bpm, xpose, scales=None):
        self.cf = cf
        self.mf = mf
        self.mi = mi
        self.setCarrierFrequency(cf)
        self.setModulationFrequency(mf)
        self.setModulationIndex(mi)

        self.duration = duration
        self.queue = []
        self.cPhase = 0.0
        self.mPhase = 0.0

        self.rhythm = RhythmHelper(bpm, 44100)

        if scales is None:
            self.scales = ScaleHelper(xpose, self.cf)
        else:
            self.scales = scales
        self.setCarrierFrequency(self.scales.frequency())

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

    def transpose(self, n):
        self.scales.transpose(n)
        self.setCarrierFrequency(self.scales.frequency())

    def transposeFromCenter(self, n):
        self.scales.reset()
        self.scales.transpose(n)
        self.setCarrierFrequency(self.scales.frequency())
    
    def interval(self):
        self.scales.fromStart % 8

    def intervalFull(self):
        return self.scales.fromStart

    def next(self):
        s = 0.3 * sin(self.cPhase + (self.mi * cos(self.mPhase)))
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
        return array('i', [int(32767 * self.next()) for _ in range(int(t))])
    
    # t = time in samples
    def rest(self, t):
        return array('i', [0 for _ in range(int(t))])

    def queueSamples(self, duration=None):
        if duration is None:
            self.queue.append(self.samples(self.duration))
        else:
            self.queue.append(self.samples(duration))
        
    def queueRest(self, duration=None):
        if duration is None:
            self.queue.append(self.rest(self.duration))
        else:
            self.queue.append(self.rest(duration))

    # does not copy its queue over (?)
    def copy(self):
        c = PMNeuron(self.cf, self.mf, self.mi, self.duration, self.bpm, self.interval(), self.scales.copy())
        return c
    
    # returns a copy with a queue filled with silence as long as this queue is filled with sound
    def copyWithSilence(self):
        c = self.copy()
        restLength = sum([len(self.queue[i]) for i in range(len(self.queue))])
        c.queueRest(restLength)
        return c


    def fire(self):
        pass