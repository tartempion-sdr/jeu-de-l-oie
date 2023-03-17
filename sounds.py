import pygame


class SoundManager:
    def __init__(self):
        self.sound = {
            "pion": pygame.mixer.Sound("assets/sounds/pion-son.ogg"),
            "de": pygame.mixer.Sound("assets/sounds/de.ogg"),
            "hotel": pygame.mixer.Sound("assets/sounds/hotel.ogg"),
            "plouf": pygame.mixer.Sound("assets/sounds/plouf.ogg"),
            "prison": pygame.mixer.Sound("assets/sounds/prison.ogg"),
            "mort": pygame.mixer.Sound("assets/sounds/mort.ogg"),
            "oie": pygame.mixer.Sound("assets/sounds/oie.ogg")}
        

    def play(self, name):
        self.sound[name].play()