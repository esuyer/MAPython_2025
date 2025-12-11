import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'

import pygame
import math
import random
import sys
pygame.init()
w,h=900,600
sc=pygame.display.set_mode((w,h))
clock=pygame.time.Clock()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

world=[
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

px,py=2.5,2.5
pa=0
ps=0.05
rs=0.002

health=100
weapon=0
weapons=["pistol","shotgun"]
ammo=[999,20]
cooldown=0
shooting=False
shoot_frame=0

explosions=[]
pickup_radius=0.3

tex=[]
def gen(c):
    s=64
    t=pygame.Surface((s,s))
    for y in range(s):
        for x in range(s):
            v=(x^y)%40
            t.set_at((x,y),(c[0]-v,c[1]-v,c[2]-v))
    return t
tex.append(gen((200,20,20)))
tex.append(gen((20,200,20)))
tex.append(gen((20,20,200)))
tex.append(gen((200,200,50)))
floor_tex=gen((80,80,80))
ceil_tex=gen((50,50,70))

gun1=pygame.Surface((200,200),pygame.SRCALPHA)
pygame.draw.rect(gun1,(100,100,100),(80,120,40,80))
gun2=pygame.Surface((200,200),pygame.SRCALPHA)
pygame.draw.rect(gun2,(100,100,100),(80,100,40,100))
shot1=pygame.Surface((220,220),pygame.SRCALPHA)
pygame.draw.rect(shot1,(160,140,80),(70,130,80,90))
shot2=pygame.Surface((220,220),pygame.SRCALPHA)
pygame.draw.rect(shot2,(160,140,80),(70,90,80,130))

enemy_tex=pygame.Surface((64,64),pygame.SRCALPHA)
pygame.draw.circle(enemy_tex,(255,50,50),(32,32),22)
pygame.draw.circle(enemy_tex,(0,0,0),(25,28),5)
pygame.draw.circle(enemy_tex,(0,0,0),(39,28),5)
pygame.draw.rect(enemy_tex,(0,0,0),(22,40,20,8))

boss_tex=pygame.Surface((128,128),pygame.SRCALPHA)
pygame.draw.circle(boss_tex,(255,0,255),(64,64),60)
pygame.draw.circle(boss_tex,(0,0,0),(50,60),10)
pygame.draw.circle(boss_tex,(0,0,0),(78,60),10)
pygame.draw.rect(boss_tex,(0,0,0),(40,80,48,16))

enemies=[]
boss=None
for y,row in enumerate(world):
    for x,ch in enumerate(row):
        if ch=="E":
            enemies.append([x+0.5,y+0.5,True,0])
        if ch=="B":
            boss=[x+0.5,y+0.5,200,0]

doors=[]
for y,row in enumerate(world):
    for x,ch in enumerate(row):
        if ch=="D":
            doors.append([x,y,0])

pickups=[]
for y,row in enumerate(world):
    for x,ch in enumerate(row):
        if ch=="H": pickups.append([x+0.5,y+0.5,"health"])
        if ch=="A": pickups.append([x+0.5,y+0.5,"ammo"])

def cast():
    z=[0]*w
    for i in range(w):
        ra=pa+math.atan((i-w/2)/350)
        sin=math.sin(ra)
        cos=math.cos(ra)
        d=0
        hit=0
        txid=0
        wx=0
        while hit==0:
            d+=0.01
            xx=px+d*cos
            yy=py+d*sin
            c=world[int(yy)][int(xx)]
            if c=="#":
                hit=1
                txid=(int(xx)+int(yy))%4
                wx=(xx+yy)*32%64
            if c=="D":
                for dr in doors:
                    if dr[0]==int(xx) and dr[1]==int(yy):
                        if d>dr[2]:
                            hit=1
                            txid=3
                            wx=(xx+yy)*32%64
        z[i]=d
        col=tex[txid].subsurface(int(wx),0,1,64)
        h2=min(int(350/d),h)
        col=pygame.transform.scale(col,(1,h2))
        sc.blit(col,(i,(h-h2)//2))

        for ypix in range((h-h2)//2,h):
            dy=ypix-h/2
            dfd=(32/dy) if dy!=0 else 0
            fx=px+math.cos(pa)*dfd*math.cos(ra-pa)
            fy=py+math.sin(pa)*dfd*math.cos(ra-pa)
            fx%=1
            fy%=1
            if fy>0:
                sc.set_at((i,ypix),floor_tex.get_at((int(fx*63),int(fy*63))))
                sc.set_at((i,h-ypix-1),ceil_tex.get_at((int(fx*63),int(fy*63))))
    return z

def draw_enemies(z):
    lst=[]
    for e in enemies:
        if e[2]:
            dx=e[0]-px
            dy=e[1]-py
            dist=math.hypot(dx,dy)
            ang=math.atan2(dy,dx)-pa
            if -math.pi<ang<math.pi:
                size=int(280/dist)
                sx=int(w/2+math.tan(ang)*350-size/2)
                sy=int(h/2-size/2)
                lst.append((dist,sx,sy,size,e))
    if boss and boss[2]>0:
        dx=boss[0]-px
        dy=boss[1]-py
        dist=math.hypot(dx,dy)
        ang=math.atan2(dy,dx)-pa
        if -math.pi<ang<math.pi:
            size=int(500/dist)
            sx=int(w/2+math.tan(ang)*350-size/2)
            sy=int(h/2-size/2)
            lst.append((dist,sx,sy,size,boss))
    lst.sort(reverse=True)
    for dist,sx,sy,size,e in lst:
        if 0<sx<w and dist<z[int(min(max(sx,0),w-1))]*1.2:
            img=boss_tex if len(e)==4 else enemy_tex
            img2=pygame.transform.scale(img,(size,size))
            sc.blit(img2,(sx,sy))

def update_enemies():
    global health
    for e in enemies:
        if e[2]:
            dx=px-e[0]
            dy=py-e[1]
            d=math.hypot(dx,dy)
            if d>0.4:
                e[0]+=dx*0.008
                e[1]+=dy*0.008
            else:
                e[3]+=1
                if e[3]>50:
                    health-=10
                    e[3]=0
    if boss and boss[2]>0:
        dx=px-boss[0]
        dy=py-boss[1]
        d=math.hypot(dx,dy)
        if d>0.5:
            boss[0]+=dx*0.004
            boss[1]+=dy*0.004
        else:
            boss[3]+=1
            if boss[3]>30:
                health-=20
                boss[3]=0

def open_doors():
    for d in doors:
        if abs(px-d[0])<1.2 and abs(py-d[1])<1.2:
            d[2]=1

def shoot():
    global enemies,boss,explosions
    if weapon==0: rng=5;ang=0.1
    else: rng=6;ang=0.3
    for e in enemies:
        if e[2]:
            dx=e[0]-px
            dy=e[1]-py
            a=math.atan2(dy,dx)-pa
            if abs(a)<ang and math.hypot(dx,dy)<rng:
                e[2]=False
                explosions.append([e[0],e[1],20])
    if boss and boss[2]>0:
        dx=boss[0]-px
        dy=boss[1]-py
        a=math.atan2(dy,dx)-pa
        if abs(a)<ang and math.hypot(dx,dy)<rng:
            boss[2]-=10
            explosions.append([boss[0],boss[1],30])

def draw_gun():
    global shooting,shoot_frame
    if weapon==0:
        if shooting: sc.blit(gun2,(w//2-100,h-200));shoot_frame+=1; shooting=False if shoot_frame>3 else shooting
        else: sc.blit(gun1,(w//2-100,h-200))
    else:
        if shooting: sc.blit(shot2,(w//2-110,h-220));shoot_frame+=1; shooting=False if shoot_frame>4 else shooting
        else: sc.blit(shot1,(w//2-110,h-220))

def draw_hud():
    pygame.draw.rect(sc,(200,0,0),(20,20,health*2,20))
    font=pygame.font.SysFont(None,40)
    t=font.render(weapons[weapon]+" Ammo:"+str(ammo[weapon]),True,(255,255,255))
    sc.blit(t,(20,50))

def draw_minimap():
    for y,row in enumerate(world):
        for x,ch in enumerate(row):
            color=(100,100,100) if ch=="#" else (50,50,50)
            pygame.draw.rect(sc,color,(w-150+x*10,10+y*10,10,10))
    pygame.draw.circle(sc,(0,255,0),(w-150+int(px*10),10+int(py*10)),3)
    for e in enemies:
        if e[2]: pygame.draw.circle(sc,(255,0,0),(w-150+int(e[0]*10),10+int(e[1]*10)),3)
    if boss and boss[2]>0: pygame.draw.circle(sc,(255,0,255),(w-150+int(boss[0]*10),10+int(boss[1]*10)),4)

def draw_explosions():
    for ex in explosions:
        pygame.draw.circle(sc,(255,150,0),(int(ex[0]*64),int(ex[1]*64)),ex[2])
        ex[2]-=1
    while explosions and explosions[0][2]<=0: explosions.pop(0)

def check_pickups():
    global health,ammo
    for p in pickups[:]:
        if abs(px-p[0])<pickup_radius and abs(py-p[1])<pickup_radius:
            if p[2]=="health": health=min(100,health+50)
            if p[2]=="ammo": ammo[1]+=10
            pickups.remove(p)

running=True
while running:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: sys.exit()
        if ev.type==pygame.MOUSEMOTION: pa+=ev.rel[0]*rs
        if ev.type==pygame.MOUSEBUTTONDOWN:
            if cooldown<=0:
                shooting=True
                cooldown=10 if weapon==0 else 20
                if ammo[weapon]>0: ammo[weapon]-=1; shoot()
        if ev.type==pygame.KEYDOWN:
            if ev.key==pygame.K_q: weapon=(weapon+1)%2

    keys=pygame.key.get_pressed()
    if keys[pygame.K_e]: open_doors()
    if keys[pygame.K_w]: nx=px+math.cos(pa)*ps; ny=py+math.sin(pa)*ps; px,py=(nx,ny) if world[int(ny)][int(nx)] not in "#D" else (px,py)
    if keys[pygame.K_s]: nx=px-math.cos(pa)*ps; ny=py-math.sin(pa)*ps; px,py=(nx,ny) if world[int(ny)][int(nx)] not in "#D" else (px,py)
    if keys[pygame.K_a]: nx=px-math.sin(pa)*ps; ny=py+math.cos(pa)*ps; px,py=(nx,ny) if world[int(ny)][int(nx)] not in "#D" else (px,py)
    if keys[pygame.K_d]: nx=px+math.sin(pa)*ps; ny=py-math.cos(pa)*ps; px,py=(nx,ny) if world[int(ny)][int(nx)] not in "#D" else (px,py)

    sc.fill((20,20,20))
    z=cast()
    update_enemies()
    draw_enemies(z)
    draw_gun()
    draw_hud()
    draw_minimap()
    draw_explosions()
    check_pickups()
    if cooldown>0: cooldown-=1
    pygame.display.flip()
    clock.tick(60)
