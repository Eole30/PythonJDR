from tkinter import *

class New_Personnage:
    def __init__(self, window, links):
        self.window = window
        self.links = links
        self.frame = Frame(self.window, bg='#FF0000')
        self.frame["width"] = 500
        self.frame["height"] = 500
        self.labels()
        self.frame.pack(expand=YES)

    def reset_frame(self):
        self.frame.destroy()
        self.frame = Frame(None, bg='#FF0000')
        self.frame["width"]=500
        self.frame["height"]=500

    def labels(self):
        font = ("Courrier", 20)
        label_name = Label(self.frame, text="name : ", font=font, bg='#41B77F',fg='white')
        label_name.grid(column=0,row=0)

        label_pc_class = Label(self.frame, text="pc_class : ", font=font, bg='#41B77F',fg='white')
        label_pc_class.grid(column=0, row=1)

        label_level = Label(self.frame, text="level : ", font=font, bg='#41B77F',fg='white')
        label_level.grid(column=0, row=2)

        label_race = Label(self.frame, text="race : ", font=font, bg='#41B77F',fg='white')
        label_race.grid(column=0, row=3)

        label_speed = Label(self.frame, text="speed : ", font=font, bg='#41B77F',fg='white')
        label_speed.grid(column=0, row=4)

        label_hit_points = Label(self.frame, text="hit_points : ", font=font, bg='#41B77F',fg='white')
        label_hit_points.grid(column=0, row=5)

        label_hit_points_max = Label(self.frame, text="hit_points_max : ", font=font, bg='#41B77F',fg='white')
        label_hit_points_max.grid(column=0, row=6)

        label_armor_class = Label(self.frame, text="armor_class : ", font=font, bg='#41B77F',fg='white')
        label_armor_class.grid(column=0, row=7)

        label_strength = Label(self.frame, text="strength : ", font=font, bg='#41B77F',fg='white')
        label_strength.grid(column=0, row=8)

        label_dexterity = Label(self.frame, text="dexterity : ", font=font, bg='#41B77F',fg='white')
        label_dexterity.grid(column=0, row=9)

        label_constitution = Label(self.frame, text="constitution : ", font=font, bg='#41B77F',fg='white')
        label_constitution.grid(column=0, row=10)

        label_intelligence = Label(self.frame, text="intelligence : ", font=font, bg='#41B77F',fg='white')
        label_intelligence.grid(column=0, row=11)

        label_wisdom = Label(self.frame, text="wisdom : ", font=font, bg='#41B77F',fg='white')
        label_wisdom.grid(column=0, row=12)

        label_charisma = Label(self.frame, text="charisma : ", font=font, bg='#41B77F',fg='white')
        label_charisma.grid(column=0, row=13)




