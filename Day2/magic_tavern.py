print("--- Welcome to the Magic Tavern ---")

# 1. Getting player info
name = input("Innkeeper: What is your name, traveler? ")
coins = int(input(f"Innkeeper: Well met, {name}. How many gold coins do you have? "))

# 2. NEW: Setting up the player's inventory
backpack = ["rusty sword", "health potion", "mysterious map"]

# 3. Tavern logic
if coins >= 100:
    print("Innkeeper: Ah, a wealthy noble! Let me show you to the VIP suite.")
elif coins >= 10:
    print("Innkeeper: Grab a seat at the bar. A warm meal is 10 coins.")
elif coins > 0:
    print(f"Innkeeper: {coins} coins? That's only enough for a glass of water.")
else:
    print("Innkeeper: No money?! Get out before I call the guards!")

# 4. NEW: Looping through the backpack
print("\n--- You sit at a table and check your backpack ---")
print("You are currently carrying:")

# This loop runs once for every item in the list
for item in backpack:
    # Bonus trick: .title() capitalizes the first letter of each word!
    print(f"- {item.title()}")