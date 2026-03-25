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