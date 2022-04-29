import pygame
import sys
from enemy import Enemy
from enemy_horde import Horde
from gun import Gun

FPS = 60
PLAYER_SPEED = 5
MAX_BULLETS = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode( (800,600) )
    pygame.display.set_caption("Защитник космоса")
    fps_clock = pygame.time.Clock()
    bg_color = (0, 33, 33)
    
    player = Gun(screen, 10)
    horde = Horde( screen, (60,10), 10, 3 )
    
    pygame.font.init()
    font = pygame.font.SysFont('New Times Roman', 36)
    
    is_win = False
    is_paused = True
    
    pause_text = font.render('Пауза / Pause\nPress Space to Continue', False, (206, 0, 0))
    
    win_text = font.render('ТЫ ПОБЕДИЛ ИНОПЛАНЕТНЫХ ЗАХВАТЧИКОВ!', False, (194, 98, 0))
    win_icon = pygame.image.load('sprites/sprite_like.png')
    
    lose_text = font.render('ДЕЛА ХРЕНОВЫЕ, МЫ ПРОИГРАЛИ :(', False, (206, 0, 0))
    lose_icon = pygame.image.load('sprites/sprite_dislike.png')
    
    deadline = ( (0, player.rect.y - 40), (screen.get_rect().right, player.rect.y - 40) )
    
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE:
                    if is_paused:
                        is_paused = False
                        break
                    else:
                        if player.get_bullet_count() < MAX_BULLETS:
                            player.fire()
                
                if not is_paused:
                    if event.key == pygame.K_LEFT:
                        player.set_acceleration_x(-PLAYER_SPEED)
                    elif event.key == pygame.K_RIGHT:
                        player.set_acceleration_x(PLAYER_SPEED)
                        
                
                    
            elif event.type == pygame.KEYUP and not is_paused:
                if event.key == pygame.K_LEFT and player.get_acceleration_x() == -PLAYER_SPEED:
                    player.set_acceleration_x(0)
                elif event.key == pygame.K_RIGHT and player.get_acceleration_x() == PLAYER_SPEED:
                    player.set_acceleration_x(0)
            
                
        screen.fill(bg_color)
        
        enemies_list = horde.get_enemy_list()
        
        #Check bullet collision for enemies
        for bullet in player.get_bullet_list():
            flag = False
            
    
            for row in range(horde.get_shape()[1]):
                for col in range(horde.get_shape()[0]):
                    if flag:
                        break
                    elif enemies_list[col][row] != None:
                        if bullet != None:
                            if enemies_list[col][row].is_in_collision( bullet.get_position() ):
                                horde.kill(col, row)
                                player.remove_bullet(bullet)
                                flag = True
                                
                                
        #Check bullet collision for player
        for enemy_bullet in horde.get_bullets_list():
            if player.is_in_collision(enemy_bullet.get_position()):
                player.is_active = False
                is_win = False          
                
                
        #Check enemy deadline collision
        for col in horde.get_enemy_list():
            for enemy in col:
                if enemy != None:
                    if enemy.rect.bottomleft[1] >= deadline[1][1]:
                        player.is_active = False
                        is_win = False
                    
        
        if player.is_active and not is_paused:
            player.move()
            player.draw()
            
            if horde.get_enemies_count() > 0:
                horde.make_random_shot()
                Enemy.draw_bullets()
                horde.move_step()
                horde.draw()
            else:
                player.is_active = False
                is_win = True
        else:
            player.draw()
            horde.draw()
            
            if is_win:
                screen.blit(win_text, (110, 300) ) 
                screen.blit(win_icon, (375, 400))
            elif is_paused:
                screen.blit(pause_text, (110, 300))
            else:
                screen.blit(lose_text, (175, 300))
                screen.blit(lose_icon, (370, 400))
        
        
        #draw deadline
        pygame.draw.line( screen, (255, 0, 0), deadline[0], deadline[1] )
        
        pygame.display.flip()
        fps_clock.tick(FPS)
    
    
if __name__ == '__main__':
    main()