import pygame
import quadrado

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_vel_y = 0

gravity = 0.8
jump_force = -20
in_ground = True
fonte = pygame.font.SysFont("arial", 30)
obstaculo = pygame.Rect(pygame.draw.rect(screen, "blue", (800,400, 100, 200)))

player_pos = pygame.Vector2(screen.get_width() / 4, 400)
player_vel = pygame.Vector2(320, 470)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('green')
    pygame.draw.rect(screen, "gray", (0, 520, 1280, 200))
    pygame.draw.rect(screen, "gray", (0, 500, 1280, 200))
    pygame.draw.rect(screen, "black", (int(player_pos.x), int(player_pos.y),100, 100))
    pygame.draw.rect(screen, "blue", (800,400, 100, 200))
    hitbox_player = pygame.Rect(pygame.draw.rect(screen,"red",(int(player_pos.x),int(player_pos.y) , 100, 100), 5))
    quadrado.quadradocinza_criar(screen)


    texto_surface = fonte.render("Colisão Detectada", True, (255, 255, 255))

    Control = True


    if hitbox_player.colliderect(obstaculo):
        Control = False
        screen.blit(texto_surface, (200, 200))

    if Control == True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and in_ground:
            player_vel_y = jump_force
            in_ground = False
        if keys[pygame.K_a]:
            player_pos.x += -30
        if keys[pygame.K_d]:
            player_pos.x += 30
        if Control == False:
            None

    player_vel_y += gravity
    player_pos.y += player_vel_y

    if player_pos.y > 470:
        player_pos.y = 470
        player_vel_y = 0
        in_ground = True
    else:
        in_ground = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()