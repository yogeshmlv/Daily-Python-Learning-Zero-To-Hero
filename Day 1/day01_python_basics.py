print('Hello, World!')
name = 'Yogesh'
age = 20
print (f'My Name Is {name} And My Age Is {age}')
# f-String Is A New Way To Format String In Python 3.6 And Above Version
num1 = 20
num2 = 30
print (f'Adding Two Number {num1+num2}')

Name2 = 'Solo'
print(f'Print The Above Name {Name2}')

Score = 200
Percentile = 80
print (f'Checking The f-String {Score=} And {Percentile=}') # It Will Take The Refrence After = Which Asigned Above Variables

large_number = 10000000 # Snakecase Variable Name
print (f"Checkign With Large Number {large_number:,}") #It Will Auto Add The Comma For Large Value

pi_value = 3.12159 #Snakecase Variable Name
print (f'Checking f-String With three Decimal {pi_value:.3f}') #.3f means 3 decimal places

# Array and Object In Python
# In Python Array Is Called List And Object Is Called Dictionary
my_list = [2,4,5,6,7]
print (f'Print Array With f-String, {my_list}')

my_list.append(8) # Adding New Value To The Array
print (f'Print Array With Adding New Extra Number ,{my_list}')
print (len(my_list)) # It Will Print The Length Of The Array

#Obejct 
#Two Major Diffrence In Python Object And JavaScript Object
#1. In Python Object Is Called Dictionary
#2 Key Will Be In String Format 
#3 We Can Not Mutation The Object Like JavaScript Object We need To Reassign The Object To Update The Value In Python Dictionary'

my_dict = {
    'name': 'Yogesh',
    'age': 20,
    'city': 'Delhi'
}

print (f'Print The Object With f-String {my_dict}')

print ({my_dict["age"]}) # It Will Print The Age By Accesing The Key Value

print(f"Print The Name By f-String {my_dict['name']} and Age Is {my_dict['age']}") # It Will Print The Name And Age By Accesing The Key Value

my_dict['city'] = 'Gorakhpur City' # It Will Update The City Value

print ('Print The Updated City Name',my_dict['city'])

#if Else Condition In Python 

mob_number = 30

if (mob_number >20):
    print (f'Mobile Number is Greater Than 20',{mob_number})
elif (mob_number ==20):
    print (f"Mobile Number  Is Eqaul to 20",{mob_number})
else:
    print (f'Mobile Number Is Less Than 20',{mob_number})

healthy_point = 100

if (healthy_point>80):
    print(f'healthy point is greater than 80',{healthy_point})
elif (healthy_point == 80):
    print(f'healthy point is equal to 80',{healthy_point})
else:
    print(f'healthy point is less than 80',{healthy_point})

# Data Type In Python
#1. String
#2. Integer
#3. Float
#4. Boolean (True Or False Value Shoule Be First Letter Capital In Python)
#5. List (array in python)
#6. Dictionary (object in python)
#7 Nothing (None In Python)

type_of_name = 'Yogesh Singh'
type_of_number = 20
type_of_digit = 3.14
type_of_boolean = True
type_of_list = [1,2,3,4,5]
type_of_dict = {
    'name': 'Yogesh',
    'age': 20,
    'city': 'Delhi'
}
# type_of_none = None

print(f'Type Of The Name Is {type(type_of_name)}')
print(f'Type Of The Number Is {type(type_of_number)}')
print(f'Type Of The Digit Is {type(type_of_digit)}')
print(f'Type Of The Boolean Is {type(type_of_boolean)}')
print(f'Type Of The List Is {type(type_of_list)}')
print(f'Type Of The Dictionary Is {type(type_of_dict)}')
# print(f'Type Of The None Is {type(type_of_none)}')

# Input In Python
# input() Function Is Used To Take Input From The User In Python
# By Default It Will Take Input As String So We Need To Convert It To The Desired Data Type

player_name = int(input('Enter Player Number:'))
print (f'Player Name Is type{type(player_name)} And Value Is {player_name}')

player_age = (input('Enter Player Age:')) # It Will Give Error TypeError: '>' not supported between instances of 'str' and 'int'
player_age = int(input('Enter Player Age:')) # It Will Convert The Input To Integer Type So We Can Compare It With Integer Value
if player_age > 18:    
    print (f'Player is Eligible to Play The Game,{player_age}')