import pygame
import random
from joueurclass import Joueur1
from game import Game
pygame.init()



    

# generer la fenetre de notre jeu
#pygame_icon = pygame.image.load("/home/tartempion/Documents/python/pygame jeu de loie python/assets/oie-alsace.jpg")
#pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("jeu de l'oie")
screen = pygame.display.set_mode((850,567))

background = pygame.image.load("assets/verdure850x567.jpg")

# charger joueur1

game = Game()
running = True


# boucle tant que cette condition est vrai
while running:

    # appliquer a l'arriere plan de notre jeu
    screen.blit(background,(0,0))
    
    # applique l'image de mon joueur1
    screen.blit(game.joueur.image, game.joueur.rect)

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
                deresultat = game.joueur.printrandom()