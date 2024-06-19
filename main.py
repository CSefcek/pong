import pygame, sys

pygame.init()
WINDOW_SIZE = (960, 540)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
running = True
dt = 0

player_speed = 400
player_height = 100
player_width = 20
player1_x_pos = 10
player1_y_pos = WINDOW_SIZE[1] / 2 - (player_height / 2)
player1_rect = pygame.Rect(player1_x_pos,player1_y_pos,player_width,player_height)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    screen.fill((50,60,57))
    pygame.draw.rect(screen, (211,201,161), player1_rect)
#!!! sistemare input/movimento !!!
    if pygame.key.get_pressed()[pygame.K_s] and player1_rect.bottom < WINDOW_SIZE[1]:
        player1_rect.y += player_speed * dt
    if pygame.key.get_pressed()[pygame.K_w] and player1_rect.top > 0:
        player1_rect.y -= player_speed * dt
                                          
                                  


    #RENDER MY GAME BELOW THIS LINE
    
    #RENDER MY GAME ABOVE THIS LINE
    pygame.display.flip()

    dt = clock.tick(60) / 1000   