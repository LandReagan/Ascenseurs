import tkinter as tk

import ressources
from signaux import miseAJour, ajouter


# Redéfinition de la classe tk.Button pour notre usage
class Bouton(tk.Button):

    def __init__(self, parent=None, height=None, signal=None):
        super().__init__(master=parent, height=height)
        self.actif = False
        super().config(command=self.clic, bg='white')
        if not ressources.images_chargees:
            ressources.chargerDessins()
        self.signal = signal
        ajouter({self.signal: False})

    def clic(self):
        self.actif = not self.actif
        if self.actif:
            super().config(bg='green')
            miseAJour(self.signal, True)
        else:
            super().config(bg='white')
            miseAJour(self.signal, False)


class BoutonTexte(Bouton):
    def __init__(
            self, parent=None, height=None, signal=None,
            texte=None):
        super().__init__(
            parent=parent, height=height, signal=signal)
        super().config(text=texte)


class BoutonHaut(Bouton):
    def __init__(self, parent=None, height=None, signal=None):
        super().__init__(
            parent=parent, height=height, signal=signal)
        super().config(image=ressources.dessin_bouton_haut)


class DoubleBoutonHaut(Bouton):
    def __init__(self, parent=None, height=None, signal=None):
        super().__init__(
            parent=parent, height=height, signal=signal)
        super().config(image=ressources.dessin_bouton_double_haut)


class BoutonBas(Bouton):
    def __init__(self, parent=None, height=None, signal=None):
        super().__init__(
            parent=parent, height=height, signal=signal)
        super().config(image=ressources.dessin_bouton_bas)


class DoubleBoutonBas(Bouton):
    def __init__(self, parent=None, height=None, signal=None):
        super().__init__(
            parent=parent, height=height, signal=signal)
        super().config(image=ressources.dessin_bouton_double_bas)


class BoutonRond(Bouton):
    def __init__(self, parent=None, height=None, signal=None):
        super().__init__(
            parent=parent, height=height, signal=signal)
        super().config(image=ressources.dessin_bouton_rond)
