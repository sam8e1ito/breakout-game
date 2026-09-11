# BREAKOUT GAME

A simple **Breakout-style game built with Python and Pygame**.

Break the bricks, control the paddle, collect power-ups and try to achieve the highest score.

---

## Features

- Classic Breakout gameplay
- Ball and paddle mechanics
- Brick destruction
- High-score system with SQLite _(in progress)_
- Power-ups
- Object-oriented project structure
- Modular game features

---

## Power-Ups

Destroyed bricks can drop different power-ups during the game.

### New Ball

Adds an additional ball to the game.

Having multiple balls allows you to destroy more bricks at the same time and potentially increase your score faster.

### Big Ball

Makes the ball bigger for **3 seconds**.

A bigger ball makes it easier to hit and can help you keep the game going.

### Big Paddle

Makes the paddle bigger for **3 seconds**.

This gives you a larger area to hit the ball and makes it easier to keep the ball in play.

---

## Project Structure

```text
root/
├── index.py
│
├── classes/
│   ├── __init__.py
│   ├── Ball.py
│   ├── Board.py
│   ├── PowerUp.py
│   └── User.py
│
├── data/
│   ├── __init__.py
│   ├── constants.py
│   ├── powerup_types.py
│   └── state.py
│
├── features/
│   ├── ball_feature.py
│   └── powerup_feature.py
│
└── store/
    ├── __init__.py
    ├── db_init.py
    ├── db_utils.py
    └── score.sqlite
```

### Structure Overview

| File / Folder | Description                                                     |
| ------------- | --------------------------------------------------------------- |
| `classes/`    | Main game classes such as the ball, board, paddle and power-ups |
| `data/`       | Constants, game state and power-up types                        |
| `features/`   | Separate gameplay features and mechanics                        |
| `store/`      | SQLite database and database utilities                          |
| `index.py`    | Main entry point of the game                                    |

---

## Requirements

- Python 3
- Pygame
- Pymunk
- random_username
- SQLite

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sam8e1ito/breakout-game
cd breakout-game
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Database Setup

The game uses SQLite to store users' highscores.

Create an empty database file:

```text
store/score.sqlite
```

Then open the database with SQLite and create the `score` table:

```sql
CREATE TABLE score (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    username TEXT UNIQUE,
    score INTEGER
);
```

> **Note:** The database setup is currently manual and the high-score system is still in progress.

---

## Run the Game

Start the game with:

```bash
python3 index.py
```

On Windows:

```bash
python index.py
```

---

## Controls

| Key     | Action            |
| ------- | ----------------- |
| `A`     | Move paddle left  |
| `D`     | Move paddle right |
| `SPACE` | Create a new ball |

---

## Goal

Destroy as many bricks as possible and achieve the highest score.

Use the power-ups strategically and try not to lose the ball.

---

## Tech Stack

- **Python**
- **Pygame**
- **Pymunk**
- **SQLite**

---

## Project Status

This project is currently under development.

The core Breakout gameplay and power-up system are implemented. The SQLite-based high-score system is still being developed.

---

## License

This project was created for learning and experimentation with Python, Pygame and game development.
