# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:15:20 2026

@author: jojo2
"""

#Préparation

#f(x) = x avec x  ∈ [−1; 1]
#f(0) = 0

#f(x) = sin(x) avec x [−π/2; π/2]
#f(0) = 0

#f(x) = cos(x) avec x ∈ [0; π]
#f(π/2) = 0

#f(x) = tan(x) avec x ∈ [−π/2; π/2]
#f(0) = 0

#f(x) = −2x+5 avec x ∈ [2; 3]
#f(5/2) = 0

#f(x) = −3x² + 5x −1 avec x ∈ [1; 2]
#f(x) = -3(x-0.23)(x-1.43)
#f(0.23) = 0 et f(1.43) = 0

#f(x) = x^3 +2x² −6x +3 avec x ∈ [−5; −3]
#f(x) = (x-1)(x²+3x-3)
#f(x) = (x-1)(x-0.791)(x+3.791)
#f(1) = 0 et f(0.791) = 0 et f(-3.791) = 0 

epsilon = 1*10**-15
a = 1
b = 2

def f(x):
    return -3*x**2 + 5*x -1

def dichotomique(a,b,f):
    if f(a) == 0 : return a
    if f(b) == 0 : return b

    while abs(f((a+b)/2)) >= epsilon :

        if f(a)*f((a+b)/2) < 0:
            a,b = a,(a+b)/2
        else:
            a,b = ((a+b)/2),b
            
    return (a+b)/2

print(f"Zéro de fonction linéaire est {dichotomique(a,b,f)}")  

def secante(a,b,f):
        if f(a) == 0 : return a
        if f(b) == 0 : return b
        x = a
        while abs(f(x)) > epsilon:
            x = x- f(x)*(b-x)/(f(b)) - f(x)
        return x
    
print(f"Zéro de fonction linéaire est {secante(a,b,f)}")  

pas = 0.1
def multiples(a,b,f):
    zeros = []
    if f(a) == 0:
        zeros += [a]
        x = a + pas
        while x <= b:
            if f(a)*f(x) < 0:
                zeros += [secante(a,x,f)]
            a += pas
            x = a + pas
        return zeros
        













# import math
# def f(x):
#     i = int(input("Quel cas voulez-vous choisir ? :"))
#     match i:
#         case 0 :
#             return x
#         case 1:
#             return math.sin(x)