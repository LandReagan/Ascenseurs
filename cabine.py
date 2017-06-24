from globales import *


class Cabine:
    def __init__(self, canevas):
        self.canevas = canevas
        self.dessin = self.canevas.create_rectangle(
            DIMENSIONS_CABINE[0] / 2,
            0,
            DIMENSIONS_CABINE[0] * 3 / 2,
            DIMENSIONS_CABINE[1],
            outline='red')
        self.hauteur_max = HAUTEUR_ETAGE * (NOMBRE_ETAGES - 1)
        self.montee = False
        self.descente = False

    @property
    def hauteur(self):
        h = self.canevas.coords(self.dessin)[3]  # coordonnée bas gauche
        h = NOMBRE_ETAGES * HAUTEUR_ETAGE - h
        return h

    @property
    def arretee(self):
        return (self.montee and self.descente) or\
            (not self.montee and not self.descente)

    def miseAJour(self):
        if self.hauteur > 0 and self.descente:
            self.canevas.move(self.dessin, 0, 1)
        if self.hauteur < self.hauteur_max and self.montee:
            self.canevas.move(self.dessin, 0, -1)
