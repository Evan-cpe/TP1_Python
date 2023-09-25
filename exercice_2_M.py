# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:21:29 2023

@author: Utilisateur
"""

import exercice_2

def validation_date_2():
    annee = int(input("Entrez l'année : "))
    mois = int(input("Entrez le mois (1-12) : "))
    jour = int(input("Entrez le jour : "))

    if exercice_2.validation_date_1(annee, mois, jour):
        print("Date valide.")
    else:
        print("Date non valide.")

"""
    Input : rien
    Output : renvoie Date valide ou non
    Fonctionnement : valide ou non la date proposé
    """