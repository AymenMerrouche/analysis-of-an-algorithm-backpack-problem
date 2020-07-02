#!/usr/bin/python3.3
import math
from typing import List, Any
from pylab import *

def generationSystemCapacite(K, P_max):
    V = [1] * (K+1)
    for i in range(2, K+1):
        V[i] = randint(2, P_max)
    V.sort()
    return V


def generationSystemsCapacite(nbSys, P_max):
    V = []
    for i in range(1, nbSys):
        V.append(generationSystemCapacite(i, P_max))
    return V


def generationSystemCapaciteExpo(K, d):
    V=[]
    V.append(0)
    for i in range(1, K+1):
        V.append(int(math.pow(d, i-1)))
    V.sort()
    return V


