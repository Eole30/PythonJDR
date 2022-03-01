CAMPAIGN_DIR = "./campaigns/"
from classes import Player as P
import json
class Campaign:
    def __init__(self, campaign_name):
        self.players = {}
        self.campaign_name = campaign_name

    def add_player(self, player):
        self.players[player.name] = player

    def load_campaign(self):
        file_path = CAMPAIGN_DIR + self.campaign_name + ".json"
        try:
            f = open(file_path, "r")
            dic_campaign = json.load(f)
            f.close()
            for key in dic_campaign:
                new_player = P.Player(key)
                new_player.load_player()
                new_player.hit_points = dic_campaign[key]
                self.add_player(new_player)
        except FileNotFoundError:
            print(file_path + " not found")

    def save_campaign(self):
        file_path = CAMPAIGN_DIR + self.campaign_name + ".json"
        f = open(file_path, "w")
        parsed = {}
        for key in self.players:
            parsed[key] = self.players[key].hit_points
        f.write(json.dumps(parsed))
        f.close()

    def __str__(self):
        res = "Campaign %s\n" % self.campaign_name
        for key in self.players:
            res = res + str(self.players[key])
        return res + "\n"
