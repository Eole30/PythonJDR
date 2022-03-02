from classes.Player import Player
from classes.Campaign import Campaign

##tests d'appels

player = Player.load_player("Vincent")
print(player)
player.speed = 34
player.save_player()

campaign = Campaign.load_campaign("Test")
player.hit_points = 10
#campaign.add_player(player)
#campaign.save_campaign()
print(campaign)

##
# partie UI

from tkinter import *
from UI.accueil_frame import Accueil_Frame
from UI.new_personnage_frame import New_Personnage_Frame
from UI.new_campaign_frame import New_Campaign_Frame

class Main:
    def __init__(self):
        self.window = Tk()
        self.window.grid_columnconfigure(0,weight = 1)
        self.window.grid_rowconfigure(0,weight = 1)
        self.window.title("JDR Manager")
        self.window.geometry("1280x720")
        self.window.minsize(1280, 720)
        self.window.iconbitmap("UI/ressource/D_D5_logo.ico")
        #self.window.config(bg='#41B77F')
        self.links = {
            'open_new_campagne': self.open_new_campaign,
            'open_campagne': self.open_campaign,
            'open_new_personnage': self.open_new_personnage,
            'open_accueil': self.open_accueil,
        }

        self.accueil_frame = Accueil_Frame(self.window, self.links)
        self.new_personnage_frame = New_Personnage_Frame(self.window, self.links)
        self.new_campaign_frame = New_Campaign_Frame(self.window, self.links)

    def reset_all(self):
        self.accueil_frame.reset_frame()
        self.new_personnage_frame.reset_frame()

    def open_new_campaign(self):
        print("new_campaign")
        self.reset_all()
        self.new_campaign_frame.frame.grid(column = 0, row = 0)

    def open_campaign(self):
        print("campaign")
        self.reset_all()

    def open_new_personnage(self):
        print("new_personnage")
        self.reset_all()
        self.new_personnage_frame.frame.grid(column = 0, row = 0)

    def open_accueil(self):
        self.reset_all()
        self.accueil_frame.frame.grid(column = 0, row = 0)


main = Main()
main.window.mainloop()