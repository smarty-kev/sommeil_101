# imports
from tkinter import *
import tkinter.ttk as ttk


# text_file = open("text_fonctionnement_sommeil.txt", "r")
# text = text_file.readlines()
text = "Tout le monde dort pour environ le quart jusqu’au tier de sa vie." \
       " Contrairement à ce que beaucoup le pense, le corps et le surtout le cerveau ne sont PAS inactif." \
       " Durant le sommeil, beaucoup de procès biologique vitaux se déroulent : le cerveau stock les nouvelles informations et se débarrasse de déchets toxiques, réorganisation des cellules nerveuses," \
       " les cellules du corps se réparent et sécrètent des hormones et protéines."\
       "\n\nFait intéressant : Dans le 19e siècle, dans la société occidentale, la plupart dormait « deux fois »." \
       " Une fois à 9 ou 10pm pour environ 3 heures." \
       " Par la suite, les gens se lèvent pour pratiquer des taches banales avant de se rendormir une fois, pour finalement se réveiller une deuxième fois, à l’aube." \
       " Ce n’est qu’avec la Révolution Industrielle, où la lumière artificielle se développa qu’un sommeil continu devint normalisé. " \
       "Dans presque toutes les sociétés préindustrielles, il y a évidence de sommeil biphasique."

class TextScrollCombo(ttk.Frame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = Text(self)
        self.txt.insert(INSERT, text)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set


def open_window_fonctionnement():
    global window
    window = Tk()
    window.title("Projet Personnel : Sommeil")
    window.geometry("640x480")
    window.configure(bg="burlywood2")

    window.iconphoto(False, PhotoImage(file= "bed_icon.png"))

    texte_page_acceuil_titre = "Le sommeil, c'est quoi?"
    label1 = Label(text=texte_page_acceuil_titre, font=("Times New Roman", 30), bg="burlywood1")
    label1.grid(padx=100, pady=20, row=0, column=0)

    combo = TextScrollCombo(window)
    combo.grid(padx=20, row=1, columnspan=2)
    combo.config(width=600, height=300)

    combo.txt.config(font=("Times New Roman", 14), undo=True, wrap='word')
    combo.txt.config(borderwidth=3, relief="sunken")

    label_author_credits = Label(text="Par Kevin Liu, F. 511")
    label_author_credits.grid(pady=15, row=2)

    window.mainloop()

# open_window_fonctionnement()