"""
HarmonyHelper.py
Help with identifying intervals and finding the transpositions required to make chords, etc.
"""

from math import abs

def intervalFull(pm1, pm2):
    return pm1.intervalFull() - pm2.intervalFull()

def interval(pm1, pm2):
    return pm1.interval() - pm2.interval()

"""
a = current interval
x = transpose required to reach target interval
a + x = target
x = target - a
"""
def findTransposeFull(pm1, pm2, target):
    return (target - 1) - intervalFull(pm1, pm2)

def findTranspose(pm1, pm2, target):
    return (target - 1) - interval(pm1, pm2)

"""
EXPERIMENTAL
transposes pmResult based on the interval between pm1 and pm2
"""
def makeChord(pm1, pm2, pmResult):
    i = abs(interval(pm1, pm2))
    if i == 1: # second
        pmResult.transpose(findTransposeFull(pm2, pmResult, 5))
    elif i == 2: # third
        pmResult.transpose(findTransposeFull(pm2, pmResult, 7))
    elif i == 3: # fourth
        pmResult.transpose(findTransposeFull(pm2, pmResult, 6))
    elif i == 4: # fifth
        pmResult.transpose(findTransposeFull(pm2, pmResult, 9)) 
    elif i == 5: # sixth
        pmResult.transpose(findTransposeFull(pm2, pmResult, 5))
    elif i == 6: # seventh
        pmResult.transpose(findTransposeFull(pm2, pmResult, 3))
    else:
        pmResult.transpose(findTransposeFull(pm2, pmResult), 5)