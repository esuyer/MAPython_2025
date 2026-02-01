import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game Collection")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 32)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((30, 30, 30))
    text = font.render("Welcome to the Game Collection!", True, (255, 255, 255))
    screen.blit(text, (400 - text.get_width()//2, 300 - text.get_height()//2))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
