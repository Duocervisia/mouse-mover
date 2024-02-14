import pyautogui
import time
import sys
import keyboard

counter = 0

while True: #Infinite loop
    pyautogui.moveTo(100, 150 + counter)
    if(counter%2 == 0):
        pyautogui.moveTo(100, 250)
    else:
        pyautogui.moveTo(100, 350)
    pyautogui.click()
    counter += 1
    try:
        if keyboard.is_pressed('ENTER'):
            print("you pressed Enter, so printing the list..")
            break
    except:
        break
    time.sleep(10) #Wait 600s (10 min) before re-entering the cycle

