import pygame
from bullet import Bullet


class Gun:
    
    def __init__(self, screen, bullet_speed):
        self.screen = screen
        self.sprite = pygame.image.load('sprites/sprite_canon.png')
        self.rect = self.sprite.get_rect()
        self.screen_rect = screen.get_rect()
        self.bullet_sprite = pygame.image.load('sprites/sprite_bullet_player.png')
        self.bullet_speed = bullet_speed
        self.is_active = True
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.acceleration_x = 0
        
        self.bullet_list = []
        
    
    def draw(self):
        self.screen.blit(self.sprite, self.rect)
        
        self.remove_bullets()
        for bullet in self.bullet_list:
            bullet.move()
            bullet.draw()
        
    
    def move(self):
        if self.is_active:
            if self.rect.x + self.acceleration_x < self.screen_rect.left:
                self.rect.x = self.screen_rect.left
            elif self.rect.x + self.acceleration_x > self.screen_rect.right - self.rect.size[0]:
                self.rect.x = self.screen_rect.right - self.rect.size[0]
            else:        
                self.rect.x += self.acceleration_x
        
        
    def set_acceleration_x(self, dx):
        self.acceleration_x = dx
        
    
    def get_acceleration_x(self):
        return self.acceleration_x
    

    def fire(self):
        if self.is_active:
            self.bullet_list.append( Bullet(self.screen, (self.rect.centerx, self.rect.y), self.bullet_sprite, self.bullet_speed) )
        
        
    def get_bullet_count(self):
        return len(self.bullet_list) - self.bullet_list.count(None)
    
    
    def remove_bullets(self):
        for bullet in self.bullet_list:
            if bullet.get_position()[1] < 0:
                self.bullet_list.remove(bullet)
                
                
    def get_bullet_list(self):
        return self.bullet_list
    
    
    def remove_bullet(self, bullet):
        self.bullet_list.remove(bullet)
        
    
    def is_in_collision(self, object_position: tuple):
        if object_position[0] >= self.rect.x and\
            object_position[0] <= self.rect.bottomright[0] and\
            object_position[1] >= self.rect.y and\
            object_position[1] <= self.rect.bottomright[1]:
                return True
        else:
            return False