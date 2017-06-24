import tkinter as tk

photo_bouton_haut = None
photo_bouton_rond = None
photo_bouton_bas = None
images_chargees = False


def chargerPhotos():
    try:
        global photo_bouton_bas
        global photo_bouton_haut
        global photo_bouton_rond
        global images_chargees
        photo_bouton_haut = tk.PhotoImage(file='haut.gif')
        photo_bouton_bas = tk.PhotoImage(file='bas.gif')
        photo_bouton_rond = tk.PhotoImage(file='rond.gif')
        images_chargees = True
        print('Photos chargées ! ' + str(type(photo_bouton_rond)))
    except tk.TclError as e:
        print('''Les images GIF des boutons n'ont pas pu être chargées''')
        exit()


if __name__ == '__main__':
    fenetre = tk.Tk()
    canevas = tk.Canvas(fenetre, height=300, width=400)
    canevas.pack()
    chargerPhotos()
    pbh = canevas.create_image(0, 0, image=photo_bouton_haut)

    fenetre.mainloop()
