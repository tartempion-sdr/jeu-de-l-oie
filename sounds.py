import pygame


class SoundManager:
    def __init__(self):
        self.sound = {
            "pion": pygame.mixer.Sound("assets/sounds/pion-son.ogg"),
            "de": pygame.mixer.Sound("assets/sounds/de.ogg"),
            "oie": pygame.mixer.Sound("assets/sounds/oie.ogg")}
        

    def play(self, name):
        self.sound[name].play()