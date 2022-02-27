from tkinter import *

class New_Personnage:
    def __init__(self, window):
        self.window = window
        self.frame = Frame(self.window, bg='#41B77F')
        self.labels()

    def labels(self):
        label_name = Label(self.frame, text="name : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_name.grid(column=0,row=0)
        label_name.pack()

        label_pc_class = Label(self.frame, text="pc_class : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_pc_class.grid(column=0, row=1)
        label_pc_class.pack()

        label_level = Label(self.frame, text="level : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_level.grid(column=0, row=2)
        label_level.pack()

        label_race = Label(self.frame, text="race : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_race.grid(column=0, row=3)
        label_race.pack()

        label_speed = Label(self.frame, text="speed : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_speed.grid(column=0, row=4)
        label_speed.pack()

        label_hit_points = Label(self.frame, text="hit_points : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_hit_points.grid(column=0, row=5)
        label_hit_points.pack()

        label_hit_points_max = Label(self.frame, text="hit_points_max : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_hit_points_max.grid(column=0, row=6)
        label_hit_points_max.pack()

        label_armor_class = Label(self.frame, text="armor_class : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_armor_class.grid(column=0, row=7)
        label_armor_class.pack()

        label_strength = Label(self.frame, text="strength : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_strength.grid(column=0, row=8)
        label_strength.pack()

        label_dexterity = Label(self.frame, text="dexterity : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_dexterity.grid(column=0, row=9)
        label_dexterity.pack()

        label_constitution = Label(self.frame, text="constitution : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_constitution.grid(column=0, row=10)
        label_constitution.pack()

        label_intelligence = Label(self.frame, text="intelligence : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_intelligence.grid(column=0, row=11)
        label_intelligence.pack()

        label_wisdom = Label(self.frame, text="wisdom : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_wisdom.grid(column=0, row=12)
        label_wisdom.pack()

        label_charisma = Label(self.frame, text="charisma : ", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_charisma.grid(column=0, row=13)
        label_charisma.pack()




