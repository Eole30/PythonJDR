import os.path
import pathlib
from tkinter import *
from classes.Player import Player
from classes.Campaign import Campaign

class New_Campaign_Frame:

    def __init__(self, window, links):
        self.window = window
        self.links = links
        self.frame = Frame(self.window, bg='#41B77F')
        self.frame.columnconfigure(index=0, weight=1)
        self.frame.rowconfigure(index=0, weight=1)
        self.campaign_name = StringVar()
        self.check_box_dict = {}
        self.labels()
        self.print_player_list()
        self.button_submit()


    def reset_frame(self):
        self.frame.grid_forget()


    def button_submit(self):
        submit_button = Button(self.frame, text="Create", font=("Courrier", 25), bg='white',
                               fg='#41B77F', command=self.create_campaign)
        submit_button.grid(column=0, columnspan=2, row=2,sticky="ew")

    def labels(self):
        font = ("Courrier", 20)
        label_name = Label(self.frame, text="Campaign name : ", font=font, bg='#41B77F',fg='white')
        label_name.grid(column=0,row=0,sticky="news")

        entry_name = Entry(self.frame, textvariable=self.campaign_name)
        entry_name.grid(column=1, row=0, sticky="e")

    def print_campaign(self):
        print()

    def player_list(self):
        players = []
        for path in pathlib.Path("./players/").iterdir():
            player = Player.load_player(path.name.split(".")[0])
            if player:
                players.append(player)
        return players

    def print_player_list(self):
        frame_list_players = Frame(self.frame)
        frame_list_players.grid(column=0, columnspan=2, row=1,sticky="ew")
        i = 0
        for player in self.player_list():
            self.check_box_dict[player.name] = IntVar()
            check_box = Checkbutton(frame_list_players, text = player.name+" "+player.pc_class, variable = self.check_box_dict[player.name])
            check_box.grid(column=0, row=i,sticky="w")
            i =i+1

    def create_campaign(self):
        campaign = Campaign(self.campaign_name.get())
        for player in self.player_list():
            if self.check_box_dict[player.name].get() == 1:
                campaign.add_player(player)
        campaign.save_campaign()
        #self.links['open_accueil']()