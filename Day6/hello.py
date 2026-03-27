#Classes and Object-Oriented Programming (OOP)
# __init__() # Used This As A Constructor To Initialize The Class And Create An Object Of The Class To Access The Attributes And Methods Of The Class.
# class Player:
#     def __init__(self, name, gold, weapon):
#         self.name = name
#         self.gold = gold
#         self.weapon = weapon

#     def display_info(self):
#         print(f"Player Name: {self.name}")
#         print(f"Player Gold: {self.gold}")
#         print(f"Player Weapon: {self.weapon}")

# Player1 = Player("John", 100, "Sword")
# Player1.display_info()


class Monster:
    def __init__(self, name, health, damage):
        self.name = name #If you write self.health = 30, Python writes it on the Monster's permanent nametag so it remembers it forever.
        self.health = health
        self.damage = damage
        
    # We pass 'self' in so the function knows WHICH monster is attacking!
    def attack(self):
        print(f"The {self.name} attacks for {self.damage} damage!")
        
    def take_damage(self, amount):
        self.health = self.health - amount
        print(f"The {self.name} takes {amount} damage! HP is now {self.health}.")

# 1. Create three totally different monsters using the ONE blueprint
goblin = Monster("Sneaky Goblin", 30, 5)
orc = Monster("Brutal Orc", 80, 15)
dragon = Monster("Ancient Dragon", 500, 75)

# 2. Make them do things!
goblin.attack()
orc.attack()

# 3. Hit the dragon!
dragon.take_damage(50)

# Output:
# The Sneaky Goblin attacks for 5 damage!
# The Brutal Orc attacks for 15 damage!
# The Ancient Dragon takes 50 damage! HP is now 450.