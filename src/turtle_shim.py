import os
import sys
from types import ModuleType
import pygame
import math

# Mandatory audio driver fix for Replit
os.environ['SDL_AUDIODRIVER'] = 'dummy'

# Implementation of a Turtle Shim using Pygame
class TurtleShim(ModuleType):
    def __init__(self):
        super().__init__('turtle')
        self.Screen = self._Screen
        self.Turtle = self._Turtle
        self.Pen = self._Turtle
        self.done = self._done
        self.exitonclick = self._done
        self.setup = lambda **kwargs: None
        self.title = lambda t: pygame.display.set_caption(t)
        self.speed = lambda *args: None
        self.color = self._color
        self.forward = self._forward
        self.right = self._right
        self.left = self._left
        self.stamp = lambda: None
        self.penup = self._penup
        self.pendown = self._pendown
        self.goto = self._goto
        self.pencolor = self._color
        self.circle = self._circle
        self.shape = lambda *args: None
        self.width = lambda *args: None
        self.pensize = lambda *args: None
        self.begin_fill = lambda: None
        self.end_fill = lambda: None
        self.hideturtle = lambda: None
        self.showturtle = lambda: None
        
        # Internal state
        self._pos = [400, 300]
        self._angle = 0
        self._points = []
        self._drawing = True
        self._current_color = (0, 255, 255)
        self._init_pygame = False
        self._screen_surf = None

    def _Screen(self):
        if not self._init_pygame:
            pygame.init()
            self._screen_surf = pygame.display.set_mode((800, 600))
            self._init_pygame = True
        return self

    def _Turtle(self):
        return self

    def _penup(self):
        self._drawing = False

    def _pendown(self):
        self._drawing = True

    def _color(self, *args):
        if args:
            if isinstance(args[0], str):
                try:
                    self._current_color = pygame.Color(args[0])
                except:
                    pass
            elif isinstance(args[0], tuple):
                self._current_color = args[0]

    def _goto(self, x, y):
        old_pos = list(self._pos)
        self._pos = [x + 400, 300 - y] # Convert turtle coords to screen coords
        if self._drawing:
            self._points.append(("line", old_pos, list(self._pos), self._current_color))

    def _forward(self, d):
        old_pos = list(self._pos)
        rad = math.radians(self._angle)
        self._pos[0] += d * math.cos(rad)
        self._pos[1] += d * math.sin(rad)
        if self._drawing:
            self._points.append(("line", old_pos, list(self._pos), self._current_color))

    def _right(self, a):
        self._angle += a

    def _left(self, a):
        self._angle -= a
        
    def _circle(self, radius, extent=None, steps=None):
        center = [self._pos[0], self._pos[1]]
        if self._drawing:
            self._points.append(("circle", list(center), radius, self._current_color))

    def _done(self):
        if not self._init_pygame: self._Screen()
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self._screen_surf.fill((30, 30, 30))
            for type, *args in self._points:
                if type == "line":
                    start, end, col = args
                    pygame.draw.line(self._screen_surf, col, start, end, 2)
                elif type == "circle":
                    pos, rad, col = args
                    pygame.draw.circle(self._screen_surf, col, (int(pos[0]), int(pos[1])), int(rad), 2)
            pygame.display.flip()
            clock.tick(60)

# Inject the shim into sys.modules
sys.modules['turtle'] = TurtleShim()
sys.modules['tkinter'] = ModuleType('tkinter') # Mock tkinter too
