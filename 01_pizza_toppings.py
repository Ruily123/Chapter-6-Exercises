# -*- coding: utf-8 -*-
"""01-Pizza_Toppings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/176BKxKSX9zQegqAufG4wHhCTWN9AFNZR
"""

toppings = "Input 'quit' when you are satisfied with the amount of toppings."
toppings += "\nWhat pizza toppings would you like on your pizza? "
message = " "
while message != "quit":
    message = input(toppings)
    print(message, "will be added to your pizza. ('quit' will not be added to your pizza)\n")