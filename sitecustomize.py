import os
import sys
import math
from types import ModuleType

os.environ['SDL_AUDIODRIVER'] = 'dummy'

import pygame

class _TurtleInstance:
    def __init__(self, shim):
        self._shim = shim
        self._pos = [400, 300]
        self._angle = 0
        self._drawing = True
        self._color = (255, 255, 255)

    def speed(self, *args): pass
    def hideturtle(self): pass
    def showturtle(self): pass
    def shape(self, *args): pass
    def begin_fill(self): pass
    def end_fill(self): pass
    def stamp(self): pass

    def penup(self): self._drawing = False
    def pu(self): self._drawing = False
    def pendown(self): self._drawing = True
    def pd(self): self._drawing = True

    def color(self, *args):
        if args:
            try:
                self._color = pygame.Color(args[0]) if isinstance(args[0], str) else tuple(int(c * 255) for c in args[0])
            except: pass
    def pencolor(self, *args): self.color(*args)
    def fillcolor(self, *args): self.color(*args)
    def width(self, *args): pass
    def pensize(self, *args): pass

    def forward(self, d):
        rad = math.radians(self._angle)
        old = list(self._pos)
        self._pos[0] += d * math.cos(rad)
        self._pos[1] -= d * math.sin(rad)
        if self._drawing:
            self._shim._lines.append((old, list(self._pos), self._color))
    def fd(self, d): self.forward(d)

    def backward(self, d): self.forward(-d)
    def bk(self, d): self.forward(-d)

    def right(self, a): self._angle -= a
    def rt(self, a): self._angle -= a
    def left(self, a): self._angle += a
    def lt(self, a): self._angle += a

    def goto(self, x, y=None):
        if y is None and hasattr(x, '__iter__'):
            x, y = x
        old = list(self._pos)
        self._pos = [x + 400, 300 - y]
        if self._drawing:
            self._shim._lines.append((old, list(self._pos), self._color))

    def setx(self, x): self.goto(x, 300 - self._pos[1])
    def sety(self, y): self.goto(self._pos[0] - 400, y)

    def setheading(self, a): self._angle = a
    def seth(self, a): self._angle = a

    def xcor(self): return self._pos[0] - 400
    def ycor(self): return 300 - self._pos[1]
    def pos(self): return (self.xcor(), self.ycor())
    def position(self): return self.pos()
    def heading(self): return self._angle

    def circle(self, radius, extent=360, steps=None):
        steps = steps or max(int(abs(radius) * 0.5), 12)
        angle_step = extent / steps
        for _ in range(steps):
            self.forward(2 * math.pi * abs(radius) * angle_step / 360)
            self.left(angle_step)

    def write(self, text, *args, **kwargs):
        if self._shim._screen_surf:
            font = pygame.font.SysFont("arial", 14)
            surf = font.render(str(text), True, self._color)
            self._shim._screen_surf.blit(surf, (int(self._pos[0]), int(self._pos[1])))


class _ScreenProxy:
    def __init__(self, shim):
        self._shim = shim
    def title(self, t): pygame.display.set_caption(t)
    def bgcolor(self, c):
        try: self._shim._bg = pygame.Color(c) if isinstance(c, str) else c
        except: pass
    def setup(self, *args, **kwargs): pass
    def tracer(self, *args, **kwargs): pass
    def update(self): self._shim._render()
    def exitonclick(self): self._shim._mainloop()
    def bye(self): pygame.quit(); sys.exit()
    def screensize(self, *args, **kwargs): pass
    def setworldcoordinates(self, *args, **kwargs): pass
    def listen(self, *args, **kwargs): pass
    def onkey(self, *args, **kwargs): pass
    def onclick(self, *args, **kwargs): pass


class _TurtleModule(ModuleType):
    def __init__(self):
        super().__init__('turtle')
        self._lines = []
        self._bg = (30, 30, 30)
        self._screen_surf = None
        self._clock = None
        self._instance = _TurtleInstance(self)
        self._screen_proxy = _ScreenProxy(self)

    def _init_display(self):
        if self._screen_surf is None:
            pygame.init()
            self._screen_surf = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("Turtle")
            self._clock = pygame.time.Clock()

    def Screen(self):
        self._init_display()
        return self._screen_proxy

    def Turtle(self):
        self._init_display()
        t = _TurtleInstance(self)
        return t

    def Pen(self):
        return self.Turtle()

    def _render(self):
        if self._screen_surf:
            self._screen_surf.fill(self._bg)
            for start, end, col in self._lines:
                pygame.draw.line(self._screen_surf, col,
                                 (int(start[0]), int(start[1])),
                                 (int(end[0]), int(end[1])), 2)
            pygame.display.flip()

    def _mainloop(self):
        self._init_display()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self._render()
            self._clock.tick(60)

    def done(self): self._mainloop()
    def exitonclick(self): self._mainloop()
    def mainloop(self): self._mainloop()

    # Module-level turtle functions (delegate to a shared instance)
    def speed(self, *a): self._instance.speed(*a)
    def forward(self, d): self._instance.forward(d)
    def fd(self, d): self._instance.forward(d)
    def backward(self, d): self._instance.backward(d)
    def bk(self, d): self._instance.backward(d)
    def right(self, a): self._instance.right(a)
    def rt(self, a): self._instance.right(a)
    def left(self, a): self._instance.left(a)
    def lt(self, a): self._instance.left(a)
    def penup(self): self._instance.penup()
    def pu(self): self._instance.penup()
    def pendown(self): self._instance.pendown()
    def pd(self): self._instance.pendown()
    def color(self, *a): self._instance.color(*a)
    def pencolor(self, *a): self._instance.color(*a)
    def fillcolor(self, *a): self._instance.color(*a)
    def goto(self, x, y=None): self._instance.goto(x, y)
    def setx(self, x): self._instance.setx(x)
    def sety(self, y): self._instance.sety(y)
    def setheading(self, a): self._instance.setheading(a)
    def seth(self, a): self._instance.setheading(a)
    def circle(self, r, e=360, s=None): self._instance.circle(r, e, s)
    def stamp(self): self._instance.stamp()
    def hideturtle(self): self._instance.hideturtle()
    def showturtle(self): self._instance.showturtle()
    def begin_fill(self): self._instance.begin_fill()
    def end_fill(self): self._instance.end_fill()
    def width(self, *a): pass
    def pensize(self, *a): pass
    def shape(self, *a): pass
    def write(self, t, *a, **k): self._instance.write(t)
    def xcor(self): return self._instance.xcor()
    def ycor(self): return self._instance.ycor()
    def pos(self): return self._instance.pos()
    def position(self): return self._instance.pos()
    def heading(self): return self._instance.heading()
    def bgcolor(self, c): self._screen_proxy.bgcolor(c)
    def title(self, t): self._screen_proxy.title(t)
    def setup(self, *a, **k): pass
    def tracer(self, *a, **k): pass
    def update(self): self._render()


sys.modules['turtle'] = _TurtleModule()
sys.modules['_tkinter'] = ModuleType('_tkinter')
sys.modules['tkinter'] = ModuleType('tkinter')
