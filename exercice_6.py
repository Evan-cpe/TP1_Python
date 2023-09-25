# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:15:07 2023

@author: Utilisateur
"""

def Syracuse(n, L=[]):
    if not isinstance(n, int):
        return "Merci de donner un nombre entier"
    L.append(n)
    if n <= 1 :
        return L
    elif (n % 2) == 0:
        n = int(n / 2)
        return Syracuse(n, L)
    else:
        n = n * 3 + 1
        return Syracuse(n, L)

"""
    Input : prend un nombre entier
    Output : renvoi une liste
    Fonctionnement : donner la suite de Syracuse
    """

def donnée(n):
    L = Syracuse(n, [])
    Max = max(L)
    temps_vol = len(L)
    return Max, temps_vol

"""
    Input : prend un nombre entier
    Output : renvoie 2 nombre entier
    Fonctionnement : donne le temps de vol et l'altitude d'une liste de Syracuse
    """

def balayage():
    T = 0
    iT = 0
    M = 0
    iM = 0
    for i in range(1, 1001):
        m, t =donnée(i)
        if T < t:
            iT = i
            T = t
        if M < m:
            iM = i
            M = m
    return (f"""le nombre avec le vol le plus long est {iM:.0f} ,
            celui avec l'altitude la plus haute est {iT:.0f}""")

"""
    Input : rien
    Output : renvoie 2 nombre entier
    Fonctionnement : teste les suites de Syracuse de 1 à 1000 et 
                    donne la suite qui a la plus grande altitude et 
                    le plus grand temps de vol
    """