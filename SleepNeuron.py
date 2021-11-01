import time
from Neuron import Neuron


class SleepNeuron(Neuron):
    def __init__(self, t):
        self.t = t

    def fire(self):
        time.sleep(self.t)