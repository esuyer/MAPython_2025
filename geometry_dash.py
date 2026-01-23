import pygame
import sys
import random
import math
import time

pygame.init()
pygame.mixer.init()

WIDTH = 960
HEIGHT = 540
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash Python")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (120,120,120)
RED = (255,60,60)
BLUE = (60,120,255)
GREEN = (60,255,120)
YELLOW = (255,255,120)

font_big = pygame.font.SysFont("arialblack", 48)
font_mid = pygame.font.SysFont("arial", 32)
font_small = pygame.font.SysFont("arial", 20)

GROUND_Y = HEIGHT - 90

class Camera:
    def __init__(self):
        self.x = 0
        self.shake = 0

    def update(self):
        if self.shake > 0:
            self.shake -= 1

    def offset(self):
        if self.shake > 0:
            return random.randint(-5,5)
        return 0

camera = Camera()

class Particle:
    def __init__(self, x, y, vx, vy, life, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = life
        self.color = color

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.3
        self.life -= 1

    def draw(self):
        if self.life > 0:
            pygame.draw.rect(screen, self.color, (self.x, self.y, 4, 4))

particles = []

class Player:
    def __init__(self):
        self.size = 40
        self.x = 200
        self.y = GROUND_Y - self.size
        self.vel_y = 0
        self.gravity = 1
        self.jump_power = -18
        self.on_ground = True
        self.alive = True
        self.rotation = 0

    def reset(self):
        self.y = GROUND_Y - self.size
        self.vel_y = 0
        self.on_ground = True
        self.alive = True
        self.rotation = 0

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def update(self):
        self.vel_y += self.gravity
        self.y += self.vel_y
        if not self.on_ground:
            self.rotation += 8
        if self.y >= GROUND_Y - self.size:
            self.y = GROUND_Y - self.size
            self.vel_y = 0
            self.on_ground = True
            self.rotation = 0

    def draw(self):
        surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.rect(surf, BLUE, (0,0,self.size,self.size))
        rot = pygame.transform.rotate(surf, self.rotation)
        r = rot.get_rect(center=(self.x + self.size//2, self.y + self.size//2))
        screen.blit(rot, (r.x + camera.offset(), r.y))

player = Player()

class Obstacle:
    def __init__(self, x, kind):
        self.x = x
        self.kind = kind
        self.width = 40
        self.height = 40
        self.passed = False

    def update(self, speed):
        self.x -= speed

    def rect(self):
        return pygame.Rect(self.x, GROUND_Y - self.height, self.width, self.height)

    def collide(self, p):
        return self.rect().colliderect(pygame.Rect(player.x, player.y, player.size, player.size))

    def draw(self):
        if self.kind == "spike":
            pts = [
                (self.x, GROUND_Y),
                (self.x + self.width//2, GROUND_Y - self.height),
                (self.x + self.width, GROUND_Y)
            ]
            pygame.draw.polygon(screen, RED, pts)
        elif self.kind == "block":
            pygame.draw.rect(screen, RED, self.rect())

class Level:
    def __init__(self):
        self.obstacles = []
        self.timer = 0
        self.speed = 6
        self.progress = 0

    def reset(self):
        self.obstacles.clear()
        self.timer = 0
        self.speed = 6
        self.progress = 0

    def spawn(self):
        kind = random.choice(["spike","block"])
        self.obstacles.append(Obstacle(WIDTH + random.randint(0,200), kind))

    def update(self):
        self.timer += 1
        if self.timer % 80 == 0:
            self.spawn()
        if self.timer % 600 == 0:
            self.speed += 1
        for o in self.obstacles:
            o.update(self.speed)
        self.obstacles = [o for o in self.obstacles if o.x > -100]
        self.progress += self.speed

    def draw(self):
        for o in self.obstacles:
            o.draw()

level = Level()

def spawn_death_particles():
    for i in range(40):
        particles.append(
            Particle(
                player.x + player.size//2,
                player.y + player.size//2,
                random.uniform(-6,6),
                random.uniform(-8,-2),
                random.randint(20,40),
                RED
            )
        )

def update_particles():
    for p in particles:
        p.update()
    particles[:] = [p for p in particles if p.life > 0]

def draw_particles():
    for p in particles:
        p.draw()

def draw_ground():
    pygame.draw.rect(screen, GRAY, (0, GROUND_Y, WIDTH, HEIGHT-GROUND_Y))

def draw_ui(score):
    txt = font_mid.render(f"Score: {score}", True, WHITE)
    screen.blit(txt, (20,20))
    prog = min(1, score / 5000)
    pygame.draw.rect(screen, WHITE, (20,60,300,10),2)
    pygame.draw.rect(screen, GREEN, (20,60,int(300*prog),10))

def main_menu():
    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        title = font_big.render("GEOMETRY DASH", True, WHITE)
        hint = font_mid.render("Press SPACE to start", True, GRAY)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 80))
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT//2))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    return

def game_over(score):
    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        over = font_big.render("GAME OVER", True, RED)
        sc = font_mid.render(f"Score: {score}", True, WHITE)
        hint = font_small.render("Press SPACE to retry", True, GRAY)
        screen.blit(over, (WIDTH//2 - over.get_width()//2, HEIGHT//2 - 100))
        screen.blit(sc, (WIDTH//2 - sc.get_width()//2, HEIGHT//2 - 30))
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT//2 + 30))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    return

def run_game():
    score = 0
    level.reset()
    player.reset()
    particles.clear()
    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    player.jump()
        player.update()
        level.update()
        camera.update()
        for o in level.obstacles:
            if o.collide(player):
                spawn_death_particles()
                camera.shake = 20
                return score
            if not o.passed and o.x + o.width < player.x:
                o.passed = True
                score += 10
        update_particles()
        draw_ground()
        level.draw()
        player.draw()
        draw_particles()
        draw_ui(score)
        pygame.display.flip()

main_menu()
while True:
    final_score = run_game()
    game_over(final_score)
