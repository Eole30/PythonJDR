from tkinter import *

import UI.accueil

class Controlleur:

class Accueil:

    def __init__(self):
        self.window = Tk()
        self.window.title("JDR Manager")
        self.window.geometry("1280x720")
        self.window.minsize(1280, 720)
        self.window.iconbitmap("ressource/D_D5_logo.ico")
        self.window.config(bg='#41B77F')


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

    def open_new_campagne(self):
        print("new_campagne")
        self.reset_frame()

    def open_campagne(self):
        print("campagne")
        self.reset_frame()

    def open_new_personnge(self):
        print("new_personnage")
        self.reset_frame()

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
                                   fg='#41B77F', command=self.open_new_personnge)
        new_player_button.pack(pady=25, fill=X)


# afficher
UI.accueil = Accueil()
UI.accueil.window.mainloop()
