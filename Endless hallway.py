import pygame
import random
from floor import *

pygame.init()

pygame.display.set_caption("hello")
screen_size = (1700, 750)

display = pygame.display.set_mode(screen_size)

player_image = pygame.image.load("Guy.png")
player_image = pygame.transform.scale(player_image, (50,105))

floor_pos = [0, 1700]
floor_spawn_pos = 850
floor_color = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]

score = 0

x_pos = 0
y_pos = 250

x_vel = 0
y_vel = 0

speed = 1

stamina = 75
stamina_cooldown = 0
sprint_last_frame = False
short_stamina_cooldown = 0
stamina_color = (0, 0, 0)

entities = []

ent_1_attck_delay = -1
ent_1_delay = 3600
ent_2_delay = -1
ent_2_attck_delay = -1
ent_2_pos = 0

health = 100

hitbox = pygame.Rect((1700/2 , y_pos, 50, 100))
feet_hitbox = pygame.Rect((1700/2, y_pos + 80, 50, 20))







clock = pygame.time.Clock()
running = True
while running:
    display.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #floor --> INCLUDES DRAWING THE FLOOR
    times_repeated = 0
    for pos in floor_pos:
        pygame.draw.rect(display, floor_color[times_repeated], (-x_pos + pos, 0, 1690, 750))
        times_repeated += 1


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y_vel -= speed
    if keys[pygame.K_s]:
        y_vel += speed
    if keys[pygame.K_a]:
        x_vel -= speed
    if keys[pygame.K_d]:
        x_vel += speed
    
    if sprint_last_frame and not keys [pygame.K_LSHIFT]:
        short_stamina_cooldown = 120
        sprint_last_frame = False

    if short_stamina_cooldown > 0:
        short_stamina_cooldown -= 1
        
    
    speed = 0.75
    if keys[pygame.K_LSHIFT] and stamina_cooldown <= 0:
        stamina -= 0.5
        speed = 1.5
        sprint_last_frame = True
    elif stamina < 75:
        if not short_stamina_cooldown > 0:
            stamina += 0.75

    if stamina_cooldown > 0:
        stamina_cooldown -= 1
    
    if stamina <= 0:
        stamina_cooldown = 300
        sprint_last_frame = False
        stamina = 1
        short_stamina_cooldown = 120
    
    y_pos += y_vel
    y_vel *= 0.8
    x_pos += x_vel
    x_vel *= 0.8

    
    

    if x_pos >= floor_spawn_pos:
        floor_spawn_pos += 1700
        floor_pos.append(floor_spawn_pos + 850)
        floor_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        score += 1

        if random.randint(1,5) == 1:
            ent_2_delay = 300
            ent_2_pos = x_pos - random.randint(7500, 10000)
            
    
    if len(floor_pos) > 100:
        floor_pos.pop(0)
        floor_color.pop(0)



    # Draw Player
    display.blit(player_image, hitbox)

    

    hitbox = pygame.Rect((1700/2 , y_pos, 50, 100))
    feet_hitbox = pygame.Rect((1700/2, y_pos + 80, 50, 20))
    #player
    if keys[pygame.K_p]:
        pygame.draw.rect(display, (232, 171, 30), hitbox, 5)
        pygame.draw.rect(display, (232, 56, 30),  feet_hitbox, 5)
    
    #entity 1
    ent_1_delay -= 1

    if ent_1_delay <= 0:
        ent_1_attck_delay = 60
        ent_1_delay = random.randint(0, 3600)
    
    
    if ent_1_attck_delay > 0:
        ent_1_attck_delay -= 1
    
    
        pygame.draw.rect(display, (random.randint(0, 255), 0, 0), (0, 0, 1700, 750))

        if ent_1_attck_delay == 0:
            ent_1_attck_delay = -1
            if abs(x_vel) > 1 or abs(y_vel) > 1:
                health -= 40

    #entity 2
    
    if ent_2_delay > 0:
        
        
        if ent_2_attck_delay > 0:
            ent_2_pos = x_pos - 3400
            

        else:
            pygame.draw.rect(display, (255, 150, 0), (ent_2_pos - x_pos, 375, 250, 200))
            ent_2_pos += 50
            


    
    
    #stamina bar
    if stamina_cooldown <= 0:
        stamina_color = (255, 255, 255)
    else:
        stamina_color = (240, 120, 0)
    pygame.draw.rect(display, stamina_color, (10, 715 , stamina * 2 + 5, 10), border_radius=5)
    pygame.draw.rect(display, (0, 0 ,0), (10, 715, 155, 10), 3, 5)

    #health bar
    
    pygame.draw.rect(display, (200, 10, 10), (10, 725 , health * 3, 20), border_radius=5)
    pygame.draw.rect(display, (0, 0 ,0), (10, 725, 300, 20), 3, 5)

    
    if health <= 0:
        running = False


    pygame.display.flip()
    clock.tick(60)


wait = 600
while wait > 0:
    color = random.randint(0, 25)
    display.fill((color, color, color))
    wait -= 1
    print(color)
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wait = 0
pygame.quit()
