import pygame
import random
from joueurclass import Joueur
from game import Game
import time
pygame.init()


# future icone
#pygame_icon = pygame.image.load("/home/tartempion/Documents/python/pygame jeu de loie python/assets/oie-alsace.jpg")
#pygame.display.set_icon(pygame_icon)

# titre
pygame.display.set_caption("jeu de l'oie")
# generer la fenetre de notre jeu
screen = pygame.display.set_mode((850,567))

background = pygame.image.load("assets/verdure850x567.jpg")

# en cour - generer dé, pion, face123456

     
pionQuiIndiquePoint_joueur1 = pygame.image.load("assets/blanc-chess-mini.png")
pionQuiIndiquePoint_joueurIA = pygame.image.load("assets/noir-chess-mini.png")
        


decliquable = pygame.image.load("assets/de.png")
# charger joueur

game = Game()
running = True


# boucle tant que cette condition est vrai
while running:
    # recule et affiche le pion a qui le tour
    
    if game.cestaquidejouer  == True:
                pionAQuiLeTour = pygame.image.load("assets/blanc-chess-mini.png")
                
    else:
        pionAQuiLeTour = pygame.image.load("assets/noir-chess-mini.png")
        
        
   

    

    if game.joueur1.valeurdude_joueur1 == 0:    
        faceDuDe_joueur1 = pygame.image.load("assets/de.png")
    elif game.joueur1.valeurdude_joueur1 == 1:    
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-1-b.svg.png")
    elif game.joueur1.valeurdude_joueur1 == 2:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-2-b.svg.png")
    elif game.joueur1.valeurdude_joueur1 == 3:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-3-b.svg.png")
    elif game.joueur1.valeurdude_joueur1 == 4:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-4-b.svg.png")
    elif game.joueur1.valeurdude_joueur1 == 5:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-5-b.svg.png")
    elif game.joueur1.valeurdude_joueur1 == 6:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-6-b.svg.png")



    if game.joueurIA.valeurdude_joueurIA == 0:    
        faceDuDe_joueurIA = pygame.image.load("assets/de.png")
    elif game.joueurIA.valeurdude_joueur1 == 1:    
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-1-b.svg.png")
    elif game.joueurIA.valeurdude_joueur1 == 2:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-2-b.svg.png")
    elif game.joueurIA.valeurdude_joueur1 == 3:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-3-b.svg.png")
    elif game.joueurIA.valeurdude_joueur1 == 4:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-4-b.svg.png")
    elif game.joueurIA.valeurdude_joueur1 == 5:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-5-b.svg.png")
    elif game.joueurIA.valeurdude_joueur1 == 6:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-6-b.svg.png")
        

    
    

    # appliquer a l'arriere plan de notre jeu
    screen.blit(background,(0,0))
    
    # applique l'image de mon joueur1  !!!!!!  dé, pion, face123456
    screen.blit(game.joueur1.image_joueur1, game.joueur1.rect_joueur1)
    screen.blit(game.joueurIA.image_joueurIA, game.joueurIA.rect_joueurIA)
    
    screen.blit(pionQuiIndiquePoint_joueur1,(57,0))
    screen.blit(pionQuiIndiquePoint_joueurIA,(57,57))

    screen.blit(pionAQuiLeTour,(736,510))

    screen.blit(faceDuDe_joueur1,(0,0))
    screen.blit(faceDuDe_joueurIA,(0,57))

    screen.blit(decliquable,(793,510))

    #mettre à jour l'arriere plan
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    
    
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
       
            pygame.quit()

# lance le "de" avec la touche d 
#            
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_d and game.cestaquidejouer is True:
                 
                    game.joueur1.printrandom() 
                    game.joueur1.deplacementdupion()
                    game.cestaquidejouer = False
                    break
           
                 
        elif game.cestaquidejouer is False:            
            game.joueurIA.printrandom()
            game.joueurIA.deplacementdupion()
            game.cestaquidejouer = True
            time.sleep(2)
            continue
        
# a améliorer ... lance le "de" avec la souris, prochainement que la souris ne lance la fonction que sur le de
        if event.type == pygame.MOUSEBUTTONDOWN and game.cestaquidejouer is True:
             
            game.joueur1.printrandom() 
            game.joueur1.deplacementdupion()
            game.cestaquidejouer = False
            break

        elif game.cestaquidejouer is False: 
            game.joueurIA.printrandom()
            game.joueurIA.deplacementdupion()
            
            game.cestaquidejouer = True
            time.sleep(2)
            continue