from algoGlouton import *
from generationSystems import *
p_Max=8000
true=false=0
for i in range(1,101):
        V=generationSystemCapacite(i, p_Max)
        if testGloutonCompatible(i,V):
           true+=1
        else:
           false+=1
print("true =",true," false =", false, " f= ", true /(true+false))
