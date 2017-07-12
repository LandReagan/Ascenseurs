from globales import *
import signaux


class Capteurs:
    """ La classe Capteurs met à jour un dictionnnaire dont les clés sont le
        numéro d'étage et la valeur True ou False, qui représente la présence
        de la cabine à cet étage. Cette classe dessine aussi les capteurs
        allumés ou éteints.
    """
    
    def __init__(self, canevas, cabine, etages):
        self.canevas = canevas
        self.cabine = cabine
        self.etages = etages
        self.capteurs = {}
        for i in range(0, NOMBRE_ETAGES):
            self.capteurs[i] = False
        self.dessins = {}
        for i in range(0, NOMBRE_ETAGES):
            x = NOMBRE_ETAGES * HAUTEUR_ETAGE
            x -= self.etages[i] + DIMENSIONS_CABINE[1]
            self.dessins[i] = self.canevas.create_oval(
                DIMENSIONS_CABINE[0] * 3 / 2,
                x,
                DIMENSIONS_CABINE[0] * 3 / 2 + DIMENSIONS_CABINE[1] / 5,
                x + DIMENSIONS_CABINE[1] / 5)
            signaux.ajouter({'pp_c' + str(i) + '_': False})

    def miseAJour(self):
        """ Met à jour le dictionnaire des capteurs en passant à True le capteur
            correspondant si la cabine est face à un étage. Ensuite, met à jour
            le graphisme.
        """
        for i in range(0, NOMBRE_ETAGES):
            if self.etages[i] == self.cabine.hauteur:
                self.capteurs[i] = True
                signaux.miseAJour('pp_c' + str(i) + '_', True)
            else:
                self.capteurs[i] = False
                signaux.miseAJour('pp_c' + str(i) + '_', False)
            if self.capteurs[i]:
                self.canevas.itemconfigure(self.dessins[i], fill='red')
            else:
                self.canevas.itemconfigure(self.dessins[i], fill='white')

    @property
    def etat(self):
        # Renvoie l'état des capteurs d'étage
        return self.capteurs
