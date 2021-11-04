import simpleaudio as sa


from SleepNeuron import SleepNeuron
from PMNeuron import PMNeuron

from RhythmHelper import RhythmHelper
from NoteHelper import NoteHelper
from Mixer import *


r = RhythmHelper(120, 44100)
notes = NoteHelper(440)

pms = [PMNeuron(notes.frequency, 0, 3, r.quarter(), r.bpm), PMNeuron(notes.frequency, 20, 3, r.quarter(), r.bpm)]

pms[0].fire()
pms[1].fire()

out = mixN(pms)

wave = sa.WaveObject(out, 1, 2, 44100)
player = wave.play()
player.wait_done()
