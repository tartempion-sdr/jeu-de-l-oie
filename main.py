import pygame
import random
from joueurclass import Joueur

import time
from grille import Grille
pygame.init()


# future icone
pygame_icon = pygame.image.load("assets/oie-icon.png")
pygame.display.set_icon(pygame_icon)

# titre
pygame.display.set_caption("  jeu de l'oie")
# generer la fenetre de notre jeu
screen = pygame.display.set_mode((850,567))



backgroundAcceuil = pygame.image.load("assets/verdure850x567.png")
pictureAcceuil = pygame.image.load("assets/oie2.jpeg")
messageAcceuil = pygame.image.load("assets/message-acceuil.png")

background = pygame.image.load("assets/verdure-rogner2-850x567.png")

# - generer dé, pion, face123456
pionBlanc = pygame.image.load("assets/blanc-chess-mini.png")
pionNoir = pygame.image.load("assets/noir-chess-mini.png")

de0 = "assets/de.png"   
de1 = "assets/64px-Dice-1-b.svg.png"
de2 = "assets/64px-Dice-2-b.svg.png"
de3 = "assets/64px-Dice-3-b.svg.png"
de4 = "assets/64px-Dice-4-b.svg.png"
de5 = "assets/64px-Dice-5-b.svg.png"
de6 = "assets/64px-Dice-6-b.svg.png"
deListe = [de0, de1, de2, de3, de4, de5, de6] 
    
    
        



decliquable = pygame.image.load("assets/de.png")

# charger joueur

joueur = Joueur()




while joueur.acceuil :

    # appliquer a l'arriere plan de notre jeu
    screen.blit(backgroundAcceuil,(0,0))
    screen.blit(pictureAcceuil,(0,333))
    screen.blit(messageAcceuil,(0,272))
    
    
    #mettre à jour l'arriere plan
    pygame.display.flip()


    # si le joueur clic , le joueur passe au jeu
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            joueur.sound_manager.play("oie") 
            joueur.acceuil = False
            joueur.running = True
        # si le joueur ferme cette fenetre
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()    
            
    

    

# boucle tant que cette condition est vrai
while joueur.running:
    

    faceDuDejoueur1 = pygame.image.load(deListe[joueur.valeurdude_joueur1])

    faceDuDejoueurIA = pygame.image.load(deListe[joueur.valeurdude_joueurIA])    
        
#  affiche le pion a qui le tour en bas a droite
# affiche valeur du dé pour joueur1 et joueurIA
    if joueur.cestaujoueur1dejouer  == True:
                
        pionAQuiLeTour = pionBlanc
        
    else:
        pionAQuiLeTour = pionNoir
       
    
    
    
    # appliquer a l'arriere plan de notre jeu
    screen.blit(background,(0,0))
    
    # applique l'image de mon joueur1  !!!!!!  dé, pion, face123456
    screen.blit(joueur.image_joueur1, joueur.rect_joueur1)
    
    screen.blit(joueur.image_joueurIA, joueur.rect_joueurIA)
    
    # pion qui indique les des
    screen.blit(pionBlanc,(387,258))
    screen.blit(pionNoir,(387,315))
    
    #pion a qui le tour
    screen.blit(pionAQuiLeTour,(22,82))
    #de cliquable , pas encors
    screen.blit(decliquable,(79,82))

    #des
    screen.blit(faceDuDejoueur1,(330,258))
    screen.blit(faceDuDejoueurIA,(330,315))
    #mettre à jour l'arriere plan
    pygame.display.flip()
        
    # si le joueur ferme cette fenetre


    for event in pygame.event.get():
           # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
    
            pygame.quit()    
                          

    # lance le "de" avec le clic de la souris ou avec la touche d 
               
            
        if event.type == pygame.MOUSEBUTTONDOWN and joueur.cestaujoueur1dejouer == True  :
                            
            
            # 1 joueur
            joueur.printrandom1()
            joueur.deplacementdupion1()
           
            
            
            joueur.colision1()

            
            joueur.reverif1() 
    
        
            joueur.cestaujoueur1dejouer = False
            
            
        elif joueur.cestaujoueur1dejouer == False:

            # IA joueur
            time.sleep(1)           
            joueur.printrandomIA()
            joueur.deplacementdupionIA()
        
                
        
            joueur.colisionIA()
                
            joueur.revefifIA()
            joueur.cestaujoueur1dejouer = True
    
    
while joueur.findepartie == True:

     # appliquer a l'arriere plan de notre jeu
    screen.blit(backgroundAcceuil,(0,0))
    screen.blit(pictureAcceuil,(0,333))
    
    
    
    #mettre à jour l'arriere plan
    pygame.display.flip()


    # si le joueur clic , le joueur passe au jeu
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            joueur.sound_manager.play("oie") 
            joueur.findepartie = False
            joueur.acceuil = True
        # si le joueur ferme cette fenetre
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()    
                
     
                       
        
        
                    
                    
