import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame

pygame.init()
w, h = 600, 400
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Geometry Dash")
clock = pygame.time.Clock()

player = pygame.Rect(100, h - 50, 30, 30)
player_vel = 0
gravity = 0.8
jump_strength = -12

obstacles = [pygame.Rect(600, h - 50, 30, 50), pygame.Rect(900, h - 50, 30, 50)]
speed = 5
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if player.bottom >= h:
                player_vel = jump_strength

    player_vel += gravity
    player.y += player_vel
    if player.bottom > h:
        player.bottom = h
        player_vel = 0

    for ob in obstacles:
        ob.x -= speed
        if ob.right < 0:
            ob.x = 800 + (score % 300)
            score += 1

    if any(player.colliderect(ob) for ob in obstacles):
        player.y = h - 50
        player_vel = 0
        score = 0
        for i, ob in enumerate(obstacles):
            ob.x = 600 + i * 300

    win.fill((30, 30, 30))
    pygame.draw.rect(win, (0, 255, 255), player)
    for ob in obstacles:
        pygame.draw.rect(win, (255, 100, 0), ob)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
