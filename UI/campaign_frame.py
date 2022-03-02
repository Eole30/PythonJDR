from tkinter import *
from classes.Player import Player
from classes.Campaign import Campaign

class Campaign_Frame:
    def __init__(self, window, links):
        self.window = window
        self.links = links
        self.frame = Frame(self.window, bg='#000000')
        self.frame.columnconfigure(index=0, weight=1)
        self.frame.rowconfigure(index=0, weight=1)

    def reset_frame(self):
        self.frame.grid_forget()

    def choosen_campaign(self,campaign):
        i = 0
        for player in campaign.players.values():
            print("bit "+player.name)
            frame_player = Frame(self.frame, bg='#2c002e', borderwidth = 3, relief = "raised")
            frame_player.grid(column=i%2, row=int(i/2), sticky="we")

            font1 = ("Courrier", 14)
            font2 = ("Courrier", 12)
            font3 = ("Courrier", 10)

            label_name = Label(frame_player, text=player.name, font=font1, bg='#2c002e', fg='white')
            label_name.grid(column=0, row=0, sticky="w")

            label_pc_class = Label(frame_player, text=player.pc_class + " " + str(player.level), font=font1, bg='#2c002e', fg='white')
            label_pc_class.grid(column=1, row=0, sticky="w")

            label_race = Label(frame_player, text="Race: " + player.race, font=font1, bg='#2c002e', fg='white')
            label_race.grid(column=3, row=0, sticky="w")

            label_armor_class = Label(frame_player, text="AC : "+str(player.armor_class), font=font2, bg='#2c002e', fg='white')
            label_armor_class.grid(column=0, row=1, sticky="w")

            label_hit_points = Label(frame_player, text="HP: "+str(player.hit_points) + " / " + str(player.hit_points_max), font=font2, bg='#2c002e', fg='white')
            label_hit_points.grid(column=1, row=1, sticky="e")

            label_speed = Label(frame_player, text="Speed : "+str(player.speed), font=font3, bg='#2c002e', fg='white')
            label_speed.grid(column=0, row=2, sticky="w")

            label_strength = Label(frame_player, text="STR : "+str(player.strength), font=font3, bg='#2c002e', fg='white')
            label_strength.grid(column=0, row=3, sticky="w")

            label_dexterity = Label(frame_player, text="DEX : "+str(player.dexterity), font=font3, bg='#2c002e', fg='white')
            label_dexterity.grid(column=1, row=3, sticky="e")

            label_constitution = Label(frame_player, text="CON : "+str(player.constitution), font=font3, bg='#2c002e', fg='white')
            label_constitution.grid(column=3, row=3, sticky="e")

            label_intelligence = Label(frame_player, text="INT : "+str(player.intelligence), font=font3, bg='#2c002e', fg='white')
            label_intelligence.grid(column=0, row=4, sticky="w")

            label_wisdom = Label(frame_player, text="WIS : "+str(player.wisdom), font=font3, bg='#2c002e', fg='white')
            label_wisdom.grid(column=1, row=4, sticky="e")

            label_charisma = Label(frame_player, text="CHA : "+str(player.charisma), font=font3, bg='#2c002e', fg='white')
            label_charisma.grid(column=3, row=4, sticky="e")

            i=i+1
