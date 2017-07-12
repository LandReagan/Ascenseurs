import tkinter as tk

from globales import *
from boutons import BoutonRond


class PanneauCabine(tk.LabelFrame):
    """ Le panneau de la cabine définit les boutons ronds des étages, incluant
        le numéro
    """

    def __init__(self, parent, cabine):
        self.arriere_plan = couleur_vert_pale
        self.cabine = cabine
        super().__init__(master=parent, bg=self.arriere_plan, text='Cabine')
        self.grid(column=2, row=0, sticky=tk.N)
        self.rowconfigure(0, minsize=DIMENSIONS_CABINE[1])

        # Définition de la zone de titre de la cabine
        self.titre_cabine = tk.Label(master=self, text='Numéro !')
        self.titre_cabine.grid(column=1, row=0)

        # définition du canevas (dessin) de la porte
        self.canevas_porte = tk.Canvas(
            master=self,
            width=3 * DIMENSIONS_CABINE[0],
            height=3 * DIMENSIONS_CABINE[1],
            bg=couleur_vert_pale
        )
        self.canevas_porte.grid(
            column=0, row=1, rowspan=NOMBRE_ETAGES + 1, sticky=tk.S)
        # Arrière-plan
        self.arriere_plan = self.canevas_porte.create_rectangle(
            DIMENSIONS_CABINE[0] * 1 / 2,
            DIMENSIONS_CABINE[1],
            DIMENSIONS_CABINE[0] * 5 / 2,
            DIMENSIONS_CABINE[1] * 3,
            fill='grey'
        )
        # Porte gauche
        self.porte_gauche = self.canevas_porte.create_rectangle(
            DIMENSIONS_CABINE[0] * 1 / 2,
            DIMENSIONS_CABINE[1],
            DIMENSIONS_CABINE[0] * 3 / 2,
            DIMENSIONS_CABINE[1] * 3,
            fill=couleur_vert_pomme
        )
        # Porte droite
        self.porte_droite = self.canevas_porte.create_rectangle(
            DIMENSIONS_CABINE[0] * 3 / 2,
            DIMENSIONS_CABINE[1],
            DIMENSIONS_CABINE[0] * 5 / 2,
            DIMENSIONS_CABINE[1] * 3,
            fill=couleur_vert_pomme
        )

        # Définition des panneaux d'étage, reprenant le bouton et le numéro
        for i in range(NOMBRE_ETAGES):
            panneau_etage = tk.LabelFrame(self, text=str(i), labelanchor='w')
            panneau_etage.grid(
                column=int(i // 10 + 1), row=NOMBRE_ETAGES - i % 10 + 1)
            bouton = BoutonRond(
                parent=panneau_etage,
                signal='pc_e' + str(i)
            )
            bouton.grid()

    def ouverturePorte(self):
        """ Fonction d'animation de l'ouverture de la porte. Retourne True
            si la porte est ouverte, False tant qu'elle ne l'est pas.
        """
        largeur_porte = self.canevas_porte.coords(self.porte_gauche)[2]\
            - self.canevas_porte.coords(self.porte_gauche)[0]
        if largeur_porte <= 0:
            return True
        self.canevas_porte.coords(
            self.porte_gauche,
            self.canevas_porte.coords(self.porte_gauche)[0],
            self.canevas_porte.coords(self.porte_gauche)[1],
            self.canevas_porte.coords(self.porte_gauche)[2] - 1,
            self.canevas_porte.coords(self.porte_gauche)[3]
        )
        self.canevas_porte.coords(
            self.porte_droite,
            self.canevas_porte.coords(self.porte_droite)[0] + 1,
            self.canevas_porte.coords(self.porte_droite)[1],
            self.canevas_porte.coords(self.porte_droite)[2],
            self.canevas_porte.coords(self.porte_droite)[3]
        )
        return False

    def fermeturePorte(self):
        """ Fonction d'animation de la fermeture de la porte. Retourne True
            si la porte est fermée, False tant qu'elle ne l'est pas.
        """
        interstice_porte = self.canevas_porte.coords(self.porte_droite)[2]\
            - self.canevas_porte.coords(self.porte_gauche)[2]
        if interstice_porte <= 0:
            return True
        self.canevas_porte.coords(
            self.porte_gauche,
            self.canevas_porte.coords(self.porte_gauche)[0],
            self.canevas_porte.coords(self.porte_gauche)[1],
            self.canevas_porte.coords(self.porte_gauche)[2] + 1,
            self.canevas_porte.coords(self.porte_gauche)[3]
        )
        self.canevas_porte.coords(
            self.porte_droite,
            self.canevas_porte.coords(self.porte_droite)[0] - 1,
            self.canevas_porte.coords(self.porte_droite)[1],
            self.canevas_porte.coords(self.porte_droite)[2],
            self.canevas_porte.coords(self.porte_droite)[3]
        )
        return False
