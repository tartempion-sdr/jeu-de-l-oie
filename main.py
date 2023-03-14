import pygame
import random
from joueurclass import Joueur

import time
from grille import Grille
pygame.init()


# future icone
#pygame_icon = pygame.image.load("/home/tartempion/Documents/python/pygame jeu de loie python/assets/oie-alsace.jpg")
#pygame.display.set_icon(pygame_icon)

# titre
pygame.display.set_caption("jeu de l'oie")
# generer la fenetre de notre jeu
screen = pygame.display.set_mode((850,567))

background = pygame.image.load("assets/verdure-rogner2-850x567.png")

background2 = pygame.image.load("assets/verdure850x567.png")
pictureAcceuil = pygame.image.load("assets/oie2.jpeg")
messageAcceuil = pygame.image.load("assets/message-acceuil.png")

# en cour - generer dé, pion, face123456
pionQuiIndiquePoint_joueur1 = pygame.image.load("assets/blanc-chess-mini.png")
pionQuiIndiquePoint_joueurIA = pygame.image.load("assets/noir-chess-mini.png")
        


decliquable = pygame.image.load("assets/de.png")
# charger joueur

joueur = Joueur()
running = True

acceuil = True


while acceuil :

    # appliquer a l'arriere plan de notre jeu
    screen.blit(background2,(0,0))
    screen.blit(pictureAcceuil,(317,333))
    screen.blit(messageAcceuil,(251,272))
    
    
    #mettre à jour l'arriere plan
    pygame.display.flip()


    # si le joueur clic , le joueur passe au jeu
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            joueur.sound_manager.play("de") 
            acceuil = False
        # si le joueur ferme cette fenetre
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()    
            
    
    
    
    

# boucle tant que cette condition est vrai
while running:
    #  affiche le pion a qui le tour en bas a droite
    
    if joueur.cestaujoueur1dejouer  == True:
                
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
    elif game.joueurIA.valeurdude_joueurIA == 1:    
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-1-b.svg.png")
    elif game.joueurIA.valeurdude_joueurIA == 2:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-2-b.svg.png")
    elif game.joueurIA.valeurdude_joueurIA == 3:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-3-b.svg.png")
    elif game.joueurIA.valeurdude_joueurIA == 4:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-4-b.svg.png")
    elif game.joueurIA.valeurdude_joueurIA == 5:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-5-b.svg.png")
    elif game.joueurIA.valeurdude_joueurIA == 6:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-6-b.svg.png")
        

    
    

    # appliquer a l'arriere plan de notre jeu
    screen.blit(background,(0,0))
    
    # applique l'image de mon joueur1  !!!!!!  dé, pion, face123456
    screen.blit(game.joueur1.image_joueur1, game.joueur1.rect_joueur1)
    
    screen.blit(game.joueurIA.image_joueurIA, game.joueurIA.rect_joueurIA)
    
    # pion qui indique les des
    screen.blit(pionQuiIndiquePoint_joueur1,(387,258))
    screen.blit(pionQuiIndiquePoint_joueurIA,(387,315))
    
    #pion a qui le tour
    screen.blit(pionAQuiLeTour,(22,82))
    #de cliquable , pas encors
    screen.blit(decliquable,(79,82))

    #des
    screen.blit(faceDuDe_joueur1,(330,258))
    screen.blit(faceDuDe_joueurIA,(330,315))
    
    #mettre à jour l'arriere plan
    pygame.display.flip()

    # si le joueur ferme cette fenetre


    for event in pygame.event.get():
           # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
    
            pygame.quit()    
                          

    # lance le "de" avec le clic de la souris ou avec la touche d 
               
            
        if event.type == pygame.MOUSEBUTTONDOWN and game.joueur1.cestaujoueur1dejouer == True  :
                            
             
            # 1 joueur
            game.joueur1.printrandom1()
            game.joueur1.deplacementdupion1()
            print("1-1 " + str(game.joueur1.cestaujoueur1dejouer))
        
        elif game.joueur1.position1 == game.joueurIA.positionIA and game.joueurIA.positionIA != 0:
            game.joueurIA.colision1()
            print("1-2 " + str(game.joueur1.cestaujoueur1dejouer))
        
            


        else:
                
            game.joueur1.reverif1()
            
            
            print("1-3 " + str(game.joueur1.cestaujoueur1dejouer))
            print("J-1" , int(game.joueur1.position1))
            print("J-IA" , int(game.joueurIA.positionIA))    
            game.joueur1.cestaujoueur1dejouer = False
            
            #colision 
            
        
            
            
        
                

            
            
        while game.joueur1.cestaujoueur1dejouer == False:

            # IA joueur
            time.sleep(1)           
            game.joueurIA.printrandomIA()
        

            game.joueurIA.deplacementdupionIA()
            print("2-1 " + str(game.joueur1.cestaujoueur1dejouer)) 
            print("2-1 " + str(game.joueurIA.cestaujoueurIAdejouer)) 
        
            
        if game.joueurIA.positionIA == game.joueur1.position1  and game.joueurIA.positionIA != 0:
            game.joueurIA.colisionIA()

            game.joueurIA.rect_joueur1.x = Grille[game.joueurIA.position1][1] 
            game.joueurIA.rect_joueur1.y = Grille[game.joueurIA.position1][2]
            print("2-2 " + str(game.joueur1.cestaujoueur1dejouer)) 
            print("2-2 " + str(game.joueurIA.cestaujoueurIAdejouer)) 
            

        else:
            
            game.joueurIA.revefifIA()
            game.joueurIA.rect_joueurIA.x = Grille[game.joueurIA.positionIA][1] 
            game.joueurIA.rect_joueurIA.y = Grille[game.joueurIA.positionIA][2]
            print("2-3 " + str(game.joueur1.cestaujoueur1dejouer)) 
            print("2-3 " + str(game.joueurIA.cestaujoueurIAdejouer)) 

            print("J-IA" , int(game.joueurIA.positionIA))
            print("J-1" , int(game.joueur1.position1))
            game.joueur1.cestaujoueur1dejouer = True
            

    
            game.joueur1.cestaujoueur1dejouer =  True
            game.joueurIA.cestaujoueurIAdejouer = False  
            break            
        
        
                    
                    
