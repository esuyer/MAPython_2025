import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (100, 0, 0)
SOUND_FILE = "hohoho.wav"
jumpscare_sound = None

try:
    pygame.mixer.init()
    jumpscare_sound = pygame.mixer.Sound(SOUND_FILE)
except:
    pass

try:
    jumpscare_image = pygame.image.load("jumpscare.png")
    jumpscare_image = pygame.transform.scale(jumpscare_image, (WIDTH, HEIGHT))
except:
    jumpscare_image = pygame.Surface((WIDTH, HEIGHT))
    jumpscare_image.fill(DARK_RED)
    temp_font = pygame.font.Font(None, 120)
    text = temp_font.render("FREDDY", True, BLACK)
    jumpscare_image.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

clock = pygame.time.Clock()
timer = 0
duration = 120
shake_intensity = 35
flash_speed = 3

def play_jumpscare_sound():
    if jumpscare_sound:
        try:
            jumpscare_sound.play()
        except:
            pass

play_jumpscare_sound()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    timer += 1
    if timer >= duration:
        timer = 0
        play_jumpscare_sound()

    progress = timer / duration
    # Manual simple pseudo-random for shake using timer
    shake_x = (timer * 13) % (int(shake_intensity * 2) + 1) - int(shake_intensity)
    shake_y = (timer * 17) % (int(shake_intensity * 2) + 1) - int(shake_intensity)

    # Simple scaling without math.sin
    scale = 1.0 + (timer % 30) / 100.0

    screen.fill(BLACK)

    scaled_width = int(WIDTH * scale)
    scaled_height = int(HEIGHT * scale)
    scaled_image = pygame.transform.scale(jumpscare_image, (scaled_width, scaled_height))

    x = (WIDTH - scaled_width) // 2 + shake_x
    y = (HEIGHT - scaled_height) // 2 + shake_y

    screen.blit(scaled_image, (x, y))

    if (timer // flash_speed) % 2 == 0:
        flash_surface = pygame.Surface((WIDTH, HEIGHT))
        flash_surface.fill(RED)
        flash_surface.set_alpha(80)
        screen.blit(flash_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
