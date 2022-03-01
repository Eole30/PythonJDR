PLAYER_DIR = "./players/"
import json
import os
class Player:
    def __init__(self, name):
        self.name = name
        self.pc_class = "Default"
        self.level = 1
        self.race = "Human"
        self.speed = 30
        self.hit_points = 10
        self.hit_points_max = 10
        self.armor_class = 10
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

    def load_player(self):
        file_path = PLAYER_DIR + self.name + ".json"
        try:
            f = open(file_path, "r")
            dic_player = json.load(f)
            f.close()
            print("loading player %s " % (dic_player["name"]))
            self.pc_class = dic_player["pc_class"]
            self.level = dic_player["level"]
            self.race = dic_player["race"]
            self.speed = dic_player["speed"]
            self.hit_points = dic_player["hit_points"]
            self.hit_points_max = dic_player["hit_points_max"]
            self.armor_class = dic_player["armor_class"]
            self.strength = dic_player["strength"]
            self.dexterity = dic_player["dexterity"]
            self.constitution = dic_player["constitution"]
            self.intelligence = dic_player["intelligence"]
            self.wisdom = dic_player["wisdom"]
            self.charisma = dic_player["charisma"]
        except FileNotFoundError:
            print(file_path + " not found")

    def save_player(self):
        file_path = PLAYER_DIR + self.name + ".json"
        f = open(file_path, "w")
        parsed = {
            "name": self.name,
            "pc_class": self.pc_class,
            "level": self.level,
            "race": self.race,
            "speed": self.speed,
            "hit_points": self.hit_points,
            "hit_points_max": self.hit_points_max,
            "armor_class": self.armor_class,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma
        }
        f.write(json.dumps(parsed))
        f.close()

    def delete_player(self):
        file_path = PLAYER_DIR + self.name + ".json"
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("No player saved with this name")

    def __str__(self):
        return "%s - level %d %s\n\t%s\n\tSpeed %dft\n\tHP %d / %d\n\tAC %d \n\tSTR %d | DEX %d | CON %d | INT %d | WIS %d | CHA %d\n" % (
            self.name, self.level, self.pc_class, self.race, self.speed, self.hit_points, self.hit_points_max,
            self.armor_class, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom,
            self.charisma)

