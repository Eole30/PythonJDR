from tkinter import *
from classes.Player import Player

class New_Personnage_Frame:
    def __init__(self, window, links):
        self.window = window
        self.links = links
        self.frame = Frame(self.window, bg='#FF0000')
        self.name = StringVar()
        self.pc_class = StringVar()
        self.level = IntVar()
        self.race = StringVar()
        self.speed = IntVar()
        self.hit_points = IntVar()
        self.hit_points_max = IntVar()
        self.armor_class = IntVar()
        self.strength = IntVar()
        self.dexterity = IntVar()
        self.constitution = IntVar()
        self.intelligence = IntVar()
        self.wisdom = IntVar()
        self.charisma = IntVar()
        self.labels()
        self.entrys()
        self.button_submit()


    def reset_frame(self):
        self.frame.grid_forget()


    def labels(self):
        font = ("Courrier", 20)
        label_name = Label(self.frame, text="name : ", font=font, bg='#41B77F',fg='white')
        label_name.grid(column=0,row=0,sticky="e")

        label_pc_class = Label(self.frame, text="pc_class : ", font=font, bg='#41B77F',fg='white')
        label_pc_class.grid(column=0, row=1,sticky="e")

        label_level = Label(self.frame, text="level : ", font=font, bg='#41B77F',fg='white')
        label_level.grid(column=0, row=2,sticky="e")

        label_race = Label(self.frame, text="race : ", font=font, bg='#41B77F',fg='white')
        label_race.grid(column=0, row=3,sticky="e")

        label_speed = Label(self.frame, text="speed : ", font=font, bg='#41B77F',fg='white')
        label_speed.grid(column=0, row=4,sticky="e")

        label_hit_points = Label(self.frame, text="hit_points : ", font=font, bg='#41B77F',fg='white')
        label_hit_points.grid(column=0, row=5,sticky="e")

        label_hit_points_max = Label(self.frame, text="hit_points_max : ", font=font, bg='#41B77F',fg='white')
        label_hit_points_max.grid(column=0, row=6,sticky="e")

        label_armor_class = Label(self.frame, text="armor_class : ", font=font, bg='#41B77F',fg='white')
        label_armor_class.grid(column=0, row=7,sticky="e")

        label_strength = Label(self.frame, text="strength : ", font=font, bg='#41B77F',fg='white')
        label_strength.grid(column=0, row=8,sticky="e")

        label_dexterity = Label(self.frame, text="dexterity : ", font=font, bg='#41B77F',fg='white')
        label_dexterity.grid(column=0, row=9,sticky="e")

        label_constitution = Label(self.frame, text="constitution : ", font=font, bg='#41B77F',fg='white')
        label_constitution.grid(column=0, row=10,sticky="e")

        label_intelligence = Label(self.frame, text="intelligence : ", font=font, bg='#41B77F',fg='white')
        label_intelligence.grid(column=0, row=11,sticky="e")

        label_wisdom = Label(self.frame, text="wisdom : ", font=font, bg='#41B77F',fg='white')
        label_wisdom.grid(column=0, row=12,sticky="e")

        label_charisma = Label(self.frame, text="charisma : ", font=font, bg='#41B77F',fg='white')
        label_charisma.grid(column=0, row=13,sticky="e")

    def entrys(self):
        entry_name = Entry(self.frame,textvariable=self.name)
        entry_name.grid(column=1,row=0,sticky="e")

        entry_pc_class = Entry(self.frame,textvariable=self.pc_class)
        entry_pc_class.grid(column=1, row=1,sticky="e")

        entry_level = Entry(self.frame,textvariable=self.level)
        entry_level.grid(column=1, row=2,sticky="e")

        entry_race = Entry(self.frame,textvariable=self.race)
        entry_race.grid(column=1, row=3,sticky="e")

        entry_speed = Entry(self.frame,textvariable=self.speed)
        entry_speed.grid(column=1, row=4,sticky="e")

        entry_hit_points = Entry(self.frame,textvariable=self.hit_points)
        entry_hit_points.grid(column=1, row=5,sticky="e")

        entry_hit_points_max = Entry(self.frame,textvariable=self.hit_points_max)
        entry_hit_points_max.grid(column=1, row=6,sticky="e")

        entry_armor_class = Entry(self.frame,textvariable=self.armor_class)
        entry_armor_class.grid(column=1, row=7,sticky="e")

        entry_strength = Entry(self.frame,textvariable=self.strength)
        entry_strength.grid(column=1, row=8,sticky="e")

        entry_dexterity = Entry(self.frame,textvariable=self.dexterity)
        entry_dexterity.grid(column=1, row=9,sticky="e")

        entry_constitution = Entry(self.frame,textvariable=self.constitution)
        entry_constitution.grid(column=1, row=10,sticky="e")

        entry_intelligence = Entry(self.frame,textvariable=self.intelligence)
        entry_intelligence.grid(column=1, row=11,sticky="e")

        entry_wisdom = Entry(self.frame,textvariable=self.wisdom)
        entry_wisdom.grid(column=1, row=12,sticky="e")

        entry_charisma = Entry(self.frame,textvariable=self.charisma)
        entry_charisma.grid(column=1, row=13,sticky="e")

    def button_submit(self):
        submit_button = Button(self.frame, text="Create", font=("Courrier", 25), bg='white',
                               fg='#41B77F', command=self.create_player)
        submit_button.grid(column=0, columnspan=2, row=13,sticky="ew")


    def create_player(self):
        player = Player(self.name.get(),self.level.get(), self.pc_class.get(), self.race.get(), self.speed.get(), self.hit_points.get(), self.hit_points_max.get(),
            self.armor_class.get(), self.strength.get(), self.dexterity.get(), self.constitution.get(), self.intelligence.get(), self.wisdom.get(),
            self.charisma.get())
        player.save_player()

        self.links['open_accueil']()

