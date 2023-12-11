import pygame

# Initialize the pygame mixer
pygame.mixer.init()

# Dictionary to hold the sound objects
sounds = {}

# Function to load sounds
def load_sounds():
    sounds['tank_shoot'] = pygame.mixer.Sound('src/assets/audio/TankBullet.mp3')
    sounds['game_background'] = pygame.mixer.Sound('src/assets/audio/GameBackground.mp3')
    sounds['tank_move'] = pygame.mixer.Sound('src/assets/audio/TankMoving.mp3')
    # Add all other sounds you want to load

# Function to play a sound
def play_sound(sound_name):
    if sound_name in sounds:
        sounds[sound_name].play()
        print("In here")
    else:
        print(f"No sound loaded for {sound_name}")

# Load all sounds at the beginning
load_sounds()

# Play a sound by passing the sound name to the function
play_sound('tank_shoot')  # This will play the GunRocketStart.mp3 sound
