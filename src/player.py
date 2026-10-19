# Standard Libraries
import sys
import os
import time

# Add the local libs directory to the top of the search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'libs')))

# Import libraries from libs folder
from playsound3 import playsound

# Function to clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Runs only if file is executed
if __name__ == '__main__':
    file = os.path.join('misc', 'Counting Crows - Accidentally In Love (Lyric Video).mp3')
    gif_filename = os.path.join('misc', 'Accidently Falling In love.gif')

    # Loops music
    while (True):
        clear_terminal()
        print("Use 'Ctrl + C' to end music")

        # Plays MP3 File while checking for raised exceptions
        try:
            playsound(file)
        except:
            print("Music did not play due to unsupported audio backends.")
            print("May occur on systems using WSL.")
            break

        time.sleep(1)  