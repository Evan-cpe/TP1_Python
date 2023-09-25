# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:29:57 2023

@author: Utilisateur
"""


def Hanoi(palet, plot_départ=1, plot_arrivé=3, stock=2):
    if not isinstance(palet, int):
        return "Merci de donner un nombre entier"
    if palet == 0:
        return 0
    total = Hanoi(palet-1, plot_départ, stock, plot_arrivé)
    #print (f""""Déplace le palet du plot {plot_départ:.0f} vers le plot {plot_arrivé:.0f}""")
    total += 1
    total += Hanoi(palet-1, stock, plot_arrivé, plot_départ)
    return total

"""
    Input : prend un nombre entier
    Output : renvoie du texte et un nombre entier
    Fonctionnement : donner la suite de coup a faire et le nombre de coup total
    """