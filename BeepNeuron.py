import winsound
from Neuron import Neuron

class BeepNeuron(Neuron):
    # time in seconds
    def __init__(self, f, t):
        self.f = f
        self.t = int(t * 1000)

    def fire(self):
        winsound.Beep(self.f, self.t)