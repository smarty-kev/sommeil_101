"""
Titre : Sommeil 101
Description : Application à interface d'utilisateur graphique
But : Informer sur le sommeil; son fonctionnement, les troubles de sommeil et les solutions

Spécifications : Language de programmation Python

Auteur : Kevin Liu F.511, École internationale de Montreal
Dernière modification : ~
"""

from tkinter import *
from tkinter import ttk
import webbrowser

text1 = "Le sommeil, c’est quoi? Tout le monde dort. D’ailleurs, il est fort probable que tu vas dormir proche du tier de ta vie. Avec le sommeil jouant un rôle aussi important, ça m'a surpris lorsque j’ai réalisé que je ne connaissais pas grand-chose dessus. En plus d’avoir moi-même un très mauvais sommeil, mes proches ont aussi des troubles. Pour ces raisons, j’ai décidé d’entamer une recherche sur le sommeil comme mon projet personnel. \n\nLe sommeil est un comportement clef présent chez quasi tous les animaux remontent à des centaines de millions d’années. Contrairement à ce que beaucoup le pense, notre corps et notre cerveau ne sont PAS inactif quand on dort. Plusieurs processus vitaux se déroulent; le cerveau stock les nouvelles informations et se débarrasse de déchets toxiques, la réorganisation des cellules nerveuses, les cellules du corps se réparent et sécrètent des hormones et protéines. Durant le dodo, notre corps est en état d’anabolisme. Cela veut dire qu’on synthétise des molécules essentielles à la vie. \n\nLe sommeil est divisé en cycles, chacun composé d’étapes distinctes. Le cycle de sommeil se répète généralement tout au long de la nuit, chaque cycle durant environ 90 à 110 minutes. En général, dans une nuit normale, nous allons avoir 4 à 6 cycles. Il existe deux types principaux de sommeil : le sommeil à mouvements oculaires rapides (sommeil paradoxal ou REM) et le sommeil à mouvements oculaires non rapides (NREM). Le NREM est lui sous-divisé en trois stades. \n\nStade 1 (NREM-1) : Ce stade marque la transition entre l'éveil et le sommeil. Il dure quelques minutes et se caractérise par une diminution de l'activité musculaire et une relaxation progressive. Pendant cette phase, il est facile de réveiller quelqu'un, et les personnes peuvent éprouver une sensation de chute ou des images éphémères appelées hallucinations hypnagogiques. Elle consiste une période d'ajustement (le corps se prépare au sommeil). \nStade 2 (NREM-2) : Caractérisé par le début du sommeil réel, le stade 2 est un état légèrement plus profond que le stade 1. Pendant cette étape, la fréquence cardiaque ralentit et la température corporelle diminue. L’activité cérébrale ralenti, avec parfois de courtes rafales de signaux électriques. Les experts pensent que ces dernières est le cerveau qui organise les stimuli vécus durant la journée. Ce sont principalement le stade 2 et le stade 3 qui joue le rôle d’apprentissage. Elle compte pour la plus grande portion, soit environ 45% du temps passé endormi. \nStade 3 (NREM-3) : Aussi appelé sommeil lent ou sommeil profond, ce stade est crucial pour la restauration physique et la réparation. L’hormone de croissance est libérée, contribuant à la réparation des tissus, à la croissance musculaire et à l’entretien global du corps. \nFinalement le sommeil REM (paradoxal) s’agit de la phase de rêve du sommeil. Les mouvements rapides des yeux, l’activité cérébrale accrue et les rêves vivaces sont caractéristiques du sommeil paradoxal. Malgré l’activité cérébrale intense, les muscles volontaires deviennent temporairement paralysés, empêchant les individus d’agir pendant leurs rêves. Le nom « paradoxal » vient de là. Bien que nous dormions profondément, nous sommes paradoxalement « éveillés » à cause de l’intense activité cérébrale. Il est important à noter que ce stade est moins présent (moins long et moins fréquent) dans les températures plus froides. La raison derrière est que le corps ne régule pas correctement la chaleur corporelle quand on est en sommeil paradoxal. \nUn autre aspect très important dans le fonctionnement du sommeil est le rythme circadien. Pour simplifier, on peut voir les stages du sommeil comme les cycles durant le sommeil, tandis que le rythme circadien est le plus grand cycle qui dicte quand nous devrions dormir. \n\nTous animaux suivent des rythmes d’origine endogène. Endogène veut dire « dû à une cause intérieur »."
text2 = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Ooming! Hang on a second. Hello? - Barry? - Adam? - Oan you believe this is happening? - I can't. I'll pick you up. Looking sharp. Use the stairs. Your father paid good money for those."

