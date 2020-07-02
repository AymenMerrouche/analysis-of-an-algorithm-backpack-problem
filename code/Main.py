#!/usr/bin/python3.3
import math
from typing import List, Any
from pylab import *
from gestionDonnee import *
from rechercheExhaustive import *
from algoGlouton import *
from algoProgDyn import *
from generationSystems import *
import sys

choix=sys.argv[1]
nomFichier=sys.argv[2]
###Lecture de données et intialisations des variables
try :
	data = lireDonnee(nomFichier) # lecture de fichier texte et réccuperation des données
	S = data[0] 
	K = data[1]
	V = data[2]
	V = V[0:K+1]
	M = [[-1 for _ in range(K*10 + 1)] for x in range(S*100 + 1)] # matrice intialisée à -1 partout pour l'algorithme algoProgDyn
	A = [0] * (K+1) 
except:
    	sys.exit("Ce fichier n'existe pas")

if (choix=='-g'):
	V1=list(V)
	del V1[0] # On supprime la première case du tableau (car en théorie le tableau commance en 0)
	print("\n\nLes donnée lus sont: S=", S, "K=", K, "V=", V1,"\n\n")
	nbBocaux=algoGlouton(K, V, S, A)
	A1=list(A)
	del A1[0] # On supprime la première case tableau(car en théorie le tableau commance en 0) 
	print("D'après AlgoGlouton le nombre de bocaux est ",nbBocaux,"Le Tableau A :",A1,"\n\n")
  	  
if (choix=='-d'):
	V1=list(V)
	del V1[0] # On supprime la première case du tableau (car en théorie le tableau commance en 0)
	print("\n\nLes donnée lus sont: S=", S, "K=", K, "V=", V1,"\n\n")
	nbBocaux=algoProgDyn(K, V, S, M)
	A=backward(S, K, V, M)
	A1=list(A)
	del A1[0] # On supprime la première case tableau(car en théorie le tableau commance en 0) 
	print("D'après AlgoProgDyn le nombre de bocaux est ",nbBocaux,"Le Tableau A :",A1,"\n\n")

if (choix=='-r'):
	V1=list(V)
	del V1[0] # On supprime la première case du tableau (car en théorie le tableau commance en 0)
	print("\n\nLes donnée lus sont: S=", S, "K=", K, "V=", V1,"\n\n")
	nbBocaux=rechercheExhaustive(K, V, S)
	print("D'après l'algorithme rechercheExhaustive le nombre de bocaux est ",nbBocaux,"\n\n")

if (choix=='-t'):
	res=testGloutonCompatible(K, V)
	V1=list(V)
	del V1[0] # On supprime la première case du tableau (car en théorie le tableau commance en 0)
	print("\n\nLes donnée lus sont: ", "K=", K, "V=", V1,"\n\n")
	if res:
        	dec="est"
	else: 
		dec="n'est pas"
	print("Ce système de capacité", dec,"glouton-compatible\n\n")


