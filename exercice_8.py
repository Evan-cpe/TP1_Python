# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:58:16 2023

@author: Utilisateur
"""

def liste_diviseurs(n):
    if not isinstance(n, int):
        return "Merci de donner un nombre entier"
    L=[]
    for i in range(1,n+1):
        if n%i == 0:
            L.append(i)
    return L

"""
    Input : prend un nombre entier
    Output : renvoie une liste
    Fonctionnement : donne la liste des diviseurs du nombre donner
    """

def somme_div(n):
    if not isinstance(n, int):
        return "Merci de donner un nombre entier"
    L = liste_diviseurs(n)
    S = 0
    for i in L:
        S += i
    return S

"""
    Input : prend un nombre entier
    Output : renvoie un nombre entier
    Fonctionnement : somme la liste des diviseurs d'un nombre
    """

def verification(N1, N2):
    if (not isinstance(N1, int)) or (not isinstance(N2, int)):
        return "Merci de donner un nombre entier"
    if (somme_div(N1) == somme_div(N2) and somme_div(N1)== N1 + N2 ):
        return True
    return False

"""
    Input : prend 2 nombre entier
    Output : renvoie un booléen
    Fonctionnement : vérifie si 2 nombre sont amicaux
    """