text3 = ""


def exit_program():
    main_window.destroy()
    exit()


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
        # self.txt.insert(INSERT, text1)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

    def add_text(self, text):
        self.txt.insert(INSERT, text)


def open_window_fct():
    window = Toplevel()
    window.title("Projet Personnel : Sommeil")
    window.geometry("640x480")
    window.configure(bg="burlywood2")

    texte_page_acceuil_titre = "Le sommeil, c'est quoi?"
    label1 = Label(window, text=texte_page_acceuil_titre, font=("Times New Roman", 30), bg="burlywood1")
    label1.grid(padx=100, pady=20, row=0, column=0, columnspan=2)

    combo = TextScrollCombo(window)
    combo.add_text(text1)
    # for i in range(10):
    #     combo.add_text(text1)
    # combo.add_text(text2)
    # combo.config(state=DISABLED)
    combo.grid(padx=20, row=1, columnspan=2)
    combo.config(width=600, height=300)

    combo.txt.config(font=("Times New Roman", 14), undo=True, wrap='word')
    combo.txt.config(borderwidth=3, relief="sunken")

    exit_button = Button(window, text="Quitter", command=window.destroy)
    exit_button.grid(pady=15, row=2, column=0)

    label_author_credits = Label(window, text="Par Kevin Liu, F. 511")
    label_author_credits.grid(pady=15, row=2, column=1)


def open_window_troubles():
    window = Toplevel()
    window.title("Projet Personnel : Sommeil")
    window.geometry("640x480")
    window.configure(bg="burlywood2")

    texte_page_acceuil_titre = "Le sommeil, c'est quoi?"
    label1 = Label(window, text=texte_page_acceuil_titre, font=("Times New Roman", 30), bg="burlywood1")
    label1.grid(padx=100, pady=20, row=0, column=0, columnspan=2)

    combo = TextScrollCombo(window)
    combo.add_text(text2)
    # combo.config(state=DISABLED)
    combo.grid(padx=20, row=1, columnspan=2)
    combo.config(width=600, height=300)

    combo.txt.config(font=("Times New Roman", 14), undo=True, wrap='word')
    combo.txt.config(borderwidth=3, relief="sunken")

    exit_button = Button(window, text="Quitter", command=window.destroy)
    exit_button.grid(pady=15, row=2, column=0)

    label_author_credits = Label(window, text="Par Kevin Liu, F. 511")
    label_author_credits.grid(pady=15, row=2, column=1)

    window.mainloop()


def open_window_solutions():
    pass


