import tkinter as tk

from globales import *
import ressources
from boutons import *

from cabine import Cabine
from etages import Etages
from capteurs import Capteurs


# Initialisation de tkinter et création du panneau principal
fenetre = tk.Tk()
fenetre.geometry('800x600')
panneau = tk.Frame(fenetre)
panneau.grid()
ressources.chargerPhotos()


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
