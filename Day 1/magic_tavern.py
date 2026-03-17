print ('WELCOME TO THE MAGIC TAVERN')

name = input('Inkeeper : What Is Your Name , Adventurer ? ')
print (('Adventurer : My Name Is {name}'))
print (('Inkeeper : Welcome To The Magic Tavern , How Many Gold Do You Have , {name}'))
gold = input('Adventurer : I Have ')
print (f'Inkeeper : Wow , {gold} Gold Is A Lot , What Do You Want To Do In The Magic Tavern , {name} ?')
action = input('Adventurer : I Want To ')
print (f'Inkeeper : That Sounds Like A Great Idea , {name} , Enjoy Your Time In The Magic Tavern !')

if (action == 'Drink'):
    print (f'Inkeeper : Here Is Your Drink , {name} , Enjoy !')
elif (action == 'Play Games'):
    print (f'Inkeeper : Sure , {name} , We Have A Variety Of Games To Play !')
elif (action == 'Talk To Other Adventurers'):
    print (f'Inkeeper : That Sounds Like A Great Idea , {name} , You Can Meet Some Interesting People Here !')
else:
    print (f'Inkeeper : That Sounds Like A Great Idea , {name} , Enjoy Your Time In The Magic Tavern !')