# Définition des constantes
DIMENSIONS_CABINE = (50, 50)
HAUTEUR_ETAGE = 50
NOMBRE_ETAGES = 10

RAFRAICHISSEMENT = 50

couleur_orange_pale = '#FEC849'
couleur_orange_fonce = '#FE6400'
couleur_vert_pale = '#00FFCC'
couleur_vert_pomme = '#00D400'


def creerDictEtages():
    etages = {}
    for i in range(0, NOMBRE_ETAGES):
        etages[i] = i * HAUTEUR_ETAGE
    return etages
