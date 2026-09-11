## TODO

---

Todays Date: 08.09.2026
Tasks:

- [x] Create classes in places, where they are most needed, not everywhere possible
- - [x] Ball
- - [x] Board
- - [x] Box
- [x] Add actions to those classes
- [x] later on, add a randomiser, that gives some boxes a possibility to spawn a falling ball, after being removed
- [ ] Powerups:
- - [x] new ball (isnt included in failAttempts when dissapearing)
- - [x] big user paddle (3 seconds)
- - [x] big ball (3 seconds)
- - [ ] slow motion ball (5 seconds)

---

Todays Date: 11.09.2026

### Big Refactor

Tasks:

- [ ] create folders for different purposes

## Project Structure:

```
root/
├── index.py
├── classes/
│   ├── __init__.py
│   ├── Ball.py
│   ├── Board.py
│   ├── PowerUp.py
│   └── User.py
├── data/
│   ├── __init__.py
│   ├── constants.py
│   ├── powerup_types.py
│   └── state.py
├── features/
│   ├── ball_feature.py
│   └── powerup_feature.py
├── store/
│   ├── __init__.py
│   ├── db_init.py
│   ├── db_utils.py
│   └── score.sqlite
```
