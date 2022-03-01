

from classes.Player import Player
from classes.Campaign import Campaign
##tests d'appels
player = Player("Even")
print(player)
player.load_player()
print(player)
player.speed = 34
player.save_player()
player2 = Player("Dude")
player2.delete_player()

campaign = Campaign("Test")
campaign.load_campaign()
player.hit_points = 10
campaign.add_player(player)
campaign.save_campaign()
print(campaign)

campaign2 = Campaign("Test2")
campaign2.delete_campaign()
##
# partie UI

from tkinter import *
from UI.accueil_frame import Accueil
from UI.new_personnage_frame import New_Personnage

class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("JDR Manager")
        self.window.geometry("1280x720")
        self.window.minsize(1280, 720)
        self.window.iconbitmap("UI/ressource/D_D5_logo.ico")
        #self.window.config(bg='#41B77F')
        self.links = {
            'open_new_campagne': self.open_new_campagne,
            'open_campagne': self.open_campagne,
            'open_new_personnage': self.open_new_personnage,
            'open_accueil': self.open_accueil,
        }

        self.accueil = Accueil(self.window, self.links)
        self.new_personnage = New_Personnage(self.window, self.links)

    def reset_all(self):
        self.accueil.reset_frame()
        self.new_personnage.reset_frame()

    def open_new_campagne(self):
        print("new_campagne")
        self.reset_all()

    def open_campagne(self):
        print("campagne")
        self.reset_all()

    def open_new_personnage(self):
        print("new_personnage")
        self.reset_all()
        self.new_personnage = New_Personnage(self.window, self.links)

    def open_accueil(self):
        self.reset_all()


main = Main()
main.window.mainloop()