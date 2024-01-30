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

texte_fonctionnement = "Le sommeil, c’est quoi? Tout le monde dort. D’ailleurs, il est fort probable que tu vas dormir proche du tier de ta vie. Avec le sommeil jouant un rôle aussi important, ça m'a surpris lorsque j’ai réalisé que je ne connaissais pas grand-chose dessus. En plus d’avoir moi-même un très mauvais sommeil, mes proches ont aussi des troubles. Pour ces raisons, j’ai décidé d’entamer une recherche sur le sommeil comme mon projet personnel. \n\nLe sommeil est un comportement clef présent chez quasi tous les animaux remontent à des centaines de millions d’années. Contrairement à ce que beaucoup le pense, notre corps et notre cerveau ne sont PAS inactif quand on dort. Plusieurs processus vitaux se déroulent; le cerveau stock les nouvelles informations et se débarrasse de déchets toxiques, la réorganisation des cellules nerveuses, les cellules du corps se réparent et sécrètent des hormones et protéines. Durant le dodo, notre corps est en état d’anabolisme. Cela veut dire qu’on synthétise des molécules essentielles à la vie. \n\nLe sommeil est divisé en cycles, chacun composé d’étapes distinctes. Le cycle de sommeil se répète généralement tout au long de la nuit, chaque cycle durant environ 90 à 110 minutes. En général, dans une nuit normale, nous allons avoir 4 à 6 cycles. Il existe deux types principaux de sommeil : le sommeil à mouvements oculaires rapides (sommeil paradoxal ou REM) et le sommeil à mouvements oculaires non rapides (NREM). Le NREM est lui sous-divisé en trois stades. \n\nStade 1 (NREM-1) : Ce stade marque la transition entre l'éveil et le sommeil. Il dure quelques minutes et se caractérise par une diminution de l'activité musculaire et une relaxation progressive. Pendant cette phase, il est facile de réveiller quelqu'un, et les personnes peuvent éprouver une sensation de chute ou des images éphémères appelées hallucinations hypnagogiques. Elle consiste une période d'ajustement (le corps se prépare au sommeil). \nStade 2 (NREM-2) : Caractérisé par le début du sommeil réel, le stade 2 est un état légèrement plus profond que le stade 1. Pendant cette étape, la fréquence cardiaque ralentit et la température corporelle diminue. L’activité cérébrale ralenti, avec parfois de courtes rafales de signaux électriques. Les experts pensent que ces dernières est le cerveau qui organise les stimuli vécus durant la journée. Ce sont principalement le stade 2 et le stade 3 qui joue le rôle d’apprentissage. Elle compte pour la plus grande portion, soit environ 45% du temps passé endormi. \nStade 3 (NREM-3) : Aussi appelé sommeil lent ou sommeil profond, ce stade est crucial pour la restauration physique et la réparation. L’hormone de croissance est libérée, contribuant à la réparation des tissus, à la croissance musculaire et à l’entretien global du corps. \nFinalement le sommeil REM (paradoxal) s’agit de la phase de rêve du sommeil. Les mouvements rapides des yeux, l’activité cérébrale accrue et les rêves vivaces sont caractéristiques du sommeil paradoxal. Malgré l’activité cérébrale intense, les muscles volontaires deviennent temporairement paralysés, empêchant les individus d’agir pendant leurs rêves. Le nom « paradoxal » vient de là. Bien que nous dormions profondément, nous sommes paradoxalement « éveillés » à cause de l’intense activité cérébrale. Il est important à noter que ce stade est moins présent (moins long et moins fréquent) dans les températures plus froides. La raison derrière est que le corps ne régule pas correctement la chaleur corporelle quand on est en sommeil paradoxal. \nUn autre aspect très important dans le fonctionnement du sommeil est le rythme circadien. Pour simplifier, on peut voir les stages du sommeil comme les cycles durant le sommeil, tandis que le rythme circadien est le plus grand cycle qui dicte quand nous devrions dormir. \n\nTous animaux suivent des rythmes d’origine endogène. Endogène veut dire « dû à une cause intérieur ». Pour nous, les humains, ce cycle est d’environ 24 heures (une journée). Nous avons tous ce rythme synchronisé à l’alternance jour/nuit (avec l’aide de cellules rétiniennes spécialisées). Le mot circadien a ses racines latines comme suit; circa : environ et dies : jour. Le principal organe qui contrôle le rythme chez nous est le noyau suprachiasmatique (NSC) situé dans l’hypothalamus. Lorsque la lumière (peu importe la source) atteint la rétine de l’œil, cette dernière envoie des signaux au NSC indiquant s’il est jour ou nuit. Pour résumer, le rythme circadien est un crucial à la biologie humaine, régulant de nombreux aspects de nos vies quotidiennes. Maintenir un cycle circadien régulier contribue à la santé globale et à la performance quotidienne. \nLa mélatonine fut découvert en 1958 par le professeur Aaron B. Lerner. C’est un neurotransmetteur produit dans plusieurs organismes tels des bactéries et des vertèbres. Dans le contexte de mon projet, la mélatonine joue un rôle important dans les cycles de sommeils. Cependant, elle joue d’autres rôles; antioxydant, système immunitaire, régulation du poids. Il est hypothétisé que l’hormone est synthétisée dans les mitochondries et les chloroplastes, avec sa production s’effectuant en l’absence de lumière. On peut dire qu’elle a pour rôle d’aviser le corps que la nuit est arrivée. \nL’hormone polaire de la mélatonine est le cortisol et est souvent appelé l’hormone du stress. Il est nécessaire pour notre fonctionnement quotidien et joue un rôle important dans notre métabolisme et le contrôle de notre pression artérielle. Dans le sommeil, elle active l’organisme au moment du levée. \nClickez sur Image 1 (en dessous) pour voir un graph dépitant la quantité de mélatonine, de cortisol et d’hormone de croissance en fonction de l’heure du jour. \nNous pouvons voir que durant les heures menant au sommeil et durant celui-ci, la quantité de mélatonine augment graduellement. Par la suite, nous voyons aussi la graduelle diminution de la mélatonine, simultané à la graduelle croissance du cortisol dans l’individu. \n\nPour parler des différents procédés qui ont cours quand on dort, nous allons voir que le corps s’engages dans plusieurs procédés de réparation. L’hormone de croissance est libérée en grande quantité (on peut encore une fois référer à l’Image 1 pour voir ce phénomène) et cette dernière favorise la croissance et régénération des tissus. Il est souvent dit que « si on veut grandir, il faut bien dormir ». Cette affirmation est à 100% vrai et un manque de sommeil au long terme peut nuire à la croissance d’un enfant. \n Pendant le sommeil, les cellules du corps sont plus actives dans la synthèse des protéines, la régénération cellulaire et la consolidation des processus métaboliques. Ces procédés contribuent à la récupération des muscles, à la réparation des tissus, et au renforcement du système immunitaire. \n\nPour conclure, le sommeil est essentiel et contribue à la santé physique, mentale et émotionnelle. Les cycles et stades du sommeil jouent un rôle clé dans la restauration physique, la consolidation de la mémoire et la régulation émotionnelle. Il faut accorder une attention particulière à un rythme circadien régulier et à des pratiques de sommeil saines, on peut favoriser une vitalité renouvelée et une résilience accrue au quotidien."
texte_troubles = "Aujourd’hui, proche de 30% de tous les adultes se décrivent comme ayant du mal à dormir ou un sommeil non réparateur. L’insomnie et d’autres difficultés sont de plus en plus fréquents. Selon eSantéMentale, environ une personne sur dix « souffre de problèmes de sommeil si sérieux qu’elle éprouve des difficultés ou de la détresse pendant la journée ». Plusieurs facteurs peuvent affecter notre sommeil. \n\nD’un, comme mentionné dans la partie sur le fonctionnement, la luminosité (la lumière) est un signal important dans le cycle de sommeil. Pendant plus de 99% de notre existence, la nuit était noire. Cependant, avec l’invention de la lumière artificielle, nos cycles furent très perturbés. Cette invention ingénieuse qui nous a permis d’être plus productif était aussi une épée à double face en supprimant ou réduisant la sécrétion de la mélatonine (que si tu as oublié, est l’hormone qui est responsable de réguler le sommeil). De plus, dans les dernières années, une nouvelle menace s’est introduite dans nos vies; le cellulaire. Une utilisation de cette dernière avant le coucher est très nocif en raison de la lumière bleue. \nLa lumière bleue est émise de façon naturelle par le soleil et fait partie du spectre de la lumière visible. Malheureusement, en plus provoquer une fatigue oculaire et parfois de l’inconfort aux yeux, elle perturbe notre rythme circadien (horloge interne). Dans une étude fait par des chercheurs de Harvard, on remarqua que la suppression de la mélatonine fut deux fois plus longue lorsque le participant est exposé à de la lumière bleue que de la lumière verte (de similaire luminosité). Parallèlement, le décalage dans le rythme circadien fut aussi deux fois plus. Dans une autre étude, fait cette fois par l’Université de Toronto, compara des patients exposés à de des lumières vifs portant des lunettes anti-lumière-bleue à des patients exposés à des lumières sombres. La similitude des niveaux de mélatonine valide l’hypothèse que la lumière bleue est un suppresseur de mélatonine. De plus, l’utilisation excessive des smartphones augmente le niveau de cortisol (hormone polaire de la mélatonine, l’hormone du stress). \nSur le sujet du stress, ce dernier est aussi un facteur important dans le mauvais sommeil. Il est important de noter que ce dernier peut devenir un cercle vicieux; le manque de sommeil cause l’individu à stresser plus, ainsi affectant le sommeil encore plus. \nLe stress est une réponse dans le mécanisme de fuite ou combat, élément clef de notre système nerveux. Dans le temps où nos ancêtres vivaient dans la nature, pouvoir rester éveillé durant la nuit pour fuir aux dangers était primordial à notre survie. En revanche, aujourd’hui, ce stress est souvent lié directement à l’insomnie. Les pensées anxieuses et les préoccupations peuvent souvent occuper les nuits de personnes affectées. La performance scolaire est un exemple parfait de ce cercle vicieux. De hautes attentes et la peur de l’échec engendrent du stress, par conséquence du mauvais sommeil, et donc une prophétie autoréalisatrice. \n\nD’autres facteurs pouvant provoquer des troubles de sommeil incluent; le manque d’exercice, le vieillissement et les problèmes médicaux. Le fait d’être assis pendant des heures à l’école ou au travail est une autre cause du problème grandissant. Bien sûr, la quantité d’exercices dépend de plusieurs facteurs comme l’âge ou le sexe, mais en général, l’Association cardiaque américain recommande environ 150 minutes d’exercice par semaine, pour un adulte. Cela contribue à la santé en général, incluant un meilleur sommeil. \n\nMaintenant, parlons de troubles de sommeil. Ces derniers sont séparés en six catégories; l’insomnie, les troubles respiratoires liés au sommeil, les troubles de l’hypersomnolence, les troubles du rythme circadiens, les parasomnies et les troubles du mouvement liés au sommeil. Certains troubles de sommeil s’enlacent ou sont similaires/reliés. \nIl est sans doute que le trouble le plus prévalent est l’insomnie. Selon la clinique de Cleveland, un sur trois adultes ont des symptômes et 10% des adultes ont les critères du trouble de l’insomnie. Ce dernier est caractérisé par une difficulté à s’endormir et/ou à rester endormi. Les personnes atteintes de l’insomnie ont pourtant souvent un désir de dormir et du temps disponible à ce fin. On qualifie une personne comme ayant de l’insomnie chronique lorsqu’elle présente ces symptômes au moins 3 fois par semaine et pendant au moins trois mois. Bien que pour certains, l’insomnie peut être simplement une inconvenance, pour d’autres elle peut être très néfaste. Que ce soit avoir de du trouble à s’endormir, (insomnie initial), se réveiller au milieu de la nuit (le plus commun, insomnie du milieu) ou de se réveiller plus tôt (insomnie tardif), les effets sur le quotidien sont plusieurs; des réponses retardées, comme réagir trop lentement lorsque quand un conduit, difficulté à se souvenir de choses, confusion ou des difficultés de concentration, des perturbations de l'humeur, notamment de l'anxiété, de la dépression et de l'irritabilité, d'autres perturbations dans votre travail, vos activités sociales, vos passe-temps ou autres activités habituelles.  Bien que les scientifiques n’aient pas compris parfaitement l’insomnie encore, certains facteurs peuvent la causer ou y contribuer. Ces derniers incluent les gènes, l’activité cérébrale, des conditions médicaux, la santé mentale, l’alcool et d’autres circonstances (comme le stress et les routines). Lorsque l’insomnie devient trop sévère, il y a une privation (manque) de sommeil. Comme mentionné avant, il est très dangereux de conduire ou d’effectuer d’autres tâches nécessitant l’attention. La privation de sommeil augmente entre autres les risques de; dépression, anxiété, hypertension artérielle, crise cardiaque, accident vasculaire cérébral, diabète, obésité et la psychose. Si tu as ces symptômes ou tu te sens à risque, consultes rapidement un médecin (avise tes parents si tu es jeunes). \n\nLa narcolepsie est un trouble de l’hypersomnolence. Sa caractéristique définissant est l’envie presque irrésistible de s’endormir durant le jour. On surnomme cette envie des « attaques de sommeil ». D’autres symptômes incluent la cataplexie (faiblesse soudaine dans les muscles), des hallucinations reliées au sommeil ainsi que la paralysie du sommeil. \nCette dernière peut être très angoissant pour la victime; la victime se réveille (parfois, elle se réveille pleinement), mais elle ne peut bouger. Elle peut durer de quelques minutes à quelques heures. La raison derrière cela est intéressante. Durant le sommeil paradoxal (REM), le cerveau empêche les membres de bouger afin de protéger le dormeur d’agir ses rêves. Pareillement, le somnambulisme, souvent appelé « sleep-walking », est le trouble inverse. Pour revenir à la paralysie de sommeil, cette dernière survient lorsque qu’on rentre ou on sort du sommeil paradoxal. \nLa narcolepsie est séparée en deux catégories, une avec la cataplexie et une sans. Pour ne pas entrer trop en détail, seulement 20% sont de type 1 (avec cataplexie). La cataplexie est aussi parfois causée par certaines émotions. \n\nPour conclure, il existe une pléthore d’autres troubles (il en existe trop et certains sont trop scientifiques, donc je ne vais pas les expliquer). Par exemple le « jet lag » ou décalage horaire, le syndrome des jambes sans repos (envie presque irrésistible de bouger les jambes) ou des troubles reliés à la respiration. Certains sont peu nocifs et temporaires (comme le jet lag), tandis que d’autres peuvent être sérieux et nécessiter l’attention d’un professionnel. \nIl existe toutefois des méthodes/tests qu’un peut prendre. La polysomnographie (en laboratoire) est un examen médical courant utilisée afin de déterminer certains troubles. Des formats maisons sont aussi disponible (cependant elles sont moins complètes). Les avancés récentes ont aussi permet d’avoir une montre intelligente (à quelques centaines de dollars) permettant de faire un suivi des cycles de sommeil. (Voire Image 1 pour un exemple.) Maintenant, si tu ne le pas lu encore, tu peux visiter la page sur les solutions (retournes à la page d’accueil) pour des astuces afin d’éviter ces troubles."
texte_solutions = "Comme mentionné auparavant, il y a plusieurs facteurs jouant dans la qualité de sommeil. Une bonne nuit de sommeil peut régler d’innombrables problèmes qu’on pense avoir aucun rapport avec dormir. Si tu veux grandir, il faut bien dormir. Si tu es malade, le sommeil est primordial (ton corps va s’endormir lui-même parfois). Si tu veux bien performer à l’école, le sommeil joue un rôle clef dans l’apprentissage. Si tu te sens mal ou anxieux, le sommeil va aider. Bref, le « dodo » n’est pas à négliger. \n\nPour commencer, qu’est-ce une « une bonne routine de sommeil » ? Premièrement, il est essentiel de se fixer une heure précise à commencer sa routine. Certains recommandent une alarme, non pour se réveiller, mais plutôt pour commencer sa routine pré-dodo. Si tu veux savoir à quelle heure tu devrais te coucher, réfères-toi à la calculatrice que j’ai créée (retournes à la page d’accueil). Par la suite, lorsque l’heure arrive, la routine pré-dodo est cruciale. Des habitudes et des actions répétitifs à chaque soir permet de « dire » au cerveau qu’il est temps de dormir (aujourd’hui, la lumière artificielle est extrêmement perturbatrice dans ce cycle). Cela peut inclure des actions banales comme se brosser les dents ou tenir à jour son journal personnel. Tu peux aussi préparer pour tes choses pour le lendemain (comme ranger ton sac), abattant deux oiseaux d’une pierre; un esprit agité ne peut bien se reposer parce que le stress est une des causes du mauvais sommeil. Finalement, c’est le temps de dormir. Cependant, si tu n’arrives pas à t’endormir pendant longtemps; c’est correct de se lever et recommencer sa routine. Essaye de la méditation (tu peux refléter sur ta journée, ex : ce que tu es reconnaissant) ou lis quelques pages d’un livre. Il ne faut pas oublier que des habitudes saines ne se forment pas instantanément, donc décourages toi pas si tout ne passe pas selon le plan. \n\nUne chose qui sera primordial à changer si tu veux avoir du meilleur sommeil serait par rapport aux écrans; téléphones cellulaires, ordinateurs portables, télévision. Il y a deux raisons pourquoi il est recommandé par presque tous les experts de limiter son exposition à ces derniers. D’un, la lumière bleue et de deux la haute stimulation causée par diverses sources de contenus (sites web, vidéos, réseaux sociaux, etc). Les études montrent que cela inhibe la production de la mélatonine, hormone qui dit au cerveau quand dormir. À cause de cela, il est recommandé d’éviter ton cellulaire ou autre appareils électroniques 30 minutes avant le sommeil. Bien sûr, cela est un acte difficile pour beaucoup, donc je dirais de commencer par au moins l’abstention durant la routine du soir. Une parenthèse sur les liseuses (ex : Kindle), bien qu’elles soient beaucoup mieux qu’un cellulaire, elles émettent toujours de la lumière bleue. Si tu veux lire, il est bien mieux sur papier. Les couleurs chaudes et sombres (l’inverse de la lumière bleue) sont aussi utiles pour se détendre, se préparer à dormir. \n\nUne autre astuce est d’éviter de manger trop proche de l’heure du coucher. Si tu es de l’âge de majorité, l’alcool est aussi à éviter, ce dernier peut perturber ton sommeil. Il ne faut aussi pas boire beaucoup d’eau, pas que c’est mauvais, mais ça peut éviter les sorties de toilettes à 3am. \nDe l’exercice (par contre, pas juste avant de dormir, car cela peut créer l’effet inverse de se détendre) peut aider à fatiguer le corps; après un entrainement ou match intense, le cerveau vas te pousser lui-même à aller dormir (pour que ton corps se répare). \n\nMaintenant pour parler de quelques solutions directes; les médicaments. Certains peuvent être achetés sur le comptoir tandis que d’autres doivent être prescrites. Les suppléments de mélatonine par exemple. Imitant l'hormone naturelle, ils régulent les cycles veille-sommeil. Souvent utilisés pour traiter l'insomnie ou le décalage horaire, ils sont généralement sûrs et présentent peu d'effets secondaires. Cependant, il convient d'être prudent pour certaines populations, notamment les femmes enceintes et celles souffrant de troubles auto-immuns ou d'autres problèmes médicaux. D’autres incluent les benzodiazépines, une classe de médicaments utilisés principalement pour traiter l’anxiété, l’insomnie et les crises convulsives. Pour ne pas entrer en trop de détail, elles enforçant les effets du neurotransmetteur gamma-aminobutyrique (GABA) dans le cerveau, entraînant une sédation et une relaxation. Des solutions naturelles comme les suppléments à bases de plantes peuvent aussi aider les patients. La racine de valériane par exemple peut aider dans la relaxation. On peut la prendre en pilule ou en faire du thé. Cependant, il est très important de ne pas dépendre de ces médicaments car l’utilisation fréquentes et à long terme peut créer une dépendance. Toujours bien discuter avec son prestataire de santé, (ces médicaments peuvent interagir avec d’autres et pourrait en cas rare être dangereux, voir fatale). \n\nUn autre aspect que je veux toucher est la sieste. Dans les pays du sud, la sieste fait partie de la vie courante. Ici, au Canada, peu de gens en font (peut-être qu’elle est mal perçue et/manque de temps dans les horaires chargés). Toutefois, les siestes de 10 à 20 minutes ont d’ailleurs de surprenants bienfaits. Ces dernières ne sont pas nécessaires, mais si tu te sens fatigué durant la journée, une courte sieste peut te revigorer, te rendant plus attentif (pétition de créer une période de sieste au secondaire !!!). Attention, la sieste peut aussi nuire. Des siestes trop longues ou trop tard dans la journée peut au contraire aggraver les problèmes de sommeil durant la nuit. Comme m’a raconté Mme Rico; il faut garder des clefs au bout de ses doigts lorsqu’on fait la sieste. Si les clefs tombent; cela veut dire qu’on a trop dormi. Les siestes après 15h sont généralement à éviter, le meilleur temps est entre 12h et 15h. Toutefois, la sieste ne resoldera pas le problème de fatigue chronique causé par certains troubles du sommeil, donc il ne faut pas la voir comme un résolve tout. \n\nPour clore le tout (des trois volets), le sommeil est trop important pour ne pas être expliqué à tout le monde. Jouant un rôle dans presque tous les systèmes du corps, à tout âge, avoir une bonne qualité de sommeil est primordial (j’espère que tu as retenu cela au moins). Plusieurs facteurs peuvent causer des problèmes au niveau du dodo, que ce soit l’utilisation excessive de cellulaire ou de stress et anxiété. Les conséquences sont majeures et affecte la vie quotidienne; moins de réflexes, douleurs, santé mentales, problèmes cardiovasculaire… la liste ne finit pas. Toutefois, il est toujours possible à n’importe quel moment de changer les choses. Moins utiliser le cellulaire et s’habituer à une routine du soir sont des bons débuts. TOUJOURS CONSULTER UN PROFESSIONNELLE SI TU TE SENS TRÈS MAL C’est en adoptant une vie saine qu’on obtiendra un sommeil sain, qui elle te permettra de vivre pleinement (en santé). Les deux sont deux faces de la même pièce, l’un ne peut pas être sans l’autre."


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