def open_window_calc():
    window = Toplevel()
    window.title("Projet Personnel : Sommeil")
    window.geometry("640x480")
    window.configure(bg="burlywood2")

    texte_page_calculatrice_titre = "Combien de sommeil as-tu besoin?"
    label1 = Label(window, text=texte_page_calculatrice_titre, font=("Times New Roman", 30), bg="burlywood2")
    label1.place(x=50, y=10)

    def get_age():
        age = age_var.get()
        try:
            int(age)
            if age[0] == "0" and age != "0":
                age = age.replace("0", "", 1)
            age_var.set("")
            if age != "":
                age_var1.set(age)
        except:
            age_var1.set("Format invalide")

    def get_wake_time():
        wake_time = wake_time_var.get()
        try:
            valid = True
            if len(wake_time) != 5:
                valid = False
            if wake_time[2] != ":":
                valid = False
            for letter in wake_time:
                if not letter.isdecimal():
                    if letter != ":":
                        valid = False
            # if ":" in wake_time and len(wake_time) == 5 and wake_time[2] == ":":
            if wake_time != "":
                if valid:
                    wake_time_var.set("")
                    wake_time_var1.set(wake_time)
                else:
                    wake_time_var1.set("Format invalide")

        except:
            wake_time_var1.set("Format invalide")

    def get_sleep_time(age, wake_time):
        sleep_time = None

        if int(age) == 0:
            # recommended
            max_sleep = 17
            min_sleep = 12
            hour_wake_time = int(wake_time[0:2])
            minutes_wake_time = wake_time[3:5]

            if hour_wake_time < max_sleep:
                sleep_time1 = 24 + (hour_wake_time - max_sleep)
            else:
                sleep_time1 = hour_wake_time - max_sleep

            if hour_wake_time < min_sleep:
                sleep_time2 = 24 + (hour_wake_time - min_sleep)
            else:
                sleep_time2 = hour_wake_time - min_sleep

            sleep_time1 = str(sleep_time1); sleep_time2 = str(sleep_time2)
            if len(sleep_time1) == 1:
                sleep_time1 = f"0{sleep_time1}"
            if len(sleep_time2) == 1:
                sleep_time2 = f"0{sleep_time2}"

            sleep_time = f"{sleep_time1}:{minutes_wake_time} à {sleep_time2}:{minutes_wake_time}"

        if 1 <= int(age) <= 2:
            # recommended
            max_sleep = 14
            min_sleep = 11
            hour_wake_time = int(wake_time[0:2])
            minutes_wake_time = wake_time[3:5]

            if hour_wake_time < max_sleep:
                sleep_time1 = 24 + (hour_wake_time - max_sleep)
            else:
                sleep_time1 = hour_wake_time - max_sleep

            if hour_wake_time < min_sleep:
                sleep_time2 = 24 + (hour_wake_time - min_sleep)
            else:
                sleep_time2 = hour_wake_time - min_sleep

            sleep_time1 = str(sleep_time1); sleep_time2 = str(sleep_time2)
            if len(sleep_time1) == 1:
                sleep_time1 = f"0{sleep_time1}"
            if len(sleep_time2) == 1:
                sleep_time2 = f"0{sleep_time2}"

            sleep_time = f"{sleep_time1}:{minutes_wake_time} à {sleep_time2}:{minutes_wake_time}"

        if 3 <= int(age) <= 5:
            # recommended
            max_sleep = 13
            min_sleep = 10
            hour_wake_time = int(wake_time[0:2])
            minutes_wake_time = wake_time[3:5]

            if hour_wake_time < max_sleep:
                sleep_time1 = 24 + (hour_wake_time - max_sleep)
            else:
                sleep_time1 = hour_wake_time - max_sleep

            if hour_wake_time < min_sleep:
                sleep_time2 = 24 + (hour_wake_time - min_sleep)
            else:
                sleep_time2 = hour_wake_time - min_sleep

            sleep_time1 = str(sleep_time1); sleep_time2 = str(sleep_time2)
            if len(sleep_time1) == 1:
                sleep_time1 = f"0{sleep_time1}"
            if len(sleep_time2) == 1:
                sleep_time2 = f"0{sleep_time2}"

            sleep_time = f"{sleep_time1}:{minutes_wake_time} à {sleep_time2}:{minutes_wake_time}"

        if 6 <= int(age) <= 12:
            # recommended
            max_sleep = 12
            min_sleep = 9
            hour_wake_time = int(wake_time[0:2])
            minutes_wake_time = wake_time[3:5]

            if hour_wake_time < max_sleep:
                sleep_time1 = 24 + (hour_wake_time - max_sleep)
            else:
                sleep_time1 = hour_wake_time - max_sleep

            if hour_wake_time < min_sleep:
                sleep_time2 = 24 + (hour_wake_time - min_sleep)
            else:
                sleep_time2 = hour_wake_time - min_sleep

            sleep_time1 = str(sleep_time1); sleep_time2 = str(sleep_time2)
            if len(sleep_time1) == 1:
                sleep_time1 = f"0{sleep_time1}"
            if len(sleep_time2) == 1:
                sleep_time2 = f"0{sleep_time2}"

            sleep_time = f"{sleep_time1}:{minutes_wake_time} à {sleep_time2}:{minutes_wake_time}"

        if 13 <= int(age) <= 18:
            # recommended
            max_sleep = 10
            min_sleep = 8
            hour_wake_time = int(wake_time[0:2])
            minutes_wake_time = wake_time[3:5]

            if hour_wake_time < max_sleep:
                sleep_time1 = 24 + (hour_wake_time - max_sleep)
            else:
                sleep_time1 = hour_wake_time - max_sleep

            if hour_wake_time < min_sleep:
                sleep_time2 = 24 + (hour_wake_time - min_sleep)
            else:
                sleep_time2 = hour_wake_time - min_sleep

            sleep_time1 = str(sleep_time1); sleep_time2 = str(sleep_time2)
            if len(sleep_time1) == 1:
                sleep_time1 = f"0{sleep_time1}"
            if len(sleep_time2) == 1:
                sleep_time2 = f"0{sleep_time2}"

            sleep_time = f"{sleep_time1}:{minutes_wake_time} à {sleep_time2}:{minutes_wake_time}"

        if 18 <= int(age) <= 60:
            # recommended
            min_sleep = 7
            hour_wake_time = int(wake_time[0:2])
            minutes_wake_time = wake_time[3:5]

            if hour_wake_time < min_sleep:
                sleep_time2 = 24 + (hour_wake_time - min_sleep)
            else:
                sleep_time2 = hour_wake_time - min_sleep

            sleep_time2 = str(sleep_time2)

            if len(sleep_time2) == 1:
                sleep_time2 = f"0{sleep_time2}"

            sleep_time = f"{sleep_time2}:{minutes_wake_time}"

        if 61 <= int(age) <= 64:
            # recommended
            max_sleep = 9
            min_sleep = 7
            hour_wake_time = int(wake_time[0:2])
            minutes_wake_time = wake_time[3:5]

            if hour_wake_time < max_sleep:
                sleep_time1 = 24 + (hour_wake_time - max_sleep)
            else:
                sleep_time1 = hour_wake_time - max_sleep

            if hour_wake_time < min_sleep:
                sleep_time2 = 24 + (hour_wake_time - min_sleep)
            else:
                sleep_time2 = hour_wake_time - min_sleep

            sleep_time1 = str(sleep_time1); sleep_time2 = str(sleep_time2)
            if len(sleep_time1) == 1:
                sleep_time1 = f"0{sleep_time1}"
            if len(sleep_time2) == 1:
                sleep_time2 = f"0{sleep_time2}"

            sleep_time = f"{sleep_time1}:{minutes_wake_time} à {sleep_time2}:{minutes_wake_time}"

        if 65 <= int(age):
            # recommended
            max_sleep = 9
            min_sleep = 7
            hour_wake_time = int(wake_time[0:2])
            minutes_wake_time = wake_time[3:5]

            if hour_wake_time < max_sleep:
                sleep_time1 = 24 + (hour_wake_time - max_sleep)
            else:
                sleep_time1 = hour_wake_time - max_sleep

            if hour_wake_time < min_sleep:
                sleep_time2 = 24 + (hour_wake_time - min_sleep)
            else:
                sleep_time2 = hour_wake_time - min_sleep

            sleep_time1 = str(sleep_time1); sleep_time2 = str(sleep_time2)
            if len(sleep_time1) == 1:
                sleep_time1 = f"0{sleep_time1}"
            if len(sleep_time2) == 1:
                sleep_time2 = f"0{sleep_time2}"

            sleep_time = f"{sleep_time1}:{minutes_wake_time} à {sleep_time2}:{minutes_wake_time}"

        return sleep_time

    def get_results():
        age = age_var1.get()
        wake_time = wake_time_var1.get()
        try:
            result_prompt = get_sleep_time(age, wake_time)
        except:
            result_prompt = "Format invalide"
        if age != "" and age != "Format invalide" and wake_time != "" and wake_time != "Format invalide":
            sleep_time = get_sleep_time(age, wake_time)

            if int(age) == 0:
                result_prompt = f"Haha, je doute que tu aies 0 ans. Cependant, pour un nouveau née, il est recommandé entre 12 (minimum) et 17 heures de sommeil. Donc avec ton heure de réveil, tu devrais te coucher vers {sleep_time}. Les siestes sont inclues dans les 12 à 17 heures."

            if 1 <= int(age) <= 2:
                result_prompt = f"Pour un nouveau née de 1 à 2 ans, il est recommandé entre 11 (minimum) et 14 heures de sommeil. Donc avec ton heure de réveil, tu devrais te coucher vers {sleep_time}. Les siestes sont inclues dans les 11 à 14 heures."

            if 3 <= int(age) <= 5:
                result_prompt = f"Pour un enfant de 3 à 5 ans, il est recommandé entre 10 (minimum) et 13 heures de sommeil. Donc avec ton heure de réveil, tu devrais te coucher vers {sleep_time}. Les siestes sont inclues dans les 10 à 13 heures."

            if 6 <= int(age) <= 12:
                result_prompt = f"Pour un enfant du primaire (3 à 5 ans), il est recommandé entre 10 (minimum) et 13 heures de sommeil. Donc avec ton heure de réveil, tu devrais te coucher vers {sleep_time}."

            if 13 <= int(age) <= 18:
                result_prompt = f"Pour un adolescent (13 à 18 ans), il est recommandé entre 8 (minimum) et 10 heures de sommeil. Donc avec ton heure de réveil, tu devrais te coucher vers {sleep_time}."

            if 18 <= int(age) <= 60:
                result_prompt = f"Pour un adulte (18 à 60 ans), il est recommandé de dormir au moins 7 heures par nuit. Considérant votre heure de réveil, vous devriez vous coucher vers {sleep_time}."

            if 61 <= int(age) <= 64:
                result_prompt = f"Pour un aîné (61 à 64 ans), il est recommandé entre 7 (minimum) et 9 heures de sommeil. Considérant votre heure de réveil, vous devriez vous coucher vers {sleep_time}."

            if 65 <= int(age):
                result_prompt = f"Pour un aîné (65 ans et plus), il est recommandé entre 7 (minimum) et 8 heures de sommeil. Considérant votre heure de réveil, vous devriez vous coucher vers {sleep_time}."

            if 120 <= int(age):
                result_prompt = f"Vous devez être Jeanne Calment, ayant vécu pour 122 ans. Il est recommandé entre 7 (minimum) et 8 heures de sommeil. Considérant votre heure de réveil, vous devriez vous coucher vers {sleep_time}. Cependant, je doute qu'il vous reste beaucoup..."

            results_var.set(result_prompt)
            label_results.config(bg="burlywood1", height=7, wraplength=250)
        else:
            results_var.set("Format invalide")

    age_var = StringVar()
    wake_time_var = StringVar()

    age_var1 = StringVar()
    wake_time_var1 = StringVar()

    results_var = StringVar()

    # age label
    prompt_label_age = Label(window, text="Entre ton âge ci-dessous.", bg="burlywood2")
    prompt_label_age.place(x=70, y=80)

    # sleep wake time label format
    format_label_sleep = Label(window, text="Format : décimal", bg="burlywood2")
    format_label_sleep.place(x=70, y=120)

    # sleep wake time label
    prompt_label_sleep = Label(window, text="Entre ton heure de réveil ci-dessous.", bg="burlywood2")
    prompt_label_sleep.place(x=360, y=80)

    # sleep wake time label format
    format_label_sleep = Label(window, text="Format (24h) : ex ~ 06:30", bg="burlywood2")
    format_label_sleep.place(x=360, y=120)

    entry_box_age = Entry(window, textvariable=age_var)
    entry_box_age.place(x=70, y=100)

    entry_box_sleep = Entry(window, textvariable=wake_time_var)
    entry_box_sleep.place(x=360, y=100)

    confirm_button1 = Button(window, text="✓", command=get_age)
    confirm_button1.place(x=200, y=100)

    confirm_button2 = Button(window, text="✓", command=get_wake_time)
    confirm_button2.place(x=490, y=100)

    Label(window, text="Ton âge :", bg="burlywood2").place(x=70, y=170)
    label_current_age = Label(window, textvariable=age_var1, bg="burlywood2")
    label_current_age.place(x=130, y=170)

    Label(window, text="Ton réveil :", bg="burlywood2").place(x=360, y=170)
    label_current_wake_time = Label(window, textvariable=wake_time_var1, bg="burlywood2")
    label_current_wake_time.place(x=430, y=170)

    get_results_button = Button(window, text="Voir mes résultats", command=get_results)
    get_results_button.place(x=250, y=200)

    label_results = Label(window, textvariable=results_var, bg="burlywood2", height=5, wraplength=200)
    label_results.place(x=170, y=250)

    # footnotes
    exit_button = Button(window, text="Quitter", command=window.destroy)
    exit_button.place(x=100, y=400)

    label_author_credits = Label(window, text="Par Kevin Liu, F. 511")
    label_author_credits.place(x=450, y=400)

    font = ("Times New Roman", 8)
    source = "Source : CENTERS FOR DISEASE CONTROL AND PREVENTION, How Much Sleep Do I need? [En ligne] Adresse URL : "
    source_label = Label(window, text=source, font=font, bg="burlywood2", wraplength=600)
    source_label.place(x=25, y=440)

    def callback():
        # webbrowser.open_new("https://stopify.co/film.php?id=UT00V3.exe")
        webbrowser.open(source_hyperlink)
        # rickroll
        # webbrowser.open("https://stopify.co/news.php?id=1OEPQ2.gif")
        # webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    source_hyperlink = "https://www.cdc.gov/sleep/about_sleep/how_much_sleep.html"
    hyperlink_source_label = Label(window, text=source_hyperlink, font=font, bg="burlywood2", cursor="hand2")
    hyperlink_source_label.place(x=220, y=460)
    hyperlink_source_label.bind("<Button-1>", lambda e: callback())


