# Python Environment Project

## Overview
A graphical development environment using Pygame to emulate standard libraries like Turtle.

## Architecture
- `main.py`: FNAF jumpscare simulator
- `doom.py`: FPS game using pygame.Vector2 for math
- `HW8.py`: Side-scrolling obstacle game
- `Classwork.py`: Turtle-based classwork (using Pygame shim)
- `src/turtle_shim.py`: Pygame-based shim for `turtle` and `tkinter` to bypass missing system dependencies.

## Recent Changes
- Implemented `src/turtle_shim.py` to provide `turtle` functionality without `_tkinter`.
- Updated `Classwork.py` to use the shim.
- Configured audio driver fix for all graphical scripts.
