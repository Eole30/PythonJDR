CAMPAIGN_DIR = "./campaigns/"
from classes.Player import Player
import json
class Campaign:
    def __init__(self, campaign_name):
        self.players = {}
        self.campaign_name = campaign_name

    def add_player(self, player):
        self.players[player.name] = player

    @staticmethod
    def load_campaign(campaign_name):
        file_path = CAMPAIGN_DIR + campaign_name + ".json"
        try:
            f = open(file_path, "r")
            dic_campaign = json.load(f)
            f.close()
            campaign = Campaign(campaign_name)
            for key in dic_campaign:
                player=Player.load_player(key)
                player.hit_points = dic_campaign[key]
                campaign.add_player(player)
                return campaign
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
