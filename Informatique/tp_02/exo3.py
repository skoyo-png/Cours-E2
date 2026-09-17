import random 
n = random.randint(3, 99)
tab = [random.randint(0, 500) for i in range(n)]

def similaire(tab):
    for i in range(len(tab)):
        for j in range(i + 1, len(tab)):
            if tab[i] == tab [j] and i != j:
                return ("Il y a des éléments similaires dans le tableau.")
            return ("Il n'y a pas d'éléments similaires dans le tableau.")

print(tab)
print(similaire(tab))