# Définition des constantes
DIMENSIONS_CABINE = (50, 50)
HAUTEUR_ETAGE = 50
NOMBRE_ETAGES = 8
couleur_orange_pale = '#FEC849'
couleur_orange_fonce = '#FE6400'


def creerDictEtages():
    etages = {}
    for i in range(0, NOMBRE_ETAGES):
        etages[i] = i * HAUTEUR_ETAGE
    return etages
