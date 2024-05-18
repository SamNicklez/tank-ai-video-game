# Gait Tanks Repository Overview
Note: All sounds, images, and video in this game were made using generative AI

https://github.com/ColeArduser/gait_tanks/assets/81708973/45181a21-2a24-4729-97c9-1a795bac7324


## To Run
- **[game.exe](https://github.com/ColeArduser/gait_tanks/blob/master/dist/game.exe)** can be downloaded and run to play the game

  or

- Clone the repository, setup your environment, install the dependencies in the [requirements.txt](https://github.com/ColeArduser/gait_tanks/blob/master/requirements.txt), and run [game.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/game.py)

## Introduction
Gait Tanks is a Python-based, tank-themed game. This project encompasses a variety of functionalities from game mechanics to audio and state management, providing an immersive gaming experience.

## Key Components

### Core Game Mechanics
- **Main Game File ([game.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/game.py))**: Initializes the main game loop, which handles updating and rendering game states. When the player moves from state to state in the app the current state is updated to show to correct one on the screen.
- **[States](https://github.com/ColeArduser/gait_tanks/blob/master/src/states/)**: Each state inherits from the main [state.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/states/state.py) class. Each has its own update and render functions which handle updating the game objects and then rendering the screen with those updated objects.
- **Audio Management ([audio.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/level/audio.py))**: Manages all audio aspects of the game, including loading and playing sound effects for different game actions like tank movements and explosions.
- **Pathfinding ([pathfinding.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/level/pathfinding.py))**: Implements A* pathfinding algorithms for AI-controlled tanks, ensuring efficient movement and navigation within the game environment.

### Objects
- **Player and Enemies**: Both [Player](https://github.com/ColeArduser/gait_tanks/blob/master/src/level/player.py) and [Enemy](https://github.com/ColeArduser/gait_tanks/blob/master/src/level/enemy.py) inherit from the main [Tank Class](https://github.com/ColeArduser/gait_tanks/blob/master/src/level/tank.py) which provides base properties that apply to both player and enemies. Both inheriting classes add the more specific functionality that only applies to them.
- **Bullet and FireEffect**: Both housed in the [bullet.py](https://github.com/ColeArduser/gait_tanks/blob/master/src/level/bullet.py) file and deal with the creation, updating, rendering, and deletion of the bullet sprites during the gameplay.

### Assets
- **Audio, Images, and Videos**: The project includes a comprehensive set of assets such as audio files, background images, sprites, and videos, crucial for the game's visual and auditory elements.

## File Structure

### Source Code (`src/`)
- `game.py`: Main game script
- `level/`: Directory for the in-game objects and assets
  - `audio.py`: Handles game audio
  - `bullet.py`: Manages bullet and fire effect behavior
  - `enemy.py`: Defines enemy behavior
  - `map.py`: Related to the game map
  - `pathfinding.py`: Pathfinding algorithm for the enemies
  - `player.py`: Manages player behavior
  - `tank.py`: Defines tank behavior
- `states/`: Directory for game states
  - `controls.py`: Controls Screen State
  - `game_over.py`: Game Over Screen State
  - `level.py`: In-Game Level State
  - `level_select.py`: Level Select Screen State
  - `pause_menu.py`: Pause Menu State
  - `state.py`: Base class for states
  - `title.py`: Title Screen State

### Assets (`src/assets/`)
- `audio/`: Audio files for the game
- `background_images/`: Images for the game
- `map/`: Individual 32x32px tiles for in-game map creation
- `sprites/`: Sprite images for game elements
- `videos/`: Video files for the game
