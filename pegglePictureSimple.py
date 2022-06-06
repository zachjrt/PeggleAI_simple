from pickle import TRUE
import pyautogui
import time
import keyboard
from sympy import false
import win32api, win32con
import math

#Function for clicking
def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0) 

#Parameters
#Image to search
#Confidence to start with
def search(img, startConf):
    pyautogui.moveRel(0, -10)
    i = 0

    #This variable is incremented down each loop, to lower its confidence (how sure it has to be in order for it think it is a peg). 
    #Less confidence can lead to more false positives. But makes it more likely for it to find something. (doesn't have to be a 1 for 1 of exaclty peg.png)
    conf = startConf

    #The while loop here with the if peg is not None is used to help minimize crashing errors if the image is not found
    while True:
        #This is how python finds the image
        peg = pyautogui.locateOnScreen(img, confidence=conf)
        i += 1

        #How much to decrease confidence per attempt
        conf -= .01

        #If the bot finds a match, move on
        if peg is not None:
            break
        #If it fails four times, move on and let you know it can't find it
        if i > 4:
            print("missed image")
            break
    
    if i <= 4:
        pegpoint = pyautogui.center(peg)

        click(pegpoint.x, math.floor(pegpoint.y - 10))
        return True
    else:
        return False


#Sometimes it sticks a bit. Keep hitting q to stop the program
while keyboard.is_pressed('q') == False:
    search('peg.png', .85)





   