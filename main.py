import pygame, sys

pygame.init()
WINDOW_SIZE = (960, 540)
screen = pygame.display.set_mode(WINDOW_SIZE)

clock = pygame.time.Clock()
running = True
dt = 0

player_speed = 400
player_width = 20
player_height = 100

ball_speed = 400
ball_width = 10
ball_height = 10

player1_x_pos = 10
player1_y_pos = WINDOW_SIZE[1] / 2 - (player_height / 2)
player1_rect = pygame.Rect(player1_x_pos,player1_y_pos,player_width,player_height)

player2_x_pos = WINDOW_SIZE[0] - 30
player2_y_pos = WINDOW_SIZE[1] / 2 - (player_height / 2)
player2_rect = pygame.Rect(player2_x_pos, player2_y_pos, player_width, player_height)

ball_x_pos = WINDOW_SIZE[0] / 2 - (ball_width / 2)
ball_y_pos = 0 #WINDOW_SIZE[1] / 2 
ball_rect = pygame.Rect(ball_x_pos, ball_y_pos, ball_width, ball_height)
ball_angle = 0.5



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    screen.fill((50,60,57))
    pygame.draw.line(screen, (211,201,161), (WINDOW_SIZE[0]/2,0),(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]), 3)
    pygame.draw.rect(screen, (211,201,161), player1_rect)
    pygame.draw.rect(screen, (211,201,161), player2_rect)
    pygame.draw.rect(screen, (211,201,161), ball_rect)
    

    # Input and movement
    if pygame.key.get_pressed()[pygame.K_s] and player1_rect.bottom < WINDOW_SIZE[1]:
        player1_rect.y += player_speed * dt
    if pygame.key.get_pressed()[pygame.K_w] and player1_rect.top > 0:
        player1_rect.y -= player_speed * dt

    if pygame.key.get_pressed()[pygame.K_DOWN] and player2_rect.bottom < WINDOW_SIZE[1]:
        player2_rect.y += player_speed * dt
    if pygame.key.get_pressed()[pygame.K_UP] and player2_rect.top > 0:
        player2_rect.y -= player_speed * dt

    ball_rect.x += ball_speed * dt
    ball_rect.y += ball_speed * ball_angle * dt

    if ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect):
        ball_speed = -ball_speed
        ball_angle = -ball_angle

    # NEXT STEP: program bouncing on the upper and lower border of the screen

    if ball_rect.y > WINDOW_SIZE[1] - ball_height:
        ball_angle = -ball_angle
    elif ball_rect.y < 0:
        ball_angle = -ball_angle
                                          
                                  


    #RENDER MY GAME BELOW THIS LINE
    
    #RENDER MY GAME ABOVE THIS LINE
    pygame.display.flip()

    dt = clock.tick(60) / 1000   