print ("Welcome To Python Second Day Learing Loop")
name_school = ["Mlv","JPIT","Gkv","IIT"]

for nam in name_school:
   print (f'Name Of The School is ,{nam}')

number = [0,1,2,3,4,5,6,7,8,9,10]
for num in number :
   print (f'Number Is {num}')

for i in range (5):
      print (f'Number Is Yogesh Singh') # range() Function Used To Generate A Sequence Of Numbers , It Will Start From 0 By Default And It Will End At The Number We Provide In The Range Function -1

friends_name = ["Yogesh","Rohit","Satyarth","Ankit","Rahul"]
for friend in friends_name:
    if (friend=="Yogesh"):
        print (f'Hello {friend},You Are My Best Friend')
    else:
        print(f'Hello {friend},You Are Just A Friend')

vegetables= ["carrot", "broccoli", "spinach"]
print ("\n Name Of Vegetable is Here")
for i, veg in enumerate(vegetables):
 print (f'{i+1} {veg}') # enumerate() Function Used For The Index Of The List And It Will Start From 0 So We Need To Add 1 To The Index To Start From 1 
 
shop_list = {
    'fruits':['apple','banana','orange'],
    'vegetables':['carrot','broccoli','spinach'],
    'dairy':['milk','cheese','yogurt']
}
for type in shop_list:
    print(f'\n {type.title()} : {shop_list[type][0]}') # .title() Function Used To Capitalize The First Letter Of Each Word In The String

for category,item in shop_list.items():
    print(f'\n {category.title()} : {item[0]}') # .items() Function Used To Get The Key And Value Of The Dictionary At The Same Time

backpack = ["rusty sword", "health potion", "mysterious map"]
coins = 50

print("\n-- Purcahsijg the More Backpack")
coins = coins -40
backpack.append("leather backpack") # .append() Function Used To Add An Item To The List
print (f' You Have {coins} Coins Left And Your Backpack Now Contains : {backpack}')

print ('\n -- Selling The  Rusty Sword --')
backpack.remove("rusty sword") # .remove() Function Used To Remove An Item From The List
coins = coins + 10
print (f' You Sold The Rusty Sword For 10 Coins , Now You Have {coins} Coins And Your Backpack Now Contains : {backpack}')

#The Day Two "Final Boss"