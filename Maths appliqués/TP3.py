# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:52:36 2026

@author: jojo2
"""

import math

def f(x):
    return math.sin(x)

#Méthodes Rectangles
def rect_gauche(a,b,n):
    S = 0
    pas = (b-a)/n
    for i in range(n):
        A = pas * f(a + i*pas)
        S = S + A
    return(f"La valeur approchée de l'intégrale avec la méthode de rectangle à gauche est : {S}")

def rect_droite(a,b,n):
    pas = (b-a)/n
    S = 0
    for i in range(n):
        S += f(b - i*pas)*pas
    return(f"La valeur approchée de l'intégrale avec la méthode de rectangle à droite est : {S}")
    
def rect_milieu(a,b,n):
    pas = (b-a)/n
    S = 0
    for i in range(n):
        S += f(((a+b)/2+i)*pas)*pas
    return(f"La valeur approchée de l'intégrale avec la méthode de rectangle au milieu est : {S}")
    
def aire_trap(a,b,n):
    pas = (b-a)/n
    S = 0
    for i in range(n):
        S += pas * (f(a+i*pas) + f(a+(i+1)*pas))/2
    return(f"La valeur approchée de l'intégrale d'un trapèeze est : {S}")   
    
def simpson(a,b,n):
    S = 0
    pas = (b-a)/n
    for i in range(0,n):
        S += pas* (f(a+pas*pas) + 4*f(a+(pas+0.5)*pas) + f(a+(pas+1)*pas))
    return(f"La valeur approchée de l'intégrale avec la méthode de Simpson est : {S}")   