def open_image_window(image, dimensions="640x480"):
    window = Toplevel()
    window.title("Projet Personnel : Sommeil")
    window.geometry(dimensions)
    window.configure(bg="burlywood2")

    image_label1 = Label(window, image=image)
    image_label1.grid(padx=30, pady=50, columnspan=2)

    exit_button = Button(window, text="Quitter", command=window.destroy)
    exit_button.grid(pady=5, row=3, column=0)

    label_author_credits = Label(window, text="Par Kevin Liu, F. 511")
    label_author_credits.grid(pady=5, row=3, column=1)


def open_window_fct():
    global img_hormones
    window = Toplevel()
    window.title("Projet Personnel : Sommeil")
    window.geometry("640x480")
    window.configure(bg="burlywood2")

    texte_page_acceuil_titre = "Le fonctionnement"
    label1 = Label(window, text=texte_page_acceuil_titre, font=("Times New Roman", 30), bg="burlywood1")
    label1.grid(padx=100, pady=20, row=0, column=0, columnspan=2)

    combo = TextScrollCombo(window)
    combo.add_text(texte_fonctionnement)
    # for i in range(10):
    #     combo.add_text(text1)
    # combo.add_text(text2)
    # combo.config(state=DISABLED)
    combo.grid(padx=20, row=1, columnspan=2)
    combo.config(width=600, height=300)

    combo.txt.config(font=("Times New Roman", 14), undo=True, wrap='word')
    combo.txt.config(borderwidth=3, relief="sunken")

    open_image_hormones = Button(window, text="Image 1", command=lambda: open_image_window(img_hormones))
    open_image_hormones.grid(pady=(10, 0), row=2, column=0)

    exit_button = Button(window, text="Quitter", command=window.destroy)
    exit_button.grid(pady=5, row=3, column=0)

    label_author_credits = Label(window, text="Par Kevin Liu, F. 511")
    label_author_credits.grid(pady=5, row=3, column=1)


