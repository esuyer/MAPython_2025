import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'

import pygame
import sys
import random
pygame.init()

w, h = 600, 400
win = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
player = pygame.Rect(50, h - 50, 30, 30)
player_vel = 0
gravity = 0.8
jump_strength = -12
obstacles = []
speed = 5
score = 0
level = 1
levels = [
    [[200, 350, 50, 50], [400, 300, 50, 50], [600, 350, 50, 50]],
    [[150, 300, 50, 50], [350, 350, 50, 50], [550, 300, 50, 50], [750, 350, 50, 50]]
]
font = pygame.font.SysFont(None, 30)

def reset():
    global player, player_vel, obstacles, score
    player.y = h - 50
    player_vel = 0
    obstacles = [pygame.Rect(x, y, w_, h_) for x, y, w_, h_ in levels[level - 1]]
    score = 0

reset()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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

    if obstacles and obstacles[0].right < 0:
        obstacles.pop(0)

    if len(obstacles) < len(levels[level - 1]):
        last_x = obstacles[-1].x if obstacles else w
        lvl_data = levels[level - 1]
        for x, y, w_, h_ in lvl_data:
            if x > last_x:
                obstacles.append(pygame.Rect(x, y, w_, h_))

    win.fill((135, 206, 235))
    pygame.draw.rect(win, (255, 0, 0), player)
    
    for ob in obstacles:
        pygame.draw.rect(win, (0, 0, 0), ob)

    if any(player.colliderect(ob) for ob in obstacles):
        reset()

    score += 1
    win.blit(font.render(f'Score: {score}', True, (0, 0, 0)), (10, 10))
    win.blit(font.render(f'Level: {level}', True, (0, 0, 0)), (10, 40))

    pygame.display.flip()
    clock.tick(60)

    if score > 2000 and level < 2:
        level += 1
        reset()
