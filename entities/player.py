from pygame import sprite

class Player(sprite.Sprite):
    def __init__(self):
        self.health = 0
        self.damage = 0
        self.speed = 0
