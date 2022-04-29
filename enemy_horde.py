from enum import EnumMeta
import pygame
import random
from enemy import Enemy
import time
import random

class Horde:
    
    def __init__(self, screen, position: tuple, width, height):
        
        self.screen = screen
        self.width = width
        self.height = height
        self.last_moved = time.time()
        self.last_shot = time.time()
        self.is_moving_right = True
        
        self.enemy_sample_rect = Enemy.sprite.get_rect()
        self.enemy_width = self.enemy_sample_rect.bottomright[0] - self.enemy_sample_rect.bottomleft[0]
        self.enemy_height = self.enemy_sample_rect.y + self.enemy_sample_rect.bottom
        
        self.enemies = []
        for w in range(width):
            enemy_row = []
            for h in range(height):
                enemy_row.append(Enemy(screen, (position[0] + self.enemy_width * w, position[1] + self.enemy_height * h)  ))
            self.enemies.append(enemy_row)
            
                
    def draw(self):
        
        
        for row in self.enemies:
            for enemy in row:
                if enemy != None:
                    enemy.draw()
            
    
    def get_enemy_list(self):
        return self.enemies
    
    
    def get_shape(self):
        return (self.width, self.height)
    
    
    def kill(self, row, col):
        self.enemies[row][col] = None
        

    def move_step(self):
        if time.time() - self.last_moved >= 0.1 + 1 * ( self.get_enemies_count() / (self.width * self.height)) and self.get_enemies_count() > 0:
            
            first_pos, last_pos = (0,0), (0,0)
            
            #Determine position of most-right alive enemy
            for row in range(self.width - 1, 0, -1):
                col = [ self.enemies[row][i] for i in range(self.height) if self.enemies[row][i] != None]
                if len(col) > 0:
                    #if in some column there are at least 1 alive enemy
                    last_pos = (col[0].rect.x, col[0].rect.y)
                    break
                
            #Determine position of most-left alive enemy
            for row in range(self.width):
                col = [ self.enemies[row][i] for i in range(self.height) if self.enemies[row][i] != None]
                if len(col) > 0:
                    #if in some column there are at least 1 alive enemy
                    first_pos = (col[0].rect.x, col[0].rect.y)
                    break
                    
            if self.is_moving_right and last_pos[0] + self.enemy_width < self.screen.get_rect().right or\
            not self.is_moving_right and first_pos[0] - self.enemy_width > 0:
                dx, dy = self.enemy_width if self.is_moving_right else -self.enemy_width, 0
            else:
                dx, dy = 0, self.enemy_height
                self.is_moving_right = not self.is_moving_right
            
            
            for row in self.enemies:
                for enemy in row:
                    if enemy != None:
                        enemy.move(dx, dy)
            
            self.last_moved = time.time()
        
        
        
    def get_enemies_count(self):
        c = 0
        
        for row in range(self.width):
            for col in range(self.height):
                if self.enemies[row][col] != None:
                    c += 1
                    
        return c
    
    
    def make_random_shot(self):
        
        if time.time() - self.last_shot > 1.5 - 1 * ( self.get_enemies_count() / (self.width * self.height)):
            if random.choice([True, False]):
                #If shot happens
                
                possible_shooters = []
                for col in range(self.width):
                    for enemy in self.enemies[col][::-1]:
                        if enemy != None:
                            possible_shooters.append(enemy)
                            break
                
                #choose random enemy to shot
                shooter = random.choice(possible_shooters)
                shooter.shoot_down()
                self.last_shot = time.time()
                
                
                
                
    def get_bullets_list(self):
        return Enemy.bullets_list