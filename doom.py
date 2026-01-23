import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame

pygame.init()
w, h = 900, 600
sc = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

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
pa = 0.0
ps = 0.05
rs = 0.05

health = 100
weapon = 0
ammo = [999, 20]
cooldown = 0
shooting = False
shoot_frame = 0

def gen(c):
    s = 64
    t = pygame.Surface((s, s))
    for y in range(s):
        for x in range(s):
            v = (x ^ y) % 40
            t.set_at((x, y), (max(0, c[0] - v), max(0, c[1] - v), max(0, c[2] - v)))
    return t

tex = [gen((200, 20, 20)), gen((20, 200, 20)), gen((20, 20, 200)), gen((200, 200, 50))]

gun1 = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.rect(gun1, (100, 100, 100), (80, 120, 40, 80))
gun2 = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.rect(gun2, (100, 100, 100), (80, 100, 40, 100))

enemy_tex = pygame.Surface((64, 64), pygame.SRCALPHA)
pygame.draw.circle(enemy_tex, (255, 50, 50), (32, 32), 22)

enemies = []
boss = None
for y, row in enumerate(world):
    for x, ch in enumerate(row):
        if ch == "E": enemies.append([x + 0.5, y + 0.5, True, 0])
        if ch == "B": boss = [x + 0.5, y + 0.5, 200, 0]

doors = []
for y, row in enumerate(world):
    for x, ch in enumerate(row):
        if ch == "D": doors.append([x, y, 0])

PI = 3.14159

def cast():
    z = [0.0] * w
    for i in range(w):
        ang = pa + (i - w/2) * 0.0015
        vec = pygame.Vector2(1, 0).rotate(ang * 180 / PI)
        vx, vy = vec.x, vec.y
        
        d = 0.0
        hit = 0
        txid = 0
        wx = 0
        while hit == 0 and d < 15:
            d += 0.1
            xx, yy = px + d * vx, py + d * vy
            if not (0 <= int(yy) < len(world) and 0 <= int(xx) < len(world[0])):
                hit = 1
                break
            c = world[int(yy)][int(xx)]
            if c == "#":
                hit = 1
                txid = (int(xx) + int(yy)) % 4
                wx = (xx + yy) * 32 % 64
            elif c == "D":
                for dr in doors:
                    if dr[0] == int(xx) and dr[1] == int(yy) and dr[2] == 0:
                        hit = 1; txid = 3; wx = (xx + yy) * 32 % 64
        z[i] = d
        h2 = int(300 / d) if d > 0.1 else h
        if h2 > h: h2 = h
        col_img = pygame.transform.scale(tex[txid].subsurface(int(wx)%64, 0, 1, 64), (1, h2))
        sc.blit(col_img, (i, (h - h2) // 2))
    return z

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: running = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_q: weapon = (weapon + 1) % 2
            if ev.key == pygame.K_SPACE:
                if cooldown <= 0:
                    shooting, shoot_frame = True, 0
                    cooldown = 15
                    for e in enemies:
                        if e[2]:
                            vec = pygame.Vector2(e[0]-px, e[1]-py)
                            if vec.length() < 5: e[2] = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: pa -= rs
    if keys[pygame.K_RIGHT]: pa += rs
    
    move = pygame.Vector2(0, 0)
    if keys[pygame.K_w]: move += pygame.Vector2(1, 0).rotate(pa * 180 / PI)
    if keys[pygame.K_s]: move -= pygame.Vector2(1, 0).rotate(pa * 180 / PI)
    
    if move.length() > 0:
        move = move.normalize() * ps
        if world[int(py)][int(px + move.x)] != "#": px += move.x
        if world[int(py + move.y)][int(px)] != "#": py += move.y

    sc.fill((30, 30, 30))
    z_buf = cast()
    sc.blit(gun2 if shooting else gun1, (w//2 - 100, h - 200))
    if shooting:
        shoot_frame += 1
        if shoot_frame > 5: shooting = False
    
    if cooldown > 0: cooldown -= 1
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
