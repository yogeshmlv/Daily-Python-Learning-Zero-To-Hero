print('A wild Goblin appears!')

while True:
    action = input ('What do you want to do? (attack/run) ')
    if action == 'attack':
        print('You attack the Goblin!')
        print('The Goblin is defeated!')
        break
    elif action == 'run':
        print('You run away from the Goblin!')
        break
    else:
        print('Invalid action. Please choose "attack" or "run".')