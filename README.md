# Gait Tanks Repository Overview
https://github.com/ColeArduser/gait_tanks/assets/81708973/45181a21-2a24-4729-97c9-1a795bac7324

## Introduction
Gait Tanks is a Python-based, tank-themed game. This project encompasses a variety of functionalities from game mechanics to audio and state management, providing an immersive gaming experience.

## Key Components

### Core Game Mechanics
- **Main Game Loop ([game.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/game.py))**: Initializes the game, sets up the main loop, handles events, updates, and rendering. Includes functions for playing intro videos and loading game states.
- **Audio Management ([audio.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/level/audio.py))**: Manages all audio aspects of the game, including loading and playing sound effects for different game actions like tank movements and explosions.
- **Pathfinding ([pathfinding.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/level/pathfinding.py))**: Implements algorithms for AI-controlled tanks, ensuring efficient movement and navigation within the game environment.

### Game State Management
- **State System ([state.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/states/state.py))**: A base class for managing various states within the game, such as the title screen, level selection, and gameplay.
- **Specific States**: Includes implementations for different game states like the title screen ([title.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/states/title.py)), level management ([level.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/states/level.py)), and others.

### Level Components
- **Bullet Behavior ([bullet.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/level/bullet.py))**: Manages the behavior of bullets in the game, including their movement and interactions with other objects.

### Assets
- **Audio, Images, and Videos**: The project includes a comprehensive set of assets such as audio files, background images, sprites, and videos, crucial for the game's visual and auditory elements.

## File Structure

### IDE Configuration Files
- `.idea/`: Directory containing configuration files for JetBrains IDEs.

### Root Directory
- `README.md`: The main documentation file for the repository.

### Source Code (`src/`)
- `game.py`: Main game script.
- `level/`: Directory for level-related modules.
  - `audio.py`: Handles game audio.
  - `bullet.py`: Manages bullet behavior.
  - `enemy.py`: Defines enemy behavior.
  - `map.py`: Related to the game map.
  - `pathfinding.py`: Implements pathfinding algorithms.
  - `player.py`: Manages player behavior.
  - `tank.py`: Defines tank behavior.
- `states/`: Directory for game state management.
  - `controls.py`: Related to game controls.
  - `game_over.py`: Manages the game over state.
  - `level.py`: Handles individual game levels.
  - `level_select.py`: Manages level selection.
  - `pause_menu.py`: Pause menu implementation.
  - `state.py`: Base class for game states.
  - `title.py`: Manages the title screen.

### Assets (`src/assets/`)
- `audio/`: Contains audio files like background music and sound effects.
- `background_images/`: Background images for the game.
- `map/`: Images and tiles for the game map.
- `sprites/`: Sprite images for various game elements.
- `videos/`: Video files used in the game.
