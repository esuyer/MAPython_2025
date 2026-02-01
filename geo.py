import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame
import sys
import random
import math
import json

pygame.init()

WIDTH=1200
HEIGHT=700
FPS=60
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Geometry Dash Python")
clock=pygame.time.Clock()

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,60,60)
BLUE=(80,160,255)
GREEN=(80,255,160)
YELLOW=(255,255,120)
PURPLE=(200,120,255)
CYAN=(120,255,255)
GRAY=(120,120,120)

font_big=pygame.font.SysFont("arialblack",54)
font_mid=pygame.font.SysFont("arial",28)
font_small=pygame.font.SysFont("arial",16)

GROUND=HEIGHT-120
SAVE_FILE="save.json"

def load_save():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"best":0}

def save_game(data):
    try:
        with open(SAVE_FILE, 'w') as f:
            json.dump(data, f)
    except:
        pass

save_data=load_save()

class Camera:
    def __init__(self):
        self.shake=0
        self.offset=0
    def update(self):
        if self.shake>0:
            self.shake-=1
            self.offset=random.randint(-8,8)
        else:
            self.offset=0

camera=Camera()

class Particle:
    def __init__(self,x,y,vx,vy,l,c,s):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.life=l
        self.c=c
        self.s=s
    def update(self):
        self.x+=self.vx
        self.y+=self.vy
        self.vy+=0.3
        self.life-=1
    def draw(self):
        if self.life>0:
            pygame.draw.rect(screen,self.c,(self.x+camera.offset,self.y,self.s,self.s))

particles=[]

def spawn_particles(x,y,c,n):
    for i in range(n):
        particles.append(Particle(x,y,random.uniform(-6,6),random.uniform(-10,-2),random.randint(20,60),c,random.randint(3,6)))

