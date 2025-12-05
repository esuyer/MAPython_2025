import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'

import pygame
import random
import sys
import math
import time
import turtle
print("Question 1 \n")
x = int(input("Enter an odd number: "))
for x in range(1, x+2):
 if x % 2 != 0:
    print(x, end=" ""\n")
print("-"*10)
for x in range(0, x+0):
  print(x**2)
print("\nQuestion 2 \n")
y = random. randint(3, 10)
print("You will get scared in ", y," seconds")
for y in range(y, 1, -1):
   time. sleep(1)
   print(y)
time. sleep(1)
print("1")
time. sleep(1)
print("BOO!")
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (100, 0, 0)
SOUND_FILE = "hohoho.wav"
jumpscare_sound = SOUND_FILE
try:
    pygame.mixer.init()
    jumpscare_sound = pygame.mixer.Sound(SOUND_FILE)
    print(f"Sound loaded successfully: {SOUND_FILE}")
except Exception as e:
    print(f"Sound not loaded: {SOUND_FILE}")
    print("(This is normal in Replit - sound will work when run locally)")

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
    intensity = shake_intensity * (1 - progress * 0.5)
    shake_x = random.randint(-int(intensity), int(intensity))
    shake_y = random.randint(-int(intensity), int(intensity))

    zoom = 1.0 + math.sin(progress * math.pi) * 0.2
    rapid_zoom = 1.0 + math.sin(timer * 0.5) * 0.08
    scale = zoom * rapid_zoom

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
    clock.tick(10)

print("\nQuestion 3 \n")
z = int(input("Enter a number: "))
z = (z // 10) * 10
print(z)
print("\nQuestion 4 \n")
pen = turtle.Pen()
pen.shape("turtle")
pen.hideturtle()
pen.up()
N = random.randint(5,10)
print(N)
for i in range(N):
    if i % 2 == 0:
        pen.color("red")
    else:
        pen.color("green")
    pen.stamp()
    pen.forward(50)
time.sleep(5)
turtle.clear()
colors = ["purple", "yellow", "blue"]
for i in range(N):
        pen.color(colors[i % 3])
        pen.stamp()
        pen.forward(50)
turtle.done()
print("\nQuestion 5 \n")
S = int(input())
hours = S // 3600
minutes = (S % 3600) // 60
seconds = S % 60
print("hours:", hours, "minutes:", minutes, "seconds:", seconds)
pygame.quit()
sys.exit()
