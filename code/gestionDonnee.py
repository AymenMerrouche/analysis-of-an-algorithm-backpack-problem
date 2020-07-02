def lireDonnee(nomFichier):
    fichier = open(nomFichier, "r")
    lines = fichier.read().split("\n")
    S = (int(lines[0]))
    K = (int(lines[1]))
    V = [0]
    for e in lines[2].split(" "):
        V.append(int(e))
    V.sort()
    data = [S, K, V]
    return data


def ecrireResultat(nomFichier, Tab1, Tab2, Tab3, Tab4, Tab5):
    f = open(nomFichier, "w+")
    Taille=len(Tab1)
    for i in range(0, Taille):
        f.write(str(Tab1[i])+" "+str(Tab2[i])+" "+str(Tab3[i])+" "+str(Tab4[i])+" "+str(Tab5[i])+"\n")

