import json

PLAYER_DIR = "./players/"
CAMPAIGN_DIR = "./campaigns/"


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
        except FileNotFoundException:
            print(file_path + " not found")

    def __str__(self):
        return "%s - level %d %s\n\t%s\n\tSpeed %dft\n\tHP %d / %d\n\tAC %d \n\tSTR %d | DEX %d | CON %d | INT %d | WIS %d | CHA %d\n" % (
            self.name, self.level, self.pc_class, self.race, self.speed, self.hit_points, self.hit_points_max,
            self.armor_class, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom,
            self.charisma)


class Campaign:
    def __init__(self, campaign_name):
        self.players = {}
        self.campaign_name = campaign_name

    def add_player(self, player):
        self.players[player.name] = player

    def load_campaign(self):
        file_path = CAMPAIGN_DIR + campaign.campaign_name + ".json"
        try:
            f = open(file_path, "r")
            dic_campaign = json.load(f)
            f.close()
            for key in dic_campaign:
                new_player = Player(key)
                new_player.load_player()
                new_player.hit_points = dic_campaign[key]
                self.add_player(new_player)
        except FileNotFoundError:
            print(file_path + " not found")

    def __str__(self):
        res = "Campaign %s\n" % self.campaign_name
        for key in self.players:
            res = res + str(self.players[key])
        return res + "\n"


player = Player("Even")
print(player)
player.load_player()
print(player)

campaign = Campaign("Test")
campaign.add_player(player)
campaign.load_campaign()
print(campaign)
