# def test_function ():
#     print("Hello World")
# test_function()
# def is Keyword in Python?
# def Keyword in Python is a reserved word that has a specific meaning and cannot be used as an identifier (such as variable names, function names, etc.) in the code. Examples of keywords in Python include "if", "else", "for", "while", "def", "return", and many more. These keywords are essential for the structure and syntax of the Python programming language.
def greet(name):
    print(f"Hello, {name}!")
greet("Yogesh Singh")
greet("Alice")
greet("Bob")


def tax_calculation (price,tax_rate):
    tax_amount = price*tax_rate
    total_price = price +tax_amount
    return total_price

my_total_price = tax_calculation(1000,0.09)
print (f"Yogesh Singh , The Total Price After Tax is {my_total_price}")