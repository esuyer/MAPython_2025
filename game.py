import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'

import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Squares!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
GREEN = (50, 255, 50)
YELLOW = (255, 255, 50)

COLORS = [RED, BLUE, GREEN, YELLOW]

player_width = 100
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 8

class FallingSquare:
    def __init__(self):
        self.size = random.randint(20, 40)
        self.x = random.randint(0, WIDTH - self.size)
        self.y = -self.size
        self.speed = random.randint(3, 7)
        self.color = random.choice(COLORS)
    
    def move(self):
        self.y += self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 32)

squares = []
score = 0
spawn_timer = 0
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_r and game_over:
                squares = []
                score = 0
                spawn_timer = 0
                game_over = False
                player_x = WIDTH // 2 - player_width // 2

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed
        
        player_x = max(0, min(WIDTH - player_width, player_x))
        
        spawn_timer += 1
        if spawn_timer > 30:
            squares.append(FallingSquare())
            spawn_timer = 0
        
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        
        for square in squares[:]:
            square.move()
            
            square_rect = pygame.Rect(square.x, square.y, square.size, square.size)
            if player_rect.colliderect(square_rect):
                squares.remove(square)
                score += 10
            
            elif square.y > HEIGHT:
                game_over = True

    screen.fill(BLACK)
    
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    
    for square in squares:
        square.draw(screen)
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render("GAME OVER!", True, RED)
        restart_text = small_font.render("Press R to restart or ESC to quit", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 30))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20))
    else:
        instructions = small_font.render("Use Arrow Keys or A/D to move - Catch all squares!", True, WHITE)
        screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT - 25))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
