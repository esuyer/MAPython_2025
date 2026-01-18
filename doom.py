import os
import sys

# Audio fix for headless environments
os.environ['SDL_AUDIODRIVER'] = 'dummy'

import pygame
import math
import random

pygame.init()
w, h = 900, 600
sc = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

world = [
    "##########",
    "#........#",
    "#..D..H..#",
    "#..##....#",
    "#........#",
    "#.....E..#",
    "#....A...#",
    "#........#",
    "#..B.....#",
    "##########"
]

px, py = 2.5, 2.5
pa = 0
ps = 0.05
rs = 0.002

health = 100
weapon = 0
weapons = ["pistol", "shotgun"]
ammo = [999, 20]
cooldown = 0
shooting = False
shoot_frame = 0

explosions = []
pickup_radius = 0.3

tex = []
def gen(c):
    s = 64
    t = pygame.Surface((s, s))
    for y in range(s):
        for x in range(s):
            v = (x ^ y) % 40
            t.set_at((x, y), (max(0, c[0] - v), max(0, c[1] - v), max(0, c[2] - v)))
    return t

tex.append(gen((200, 20, 20)))
tex.append(gen((20, 200, 20)))
tex.append(gen((20, 20, 200)))
tex.append(gen((200, 200, 50)))
floor_tex = gen((80, 80, 80))
ceil_tex = gen((50, 50, 70))

gun1 = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.rect(gun1, (100, 100, 100), (80, 120, 40, 80))
gun2 = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.rect(gun2, (100, 100, 100), (80, 100, 40, 100))
shot1 = pygame.Surface((220, 220), pygame.SRCALPHA)
pygame.draw.rect(shot1, (160, 140, 80), (70, 130, 80, 90))
shot2 = pygame.Surface((220, 220), pygame.SRCALPHA)
pygame.draw.rect(shot2, (160, 140, 80), (70, 90, 80, 130))

enemy_tex = pygame.Surface((64, 64), pygame.SRCALPHA)
pygame.draw.circle(enemy_tex, (255, 50, 50), (32, 32), 22)
pygame.draw.circle(enemy_tex, (0, 0, 0), (25, 28), 5)
pygame.draw.circle(enemy_tex, (0, 0, 0), (39, 28), 5)
pygame.draw.rect(enemy_tex, (0, 0, 0), (22, 40, 20, 8))

boss_tex = pygame.Surface((128, 128), pygame.SRCALPHA)
pygame.draw.circle(boss_tex, (255, 0, 255), (64, 64), 60)
pygame.draw.circle(boss_tex, (0, 0, 0), (50, 60), 10)
pygame.draw.circle(boss_tex, (0, 0, 0), (78, 60), 10)
pygame.draw.rect(boss_tex, (0, 0, 0), (40, 80, 48, 16))

enemies = []
boss = None
for y, row in enumerate(world):
    for x, ch in enumerate(row):
        if ch == "E":
            enemies.append([x + 0.5, y + 0.5, True, 0])
        if ch == "B":
            boss = [x + 0.5, y + 0.5, 200, 0]

doors = []
for y, row in enumerate(world):
    for x, ch in enumerate(row):
        if ch == "D":
            doors.append([x, y, 0])

pickups = []
for y, row in enumerate(world):
    for x, ch in enumerate(row):
        if ch == "H": pickups.append([x + 0.5, y + 0.5, "health"])
        if ch == "A": pickups.append([x + 0.5, y + 0.5, "ammo"])

