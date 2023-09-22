#AutoBluePrintMerger V2 for Crafting Idle Click by Aasum.
#A few places use absolute pixel values which must be changed.
#Currently does a flat 51.
import cv2
import numpy as np
import pyautogui
import random
import time
import platform
import subprocess
import os
import mss

#260 152 255 255 255
def pixel_loop(x, y, r, g, b):
    pos = pyautogui.pixelMatchesColor(x, y, (r, g, b))
    while pos == False:
        print("Pixel not found, waiting")
        time.sleep(SleepDelay)
        pos = pyautogui.pixelMatchesColor(x, y, (r, g, b))
    return True

def BPSwitcher():
    DownArrow = pixel_loop(260, 152, 255, 255, 255)
    if DownArrow == True:
      print("DownArrow is found!")
      pyautogui.click(x=260, y=152)
      pyautogui.press('down')
      pyautogui.press('enter')

#Main Code
BPSwitcher()
