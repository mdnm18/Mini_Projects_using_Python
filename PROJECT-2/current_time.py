import time
import os
import keyboard  # Requires 'keyboard' package, install via 'pip install keyboard'

def stop_watch():
    
    hours, minutes, seconds = 0, 0, 0
    laps = []
    paused = False
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{hours:02d} : {minutes:02d} : {seconds:02d}")
        print("Press 'L' to record a lap, 'P' to pause/resume, 'Q' to quit.")
        if not paused:
            time.sleep(1)
            seconds += 1
            if seconds == 60:
                seconds = 0
                minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
            if hours == 24:
                hours, minutes, seconds = 0, 0, 0
        if keyboard.is_pressed('l'):
            laps.append(f"{hours:02d} : {minutes:02d} : {seconds:02d}")
        if keyboard.is_pressed('p'):
            paused = not paused
            time.sleep(1)  # Prevent immediate toggling
        if keyboard.is_pressed('q'):
            break

    print("Laps recorded:")
    for lap in laps:
        print(lap)

stop_watch()
