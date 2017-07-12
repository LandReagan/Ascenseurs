""" Ce module contient le dictionnaire des signaux lancés par les différents
    objets de l'application.
"""
from logger import logD

signaux = {}

signaux_precedents = {}


# Ajoute liste_signaux à signaux
def ajouter(liste_signaux):
    logD('Ajout signal ' + str(liste_signaux))
    signaux.update(liste_signaux)
    signaux_precedents.update(liste_signaux)


# met à jour une valeur du dictionnaire
def miseAJour(signal, valeur):
    signaux[signal] = valeur
    for k in signaux.keys():
        if signaux[k] is not signaux_precedents[k]:
            print(str(k) + ' ' + str(signaux[k]))
            signaux_precedents[k] = signaux[k]


def etat():
    for k in signaux.keys():
        print(k, ': ', signaux[k])


if __name__ == '__main__':
    ajouter({'signal1': False, 'signal2': True, 'signal3': False})
    etat()
    miseAJour('signal1', True)
    etat()
