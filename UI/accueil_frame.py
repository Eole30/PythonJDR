from tkinter import *


import UI.accueil_frame


class Accueil_Frame:
    def __init__(self, window, links):
        self.window = window
        self.links = links
        self.frame = Frame(self.window, bg='#41B77F')
        self.frame.grid(column=0, row=0, sticky="NESW")
        self.frame.columnconfigure(index=0,weight=1)
        self.frame.rowconfigure(index=0,weight=1)
        self.create_widgets()



    def reset_frame(self):
        self.frame.grid_forget()


    def create_widgets(self):
        self.create_title()
        self.create_new_campaign_button()
        self.load_campaign_button()
        self.create_new_player_button()

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#41B77F',
                            fg='white')
        label_title.grid()

    def create_new_campaign_button(self):
        new_campagne_button = Button(self.frame, text="Crée une nouvelle campagne", font=("Courrier", 25), bg='white',
                                     fg='#41B77F', command=self.links['open_new_campaign'])
        new_campagne_button.grid(pady=25)

    def load_campaign_button(self):
        load_campagne_button = Button(self.frame, text="Chargé une campagne", font=("Courrier", 25), bg='white',
                                      fg='#41B77F', command=self.links['open_campaign_load'])
        load_campagne_button.grid(pady=25)

    def create_new_player_button(self):
        new_player_button = Button(self.frame, text="Crée un nouveau joueur", font=("Courrier", 25), bg='white',
                                   fg='#41B77F', command=self.links['open_new_personnage'])
        new_player_button.grid(pady=25)


# afficher

