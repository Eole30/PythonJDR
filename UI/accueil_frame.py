from tkinter import *


import UI.accueil_frame


class Accueil_Frame:
    def __init__(self, window, links):
        self.window = window
        self.links = links
        self.frame = Frame(self.window, bg='#000000')
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
        label_title = Label(self.frame, text="Welcome", font=("Courrier", 40), bg='#000000',
                            fg='white')
        label_title.grid()

    def create_new_campaign_button(self):
        new_campagne_button = Button(self.frame, text="New Campaign", font=("Courrier", 25), bg='#000000',
                                     fg='white', command=self.links['open_new_campaign'])
        new_campagne_button.grid(pady=25)

    def load_campaign_button(self):
        load_campagne_button = Button(self.frame, text="Load Campaign", font=("Courrier", 25), bg='#000000',
                                      fg='white', command=self.links['open_campaign_load'])
        load_campagne_button.grid(pady=25)

    def create_new_player_button(self):
        new_player_button = Button(self.frame, text="New Player", font=("Courrier", 25), bg='#000000',
                                   fg='white', command=self.links['open_new_personnage'])
        new_player_button.grid(pady=25)


# afficher

