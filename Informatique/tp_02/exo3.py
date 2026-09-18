import random 
n = random.randint(3, 99)
tab = [random.randint(0, 500) for i in range(n)]
double = []

def similaire(tab):
    for i in range(0, len(tab)-1):
        for j in range(i + 1, len(tab)):
            if tab[i] == tab [j]:
                double.append(tab[i])
    if (len(double) == 0):
        return "Aucun doublon"
    else:
        return "Il y a des doublons"
        return double

print(similaire(tab))