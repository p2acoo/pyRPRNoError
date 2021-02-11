# jeu du juste prix améliorer + gestion d'erreur + condition

import random
import sys

MIN = 1
MAX = 1000

nombre = random.randint(1, 999)
while True:
    while True:
        essai = input("Veuillez saisir un chiffre ou un nombre entre " + str(MIN) + " et " + str(MAX) + ". ")
        try:
            essai = int(essai)
        except:
            print("UN CHIFFRE OU UN NOMBRE")
            pass
        else:
            if 0 <= essai <= 999:
                break
            if essai > 999:
                print("EN DESSOUS DE 1000")
            if essai < 0:
                print("A PARTIR DE 0")
    if essai < nombre:
        print("Plus grand !")
    elif essai > nombre:
        print("Plus petit !")
    else:
        print("C'est Gagner !")
        break
