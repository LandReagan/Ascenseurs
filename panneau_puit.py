import tkinter as tk

from globales import *

class PanneauPuit(tk.Frame):
    """ Le panneau du puit est la partie centrale de l'interface.
        On y trouve le titre et le canevas de dessin des étages, des
        capteurs, des boutons d'étage, des utilisateurs et de la cabine
    """

    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(column=1, row=0)
        self.rowconfigure(0, minsize=DIMENSIONS_CABINE[1])

        # Création du Titre
        self.panneau_titre = tk.LabelFrame(
            master=self, text='Ascenseurs',
            height=DIMENSIONS_CABINE[1],
            width=DIMENSIONS_CABINE[0] * 4,
            bg='white')
        self.panneau_titre.grid(column=0, row=0)
        self.titre = tk.Label(
            master=self.panneau_titre, text='TITRE', bg='white')
        self.titre.grid()

        # Création de la zone de dessin pour le puit d'ascenseur
        self.dessin_puit = tk.Canvas(self, bg='white')
        self.dessin_puit.config(
            width=4 * DIMENSIONS_CABINE[0],
            height=NOMBRE_ETAGES * HAUTEUR_ETAGE)
        self.dessin_puit.create_rectangle(
            DIMENSIONS_CABINE[0] / 2,
            0,
            DIMENSIONS_CABINE[0] * 3 / 2,
            NOMBRE_ETAGES * HAUTEUR_ETAGE)
        self.dessin_puit.grid(column=0, row=1)


if __name__ == '__main__':
    fenetre = tk.Tk()
    pp = PanneauPuit(fenetre)
    pp.grid()
    fenetre.mainloop()
