from algoGlouton import *
from algoProgDyn import *
from generationSystems import *
p_Max=800 #  la capacité du plus grand bocal
f=500 # une variable muette
true=false=0 # pour compter le nombre de systemes glouton compatible
maxLocal=maxGlobal=0 # contient repectivement le maximum locale et globale 
cpt=moy=0
A=[0]*1000
j=20
for i in range(1,j):
    V=generationSystemCapacite(i, p_Max)
    if testGloutonCompatible(i,V):
        true+=1
    else:
        false+=1
        M = [[-1 for _ in range(i + 1)] for x in range(800000 + 1)] # on initialise la matrice par des -1 afin d'utiliser l'algorithme algoProgDyn
        cpt=maxLocal=tr=0
        for S in range(p_Max,f*p_Max):    # pour tout les S entre p_max et f*pmax on utilise les deux algorithmes ( algoProgDyn et algoGlouton ) 
            a = algoProgDyn(i, V, S,M)   
            b = algoGlouton(i, V, S,A)
            cpt = cpt+b-a                 # on cumul l'écart entre les deux solution 
            tr+=1
            if maxLocal<(b-a):
               maxLocal=b-a                  # on met a jour le maximum local
        V1=list(V)
        del V1[0]
        print("     Systeme", false ,"l'écart moyen:",'%.2f' % (cpt/tr), "l'ecart max",maxLocal) # l'écarte moyen est la somme des écarts divisée par le nombre de quantités testés  
        moy+=cpt/tr # on cumul l'écart moyen 
        if maxLocal>maxGlobal:
           maxGlobal=maxLocal # on met a jour le maximum global 
print("Pour les systemes non glouton-compatible           l'écart moyen moyen =",'%.2f' % (moy /false), "le pire ecart",maxGlobal) # l'écart moyen moyen est la somme des écarts moyens divisée par le nombre de systemes non glouton-compatible
print("EN TOUT            l'écart moyen moyen =",'%.2f' % (moy /j), "     le pire ecart",maxGlobal,"       le nombre de systemes non glouton-compatible:",false,"      la proportion de systeme glouton compatible :",'%.2f' % (true/(true+false))) # des statistiques globales c-à-d en prenant en considération tout les systemes (glouton-compatible ou non ) 

