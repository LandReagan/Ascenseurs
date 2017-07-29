from globales import *
import ressources
from signaux import listeSignauxEtagesBas, listeSignauxEtagesHaut


class Etages:
    """ Cette classe définit le graphisme des étages, constitué d'une ligne de
        plancher et des boutons d'appel.
    """

    def __init__(self, canevas):
        self.canevas = canevas
        self.etages = creerDictEtages()
        self.boutons_etages_haut = {}
        self.boutons_etages_bas = {}

        for e in self.etages.keys():
            hauteur_plancher = (
                NOMBRE_ETAGES * HAUTEUR_ETAGE - self.etages[e])

            self.canevas.create_line(  # ligne du plancher
                DIMENSIONS_CABINE[0] / 2,
                hauteur_plancher,
                DIMENSIONS_CABINE[0] * 7 / 2,
                hauteur_plancher,
                dash=(4, 1))

            bouton_haut = self.canevas.create_image(
                0, 0, image=ressources.dessin_bouton_haut)
            bouton_coordonnees = self.canevas.bbox(bouton_haut)
            hauteur_bouton = bouton_coordonnees[3] - bouton_coordonnees[1]
            self.canevas.coords(
                bouton_haut,
                2 * DIMENSIONS_CABINE[0],
                hauteur_plancher - HAUTEUR_ETAGE / 2 - hauteur_bouton / 2)
            self.boutons_etages_haut[e] = bouton_haut

            bouton_bas = self.canevas.create_image(
                0, 0, image=ressources.dessin_bouton_bas)
            self.canevas.coords(
                bouton_bas,
                2 * DIMENSIONS_CABINE[0],
                hauteur_plancher - HAUTEUR_ETAGE / 2 + hauteur_bouton / 2)
            self.boutons_etages_bas[e] = bouton_bas

    def miseAJour(self):
        """ Cette fonction met à jour le dessin des boutons d'appel selon
            l'état des signaux.
        """
        liste_bas = listeSignauxEtagesBas()
        for etage in self.boutons_etages_bas.keys():
            if etage in liste_bas:
                self.canevas.itemconfigure(
                    self.boutons_etages_bas[etage],
                    image=ressources.dessin_bouton_bas_actif
                )
            else:
                self.canevas.itemconfigure(
                    self.boutons_etages_bas[etage],
                    image=ressources.dessin_bouton_bas
                )

        liste_haut = listeSignauxEtagesHaut()
        for etage in self.boutons_etages_haut.keys():
            if etage in liste_haut:
                self.canevas.itemconfigure(
                    self.boutons_etages_haut[etage],
                    image=ressources.dessin_bouton_haut_actif
                )
            else:
                self.canevas.itemconfigure(
                    self.boutons_etages_haut[etage],
                    image=ressources.dessin_bouton_haut
                )
