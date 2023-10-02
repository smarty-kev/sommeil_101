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
    main_window.configure(bg="white")

    # menu
    menubar = Menu(main_window)

    general_menu = Menu(menubar, tearoff=0)
    general_menu.add_command(label="Vue global du sommeil", font=("", 20))
    general_menu.add_command(label="Les stages du sommeil")
    general_menu.add_command(label="Que ce passe t-il quant on dort?")
    general_menu.add_separator()
    menubar.add_cascade(label="Le fonctionnement", menu=general_menu, font=("", 30))

    main_window.config(menu=menubar)

    photo_obj = PhotoImage(file="img.png")
    # source de l'image :
    # https://casperblog.imgix.net/wp-content/uploads/2022/08/how-to-sleep-through-the-night_thumb.png?auto=format
    label = Label(main_window, image=photo_obj)
    label.grid(pady=20, padx=20)


    main_window.mainloop()
