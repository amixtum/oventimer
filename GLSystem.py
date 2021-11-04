"""
GLSystem.py
An L-System (see Lindenmyer et. al or whatever) for musical choices and numerical expansion
"""

from math import exp


class GLSystem(object):
    """
        axiom = a list of elements
        expandRules = a dict mapping all elements of some alphabet 
        (including all elements of axiom) to other elements (or sequences) of that alphabet
        in order to expand a sequence
        trimRules = a list of elements of the form ((e1, e2, ... , e_n), e_result)
        which are used to replace those sequences with a number or other unique element
    """
    def __init__(self, axiom, expandRules, trimRules) -> None:
        self.axiom = axiom
        self.expandRules = expandRules 
        self.trimRules = trimRules
        self.now = []
        for e in axiom:
            self.now.append(e)

    def expand(self):
        result = []
        for e in self.now:
            for v in self.expandRules[e]:
                self.result.append(v)
        self.now = result 

    def trim(self):
        nowIdx = 0
        replace = False
        trueFor = 0
        for rule in self.trimRules:
            for idx in range(len(rule[0])):
                if self.now[nowIdx] == rule[0][idx]:
                    trueFor += 1
                    if len(rule[0]) - 1 == trueFor:
                        replace = True
                else:
                    trueFor = 0
                nowIdx += 1
            if replace:
                for i in range(trueFor):
                    self.now.pop(nowIdx - i - 1)
                self.now.insert(nowIdx - trueFor, rule[1])
                replace = False
            nowIdx = 0
            trueFor = 0
                

            

