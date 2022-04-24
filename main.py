# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:22:11 2022

@author: youne
"""

import sys
import json 
    
file_name = "Mes_courses"
Liste_achat = []
try:
    with open(f"{file_name}.json", "r") as f:
        Liste_achat = json.load(f)
except:
    with open(f"{file_name}.json", "w") as f:
        json.dump(list(range(0)), f, indent = 4 ) 
    
def Ajouter():
    global Liste_achat
    element = input('Ajouter un élément à la liste de course :')
    element = element[0].upper() + element[1:]
    if not element in Liste_achat:
        Liste_achat.append(element)
        print(f"L'élément {element} a bien été ajouté à la liste.")
    else:
        print(f"L'élément {element} est déja dans la liste.")
def Retirer():
    global Liste_achat
    element_retirer = input("Entrer le nom d'un élément à retirer de la liste de courses : ")
    element_retirer = element_retirer[0].upper() + element_retirer[1:]
    if element_retirer in Liste_achat:
        Liste_achat.remove(element_retirer)
        print(f"L'élément {element_retirer} a bien été supprimer de la liste.")
    else:
        print(f"L'élément {element_retirer} n'est pas dans la liste.")
      
def Afficher():
    global Liste_achat      
    if not Liste_achat:
        print("Votre liste ne contient aucun élément.")
    else:
        print("Les éléments de votre liste :")
        for i, element in enumerate(Liste_achat):
            print(f"{i+1}.  {element}")
        
        
def Vider():
    global Liste_achat
    Liste_achat = []
    print("Vous n'avez aucun élement dans votre liste")


def Quitter():
    global Liste_achat
    file_name = "Mes_courses"
    
    with open(f"{file_name}.json", "r") as f:
        donnees = json.load(f)
    
    
    with open(f"{file_name}.json", "w") as f:
        
        for e in Liste_achat:
            if not e in donnees:
                donnees.append(e)
        json.dump(donnees, f, indent = 4 )
    
    print("A bientôt !")
    sys.exit()



while True:
    print("\nChoisissez parmi les 5 commandes suivante:\n  1: Ajouter un élément à la liste\n  2: Retirer un élément de la liste\n  3: Afficher la liste\n  4: Vider la liste\n  5: Quitter\n")
    print()
    cmd = input("-> Votre choix : ")
    if cmd == "1":
        Ajouter()
    elif cmd == "2":
        Retirer()
    elif cmd == "3":
        Afficher()
    elif cmd == "4":
        Vider()
    elif cmd == "5":
        Quitter()
    else:
        print("ERREUR: Commande inconnue")
        print()