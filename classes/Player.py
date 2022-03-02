PLAYER_DIR = "./players/"
import json
class Player:
    def __init__(self, name, level, pc_class, race, speed, hit_points, hit_points_max, armor_class, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.level = level
        self.pc_class = pc_class
        self.race = race
        self.speed = speed
        self.hit_points = hit_points
        self.hit_points_max = hit_points_max
        self.armor_class = armor_class
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    @staticmethod
    def default_player(name):
        return Player(name,1,"Default","Human",30,10,10,10,10,10,10,10,10,10)

    @staticmethod
    def load_player(name):
        file_path = PLAYER_DIR + name + ".json"
        try:
            f = open(file_path, "r")
            dic_player = json.load(f)
            f.close()
            player = Player(dic_player["name"],dic_player["level"],dic_player["pc_class"],dic_player["race"],dic_player["speed"],dic_player["hit_points"],dic_player["hit_points_max"],dic_player["armor_class"],dic_player["strength"],dic_player["dexterity"],dic_player["constitution"],dic_player["intelligence"],dic_player["wisdom"],dic_player["charisma"])
            return player
        except FileNotFoundError:
            print(file_path + " not found")
        return None

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

    def __str__(self):
        return "%s - level %d %s\n\t%s\n\tSpeed %dft\n\tHP %d / %d\n\tAC %d \n\tSTR %d | DEX %d | CON %d | INT %d | WIS %d | CHA %d\n" % (
            self.name, self.level, self.pc_class, self.race, self.speed, self.hit_points, self.hit_points_max,
            self.armor_class, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom,
            self.charisma)

