import pygame
import random
from joueurclass import Joueur
from game import Game
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

game = Game()
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
            game.joueur1.sound_manager.play("de") 
            acceuil = False
            
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()    
            
    
    
    # si le joueur ferme cette fenetre
    
    # for event in pygame.event.get():
    #     # que l'evenement est fermeture de fenetre
    #     if event.type == pygame.QUIT:
    #         running = False
    #         pygame.quit()

    


# boucle tant que cette condition est vrai
while running:
    #  affiche le pion a qui le tour en bas a droite
    
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
#            
        if event.type == pygame.MOUSEBUTTONDOWN and game.cestaquidejouer is True or event.type == pygame.KEYDOWN and event.key==pygame.K_d and game.cestaquidejouer is True:
                           
                # 1 joueur
                    
                    game.joueur1.printrandom1() 
                    game.joueur1.deplacementdupion1()
                    game.cestaquidejouer = False
                    
                    if game.joueur1.position1 == 63:
                        print("l'IA HALLL 9000 A GAGNER !!!!!!")
                        #acceuil = True

                    if game.joueur1.position1 == 58:
                        game.joueur1.position1 = 0
                        game.joueur1.deplacementdupion1()
                        

                    if game.joueur1.position1 == 46:
                        game.joueur1.position1 = 54
                        game.joueur1.deplacementdupion1()

                    if game.joueur1.position1 == 42:
                        game.joueur1.position1 = 30
                        game.joueur1.deplacementdupion1()

                    if game.joueur1.position1 == 40:
                        game.joueur1.position1 = 62
                        game.joueur1.deplacementdupion1()

                    if game.joueur1.position1 == 36:
                        game.joueur1.position1 += game.joueur1.valeurdude_joueur1
                        game.joueur1.deplacementdupion1()

                    if game.joueur1.position1 == 27:
                        game.joueur1.position1 = 57
                        game.joueur1.deplacementdupion1()     

                    if game.joueur1.position1 == 26:
                        game.joueur1.position1 += game.joueur1.valeurdude_joueur1
                        game.joueur1.deplacementdupion1()

                    if game.joueur1.position1 == 8:
                        game.joueur1.position1 += game.joueur1.valeurdude_joueur1
                        game.joueur1.deplacementdupion1()

                    if game.joueur1.position1 == game.joueurIA.positionIA :
                        # Celui qui est rejoint par un autre joueur sur la même case devra se rendre sur la case ou l’autre joueur se situait avant de jouer.
                        game.joueurIA.positionIA -= game.joueur1.valeurdude_joueur1
                        game.joueur1.deplacementdupion1()
                        #pass
                    
                        #break 
                    
        # IA joueur
        elif game.cestaquidejouer is False: 
            time.sleep(1)           
            game.joueurIA.printrandomIA()
            game.joueurIA.deplacementdupionIA()
            game.cestaquidejouer = True
            
            

            

            if game.joueurIA.positionIA == 63:
                print("l'IA HALLL 9000 A GAGNER !!!!!!")
                #acceuil = True

            if game.joueurIA.positionIA == 58:
                game.joueurIA.positionIA == 0
                game.joueurIA.deplacementdupionIA()

            if game.joueurIA.positionIA == 46:
                game.joueurIA.positionIA = 8
                game.joueurIA.deplacementdupionIA()

            if game.joueurIA.positionIA == 42:
                game.joueurIA.positionIA = 30
                game.joueurIA.deplacementdupionIA()

            if game.joueurIA.positionIA == 40:
                game.joueurIA.positionIA = 62
                game.joueurIA.deplacementdupionIA()

            if game.joueurIA.positionIA == 36:
                game.joueurIA.positionIA += game.joueurIA.valeurdude_joueurIA
                game.joueurIA.deplacementdupionIA()


            if game.joueurIA.positionIA == 27:
                game.joueurIA.positionIA = 57
                game.joueurIA.deplacementdupionIA()

            if game.joueurIA.positionIA == 26:
                game.joueurIA.positionIA += game.joueurIA.valeurdude_joueurIA
                game.joueurIA.deplacementdupionIA()

            if game.joueurIA.positionIA == 8:
                game.joueurIA.positionIA += game.joueurIA.valeurdude_joueurIA
                game.joueurIA.deplacementdupionIA()



            # Celui qui est rejoint par un autre joueur sur la même case devra se rendre sur la case ou l’autre joueur se situait avant de jouer.
            if game.joueurIA.positionIA == game.joueur1.position1 :
                game.joueur1.position1 -= game.joueurIA.valeurdude_joueurIA
                game.joueurIA.deplacementdupionIA()
                
                
                
        
