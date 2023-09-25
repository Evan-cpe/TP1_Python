# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:17:06 2023

@author: Utilisateur
"""
import random


def crea_matrice(n:int,p:int) -> None:
    if n < 1 or p < 1:
        return None
    M = [[0 for i in range(p)] for i in range(n)]
    for i in range(n):
        for j in range(p):
            M[i][j]=random.randint(0,100)
    return M
    
"""
    Input : prend deux nombre positifs
    Output : renvoie une liste de liste
    Fonctionnement : crée une matrice avec des élement aléatoire 
                        mais avec ses dimension de connue
    """
    
def multiplication( A:list, B:list) -> None:
    LA = len(A)
    CA = len(A[0])
    LB = len(B)
    CB = len(B[0])
    if CA != LB:
        return "Mettez des matrices compatibles pour le produit"
    C = [[0 for i in range(CB)] for i in range(LA)]
    for i in range(LA):
        for j in range(CB):
            for k in range(CA):
                C[i][j] += A[i][k]*B[k][j]
    return print ('\n'.join(str(e) for e in C))

"""
    Input : prend 2 liste de liste
    Output : renvoie une liste de liste
    Fonctionnement : fait une multiplication matricielle
    """