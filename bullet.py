from typing import Tuple
import pygame


class Bullet:
    
    def __init__(self, screen, position: tuple, sprite, bullet_speed):
        self.screen = screen
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.bullet_speed = bullet_speed
        
        self.rect.x = position[0] - self.rect.centerx
        self.rect.y = position[1]
        
        
    def move(self):
        self.rect.y -= self.bullet_speed
        
    
    def draw(self):
        self.screen.blit( self.sprite, self.rect )
        
        
    def get_position(self) -> Tuple:
        return (self.rect.x, self.rect.y)
    