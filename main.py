import pygame
import random
from joueurclass import Joueur
from game import Game
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
pionAQuiLeTour = pygame.image.load("assets/noir-chess-mini.png")
faceDuDe = pygame.image.load("assets/64px-Dice-1-b.svg.png")
decliquable = pygame.image.load("assets/de.png")
# charger joueur

game = Game()
running = True


# boucle tant que cette condition est vrai
while running:

    # appliquer a l'arriere plan de notre jeu
    screen.blit(background,(0,0))
    
    # applique l'image de mon joueur1  !!!!!!  dé, pion, face123456
    screen.blit(game.joueur1.image_joueur1, game.joueur1.rect_joueur1)
    screen.blit(game.joueurIA.image_joueurIA, game.joueurIA.rect_joueurIA)
    
    screen.blit(pionAQuiLeTour,(679,510))
    screen.blit(faceDuDe,(736,510))
    screen.blit(decliquable,(793,510))

    #mettre à jour l'arriere plan
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
       
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_d:
                
                game.joueur1.printrandom() 
                game.joueur1.deplacementdupion()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("OK OK")
            game.joueur1.printrandom() 
            game.joueur1.deplacementdupion()