def open_window_troubles():
    window = Toplevel()
    window.title("Projet Personnel : Sommeil")
    window.geometry("640x480")
    window.configure(bg="burlywood2")

    texte_page_acceuil_titre = "Les troubles de sommeil"
    label1 = Label(window, text=texte_page_acceuil_titre, font=("Times New Roman", 30), bg="burlywood1")
    label1.grid(padx=100, pady=20, row=0, column=0, columnspan=2)

    combo = TextScrollCombo(window)
    combo.add_text(texte_troubles)
    # combo.config(state=DISABLED)
    combo.grid(padx=20, row=1, columnspan=2)
    combo.config(width=600, height=300)

    combo.txt.config(font=("Times New Roman", 14), undo=True, wrap='word')
    combo.txt.config(borderwidth=3, relief="sunken")

    open_img_exemple_suivi = Button(window, text="Image 1", command=lambda: open_image_window(img_exemple_suivi, "1040x600"))
    open_img_exemple_suivi.grid(pady=(10, 0), row=2, column=0)

    exit_button = Button(window, text="Quitter", command=window.destroy)
    exit_button.grid(pady=15, row=3, column=0)

    label_author_credits = Label(window, text="Par Kevin Liu, F. 511")
    label_author_credits.grid(pady=15, row=3, column=1)

    window.mainloop()


