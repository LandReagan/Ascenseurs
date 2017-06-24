import tkinter as tk

import ressources


# Redéfinition de la classe tk.Button pour notre usage
class Bouton(tk.Button):

    def __init__(self, parent=None, height=None):
        super().__init__(master=parent, height=height)
        self.actif = False
        super().config(command=self.clic, bg='white')
        if not ressources.images_chargees:
            ressources.chargerPhotos()

    def clic(self):
        self.actif = not self.actif
        if self.actif:
            super().config(bg='green')
        else:
            super().config(bg='white')


class BoutonHaut(Bouton):
    def __init__(self, parent=None, height=None):
        super().__init__(parent=parent, height=height)
        super().config(image=ressources.photo_bouton_haut)


class BoutonBas(Bouton):
    def __init__(self, parent=None, height=None):
        super().__init__(parent=parent, height=height)
        super().config(image=ressources.photo_bouton_bas)


class BoutonRond(Bouton):
    def __init__(self, parent=None, height=None):
        super().__init__(parent=parent, height=height)
        super().config(image=ressources.photo_bouton_rond)
