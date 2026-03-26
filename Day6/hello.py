# __init__() # Used This As A Constructor To Initialize The Class And Create An Object Of The Class To Access The Attributes And Methods Of The Class.
class Player:
    def __init__(self, name, gold, weapon):
        self.name = name
        self.gold = gold
        self.weapon = weapon

    def display_info(self):
        print(f"Player Name: {self.name}")
        print(f"Player Gold: {self.gold}")
        print(f"Player Weapon: {self.weapon}")

Player1 = Player("John", 100, "Sword")
Player1.display_info()