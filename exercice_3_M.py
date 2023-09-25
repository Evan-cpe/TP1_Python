# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:23:59 2023

@author: Utilisateur
"""

import exercice_3

def calcul_impot():
    revenu = int(input("Entrez votre revenu : "))
    impot = exercice_3.mesImpots(revenu)
    return (f"Vos impots sont de {impot:.0f} euro")

"""
    Input : rien
    Output : renvoie un texte avec un nombre
    Fonctionnement : calcul les impots par rapport à la valeur d'entré
    """