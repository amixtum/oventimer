import simpleaudio as sa

from SequenceNeuron import SequenceNeuron
from LSystemNeuron import LSystemNeuron
from HarmonyNeuron import HarmonyNeuron


sNeuron = SequenceNeuron(440, 120, 0, (3, -4, 5, -4), 2, 1)
lNeuron = LSystemNeuron(sNeuron.pm, \
                        (3, -4, 5, -4), \
                        {-6: [-3, 1], -5: [4, -1], -4: [5, -3], -3: [3], -2: [2], -1: [2], 0: [0], \
                          1: [5, 1], 2: [-1], 3: [-3], 4: [-5, 3], 5: [-4, 1], 6: [3, -1]}, \
                        [[[1, 1], 1], [[2, 2], 2], [[3, 3], 3], [[4, 4], 4], [[5, 5], 5], [[6, 6], 6], \
                        [[-1, -1], -1], [[-2, -2], -2], [[-3, -3], -3], [[-4, -4], -4], [[-5, -5], -5], [[-6, -6], -6]], \
                        120, 2, 1)

hNeuron = HarmonyNeuron(sNeuron, lNeuron, 2, 2, 1)

print(lNeuron.lsystem.now)

for _ in range(32):
    hNeuron.fire()

out = hNeuron.getMix()

wave = sa.WaveObject(out, 1, 2, 44100)
player = wave.play()
player.wait_done()
