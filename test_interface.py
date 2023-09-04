"""
Project name: Password Generator and Manager
Module name: pwd_gui

Version: 1.0
Author: Guang Zhu Cui and Kevin
Date added: 22-07-25

Description: Graphics User Interface (GUI) of the project
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
    menubar.add_command(label="Activate CLI mode", )
    menubar.add_command(label="Password Generator", )
    menubar.add_command(label="Password Manager", )
    menubar.add_command(label="Quitter",  command=main_window.destroy)
    menubar.add_separator()

    main_window.config(menu=menubar)
    main_window.mainloop()
