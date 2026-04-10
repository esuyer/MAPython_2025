# Python Environment Project

## Overview
A Python learning and games project containing Pygame-based games and homework assignments.

## Files
- `geo.py`: Geometry Dash game (Pygame)
- `src/main.py`: FNAF jumpscare simulator (Pygame)
- `Classwork.py`: Turtle drawing — click to draw squares, right-click for corner lines
- `WORK.py`: List homework (Q1–Q6)
- `Hw.py`: List homework problems
- `HW13.py`: Random word/list homework
- `comp.py`: String comparison functions
- `example.py`: Simple fruit search example
- `sitecustomize.py`: Reference note only (not loaded by Python)

## Turtle Support
Turtle works automatically in **every** Python file — current and future — with no imports or setup needed beyond `import turtle`.

**How it works**: `.pythonlibs/lib/python3.11/site-packages/usercustomize.py` is loaded by Python at startup and injects a full turtle shim backed by Pygame.

**Supported features**:
- All drawing commands: `forward`, `backward`, `left`, `right`, `circle`, `dot`, `goto`, `home`, etc.
- Colors: `color()`, `pencolor()`, `fillcolor()`, `begin_fill()`, `end_fill()`
- Pen control: `penup()`, `pendown()`, `pensize()`, `speed()`
- Screen: `Screen()`, `title()`, `bgcolor()`, `setup()`, `window_width()`, `window_height()`
- **Click events**: `screen.onclick(func, btn=1)` and `screen.onclick(func, btn=3)` (left/right click)
- **Key events**: `screen.onkey(func, key)`, `screen.onkeypress()`, `screen.onkeyrelease()`
- **Timers**: `screen.ontimer(func, ms)`
- Event loop: `turtle.done()`, `turtle.mainloop()`, `turtle.exitonclick()`
- Multiple turtles: `turtle.Turtle()` returns independent instances

## Audio Fix
All Pygame scripts must have this before `import pygame`:
```python
import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
```
This is automatically set by `usercustomize.py` for turtle, but game files must set it themselves.
