import simpleaudio as sa


from SleepNeuron import SleepNeuron
from BeepNeuron import BeepNeuron
from PMNeuron import PMNeuron

from RhythmHelper import RhythmHelper
from NoteHelper import NoteHelper
from Mixer import *


r = RhythmHelper(120, 44100)
notes = NoteHelper(220)

pms = [PMNeuron(notes.frequency, 20, 3, r.quarter(), 120), PMNeuron(notes.frequency, 20, 3, r.quarter(), 120), PMNeuron(notes.frequency, 20, 3, r.quarter(), 120)]
for _ in range(10):
    for pm in pms:
        pm.fire()

out = mixN(pms)

wave = sa.WaveObject(out, 1, 2, 44100)
player = wave.play()
player.wait_done()
