import tkinter as tk

from boutons import BoutonHaut, BoutonBas
from globales import *


class PanneauMaintenance(tk.Frame):
    """ Le panneau de maintenance sert aux tests du système.
        On y retrouve le contrôle manuel de la cabine, ainsi que les
        boutons d'étage.
    """

    def __init__(self, parent=None, bg=couleur_orange_pale):
        """ Le constructeur :
            - Appel le constructeur de tk.Frame
            - Positionne le panneau
            - Crée et positionne le titre
            - Crée et positionne le contrôle manuel de la cabine
        """
        self.parent = parent
        self.arriere_plan = couleur_orange_pale
        super().__init__(master=parent, bg=bg)
        self.grid(column=0, row=0)
        print(parent.cget('bg'))

        # Titre en colonne 0 et 1 ligne 0
        self.titre = tk.Label(
            master=self, text='Maintenance', bg=self.arriere_plan)
        self.titre.grid(column=0, row=0, columnspan=2)

        # Contrôle manuel en colonne 0 ligne 1
        self.controle_manuel_cabine = tk.Frame(
            master=self, bg=couleur_orange_fonce)
        self.controle_manuel_cabine.grid(column=0, row=1)
        self.controle_manuel_cabine_titre = tk.Label(
            master=self.controle_manuel_cabine,
            text='Contrôle manuel\nde la cabine',
            bg=couleur_orange_fonce
        )
        self.controle_manuel_cabine_titre.grid(column=0, row=0)
        self.bouton_haut = BoutonHaut(parent=self.controle_manuel_cabine)
        self.bouton_haut.grid(column=0, row=1)
        self.bouton_bas = BoutonBas(parent=self.controle_manuel_cabine)
        self.bouton_bas.grid(column=0, row=2)

        # Boutons d'étage en colonne 1 ligne 1
        self.boutons_etages = tk.Frame(master=self)
        self.boutons_etages.grid(column=1, row=1)
        for i in range(0, NOMBRE_ETAGES):
            bouton_haut = BoutonHaut(self.boutons_etages)
            bouton_haut.grid(column=0, row=2 * i)
            bouton_haut.config(
                height=HAUTEUR_ETAGE // 2 - int(str(bouton_haut.cget('borderwidth'))) * 3
            )
            bouton_bas = BoutonBas(self.boutons_etages)
            bouton_bas.grid(column=0, row=2 * i + 1)
            bouton_bas.config(
                height=HAUTEUR_ETAGE // 2 - int(str(bouton_haut.cget('borderwidth'))) * 3
            )


if __name__ == '__main__':
    fenetre = tk.Tk()
    fenetre.title('Test Panneau Maintenance')
    pm = PanneauMaintenance(parent=fenetre)
    pm.grid()
    fenetre.mainloop()
