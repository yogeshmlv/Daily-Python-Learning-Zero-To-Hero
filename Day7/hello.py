single_values = [1, 2, 3, 4, 5] #In Python As A List Comprehension To Create A New List By Applying An Expression To Each Item In An Iterable. In This Example, We Are Doubling Each Value In The 'single_values' List.
double_values = [x * 2 for x in single_values]
print (double_values) # Output: [2, 4, 6, 8, 10]

human_hp = [12,10,8,6,4,2,0] #In Python As A List Comprehension To Filter Out Values From A List Based On A Condition. In This Example, We Are Filtering Out HP Values That Are Greater Than 5.
filtered_hp = [hp for hp in human_hp if hp > 5]
print(filtered_hp) # Output: [12, 10, 8, 6]

list_item = ["magic sword ", " hero shield ", "health potion ", "Bow"] #In Python As A List Comprehension To Create A New List By Applying An Expression To Each Item In An Iterable. In This Example, We Are Converting Each Item In The 'list_item' List To Uppercase.
# updated_list = [item.title() for item in list_item if item.strip()] # We Use 'strip()' To Remove Any Leading Or Trailing Whitespace From The Item Before Converting It To Title Case.
updated_list = [item.title() for item in list_item if "sword" in item] # We Use 'strip()' To Remove Any Leading Or Trailing Whitespace From The Item Before Converting It To Title Case.

print(updated_list) # Output: ['Magic Sword', 'Hero Shield', 'Health Potion', 'Bow']