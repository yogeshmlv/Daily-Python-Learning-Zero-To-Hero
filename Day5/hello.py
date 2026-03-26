# built-in Function open() is used to open a file and returns a file object, also called a handle, as it is used to read or modify the file accordingly.
# The syntax of the open() function is as follows:
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# The open() function takes several parameters, but the most commonly used ones are:
# - file: The path to the file you want to open.
# - mode: The mode in which you want to open the file. The default is 'r' (read mode). Other common modes include 'w' (write mode), 'a' (append mode), and 'b' (binary mode).
# - encoding: The encoding format to use when reading or writing the file. This is important for handling text files with different character encodings.
# - errors: Specifies how to handle encoding and decoding errors. Common values include 'ignore', 'replace', and 'strict'.
# - newline: Controls how universal newlines works (it translates different newline characters into a single '\n' character). This is useful when working with text files that may have different newline conventions (e.g., Windows uses '\r\n', while Unix/Linux uses '\n').

player_gold = 100

player_weapon = "Sword"
#with open() is used to ensure that the file is properly closed after its suite finishes, even if an exception is raised. It is a context manager that provides a cleaner and more efficient way to work with files.
with open ("player_info.txt","w") as file:
    #write() method is used to write a string to the file. It takes a string as an argument and writes it to the file at the current position of the file pointer. If the file is opened in write mode ('w'), it will overwrite the existing content of the file. If the file is opened in append mode ('a'), it will add the new content to the end of the file without overwriting it.
    file.write(f"Player Gold: {player_gold}\n")
    file.write(f"Player Weapon: {player_weapon}\n")
print("Player information has been saved to player_info.txt")

print("Main Menu ")
print ("Game Is loading...")
try:
    with open ("player_info.txt","r") as file:
        saved_lines = file.readlines() # The readlines() method is used to read all the lines from a file and return them as a list of strings. Each string in the list represents a single line from the file, including the newline character at the end of each line. This method is useful when you want to process or manipulate each line of the file separately, as it allows you to easily access and iterate through the lines using list indexing or loops.
        player_gold = int(saved_lines[0].split(":")[1].strip()) # strip() method is used to remove any leading and trailing whitespace characters from a string. In this case, it is used to clean up the extracted value of player gold after splitting the line by the colon (":") character. The split() method is used to divide the string into a list based on the specified delimiter (in this case, ":"). The [1] index is used to access the second element of the resulting list, which contains the value of player gold. Finally, int() is used to convert the string representation of player gold into an integer for further calculations or usage in the program.
        player_weapon = saved_lines[1].split(":")[1].strip() 
    print (f"Player Gold: {player_gold}")
    print (f"Player Weapon: {player_weapon}")
except FileNotFoundError:
    print("Error: player_info.txt not found. Please ensure the file exists and try again.")