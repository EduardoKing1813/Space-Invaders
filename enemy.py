import pygame
from bullet import Bullet

class Enemy:
    
    bullets_list = []
    bullet_speed = 10
    sprite_bullet_enemy = pygame.image.load('sprites/sprite_bullet_enemy.png')
    sprite = pygame.image.load('sprites/sprite_enemy1.png')
    
    def __init__(self, screen, position: tuple):
        self.screen = screen
        self.sprite = Enemy.sprite
        self.rect = self.sprite.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.x = position[0] - self.rect.centerx
        self.rect.y = position[1]
        
        
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    
    def shoot_down(self):
        Enemy.bullets_list.append( Bullet(self.screen, (self.rect.centerx, self.rect.bottomleft[1]), Enemy.sprite_bullet_enemy, -5) )
        
        
    def draw(self):
        self.screen.blit(self.sprite, self.rect)
        
        
    @classmethod
    def draw_bullets(cls):
        for bullet in cls.bullets_list:
            bullet.move()
            bullet.draw()
            
            
    def is_in_collision(self, object_position: tuple):
        if object_position[0] >= self.rect.x and\
            object_position[0] <= self.rect.bottomright[0] and\
            object_position[1] >= self.rect.y and\
            object_position[1] <= self.rect.bottomright[1]:
                return True
        else:
            return False
        