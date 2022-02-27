from tkinter import *


import UI.accueil_frame


class Accueil:
    def __init__(self, window):
        self.window = window
        # initialization des composants
        self.frame = Frame(self.window, bg='#41B77F')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def reset_frame(self):
        self.frame.destroy()
        self.frame = Frame(self.window, bg='#FF0000')
        self.frame.pack(expand=YES)





    def create_widgets(self):
        self.create_title()
        self.create_new_campagne_button()
        self.load_campagne_button()
        self.create_new_player_button()

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#41B77F',
                            fg='white')
        label_title.pack()

    def create_new_campagne_button(self):
        new_campagne_button = Button(self.frame, text="Crée une nouvelle campagne", font=("Courrier", 25), bg='white',
                                     fg='#41B77F', command=self.open_new_campagne)
        new_campagne_button.pack(pady=25, fill=X)

    def load_campagne_button(self):
        load_campagne_button = Button(self.frame, text="Chargé une campagne", font=("Courrier", 25), bg='white',
                                      fg='#41B77F', command=self.open_campagne)
        load_campagne_button.pack(pady=25, fill=X)

    def create_new_player_button(self):
        new_player_button = Button(self.frame, text="Crée un nouveau joueur", font=("Courrier", 25), bg='white',
                                   fg='#41B77F', command=self.open_new_personnage)
        new_player_button.pack(pady=25, fill=X)


# afficher

