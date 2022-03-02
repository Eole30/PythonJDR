from tkinter import *
from classes.Player import Player
from classes.Campaign import Campaign

class Campaign_Frame:
    def __init__(self, window, links):
        self.window = window
        self.links = links
        self.frame = Frame(self.window, bg='#41B77F')
        self.frame.columnconfigure(index=0, weight=1)
        self.frame.rowconfigure(index=0, weight=1)

    def reset_frame(self):
        self.frame.grid_forget()

    def choosen_campaign(self,campaign):
        i = 0
        for player in campaign.players.values():
            print("bit "+player.name)
            frame_player = Frame(self.frame, bg='#41B77F', borderwidth = 3)
            frame_player.grid(column=i%2, row=int(i/2), sticky="w")

            font1 = ("Courrier", 14)
            font2 = ("Courrier", 10)
            label_name = Label(frame_player, text="name : "+player.name, font=font1, bg='#41B77F', fg='white')
            label_name.grid(column=0, row=0, sticky="w")

            label_pc_class = Label(frame_player, text="pc_class : "+player.pc_class, font=font1, bg='#41B77F', fg='white')
            label_pc_class.grid(column=1, row=0, sticky="w")

            label_race = Label(frame_player, text="race : "+player.race, font=font1, bg='#41B77F', fg='white')
            label_race.grid(column=2, row=0, sticky="w")

            label_level = Label(frame_player, text="level : "+str(player.level), font=font1, bg='#41B77F', fg='white')
            label_level.grid(column=3, row=0, sticky="w")

            label_armor_class = Label(frame_player, text="armor_class : "+str(player.armor_class), font=font2, bg='#41B77F', fg='white')
            label_armor_class.grid(column=0, row=1, sticky="w")

            label_hit_points = Label(frame_player, text="hit_points : "+str(player.hit_points), font=font2, bg='#41B77F', fg='white')
            label_hit_points.grid(column=1, row=1, sticky="w")

            label_hit_points_max = Label(frame_player, text="/ hit_points_max : "+str(player.hit_points_max), font=font2, bg='#41B77F', fg='white')
            label_hit_points_max.grid(column=2, row=1, sticky="w")

            label_speed = Label(frame_player, text="speed : "+str(player.speed), font=font2, bg='#41B77F', fg='white')
            label_speed.grid(column=3, row=1, sticky="w")

            label_strength = Label(frame_player, text="strength : "+str(player.strength), font=font2, bg='#41B77F', fg='white')
            label_strength.grid(column=0, row=2, sticky="w")

            label_dexterity = Label(frame_player, text="dexterity : "+str(player.dexterity), font=font2, bg='#41B77F', fg='white')
            label_dexterity.grid(column=1, row=2, sticky="w")

            label_constitution = Label(frame_player, text="constitution : "+str(player.constitution), font=font2, bg='#41B77F', fg='white')
            label_constitution.grid(column=2, row=2, sticky="w")

            label_intelligence = Label(frame_player, text="intelligence : "+str(player.intelligence), font=font2, bg='#41B77F', fg='white')
            label_intelligence.grid(column=0, row=3, sticky="w")

            label_wisdom = Label(frame_player, text="wisdom : "+str(player.wisdom), font=font2, bg='#41B77F', fg='white')
            label_wisdom.grid(column=1, row=3, sticky="w")

            label_charisma = Label(frame_player, text="charisma : "+str(player.charisma), font=font2, bg='#41B77F', fg='white')
            label_charisma.grid(column=2, row=3, sticky="w")

            i=i+1