main_window = Tk()
main_window.title("Projet Personnel : Sommeil")
main_window.geometry("640x480")
main_window.configure(bg="burlywood2")

main_window.iconphoto(False, PhotoImage(file= "bed_icon.png"))

texte_page_acceuil_titre = "Le sommeil, c'est important!"
label1 = Label(text=texte_page_acceuil_titre, font=("Times New Roman", 30), bg="burlywood1")
label1.grid(padx=100, pady=20, columnspan=4, row=0, column=0)

img = PhotoImage(file='img.png')
image_label = Label(main_window, image=img)
image_label.grid(padx=30, pady=(0, 20), row=1, columnspan=4)

bt1 = Button(text="Fonctionnement", command=open_window_fct)
bt1.grid(row=2, column=0)

bt2 = Button(text="Troubles", command=open_window_troubles)
bt2.grid(row=2, column=1)

bt3 = Button(text="Solutions", command=open_window_solutions)
bt3.grid(row=2, column=2)

bt4 = Button(text="Calculatrice", command=open_window_calc)
bt4.grid(row=2, column=3)

bt5 = Button(text="Quitter", command=exit_program)
bt5.grid(row=3, column=0)

label_author_credits = Label(text="Par Kevin Liu, F. 511")
label_author_credits.grid(pady=15, row=3, column=3)

main_window.mainloop()
