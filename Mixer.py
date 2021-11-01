from array import array

from PMNeuron import PMNeuron

def mix(pm1, pm2):
    idx11 = 0
    idx12 = 0
    idx21 = 0
    idx22 = 0
    out = []

    while idx11 < len(pm1.queue) and idx12 < len(pm2.queue):
        out.append(int((pm1.queue[idx11][idx21] + pm2.queue[idx12][idx22]) / 2))

        idx21 += 1
        idx22 += 1

        if idx21 >= len(pm1.queue[idx11]):
            idx11 += 1
            idx21 = 0

        if idx22 >= len(pm2.queue[idx12]):
            idx12 += 1
            idx22 = 0

    while idx11 < len(pm1.queue):
        out.append(int(pm1.queue[idx11][idx21]))
        idx21 += 1
        if idx21 >= len(pm1.queue[idx11]):
            idx11 += 1
            idx21 = 0

    while idx12 < len(pm2.queue):
        out.append(int(pm2.queue[idx12][idx22]))
        idx22 += 1
        if idx22 >= len(pm2.queue[idx12]):
            idx12 += 1
            idx22 = 0

    return array('i', out)

def mixWithArray(pm1, a):
    idx1 = 0
    idx2 = 0
    idxa = 0
    out = []

    while idx1 < len(pm1.queue) and idxa < len(a):
        out.append(int((pm1.queue[idx1][idx2] + a[idxa]) / 2))
        idx2 += 1
        idxa += 1

        if idx2 >= len(pm1.queue[idx1]):
            idx1 += 1
            idx2 = 0
    
    while idx1 < len(pm1.queue):
        out.append(int(pm1.queue[idx1][idx2]))
        idx2 += 1

        if idx2 >= len(pm1.queue[idx1]):
            idx1 += 1
            idx2 = 0

    while idxa < len(a):
        out.append(a[idxa])
        idxa += 1
    
    return array('i', out)

def mixN(pms):
    a = mix(pms[0], pms[1])
    if len(pms) > 2:
        for i in range(2, len(pms)):
            a = mixWithArray(pms[i], a)
    return a
        