def cast():
    z = [0] * w
    for i in range(w):
        ra = pa + math.atan((i - w / 2) / 350)
        sin = math.sin(ra)
        cos = math.cos(ra)
        d = 0
        hit = 0
        txid = 0
        wx = 0
        while hit == 0 and d < 20:
            d += 0.05
            xx = px + d * cos
            yy = py + d * sin
            if not (0 <= int(yy) < len(world) and 0 <= int(xx) < len(world[0])):
                hit = 1
                break
            c = world[int(yy)][int(xx)]
            if c == "#":
                hit = 1
                txid = (int(xx) + int(yy)) % 4
                wx = (xx + yy) * 32 % 64
            if c == "D":
                for dr in doors:
                    if dr[0] == int(xx) and dr[1] == int(yy):
                        if dr[2] == 0:
                            hit = 1
                            txid = 3
                            wx = (xx + yy) * 32 % 64
        z[i] = d
        h2 = min(int(350 / d), h) if d > 0 else h
        col_img = pygame.transform.scale(tex[txid].subsurface(int(wx), 0, 1, 64), (1, h2))
        sc.blit(col_img, (i, (h - h2) // 2))
    return z

def draw_enemies(z):
    lst = []
    for e in enemies:
        if e[2]:
            dx, dy = e[0] - px, e[1] - py
            dist = math.hypot(dx, dy)
            ang = math.atan2(dy, dx) - pa
            while ang <= -math.pi: ang += 2*math.pi
            while ang > math.pi: ang -= 2*math.pi
            if abs(ang) < 1:
                size = int(280 / dist) if dist > 0.1 else 280
                sx = int(w / 2 + math.tan(ang) * 350 - size / 2)
                sy = int(h / 2 - size / 2)
                lst.append((dist, sx, sy, size, e))
    if boss and boss[2] > 0:
        dx, dy = boss[0] - px, boss[1] - py
        dist = math.hypot(dx, dy)
        ang = math.atan2(dy, dx) - pa
        while ang <= -math.pi: ang += 2*math.pi
        while ang > math.pi: ang -= 2*math.pi
        if abs(ang) < 1:
            size = int(500 / dist) if dist > 0.1 else 500
            sx = int(w / 2 + math.tan(ang) * 350 - size / 2)
            sy = int(h / 2 - size / 2)
            lst.append((dist, sx, sy, size, boss))
    lst.sort(reverse=True)
    for dist, sx, sy, size, e in lst:
        idx = min(max(sx + size // 2, 0), w - 1)
        if dist < z[idx] * 1.2:
            img = boss_tex if len(e) == 4 else enemy_tex
            sc.blit(pygame.transform.scale(img, (size, size)), (sx, sy))

def update_enemies():
    global health
    for e in enemies:
        if e[2]:
            dx, dy = px - e[0], py - e[1]
            d = math.hypot(dx, dy)
            if d > 0.4:
                e[0] += (dx / d) * 0.02
                e[1] += (dy / d) * 0.02
            else:
                e[3] += 1
                if e[3] > 50: health -= 10; e[3] = 0
    if boss and boss[2] > 0:
        dx, dy = px - boss[0], py - boss[1]
        d = math.hypot(dx, dy)
        if d > 0.5:
            boss[0] += (dx / d) * 0.01
            boss[1] += (dy / d) * 0.01
        else:
            boss[3] += 1
            if boss[3] > 30: health -= 20; boss[3] = 0

def shoot():
    global enemies, boss, explosions
    rng, ang_limit = (5, 0.1) if weapon == 0 else (6, 0.3)
    for e in enemies:
        if e[2]:
            dx, dy = e[0] - px, e[1] - py
            a = math.atan2(dy, dx) - pa
            while a <= -math.pi: a += 2*math.pi
            while a > math.pi: a -= 2*math.pi
            if abs(a) < ang_limit and math.hypot(dx, dy) < rng:
                e[2] = False
                explosions.append([e[0], e[1], 20])
    if boss and boss[2] > 0:
        dx, dy = boss[0] - px, boss[1] - py
        a = math.atan2(dy, dx) - pa
        while a <= -math.pi: a += 2*math.pi
        while a > math.pi: a -= 2*math.pi
        if abs(a) < ang_limit and math.hypot(dx, dy) < rng:
            boss[2] -= 10
            explosions.append([boss[0], boss[1], 30])

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: sys.exit()
        if ev.type == pygame.MOUSEMOTION: pa += ev.rel[0] * rs
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if cooldown <= 0 and ammo[weapon] > 0:
                shooting, shoot_frame = True, 0
                cooldown = 10 if weapon == 0 else 20
                ammo[weapon] -= 1
                shoot()
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_q: weapon = (weapon + 1) % 2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        for d in doors:
            if math.hypot(px - d[0], py - d[1]) < 1.5: d[2] = 1
    
    move_x, move_y = 0, 0
    if keys[pygame.K_w]: move_x += math.cos(pa); move_y += math.sin(pa)
    if keys[pygame.K_s]: move_x -= math.cos(pa); move_y -= math.sin(pa)
    if keys[pygame.K_a]: move_x -= math.sin(pa); move_y += math.cos(pa)
    if keys[pygame.K_d]: move_x += math.sin(pa); move_y -= math.cos(pa)
    
    if move_x or move_y:
        mag = math.hypot(move_x, move_y)
        nx, ny = px + (move_x / mag) * ps, py + (move_y / mag) * ps
        if world[int(ny)][int(nx)] not in "#" :
            door_hit = False
            for d in doors:
                if int(nx) == d[0] and int(ny) == d[1] and d[2] == 0: door_hit = True
            if not door_hit: px, py = nx, ny

    sc.fill((20, 20, 20))
    z = cast()
    update_enemies()
    draw_enemies(z)
    
    # Simple gun draw
    gun_surf = [gun1, gun2] if weapon == 0 else [shot1, shot2]
    if shooting:
        sc.blit(gun_surf[1], (w//2-100, h-200))
        shoot_frame += 1
        if shoot_frame > 5: shooting = False
    else:
        sc.blit(gun_surf[0], (w//2-100, h-200))

    # HUD
    pygame.draw.rect(sc, (200, 0, 0), (20, 20, max(0, health * 2), 20))
    # Minimap
    for y, row in enumerate(world):
        for x, ch in enumerate(row):
            pygame.draw.rect(sc, (100, 100, 100) if ch == "#" else (50, 50, 50), (w - 110 + x * 10, 10 + y * 10, 10, 10))
    pygame.draw.circle(sc, (0, 255, 0), (w - 110 + int(px * 10), 10 + int(py * 10)), 3)

    if health <= 0: running = False
    if cooldown > 0: cooldown -= 1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
