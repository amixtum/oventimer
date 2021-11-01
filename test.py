import simpleaudio as sa
from RhythmHelper import RhythmHelper

from SleepNeuron import SleepNeuron
from BeepNeuron import BeepNeuron
from PMNeuron import PMNeuron
from RhythmHelper import RhythmHelper
from NoteHelper import NoteHelper

r = RhythmHelper()
notes = NoteHelper()
n = PMNeuron(notes.frequency, 40, 2.5, r.quarter())

n.queueSamples()

while len(n.queue) > 0:
    playback = n.fire()
    while playback.is_playing():
        continue