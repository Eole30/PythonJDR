class Player:
    def __init__(self, name, pc_class, level, race, speed, hit_points_max, armor_class, strength, dexterity,
                 constitution, intelligence, wisdom, charisma):
        self.name = name
        self.pc_class = pc_class
        self.level = level
        self.race = race
        self.speed = speed
        self.hit_points_max = hit_points_max
        self.armor_class = armor_class
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


class Campaign:
    def __init__(self):
        self.players = {}

    def add_player(self, player_name, hit_points):
        self.players[player_name] = hit_points


player = Player("Even", "Rogue", 4, "Wood Elf", 35, 32, 15, 10, 18, 13, 14, 17, 12)
print(player.name)

campaign = Campaign()
campaign.add_player("Even", 30)
print(campaign.players[player.name])
