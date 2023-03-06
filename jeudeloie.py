import pygame
import random
from pynput.keyboard import  Listener, Key
from pynput.keyboard import Key
from pynput import *

class Parametres:    
    """
     blabla
    """
    def __init__(self):
        
        
        
        self.nomjoueur = ""
        self.position = int()
        self.grille = list
        self.valeurdude = int()

    def entrez_votre_nom(self):
        
        while self.nomjoueur == str(""):
       
            self.nomjoueur = input("veuillez entrer votre nom : ")
            if self.nomjoueur != str(""):
                print("Vous Vous appellez : " + self.nomjoueur)
                print("\n" + self.nomjoueur + " appuyer sur la touche a pour lancé le dé\n")
    
    def lancerlede(self):
        
        def on_press(key):
            
            if key.char ==  "a" :     
                J1.valeurdude = J1.printrandom()
                pass
                    
            
        
        with Listener(on_press=on_press, ) as listener:

            listener.join()    
        
    def printrandom(self):
            
            de = str(random.randint(1, 6))
            deresultat = de
            print(J1.valeurdude)
            return deresultat 
                
     
        
    

J1 = Parametres()

J1.entrez_votre_nom()

J1.lancerlede()







    



