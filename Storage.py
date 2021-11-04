from SequenceNeuron import SequenceNeuron
from LSystemNeuron import LSystemNeuron


sNeuron = SequenceNeuron(220, 120, 1, (3, -4, 5, -4), 1, 1)
lNeuron = LSystemNeuron(440, \
                        (3, -4, 5, -4), \
                        {-6: (),-5: (),-4: (), -3: (),-2: (),-1: (),0: (), 1: (),2: (),3: (),4: (),5: (),6: ()}, \
                        [((1, 1), 1), ((2, 2), 2), ((3, 3), 3), ((4, 4), 4), ((5, 5), 5), ((6, 6), 6), ((-1, -1), -1), ((-2, -2), -2), ((-3, -3), -3), ((-4, -4), -4), ((-5, -5), -5), ((-6, -6), -6)], \
                        120, 1, 1)
