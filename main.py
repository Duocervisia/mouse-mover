import pyautogui
import time
import sys
import keyboard

counter = 100

while True: #Infinite loop
    pyautogui.moveTo(100, 150 + counter)
    counter = -counter
    try:
        if keyboard.is_pressed('ENTER'):
            print("you pressed Enter, so printing the list..")
            break
    except:
        break
    time.sleep(300) #Wait 600s (10 min) before re-entering the cycle

