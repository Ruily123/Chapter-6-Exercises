# -*- coding: utf-8 -*-
"""02-Movie_Tickets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nRco4WbAoLsR3q3GOEjeMCo28y91xiJ4
"""

age = input("What is your age? ")
if int(age) < 3:
    print("Your ticket is free")
elif int(age) <= 12:
    print("Your ticket costs 10$")
elif int(age) > 12:
    print("Your ticket costs 15$")