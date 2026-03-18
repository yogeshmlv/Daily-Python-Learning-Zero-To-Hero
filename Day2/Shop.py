# 1. Setup the player and the shop

Coins = 100
backpack = ["apple","banana","orange","carrot"]
shop_list = {
 'health_potion' : 10,
 'leather_backpack' : 40,
 'magic_sword' : 100
}
print ('Welcome To The Shop!')
print (f'You Have {Coins} Coins And Your Backpack Contains : {backpack}')

# 2. Show the shop menu
print ('\n Here Is What You Can Buy :')
for item_name, item_price in shop_list.items():
    print (f'{item_name.title()} : {item_price} Coins')

# 3. Ask the user what they want
print('\n')
choice = input('What do you want to buy?')

# 4. Process the purchase

if choice in shop_list:
    item_price = shop_list[choice]
    if Coins >= item_price:
        Coins -= item_price
        backpack.append(choice)
        print (f'You Bought {choice} For {item_price} Coins! You Have {Coins} Coins Left And Your Backpack Now Contains : {backpack}')
    else:
        print (f'Sorry, You Do Not Have Enough Coins To Buy {choice}!')
else:
    print (f'Sorry, {choice} Is Not Available In The Shop!')

#5 Final Results
print ('\n After Your Shopping Spree , Here Is What You Have :')
print (f'Coins : {Coins}')
print (f'Backpack : {backpack}')