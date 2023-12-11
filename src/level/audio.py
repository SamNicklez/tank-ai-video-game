import pygame

# Initialize the pygame mixer
pygame.mixer.init()

# Dictionary to hold the sound objects
sounds = {}

# Function to load sounds
def load_sounds():
    # Load all sounds here
    sounds['tank_shoot'] = pygame.mixer.Sound('assets/audio/TankBullet.mp3')
    sounds['game_background'] = pygame.mixer.Sound('assets/audio/GameBackground.mp3')
    sounds['tank_move'] = pygame.mixer.Sound('assets/audio/TankMoving.mp3')
    sounds['tank_explosion'] = pygame.mixer.Sound('assets/audio/TankExplosion.mp3')
    sounds['round_start'] = pygame.mixer.Sound('assets/audio/RoundStart.mp3')
    
    # Set the volume for all sounds
    sounds['game_background'].set_volume(0.1)
    sounds['tank_shoot'].set_volume(0.4)
    sounds['tank_move'].set_volume(0.4)
    sounds['tank_explosion'].set_volume(0.4)
    # Add all other sounds you want to load

# Function to play a sound
def play_sound(sound_name):
    if sound_name in sounds:
        #if sounds['game_background']:
        #    sounds['game_background'].set_volume(0.2)
        sounds[sound_name].play()
    else:
        print(f"No sound loaded for {sound_name}")


# Tank Sounds 
def tank_moving_sound():
    play_sound('tank_move')
        
def stop_tank_moving_sound():
    sounds['tank_move'].stop()        
    
def tank_explosion_sound():
    play_sound('tank_explosion')
    
def tank_shoot_sound():
    play_sound('tank_shoot')

# Game Sounds
def round_start_sound():
    play_sound('round_start')

def game_background_sound():
    play_sound('game_background')

def stop_game_background_sound():
    sounds['game_background'].stop()            
    
    



