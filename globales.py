# Définition des constantes
DIMENSIONS_CABINE = (50, 50)
HAUTEUR_ETAGE = 80
NOMBRE_ETAGES = 8


def creerDictEtages():
    etages = {}
    for i in range(0, NOMBRE_ETAGES):
        etages[i] = i * HAUTEUR_ETAGE
    return etages
