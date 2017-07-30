import tkinter as tk

import ressources
from signaux import signaux, ajouter


class Bouton(tk.Button):
    """ Classe de base pour tous les boutons.
    """

    def __init__(self, parent=None, height=None, signal=None):
        super().__init__(master=parent, height=height)
        super().config(command=self.clic, bg='white')
        self._signal = signal
        ajouter({self._signal: False})
        if not ressources.images_chargees:
            ressources.chargerDessins()

    def clic(self):
        self.miseAJour(not signaux[self._signal])

    def miseAJour(self, actif):
        signaux[self._signal] = actif
        if signaux[self._signal]:
            super().config(bg='green')
        else:
            super().config(bg='white')


class BoutonTexte(Bouton):
    """ Classe dérivée de la classe Bouton, à laquelle on ajoute du texte
    """

    def __init__(self, parent=None, height=None, signal=None, texte=None):
        Bouton.__init__(self, parent=parent, height=height, signal=signal)
        Bouton.config(self, text=texte)


class BoutonDessin(Bouton):
    """ Classe dérivée de la classe Bouton, à laquelle on ajoute un dessin
    """

    def __init__(self, parent=None, height=None, signal=None, dessin=None):
        Bouton.__init__(self, parent=parent, height=height, signal=signal)
        Bouton.config(image=dessin)

# TODO : faire dériver les boutons ci-dessous de BoutonDessin
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
