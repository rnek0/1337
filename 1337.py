#!/usr/bin/python

""" 1337 Strings:
Prends une chaîne et la convertit en 1337.
Peut être utile pour les mots de passe ;).
"""
import sys

Dic = {"A": "4", "B": "8", "C": "(", "D": "d", "E": "3", "F": "f", "G": "6", "H": "#", "I": "|", "J": "j", "K": "k", "L": "l", "M": "m",
       "N": "n", "O": "0", "P": "p", "Q": "q", "R": "2", "S": "5", "T": "7", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z"}


def presentation_programme():
    print("Bonjour !", end='\n')
    print("Ceci est un programme \"1337 Strings\" élémentaire.\n")
    phrase = input(' Entrez vôtre phrase: ')
    return phrase


strTo1337 = presentation_programme()
print(strTo1337)

str = strTo1337.upper()
ctp = 0
while ctp < len(str):
    for key, val in Dic.items():
        if key == str[ctp]:
            print(val, end="")
        elif str[ctp] == " ":
            print("a", end="")
            break
    ctp = ctp + 1
print("\n")
