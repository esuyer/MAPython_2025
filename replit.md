# replit.md

## Overview

This is a collection of Python learning exercises, organized by lesson number. The repository contains beginner-level Python scripts covering fundamental programming concepts including variables, conditionals, loops, functions, strings, lists, turtle graphics, and random number generation. Each file follows a naming convention of `L{lesson_number}_VE_{type}.py` where type is either `CW` (classwork) or `HW` (homework). There is no overarching application architecture — this is a student's coursework repository.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

- **Language**: Python 3
- **Structure**: Flat file structure with no modules, packages, or frameworks. Each `.py` file is a standalone script meant to be run independently.
- **No build system or package manager**: The project has no `requirements.txt`, `pyproject.toml`, or similar configuration. Dependencies are limited to Python standard library modules (`turtle`, `random`, `tkinter`).
- **Naming convention**: Files are named by lesson number and type (classwork/homework), e.g., `L10.py`, `L5_VE_HW.py`.
- **No database, no API, no authentication**: This is purely a collection of standalone scripts.
- **GUI experiments**: Some scripts use `turtle` graphics for drawing and one file (`tk_test.py`) tests `tkinter` for GUI rendering.

### Key Concepts by Lesson
- **L3**: Input/output, loops, turtle basics
- **L4**: Conditionals (if/elif/else), turtle with random
- **L5**: Nested conditionals
- **L6**: Loops with range, turtle stamps, random
- **L7**: Boolean logic (and, or, not)
- **L10**: Functions (def), return values
- **L11**: Strings, indexing, len()
- **L12**: String iteration, character filtering
- **L13**: Lists, append, random lists
- **L14**: List methods (count, index, insert, remove, pop)

## External Dependencies

- **Python Standard Library only**:
  - `turtle` — used for graphical drawing exercises
  - `random` — used for generating random numbers
  - `tkinter` — used in one test file (`tk_test.py`) for GUI testing
- **No third-party packages are required**
- **No external services, APIs, or databases are used**