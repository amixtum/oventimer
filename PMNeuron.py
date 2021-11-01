from array import array

from math import modf, pi, sin, cos

from random import choice
from random import random

import simpleaudio as sa

from Neuron import Neuron
from RhythmHelper import RhythmHelper
from ScaleHelper import ScaleHelper


class PMNeuron(Neuron):
    def __init__(self, cf, mf, mi, duration, bpm):
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
        self.scales = ScaleHelper(6, 220)

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

    def queueSamples(self):
        self.queue.append(self.samples(self.duration))
    
    def queueRest(self):
        self.queue.append(self.rest(self.duration))

    def fire(self):
        durationFn = choice([self.setQuarter, self.setEighth, self.setSixteenth])
        durationFn()

        if random() > 0.5:
            interval = choice([-7, -5, -3, -1, 1, 3, 5, 7])
            self.scales.transpose(interval)
            if abs(self.scales.fromStart) > 7:
                self.scales.reset()
            self.setCarrierFrequency(self.scales.frequency())

            modScale = choice([2.5, 5, 7.5])
            self.setModulationIndex(modScale)

            modFrequencyScale = choice([0.5, 1.5, 0.25, 2])
            self.setModulationFrequency(self.mf * modFrequencyScale)
            if abs(self.mf) > 120:
                self.setModulationFrequency(20)
            self.queueSamples()
        else:
            self.queueRest()