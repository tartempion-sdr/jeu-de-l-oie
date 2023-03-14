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

# en cour - generer dé, pion, face123456
pionBlanc = pygame.image.load("assets/blanc-chess-mini.png")
pionNoir = pygame.image.load("assets/noir-chess-mini.png")
        


decliquable = pygame.image.load("assets/de.png")
# charger joueur

joueur = Joueur()
running = True
acceuil = True


while acceuil :

    # appliquer a l'arriere plan de notre jeu
    screen.blit(backgroundAcceuil,(0,0))
    screen.blit(pictureAcceuil,(0,333))
    screen.blit(messageAcceuil,(0,272))
    
    
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
                
        pionAQuiLeTour = pionBlanc
                
    else:
        pionAQuiLeTour = pionNoir
        
        


    

    if joueur.valeurdude_joueur1 == 0:    
        faceDuDe_joueur1 = pygame.image.load("assets/de.png")
    elif joueur.valeurdude_joueur1 == 1:    
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-1-b.svg.png")
    elif joueur.valeurdude_joueur1 == 2:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-2-b.svg.png")
    elif joueur.valeurdude_joueur1 == 3:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-3-b.svg.png")
    elif joueur.valeurdude_joueur1 == 4:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-4-b.svg.png")
    elif joueur.valeurdude_joueur1 == 5:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-5-b.svg.png")
    elif joueur.valeurdude_joueur1 == 6:
        faceDuDe_joueur1 = pygame.image.load("assets/64px-Dice-6-b.svg.png")



    if joueur.valeurdude_joueurIA == 0:    
        faceDuDe_joueurIA = pygame.image.load("assets/de.png")
    elif joueur.valeurdude_joueurIA == 1:    
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-1-b.svg.png")
    elif joueur.valeurdude_joueurIA == 2:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-2-b.svg.png")
    elif joueur.valeurdude_joueurIA == 3:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-3-b.svg.png")
    elif joueur.valeurdude_joueurIA == 4:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-4-b.svg.png")
    elif joueur.valeurdude_joueurIA == 5:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-5-b.svg.png")
    elif joueur.valeurdude_joueurIA == 6:
        faceDuDe_joueurIA = pygame.image.load("assets/64px-Dice-6-b.svg.png")
        

    
    

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
               
            
        if event.type == pygame.MOUSEBUTTONDOWN and joueur.cestaujoueur1dejouer == True  :
                            
             
            # 1 joueur
            joueur.printrandom1()
            joueur.deplacementdupion1()
            print("1-1 " + str(joueur.cestaujoueur1dejouer))
        
            if joueur.position1 == joueur.positionIA and joueur.positionIA != 0:
                joueur.colision1()
                print("1-2 " + str(joueur.cestaujoueur1dejouer))
           
            joueur.reverif1()
            print("1-3 " + str(joueur.cestaujoueur1dejouer))
            print("J-1" , int(joueur.position1))
            print("J-IA" , int(joueur.positionIA))    
            joueur.cestaujoueur1dejouer = False
            
            
        elif joueur.cestaujoueur1dejouer == False:

            # IA joueur
            time.sleep(1)           
            joueur.printrandomIA()
            joueur.deplacementdupionIA()
            print("2-1 " + str(joueur.cestaujoueur1dejouer)) 
            
        
            
            if joueur.positionIA == joueur.position1  and joueur.positionIA != 0:
                joueur.colisionIA()
                joueur.rect_joueur1.x = Grille[joueur.position1][1] 
                joueur.rect_joueur1.y = Grille[joueur.position1][2]
                print("2-2 " + str(joueur.cestaujoueur1dejouer)) 
                
            

       
            
            joueur.revefifIA()
            joueur.rect_joueurIA.x = Grille[joueur.positionIA][1] 
            joueur.rect_joueurIA.y = Grille[joueur.positionIA][2]            
            print("2-3 " + str(joueur.cestaujoueur1dejouer)) 
            print("J-IA" , int(joueur.positionIA))
            print("J-1" , int(joueur.position1))
            joueur.cestaujoueur1dejouer = True
            

    
            
             
            break            
        
        
                    
                    
