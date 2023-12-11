import pygame

# Initialize the pygame mixer
pygame.mixer.init()

# Dictionary to hold the sound objects
sounds = {}

# Function to load sounds
def load_sounds():
    sounds['gun'] = pygame.mixer.Sound('assets/audio/GunRocketStart.mp3')
    sounds['round'] = pygame.mixer.Sound('assets/audio/RoundStart.mp3')
    sounds['tank'] = pygame.mixer.Sound('assets/audio/TankMoving.mp3')
    # Add all other sounds you want to load

# Function to play a sound
def play_sound(sound_name):
    if sound_name in sounds:
        sounds[sound_name].play()
    else:
        print(f"No sound loaded for {sound_name}")

# Load all sounds at the beginning
load_sounds()

# Play a sound by passing the sound name to the function
play_sound('gun')  # This will play the GunRocketStart.mp3 sound
