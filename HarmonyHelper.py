from math import abs

from PMNeuron import PMNeuron

def intervalFull(pm1, pm2):
    return pm1.intervalFull() - pm2.intervalFull()

def interval(pm1, pm2):
    return pm1.interval() - pm2.interval()

def findTransposeFull(pm1, pm2, target):
    return (target - 1) - intervalFull(pm1, pm2)

def findTranspose(pm1, pm2, target):
    return (target - 1) - interval(pm1, pm2)