###Test des Algorithmes
"""
V1=list(V)
del V1[0] # On supprime la première case du tableau (car en théorie le tableau commance en 0)
print("S=", S, "K=", K, "V=", V1)
print(algoProgDyn(K, V, S, M))
A1=list(backward(S, K, V, M)) # On reccupère le tableau A 
del A1[0] # On supprime la première case tableau(car en théorie le tableau commance en 0) 
print(A1)
print(algoGlouton(K, V, S, A))
del A[0] # On supprime la première case tableau(car en théorie le tableau commance en 0)
print(A)
print(rechercheExhaustive(K,V,S))
"""
tmp1 = [] # va contenir les temps d'exécutions afin de tracer les courbes 
tmp2 = [] # va contenir les temps d'exécutions afin de tracer les courbes
tmp3 = [] # va contenir les temps d'exécutions afin de tracer les courbes
tmp4 = [] # va contenir les temps d'exécutions afin de tracer les courbes
KK   = [] # va contenir les différents nombres de capacités distincts afin de tracer les courbes
SS   = [] # va contenir les différents qunatités de confiture afin de tracer les courbes
### Stasitiques en utilisant la recherche exhaustive ( d=2 puis d=3 puis d=4 ) 
"""
S=30
for i in range(1, 10): # pour un nombre important de quantités de confiture différentes 
    V=generationSystemCapaciteExpo(3,3) # on génère un système expo de taille K=3 et d=2
    time1=time.clock() # on enregistre le temps actuel 
    rechercheExhaustive(3, V, S+i)
    tmps2 = time.clock() - time1
    tmp1.append(tmps2)
    SS.append(S+i)

    V=generationSystemCapaciteExpo(6,3)
    time1=time.clock()
    rechercheExhaustive(6, V, S+i)
    tmps2 = time.clock() - time1
    tmp2.append(tmps2)

    V=generationSystemCapaciteExpo(12,3)
    time1=time.clock()
    rechercheExhaustive(12, V, S+i)
    tmps2 = time.clock() - time1
    tmp3.append(tmps2)

    V=generationSystemCapaciteExpo(24,3)
    time1=time.clock()
    rechercheExhaustive(24, V, S+i)
    tmps2 = time.clock() - time1
    tmp4.append(tmps2)
    print(i)


ecrireResultat("rechercheExhaustiveStatistiques d=3",tmp1,tmp2,tmp3,tmp4,SS)
plot(SS,tmp1, label="K=3")
plot(SS,tmp2, label="K=6")
plot(SS,tmp3, label="K=12")
plot(SS,tmp4, label="K=24")
xlabel("Quantité de confiture S (dg)")
ylabel("Temps CPU (s)")
title("Temps d'exécution de l'algorithme Recherche exhaustive en fonction de S et K (d=3)")
legend()
show()
"""
### Stasitiques en utilisant l'algorithme glouton ( d=2 puis d=3 puis d=4 ) 
"""
A=[0]*10000
for i in range(1, 100):
    V=generationSystemCapaciteExpo(K+i,3)
    time1=time.clock()
    algoGlouton(K+i, V, 100,A)
    tmps2 = time.clock() - time1
    tmp1.append(tmps2)

    time1=time.clock()
    algoGlouton(K+i, V, 500,A)
    tmps2 = time.clock() - time1
    tmp2.append(tmps2)

    time1=time.clock()
    algoGlouton(K+i, V, 1000,A)
    tmps2 = time.clock() - time1
    tmp3.append(tmps2)

    time1=time.clock()
    algoGlouton(K+i, V, 2000,A)
    tmps2 = time.clock() - time1
    tmp4.append(tmps2)

    KK.append(K+i)

ecrireResultat("algorithmeGloutonStatistiques d=3",tmp1,tmp2,tmp3,tmp4,KK)
plot(KK,tmp1, label="Algo glouton S=100")
plot(KK,tmp2, label="Algo glouton S=500")
plot(KK,tmp3, label="Algo glouton S=1000")
plot(KK,tmp4, label="Algo glouton S=2000")
xlabel("Nombre de capacités différentes de bocaux K")
ylabel("Temps CPU (s)")
title("Temps d'exécution de l'algorithme AlgoGlouton en fonction de S et K (d=3)")
legend()
show()
"""
### Stasitiques en utilisant l'algorithme de programmation dynamique ( d=2 puis d=3 puis d=4 ) 
"""
K=5
S=20
sys.setrecursionlimit(150000)
for i in range(1, 50):
    V=generationSystemCapaciteExpo(30,4)
    M = [[-1 for _ in range(100 + 1)] for x in range(S*50 + 1)]
    time1=time.clock()
    algoProgDyn(30, V,S*i,M)
    backward(S*i, 30, V, M)
    tmps2 = time.clock() - time1
    tmp1.append(tmps2)

    V=generationSystemCapaciteExpo(40,4)
    M = [[-1 for _ in range(100 + 1)] for x in range(S*50 + 1)]
    time1=time.clock()
    algoProgDyn(40, V, S*i,M)
    backward(S*i, 40, V, M)
    tmps2 = time.clock() - time1
    tmp2.append(tmps2)

    V=generationSystemCapaciteExpo(60,4)
    M = [[-1 for _ in range(100 + 1)] for x in range(S*50 + 1)]
    time1=time.clock()
    algoProgDyn(60, V,S*i,M)
    backward(S*i, 60, V, M)
    tmps2 = time.clock() - time1
    tmp3.append(tmps2)

    V=generationSystemCapaciteExpo(100,4)
    M = [[-1 for _ in range(100 + 1)] for x in range(S*50 + 1)]
    time1=time.clock()
    algoProgDyn(100, V, S*i,M)
    backward(S*i, 100, V, M)
    tmps2 = time.clock() - time1
    tmp4.append(tmps2)
    print(i)

    SS.append(S*i)

ecrireResultat("algorithmeDynStatistiques d=4",tmp1,tmp2,tmp3,tmp4,SS)
plot(SS,tmp1, label="Algo Dyn K=30")
plot(SS,tmp2, label="Algo Dyn K=40")
plot(SS,tmp3, label="Algo Dyn K=60")
plot(SS,tmp4, label="Algo Dyn K=100")
xlabel("Quantité de confiture S (dg)")
ylabel("Temps CPU (s)")
title("Temps d'exécution de l'algorithme AlgoProgDyn en fonction de S et K (d=4)")
legend()
show()
"""

