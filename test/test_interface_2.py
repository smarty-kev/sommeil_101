"""
Nom du projet: Sommeil 101
Module name: ~

Version: 1.0
Auteur: Kevin Liu
Date de création: 23-09-04
Dernière modification ~ voir GitHub

Description: test de la mise en page
"""

# imports
from tkinter import *
import fonctionnement_du_sommeil


def open_window_fonctionnement():
    main_window.destroy()
    fonctionnement_du_sommeil.open_window_fonctionnement()


def open_main_window():
    main_window = Tk()
    main_window.title("Projet Personnel : Sommeil")
    main_window.geometry("640x480")
    main_window.configure(bg="burlywood2")

    # main_window.iconphoto(False, PhotoImage(file= "bed_icon.png"))

    texte_page_acceuil_titre = "Le sommeil, c'est important!"
    label1 = Label(text=texte_page_acceuil_titre, font=("Times New Roman", 30), bg="burlywood1")
    label1.grid(padx=100, pady=20, columnspan=4, row=0, column=0)

    global img
    img = PhotoImage(file='img.png')
    image_label = Label(main_window, image=img)
    image_label.grid(padx=30, pady=(0, 20), row=1, columnspan=4)

    bt1 = Button(text="Fonctionnement", command=open_window_fonctionnement)
    bt1.grid(row=2, column=0)

    bt2 = Button(text="Troubles")
    bt2.grid(row=2, column=1)

    bt3 = Button(text="Solutions")
    bt3.grid(row=2, column=2)

    bt4 = Button(text="Calculatrice")
    bt4.grid(row=2, column=3)

    bt5 = Button(text="Quitter", command=main_window.destroy)
    bt5.grid(row=3, column=0)

    label_author_credits = Label(text="Par Kevin Liu, F. 511")
    label_author_credits.grid(pady=15, row=3, column=3)
    return main_window

main_window = open_main_window()
main_window.mainloop()
