import tkinter as tk

from globales import *

# Redéfinition de la classe tk.Button pour notre usage
class Bouton(tk.Button):
    def __init__(self, master=None, height=None):
        super().__init__(master=master, height=height)
        self.actif = False
        super().config(command=self.clic, bg='white')

    def clic(self):
        self.actif = not self.actif
        if self.actif:
            super().config(bg='green')
        else:
            super().config(bg='white')


class BoutonHaut(Bouton):
    def __init__(self, master=None, height=None):
        super().__init__(master=master, height=height)
        super().config(image=photo_bouton_haut)


class BoutonBas(Bouton):
    def __init__(self, master=None, height=None):
        super().__init__(master=master, height=height)
        super().config(image=photo_bouton_bas)


class BoutonRond(Bouton):
    def __init__(self, master=None, height=None):
        super().__init__(master=master, height=height)
        super().config(image=photo_bouton_rond)


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


class Etages:
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
                0, 0, image=photo_bouton_haut)
            bouton_coordonnees = self.canevas.bbox(bouton_haut)
            hauteur_bouton = bouton_coordonnees[3] - bouton_coordonnees[1]
            self.canevas.coords(
                bouton_haut,
                2 * DIMENSIONS_CABINE[0],
                hauteur_plancher - HAUTEUR_ETAGE / 2 - hauteur_bouton / 2)
            self.boutons_etages_haut[e] = bouton_haut

            bouton_bas = self.canevas.create_image(
                0, 0, image=photo_bouton_bas)
            self.canevas.coords(
                bouton_bas,
                2 * DIMENSIONS_CABINE[0],
                hauteur_plancher - HAUTEUR_ETAGE / 2 + hauteur_bouton / 2)
            self.boutons_etages_bas[e] = bouton_bas


class Capteurs:
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

    def miseAJour(self):
        for i in range(0, NOMBRE_ETAGES):
            if self.etages[i] == cabine.hauteur:
                self.capteurs[i] = True
            else:
                self.capteurs[i] = False
            if self.capteurs[i]:
                self.canevas.itemconfigure(self.dessins[i], fill='red')
            else:
                self.canevas.itemconfigure(self.dessins[i], fill='white')



# Initialisation de tkinter et création du panneau principal
fenetre = tk.Tk()
fenetre.geometry('800x600')
panneau = tk.Frame(fenetre)
panneau.grid()

# Chargement des images
try:
    photo_bouton_haut = tk.PhotoImage(file='haut.gif')
    photo_bouton_bas = tk.PhotoImage(file='bas.gif')
    photo_bouton_rond = tk.PhotoImage(file='rond.gif')
except tk.TclError as e:
    print(
        '''Les images GIF des boutons n'ont pas pu être chargées\n
        Les boutons seront blancs''')

# Création du panneau de maintenance
panneau_maintenance = tk.Frame(panneau)
panneau_maintenance.grid(column=0, row=1)
titre_panneau_maintenance = tk.Label(panneau_maintenance, text="Maintenance")
titre_panneau_maintenance.grid(column=0, row=0)
bouton_maintenance_haut = BoutonHaut(panneau_maintenance)
bouton_maintenance_haut.grid(column=0, row=1)
bouton_maintenance_bas = BoutonBas(panneau_maintenance)
bouton_maintenance_bas.grid(column=0, row=2)

# Création du Titre
panneau_titre = tk.LabelFrame(
    master=panneau, text='Ascenseurs',
    height=DIMENSIONS_CABINE[1],
    width=DIMENSIONS_CABINE[0] * 4,
    bg='white')
panneau_titre.grid(column=1, row=0)
panneau_titre.grid_propagate(0)
titre = tk.Label(master=panneau_titre, text='TITRE', bg='white')
titre.grid()

# Création du puit
panneau_puit = tk.Frame(panneau)
panneau_puit.grid(column=1, row=1)
dessin_puit = tk.Canvas(panneau_puit, bg='white')
dessin_puit.config(
    width=4 * DIMENSIONS_CABINE[0],
    height=NOMBRE_ETAGES * HAUTEUR_ETAGE)
dessin_puit.create_rectangle(
    DIMENSIONS_CABINE[0] / 2,
    0,
    DIMENSIONS_CABINE[0] * 3 / 2,
    NOMBRE_ETAGES * HAUTEUR_ETAGE)
dessin_puit.grid()

# Création du panneau des boutons d'étage
panneau_boutons_etage = tk.Frame(panneau, bg='red')
panneau_boutons_etage.grid(column=2, row=1)
for i in range(0, NOMBRE_ETAGES):
    bouton_haut = BoutonHaut(panneau_boutons_etage)
    bouton_haut.grid(column=0, row=2 * i)
    bouton_haut.config(
        height=HAUTEUR_ETAGE // 2 - int(str(bouton_haut.cget('borderwidth'))) * 3
    )
    bouton_bas = BoutonBas(panneau_boutons_etage)
    bouton_bas.grid(column=0, row=2 * i + 1)
    bouton_bas.config(
        height=HAUTEUR_ETAGE // 2 - int(str(bouton_haut.cget('borderwidth'))) * 3
    )

# Création de la cabine
cabine = Cabine(dessin_puit)

# Création des étages
etages = Etages(dessin_puit)

# Création des capteurs
capteurs = Capteurs(dessin_puit, cabine, etages.etages)


def animation():
    cabine.descente = True if bouton_maintenance_bas.actif else False
    cabine.montee = True if bouton_maintenance_haut.actif else False
    cabine.miseAJour()
    capteurs.miseAJour()
    panneau.after(50, animation)


animation()
fenetre.mainloop()
