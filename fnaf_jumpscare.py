import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'

import pygame
import random
import sys
import math

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Five Nights at Freddy's - Jumpscare!")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_RED = (100, 0, 0)

try:
    jumpscare_image = pygame.image.load("jumpscare.png")
    jumpscare_image = pygame.transform.scale(jumpscare_image, (WIDTH, HEIGHT))
except:
    jumpscare_image = pygame.Surface((WIDTH, HEIGHT))
    jumpscare_image.fill(DARK_RED)
    font = pygame.font.Font(None, 120)
    text = font.render("FREDDY", True, BLACK)
    jumpscare_image.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 72)

class JumpscareEffect:
    def __init__(self):
        self.active = False
        self.timer = 0
        self.duration = 90
        self.shake_intensity = 30
        self.flash_speed = 4
        
    def start(self):
        self.active = True
        self.timer = 0
    
    def update(self):
        if self.active:
            self.timer += 1
            if self.timer >= self.duration:
                self.active = False
                return True
        return False
    
    def get_shake_offset(self):
        if not self.active:
            return (0, 0)
        intensity = self.shake_intensity * (1 - self.timer / self.duration)
        return (
            random.randint(-int(intensity), int(intensity)),
            random.randint(-int(intensity), int(intensity))
        )
    
    def get_zoom_scale(self):
        if not self.active:
            return 1.0
        progress = self.timer / self.duration
        zoom = 1.0 + math.sin(progress * math.pi) * 0.3
        rapid_zoom = 1.0 + math.sin(self.timer * 0.5) * 0.05
        return zoom * rapid_zoom
    
    def should_flash_red(self):
        if not self.active:
            return False
        return (self.timer // self.flash_speed) % 2 == 0

jumpscare = JumpscareEffect()

waiting_for_scare = True
countdown = 0
countdown_active = False
show_aftermath = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE and waiting_for_scare and not countdown_active:
                countdown_active = True
                countdown = 180
            if event.key == pygame.K_r and show_aftermath:
                waiting_for_scare = True
                show_aftermath = False
                countdown_active = False

    if countdown_active:
        countdown -= 1
        if countdown <= 0:
            jumpscare.start()
            countdown_active = False
            waiting_for_scare = False

    if jumpscare.active:
        finished = jumpscare.update()
        if finished:
            show_aftermath = True

    screen.fill(BLACK)

    if jumpscare.active:
        shake_x, shake_y = jumpscare.get_shake_offset()
        scale = jumpscare.get_zoom_scale()
        
        scaled_width = int(WIDTH * scale)
        scaled_height = int(HEIGHT * scale)
        scaled_image = pygame.transform.scale(jumpscare_image, (scaled_width, scaled_height))
        
        x = (WIDTH - scaled_width) // 2 + shake_x
        y = (HEIGHT - scaled_height) // 2 + shake_y
        
        screen.blit(scaled_image, (x, y))
        
        if jumpscare.should_flash_red():
            flash_surface = pygame.Surface((WIDTH, HEIGHT))
            flash_surface.fill(RED)
            flash_surface.set_alpha(100)
            screen.blit(flash_surface, (0, 0))
    
    elif waiting_for_scare:
        if countdown_active:
            seconds_left = countdown // 60 + 1
            
            for i in range(3):
                flicker = random.randint(200, 255)
                
            countdown_text = big_font.render(str(seconds_left), True, (flicker, 0, 0))
            screen.blit(countdown_text, (WIDTH//2 - countdown_text.get_width()//2, HEIGHT//2 - 50))
            
            warning_text = small_font.render("GET READY...", True, (flicker, flicker, flicker))
            screen.blit(warning_text, (WIDTH//2 - warning_text.get_width()//2, HEIGHT//2 + 50))
        else:
            title = big_font.render("FIVE NIGHTS AT FREDDY'S", True, RED)
            screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
            
            subtitle = font.render("JUMPSCARE SIMULATOR", True, WHITE)
            screen.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 230))
            
            if (pygame.time.get_ticks() // 500) % 2 == 0:
                prompt = small_font.render("Press SPACE to trigger jumpscare...", True, WHITE)
                screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, HEIGHT//2 + 50))
            
            warning = small_font.render("(Warning: Flashing lights and scary image!)", True, DARK_RED)
            screen.blit(warning, (WIDTH//2 - warning.get_width()//2, HEIGHT - 100))
    
    elif show_aftermath:
        game_over = big_font.render("YOU DIED", True, RED)
        screen.blit(game_over, (WIDTH//2 - game_over.get_width()//2, HEIGHT//2 - 50))
        
        restart = small_font.render("Press R to experience again or ESC to quit", True, WHITE)
        screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2 + 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
