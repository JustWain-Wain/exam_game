import pygame

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Платформер")

background_color = (255, 255, 255) # white
screen.fill(background_color)
pygame.display.flip()

player_image = pygame.image.load("assets/sprites/Player.png")
player_image = pygame.transform.scale(player_image, (32, 32))
player_x, player_y = 320, 240
screen.blit(player_image, (player_x, player_y))
pygame.display.flip()
move_ticker = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if move_ticker == 0:
            move_ticker = 10
            player_x -= 1
    if keys[pygame.K_d]:
        if move_ticker == 0:   
            move_ticker = 10     
            player_x += 1
    if keys[pygame.K_w]:
        if move_ticker == 0:
            move_ticker = 10
            player_y -= 1
    if keys[pygame.K_s]:
        if move_ticker == 0:
            move_ticker = 10
            player_y += 1

    if move_ticker > 0:
        move_ticker -= 1
        
    screen.fill(background_color)
    screen.blit(player_image, (player_x, player_y))
    pygame.display.update()