class Trail:
    def __init__(self):
        self.points=[]
    def add(self,x,y):
        self.points.append([x,y,20])
    def update(self):
        for p in self.points:
            p[2]-=1
        self.points=[p for p in self.points if p[2]>0]
    def draw(self):
        for p in self.points:
            pygame.draw.circle(screen,CYAN,(int(p[0]+camera.offset),int(p[1])),p[2]//4)

trail=Trail()

class Player:
    def __init__(self):
        self.x=260
        self.y=GROUND-40
        self.s=40
        self.vy=0
        self.g=1.2
        self.rot=0
        self.mode="cube"
        self.ground=False
        self.wave_dir=1
    def reset(self):
        self.y=GROUND-self.s
        self.vy=0
        self.rot=0
        self.mode="cube"
        self.ground=True
        self.wave_dir=1
    def rect(self):
        return pygame.Rect(self.x,self.y,self.s,self.s)
    def switch(self,m):
        self.mode=m
        self.vy=0
        self.rot=0
    def input(self,hold):
        if self.mode=="cube" and hold and self.ground:
            self.vy=-18
            self.ground=False
        elif self.mode=="ship" and hold:
            self.vy-=2.2
        elif self.mode=="ball" and hold:
            self.g*=-1
        elif self.mode=="ufo" and hold:
            self.vy=-14
        elif self.mode=="wave":
            self.wave_dir=-1 if hold else 1
        elif self.mode=="robot" and hold and self.ground:
            self.vy=-22
            self.ground=False
    def update(self):
        if self.mode=="wave":
            self.vy=10*self.wave_dir
        else:
            self.vy+=self.g
        self.y+=self.vy
        if self.mode!="wave":
            if self.y>=GROUND-self.s:
                self.y=GROUND-self.s
                self.vy=0
                self.ground=True
            if self.y<0:
                self.y=0
                self.vy=0
        self.rot+=6
        trail.add(self.x,self.y)
    def draw(self):
        surf=pygame.Surface((self.s,self.s),pygame.SRCALPHA)
        if self.mode=="cube":
            pygame.draw.rect(surf,BLUE,(0,0,self.s,self.s))
        elif self.mode=="ship":
            pygame.draw.polygon(surf,YELLOW,[(0,self.s),(self.s,self.s//2),(0,0)])
        elif self.mode=="ball":
            pygame.draw.circle(surf,GREEN,(self.s//2,self.s//2),self.s//2)
        elif self.mode=="ufo":
            pygame.draw.ellipse(surf,PURPLE,(0,10,self.s,self.s-10))
        elif self.mode=="wave":
            pygame.draw.rect(surf,CYAN,(0,0,self.s,self.s))
        elif self.mode=="robot":
            pygame.draw.rect(surf,RED,(0,0,self.s,self.s))
        glow=pygame.transform.scale(surf,(self.s+10,self.s+10))
        glow.set_alpha(80)
        r=glow.get_rect(center=(self.x+self.s//2+camera.offset,self.y+self.s//2))
        screen.blit(glow,r.topleft)
        rot=pygame.transform.rotate(surf,self.rot)
        rr=rot.get_rect(center=(self.x+self.s//2+camera.offset,self.y+self.s//2))
        screen.blit(rot,rr.topleft)

player=Player()

class Obstacle:
    def __init__(self,x,h):
        self.x=x
        self.h=h
        self.w=40
    def update(self,s):
        self.x-=s
    def rect(self):
        return pygame.Rect(self.x,GROUND-self.h,self.w,self.h)
    def draw(self):
        pygame.draw.rect(screen,RED,(self.x+camera.offset,GROUND-self.h,self.w,self.h))

class Portal:
    def __init__(self,x,m):
        self.x=x
        self.m=m
        self.w=40
        self.h=90
    def update(self,s):
        self.x-=s
    def rect(self):
        return pygame.Rect(self.x,GROUND-self.h,self.w,self.h)
    def draw(self):
        pygame.draw.rect(screen,PURPLE,(self.x+camera.offset,GROUND-self.h,self.w,self.h),3)

class SpeedPortal:
    def __init__(self,x,v):
        self.x=x
        self.v=v
        self.w=40
        self.h=90
    def update(self,s):
        self.x-=s
    def rect(self):
        return pygame.Rect(self.x,GROUND-self.h,self.w,self.h)
    def draw(self):
        pygame.draw.rect(screen,YELLOW,(self.x+camera.offset,GROUND-self.h,self.w,self.h),3)

class Level:
    def __init__(self):
        self.obs=[]
        self.port=[]
        self.spd=[]
        self.t=0
        self.speed=6
        self.score=0
    def reset(self):
        self.obs.clear()
        self.port.clear()
        self.spd.clear()
        self.t=0
        self.speed=6
        self.score=0
    def spawn(self):
        if self.t%80==0:
            self.obs.append(Obstacle(WIDTH+60,random.randint(40,120)))
        if self.t%240==0:
            self.port.append(Portal(WIDTH+100,random.choice(["cube","ship","ball","ufo","wave","robot"])))
        if self.t%360==0:
            self.spd.append(SpeedPortal(WIDTH+140,random.choice([5,7,9,11])))
    def update(self):
        self.t+=1
        self.spawn()
        for o in self.obs:
            o.update(self.speed)
        for p in self.port:
            p.update(self.speed)
        for s in self.spd:
            s.update(self.speed)
        self.obs=[o for o in self.obs if o.x>-100]
        self.port=[p for p in self.port if p.x>-100]
        self.spd=[s for s in self.spd if s.x>-100]
        self.score+=self.speed
    def draw(self):
        for o in self.obs:
            o.draw()
        for p in self.port:
            p.draw()
        for s in self.spd:
            s.draw()

level=Level()

def draw_ground():
    pygame.draw.rect(screen,GRAY,(0,GROUND,WIDTH,HEIGHT-GROUND))

def update_particles():
    for p in particles:
        p.update()
    particles[:]=[p for p in particles if p.life>0]

def draw_ui():
    screen.blit(font_mid.render(f"Score {level.score}",True,WHITE),(20,20))
    screen.blit(font_small.render(f"Best {save_data['best']}",True,GRAY),(20,50))
    pygame.draw.rect(screen,WHITE,(20,80,300,8),2)
    pygame.draw.rect(screen,GREEN,(20,80,min(300,level.score//30),8))

def pause():
    while True:
        screen.fill(BLACK)
        t=font_big.render("PAUSED",True,WHITE)
        screen.blit(t,(WIDTH//2-t.get_width()//2,HEIGHT//2-40))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.KEYDOWN and e.key==pygame.K_p:
                return
            if e.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)

def run():
    level.reset()
    player.reset()
    particles.clear()
    trail.points.clear()
    while True:
        screen.fill(BLACK)
        hold=pygame.key.get_pressed()[pygame.K_SPACE]
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type==pygame.KEYDOWN and e.key==pygame.K_p:
                pause()
        player.input(hold)
        player.update()
        trail.update()
        level.update()
        camera.update()
        for o in level.obs:
            if o.rect().colliderect(player.rect()):
                spawn_particles(player.x,player.y,RED,80)
                camera.shake=30
                save_data["best"]=max(save_data["best"],level.score)
                save_game(save_data)
                return
        for p in level.port:
            if p.rect().colliderect(player.rect()):
                player.switch(p.m)
        for s in level.spd:
            if s.rect().colliderect(player.rect()):
                level.speed=s.v
        update_particles()
        draw_ground()
        level.draw()
        trail.draw()
        player.draw()
        for p in particles:
            p.draw()
        draw_ui()
        pygame.display.flip()
        clock.tick(FPS)

def menu():
    while True:
        screen.fill(BLACK)
        t=font_big.render("GEOMETRY DASH",True,WHITE)
        h=font_mid.render("SPACE TO START",True,GRAY)
        screen.blit(t,(WIDTH//2-t.get_width()//2,HEIGHT//2-80))
        screen.blit(h,(WIDTH//2-h.get_width()//2,HEIGHT//2))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
                return
            if e.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)

menu()
while True:
    run()
