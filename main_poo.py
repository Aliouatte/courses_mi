# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 23:31:45 2022

@author: youne
"""

import json
import logging


LOGGER = logging.getLogger()
 
       
class Liste(list):
    
   def __init__(self,nom):
       self.nom = nom
    
   def Ajouter(self,element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des noms (chaine de caractéres) !")
            
        if element in self:
            LOGGER.error(f"{element} est déja dans la liste !")
            return False
        
        self.append(element)
        return True
    
   def Supprimer(self,element):
        if element in self:
            self.remove(element)  
            return True 
        return False
    
    
   def Afficher(self):
       print(f"Votre liste de {self.nom} contient les élements suivant :\n  {' - '.join(self)}")


   def Sauvegarder(self):
       
       with open(f"{self.nom}.json", "w") as f:
           json.dump(self, f, indent = 4)
           
       return True
           
        
      


#if __name__ == "__main__":
    
l = Liste("Courses")
l.Ajouter("Chocolat")
l.Sauvegarder()
l.Afficher()    