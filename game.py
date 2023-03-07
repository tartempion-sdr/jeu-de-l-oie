import pygame
from joueurclass import Joueur



class Game:
    def __init__(self):
        self.cestaquidejouer = True  
        self.joueur1 = Joueur()    
        self.joueurIA = Joueur()
            
