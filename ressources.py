import tkinter as tk

import logger
from logger import logD, logE

dessin_bouton_haut = None
dessin_bouton_haut_actif = None
dessin_bouton_double_haut = None
dessin_bouton_rond = None
dessin_bouton_bas = None
dessin_bouton_bas_actif = None
dessin_bouton_double_bas = None
images_chargees = False


def chargerDessins():
    try:
        global dessin_bouton_bas
        global dessin_bouton_bas_actif
        global dessin_bouton_double_bas
        global dessin_bouton_haut
        global dessin_bouton_haut_actif
        global dessin_bouton_double_haut
        global dessin_bouton_rond
        global images_chargees
        dessin_bouton_haut = tk.PhotoImage(file='haut.gif')
        dessin_bouton_haut_actif = tk.PhotoImage(file='haut_actif.gif')
        dessin_bouton_double_bas = tk.PhotoImage(file='double_bas.gif')
        dessin_bouton_bas = tk.PhotoImage(file='bas.gif')
        dessin_bouton_bas_actif = tk.PhotoImage(file='bas_actif.gif')
        dessin_bouton_double_haut = tk.PhotoImage(file='double_haut.gif')
        dessin_bouton_rond = tk.PhotoImage(file='rond.gif')
        images_chargees = True
        logD('Dessins chargés !')
    except tk.TclError as e:
        logE('''Les images GIF des boutons n'ont pas pu être chargées''')
        exit()


if __name__ == '__main__':
    logger.initialiser()
    fenetre = tk.Tk()
    canevas = tk.Canvas(fenetre, height=300, width=400)
    canevas.pack()
    chargerDessins()
    pbh = canevas.create_image(0, 0, image=dessin_bouton_haut)

    fenetre.mainloop()