def open_window_solutions():
    window = Toplevel()
    window.title("Projet Personnel : Sommeil")
    window.geometry("640x480")
    window.configure(bg="burlywood2")

    texte_page_acceuil_titre = "Les solutions existent"
    label1 = Label(window, text=texte_page_acceuil_titre, font=("Times New Roman", 30), bg="burlywood1")
    label1.grid(padx=100, pady=20, row=0, column=0, columnspan=2)

    combo = TextScrollCombo(window)
    combo.add_text(texte_solutions)
    # combo.config(state=DISABLED)
    combo.grid(padx=20, row=1, columnspan=2)
    combo.config(width=600, height=300)

    combo.txt.config(font=("Times New Roman", 14), undo=True, wrap='word')
    combo.txt.config(borderwidth=3, relief="sunken")

    # open_img_exemple_suivi = Button(window, text="Image 1",command=lambda: open_image_window(img_exemple_suivi, "1040x600"))
    # open_img_exemple_suivi.grid(pady=(10, 0), row=2, column=0)
    exit_button = Button(window, text="Quitter", command=window.destroy)
    exit_button.grid(pady=15, row=3, column=0)

    label_author_credits = Label(window, text="Par Kevin Liu, F. 511")
    label_author_credits.grid(pady=15, row=3, column=1)

    window.mainloop()


def open_window_calc():
    window = Toplevel()
    window.title("Projet Personnel : Sommeil")
    window.geometry("640x500")
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

    tableau_qte_necessaire = Button(window, text="Image", command=lambda: open_image_window(qte_sommeil_necessaire))
    tableau_qte_necessaire.place(x=100, y=460)

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

img = PhotoImage(file='image_de_couverture.png')
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

img_hormones = "image_hormones_sommeil.png"
img_hormones = PhotoImage(file=img_hormones)

qte_sommeil_necessaire = "qte_sommeil_necessaire.png"
qte_sommeil_necessaire = PhotoImage(file=qte_sommeil_necessaire)

img_exemple_suivi = "exemple_suivi_montre_intelligente.png"
img_exemple_suivi = PhotoImage(file=img_exemple_suivi)

main_window.mainloop()
