import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame

def run_test():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Tkinter/Turtle Fix")
    
    font = pygame.font.SysFont("arial", 20)
    text = font.render("Python configured with Pygame for UI", True, (0, 255, 0))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))
        screen.blit(text, (200 - text.get_width() // 2, 150 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        break
    pygame.quit()

if __name__ == "__main__":
    run_test()
