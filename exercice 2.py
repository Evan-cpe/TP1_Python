
"""TO DO LIST: faire des multifichier """



def est_bissextile(annee):
    if not isinstance(annee, int):
        return "Ce n'est pas une année, merci de donner un nombre entier"
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

"""
    Input : prend un nombre entier
    Output : renvoie True ou False
    Fonctionnement : verifie si l'année choisie est bien bissextile
    """

def nombre_jours_mois(annee, mois):
    if not 0 < mois < 13:
        return "Donnez un entier entre 1 et 12 pour le mois"
    elif not isinstance(annee, int):
        return "Ce n'est pas une année, merci de donner un nombre entier"
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mois in [4, 6, 9, 11]:
        return 30
    elif mois == 2:
        return 29 if est_bissextile(annee) else 28
    else:
        return None
    
"""
    Input : prend un premier nombre entier pour l'année et 
        un deuxiéme nombre pour le mois
    Output : renvoie un nombre entier ou un texte disant l'erreur
    Fonctionnement : retourne le nombre de jours dans un mois donné
    """

def validation_date_1(annee, mois, jour):
    if not 0 < mois < 13:
        return False
    jours_dans_mois = nombre_jours_mois(annee, mois)
    if jour < 1 or (type(jours_dans_mois) is int and jour > jours_dans_mois):
        return False
    return True

"""
    Input : prend un premier nombre entier pour l'année,
        un deuxiéme nombre pour le mois et un troisiéme nombre pour le jour 
    Output : renvoie True ou False
    Fonctionnement : valide ou non la date proposé
    """


def validation_date_2():
    annee = int(input("Entrez l'année : "))
    mois = int(input("Entrez le mois (1-12) : "))
    jour = int(input("Entrez le jour : "))

    if validation_date_1(annee, mois, jour):
        print("Date valide.")
    else:
        print("Date non valide.")

"""
    Input : rien
    Output : renvoie Date valide ou non
    Fonctionnement : valide ou non la date proposé
    """