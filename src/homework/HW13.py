import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame

# Turtle replacement for HW13 using Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("HW13 Visualization")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    # Simple star shape using lines to mimic turtle
    center = (400, 300)
    for i in range(5):
        # Placeholder for turtle logic
        pass
        
    font = pygame.font.SysFont("arial", 24)
    text = font.render("HW13: Pygame Visualization (Turtle Replacement)", True, (255, 255, 255))
    screen.blit(text, (20, 20))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
