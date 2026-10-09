# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:54:17 2026

@author: jojo2
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:57:05 2026
 
@author: dacruzjo
"""
#Exercie 1 (PGCD)
def pgcd(a,b):
    if b == 0:
        return a
    return pgcd(b, a%b) #rappel la fonction et change les termes jusqu'à ce que le reste soit 0

def ppcm(a,b):
    if a == 0 or b == 0:
        return 0
    return abs(a*b) // pgcd(a, b)

a = (32/pgcd(32,328)) 
b = (328/pgcd(32,328))
c = (17/pgcd(17,23))
d = (23/pgcd(17,23))
numérateur = (a*(ppcm(b,d)/b)) - (c*(ppcm(b,d)/d))
dénominateur = ppcm(b,d)
print(f"Le résultat irréductible de A est {numérateur}/{dénominateur}")

 
# Exercice 2 (Définition d'une limite)
 
def foncf(x):
    return 2+1/(x**2-3)
 
epsi = float(input("Entrer une valeur pour Epsilon :"))
epsi = abs(epsi)
print(f"La valeur absolue de epsilon est : {epsi}")

# from sympy import symbol, limit , oo
# L = limit(func_lim,x,oo)

#Exercice 3 (Archimède)
N = int(input("Entrez un entier N : "))
i = 2
k = 2
pi = 3
terme = 1
while(terme != N):
    pi = pi+(4*(-1)**k) / (i*(i+1)*(i+2))
    i += 2
    k += 1
    terme += 1
print(f"La valeur de pi est : {round(pi,terme)}")


#Exercice 4 (Euler)

def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

precision = 1e-5
def estimer_e(precision):
    n = 0
    somme = 0
    terme = 1
    while terme >= precision:
        somme += terme
        n += 1
        terme = 1 / factorielle(n)
    return somme, n

