import tkinter as tk

import logger
from logger import logD, logI, logW, logE, logC
from globales import *
import ressources
from boutons import *
from signaux import signaux
from cabine import Cabine
from etages import Etages
from capteurs import Capteurs
from panneau_maintenance import PanneauMaintenance
from panneau_puit import PanneauPuit
from panneau_cabine import PanneauCabine


class Ascenseur(tk.Tk):
    """ Cette classe est la classe principale de l'application
    """

    def __init__(self):
        """ Le constructeur de la classe Ascenseurs est la fonction la plus
            importante. Elle :
            1. Initialise le logger (voir logger.py)
            2. lance la construction de Tkinter
            3. Customise la fenêtre de l'application
            4. Crée le panneau principal contenant tous les autres widgets
            et le positionne
            5. Charge les ressources externes (dessins)
        """
        logger.initialiser()
        logI('Construction de l\'application')

        super().__init__()

        self.geometry('800x600')

        self.panneau_principal = tk.Frame(self)
        self.panneau_principal.grid()

        ressources.chargerDessins()

        # Création du panneau de maintenance
        self.panneau_maintenance = PanneauMaintenance(
            parent=self.panneau_principal)

        # Création du panneau de puit
        self.panneau_puit = PanneauPuit(self.panneau_principal)

        # Création de la cabine
        self.cabine = Cabine(self.panneau_puit.dessin_puit)

        # Création du panneau interne de la Cabine
        self.panneau_cabine = PanneauCabine(
            self.panneau_principal, self.cabine)

        # Création des étages
        self.etages = Etages(self.panneau_puit.dessin_puit)

        # Création des capteurs
        self.capteurs = Capteurs(
            self.panneau_puit.dessin_puit, self.cabine, self.etages.etages)

        logD('Lancement de l\'animation')
        self.animation()
        self.mainloop()

    def logique(self):

        # Logique du panneau de maintenance
        if signaux['pm_cmc_'] is True:
            if signaux['pm_bb_'] is True:
                self.cabine.descente = True
            else:
                self.cabine.descente = False
            if signaux['pm_bh_'] is True:
                self.cabine.montee = True
            else:
                self.cabine.montee = False

        # Logique automatique
        else:
            self.cabine.montee = False
            self.cabine.descente = False

    def animation(self):
        self.logique()
        self.cabine.miseAJour()
        self.capteurs.miseAJour()
        self.panneau_principal.after(RAFRAICHISSEMENT, self.animation)

    def __del__(self):
        logI('Fin de l\'application')


if __name__ == '__main__':
    app = Ascenseur()
