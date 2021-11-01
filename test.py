import simpleaudio as sa


from SleepNeuron import SleepNeuron
from BeepNeuron import BeepNeuron
from PMNeuron import PMNeuron

from RhythmHelper import RhythmHelper
from NoteHelper import NoteHelper
from Mixer import *


r = RhythmHelper(120, 44100)
notes = NoteHelper(440)

n1 = PMNeuron(notes.frequency, 40, 2.5, r.quarter(), r.bpm)
n1.queueSamples()

notes.transpose(4)

n2 = PMNeuron(notes.frequency, 40, 2.5, r.quarter(), r.bpm)
n2.queueSamples()

out = mix(n1, n2)

wave = sa.WaveObject(out, 1, 2, 44100)
player = wave.play()
player.wait_done()