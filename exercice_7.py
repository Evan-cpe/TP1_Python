# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:34:16 2023

@author: Utilisateur
"""

def tricolore(n):
    if not isinstance(n, int):
        return "Merci de donner un nombre entier"
    N=n**2
    a = str(N)
    for i in a:
        if i not in ['1', '4', '9']:
            return False
    return True

"""
    Input : prend un nombre entier
    Output : renvoie un bouléen
    Fonctionnement : verifie si le nombre est tricolore
    """

def tous_les_tricolore(N):
    if not isinstance(N, int):
        return "Merci de donner un nombre entier"
    L=[]
    for i in range(N):
        if tricolore(i):
            L.append(i)
    return L

"""
    Input : prend un nombre entier
    Output : renvoie une liste
    Fonctionnement : donne la liste des nombre tricolore inférieur à un certain nombre
    """