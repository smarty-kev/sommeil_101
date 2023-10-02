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


def open_main_window():
    main_window = Tk()
    main_window.title("Projet Personnel : Sommeil")
    main_window.geometry("640x480")
    main_window.configure(bg="burlywood2")

    main_window.iconphoto(False, PhotoImage(file= "bed_icon.png"))

    texte_page_acceuil_titre = "Le sommeil, c'est important!"
    label1 = Label(text=texte_page_acceuil_titre, font=("Times New Roman", 30), bg="burlywood1")
    label1.grid(padx=100, pady=20, columnspan=4, row=0, column=0)

    photo_obj = PhotoImage(file="img.png")
    # source de l'image :
    # https://casperblog.imgix.net/wp-content/uploads/2022/08/how-to-sleep-through-the-night_thumb.png?auto=format
    label_image = Label(main_window, image=photo_obj)
    label_image.grid(pady=30, row=1, columnspan=4, column=0)

    button_1 = Button(text="1")
    button_1.grid(padx=50, row=2, column=0)

    button_2 = Button(text="2")
    button_2.grid(row=2, column=1)

    button_3 = Button(text="3")
    button_3.grid(row=2, column=2)

    button_4 = Button(text="4")
    button_4.grid(row=2, column=3)

    label_author_credits = Label(text="Par Kevin Liu, F. 511")
    label_author_credits.grid(pady=15, row=3, column=3)

    main_window.mainloop()
