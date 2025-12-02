import pygame
import sys
import time
import random
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800,600))
img = pygame.image.load("jumpscare.png")
scream = pygame.mixer.Sound("hohoho.mp3")

running = True
triggered = False

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and not triggered:
            triggered = True
            scream.play()

    if not triggered:
        screen.fill((0,0,0))
    else:
        ox = random.randint(-15,15)
        oy = random.randint(-15,15)
        big = pygame.transform.scale(img, (900,700))
        screen.fill((0,0,0))
        screen.blit(big, (ox, oy))

    pygame.display.update()
    time.sleep(0.01)

pygame.quit()
sys.exit()
