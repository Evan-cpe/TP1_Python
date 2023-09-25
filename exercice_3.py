# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:38:58 2023

@author: Utilisateur
"""

Taux = [ 0, 0.11, 0.30, 0.41, 0.45]
Montant=[ 0, 10226, 26071, 74546, 160336]

def mesImpots(revenu :float) -> None:
    impot = 0
    N = len(Montant)
    if not isinstance(revenu, ( int, float)):
        return "Merci de donner votre revenu"
    
    for i in range( N):
        if revenu > Montant[N - i - 1]:
            impot += (revenu - Montant[N - i - 1]) * Taux[N - i - 1]
            revenu = Montant[N - i - 1]
    return int(impot)

"""
    Input : prend un nombre 
    Output : renvoie un nombre
    Fonctionnement : calcul les impots par rapport à la valeur d'entré
    """



