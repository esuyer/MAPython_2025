import pygame
import sys
import random
import json
import os
pygame.init()

W,H=1200,700
FPS=60
DT=1/FPS
screen=pygame.display.set_mode((W,H))
clock=pygame.time.Clock()

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,70,70)
BLUE=(90,160,255)
GREEN=(90,255,160)
YELLOW=(255,255,140)
PURPLE=(200,120,255)
CYAN=(120,255,255)
GRAY=(130,130,130)

GROUND=H-120
PLAYER_X=260
SAVE_FILE="save.json"

font_big=pygame.font.SysFont("arialblack",52)
font_mid=pygame.font.SysFont("arial",26)
font_small=pygame.font.SysFont("arial",16)

def load_save():
    if os.path.exists(SAVE_FILE):
        return json.load(open(SAVE_FILE))
    return {"best":0}

def save_game(d):
    json.dump(d,open(SAVE_FILE,"w"))

save=load_save()

class Camera:
    def __init__(self):
        self.shake=0
        self.x=0
    def update(self):
        if self.shake>0:
            self.shake-=1
            self.x=random.randint(-6,6)
        else:
            self.x=0

camera=Camera()

class Trail:
    def __init__(self):
        self.p=[]
    def add(self,x,y):
        self.p.append([x,y,18])
    def update(self):
        for t in self.p:
            t[2]-=1
        self.p=[t for t in self.p if t[2]>0]
    def draw(self):
        for x,y,s in self.p:
            pygame.draw.circle(screen,CYAN,(int(x+camera.x),int(y)),s//4)

trail=Trail()

class Player:
    def __init__(self,flip=False):
        self.flip=flip
        self.reset()
    def reset(self):
        self.y=GROUND-40 if not self.flip else 40
        self.vy=0.0
        self.g=1.25 if not self.flip else -1.25
        self.mode="cube"
        self.rot=0
        self.on_ground=True
        self.wave_dir=1
    def rect(self):
        return pygame.Rect(PLAYER_X,self.y,40,40)
    def switch(self,m):
        self.mode=m
        self.vy=0
        self.rot=0
        self.wave_dir=1
        if m!="ball":
            self.g=abs(self.g) if not self.flip else -abs(self.g)
    def input(self,hold):
        if self.mode=="cube" and hold and self.on_ground:
            self.vy=-18 if not self.flip else 18
            self.on_ground=False
        elif self.mode=="ship" and hold:
            self.vy-=2.2 if not self.flip else -2.2
        elif self.mode=="ball" and hold:
            self.g*=-1
        elif self.mode=="ufo" and hold:
            self.vy=-14 if not self.flip else 14
        elif self.mode=="wave":
            self.wave_dir=-1 if hold else 1
        elif self.mode=="robot" and hold and self.on_ground:
            self.vy=-22 if not self.flip else 22
            self.on_ground=False
    def update(self):
        if self.mode=="wave":
            self.vy=12*self.wave_dir
        else:
            self.vy+=self.g
        self.y+=self.vy
        if self.mode!="wave":
            if not self.flip and self.y>=GROUND-40:
                self.y=GROUND-40
                self.vy=0
                self.on_ground=True
            if self.flip and self.y<=40:
                self.y=40
                self.vy=0
                self.on_ground=True
        self.rot+=7
        trail.add(PLAYER_X+20,self.y+20)
    def draw(self):
        surf=pygame.Surface((40,40),pygame.SRCALPHA)
        c={"cube":BLUE,"ship":YELLOW,"ball":GREEN,"ufo":PURPLE,"wave":CYAN,"robot":RED}[self.mode]
        if self.mode=="ship":
            pygame.draw.polygon(surf,c,[(0,40),(40,20),(0,0)])
        elif self.mode=="ball":
            pygame.draw.circle(surf,c,(20,20),20)
        elif self.mode=="ufo":
            pygame.draw.ellipse(surf,c,(0,8,40,32))
        else:
            pygame.draw.rect(surf,c,(0,0,40,40))
        glow=pygame.transform.scale(surf,(52,52))
        glow.set_alpha(70)
        r=glow.get_rect(center=(PLAYER_X+20+camera.x,self.y+20))
        screen.blit(glow,r.topleft)
        rot=pygame.transform.rotate(surf,self.rot)
        rr=rot.get_rect(center=(PLAYER_X+20+camera.x,self.y+20))
        screen.blit(rot,rr.topleft)

p1=Player(False)
p2=Player(True)

class Orb:
    def __init__(self,x,y,kind):
        self.x=x
        self.y=y
        self.kind=kind
        self.used=False
    def rect(self,scroll):
        return pygame.Rect(self.x-scroll-12,self.y-12,24,24)
    def draw(self,scroll):
        c={"yellow":YELLOW,"blue":CYAN,"pink":PURPLE,"green":GREEN}[self.kind]
        pygame.draw.circle(screen,c,(int(self.x-scroll+camera.x),int(self.y)),12)

def apply_orb(p,kind):
    if kind=="yellow":
        if p.mode in ["cube","robot","ufo"]:
            p.vy=-18 if not p.flip else 18
            p.on_ground=False
        elif p.mode=="ship":
            p.vy-=4 if not p.flip else -4
        elif p.mode=="ball":
            p.g*=-1
        elif p.mode=="wave":
            p.wave_dir*=-1
    elif kind=="blue":
        if p.mode in ["cube","robot","ufo"]:
            p.vy=-22 if not p.flip else 22
            p.on_ground=False
        elif p.mode=="ship":
            p.vy-=6 if not p.flip else -6
    elif kind=="pink":
        if p.mode in ["cube","robot","ufo"]:
            p.vy=-12 if not p.flip else 12
            p.on_ground=False
    elif kind=="green":
        p.g*=-1

class Obj:
    def __init__(self,x,h):
        self.x=x
        self.h=h
    def rect(self,scroll):
        return pygame.Rect(self.x-scroll,GROUND-self.h,40,self.h)
    def draw(self,scroll):
        pygame.draw.rect(screen,RED,(self.x-scroll+camera.x,GROUND-self.h,40,self.h))

class Portal:
    def __init__(self,x,m):
        self.x=x
        self.m=m
    def rect(self,scroll):
        return pygame.Rect(self.x-scroll,GROUND-90,40,90)
    def draw(self,scroll):
        cmap={"cube":BLUE,"ship":YELLOW,"ball":GREEN,"ufo":PURPLE,"wave":CYAN,"robot":RED}
        pygame.draw.rect(screen,cmap[self.m],(self.x-scroll+camera.x,GROUND-90,40,90),3)

class Speed:
    def __init__(self,x,v):
        self.x=x
        self.v=v
    def rect(self,scroll):
        return pygame.Rect(self.x-scroll,GROUND-90,40,90)
    def draw(self,scroll):
        pygame.draw.rect(screen,YELLOW,(self.x-scroll+camera.x,GROUND-90,40,90),3)

class DualPortal:
    def __init__(self,x):
        self.x=x
    def rect(self,scroll):
        return pygame.Rect(self.x-scroll,GROUND-90,40,90)
    def draw(self,scroll):
        pygame.draw.rect(screen,WHITE,(self.x-scroll+camera.x,GROUND-90,40,90),3)

class Level:
    def __init__(self):
        self.reset()
    def reset(self):
        self.scroll=0
        self.speed=6
        self.score=0
        self.obs=[]
        self.port=[]
        self.spd=[]
        self.orbs=[]
        self.dual=[]
        for i in range(40):
            self.obs.append(Obj(600+i*200,random.randint(40,120)))
        modes=["cube","ship","ball","ufo","wave","robot"]
        for i in range(8):
            self.port.append(Portal(1000+i*800,random.choice(modes)))
        for i in range(6):
            self.spd.append(Speed(1400+i*900,random.choice([5,7,9,11])))
        for i in range(20):
            self.orbs.append(Orb(800+i*300,random.randint(200,GROUND-80),random.choice(["yellow","blue","pink","green"])))
        self.dual.append(DualPortal(2600))
    def update(self):
        self.scroll+=self.speed
        self.score+=self.speed
    def draw(self):
        for o in self.obs:o.draw(self.scroll)
        for p in self.port:p.draw(self.scroll)
        for s in self.spd:s.draw(self.scroll)
        for o in self.orbs:o.draw(self.scroll)
        for d in self.dual:d.draw(self.scroll)

level=Level()

def draw_ui():
    screen.blit(font_mid.render(f"Score {level.score}",True,WHITE),(20,20))
    screen.blit(font_small.render(f"Best {save['best']}",True,GRAY),(20,50))
    pygame.draw.rect(screen,WHITE,(20,80,300,8),2)
    pygame.draw.rect(screen,GREEN,(20,80,min(300,level.score//30),8))

def menu():
    while True:
        screen.fill(BLACK)
        t=font_big.render("GEOMETRY DASH",True,WHITE)
        h=font_mid.render("SPACE TO START",True,GRAY)
        screen.blit(t,(W//2-t.get_width()//2,H//2-80))
        screen.blit(h,(W//2-h.get_width()//2,H//2))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
                return
            if e.type==pygame.QUIT:
                pygame.quit();sys.exit()
        clock.tick(FPS)

def run():
    level.reset()
    p1.reset()
    p2.reset()
    trail.p.clear()
    dual=False
    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        hold=pygame.key.get_pressed()[pygame.K_SPACE]
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit();sys.exit()
        for p in [p1,p2] if dual else [p1]:
            p.input(hold)
            p.update()
        trail.update()
        level.update()
        camera.update()
        for o in level.obs:
            for p in [p1,p2] if dual else [p1]:
                if o.rect(level.scroll).colliderect(p.rect()):
                    camera.shake=25
                    save["best"]=max(save["best"],level.score)
                    save_game(save)
                    return
        for po in level.port:
            for p in [p1,p2] if dual else [p1]:
                if po.rect(level.scroll).colliderect(p.rect()):
                    p.switch(po.m)
        for sp in level.spd:
            if sp.rect(level.scroll).colliderect(p1.rect()):
                level.speed=sp.v
        for d in level.dual:
            if d.rect(level.scroll).colliderect(p1.rect()):
                dual=True
        if hold:
            for o in level.orbs:
                for p in [p1,p2] if dual else [p1]:
                    if not o.used and o.rect(level.scroll).colliderect(p.rect()):
                        o.used=True
                        apply_orb(p,o.kind)
        pygame.draw.rect(screen,GRAY,(0,GROUND,W,H-GROUND))
        level.draw()
        trail.draw()
        p1.draw()
        if dual:p2.draw()
        draw_ui()
        pygame.display.flip()

menu()
while True:
    run()
