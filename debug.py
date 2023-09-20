import cv2
import numpy as np
import pyautogui
import random
import time
import platform
import subprocess
import os
import mss
def SleepDelayF():
    print("Sleep:", SleepDelay, "Seconds")
    time.sleep(SleepDelay)
def pixel_loop(x, y, r, g, b):
    pos = pyautogui.pixelMatchesColor(x, y, (r, g, b))
    while pos == False:
        print("Pixel not found, waiting")
        pos = pyautogui.pixelMatchesColor(x, y, (r, g, b))
    return True
def UpgradeBPS():
    SleepDelayF()
    Upgrade = pixel_loop(683, 683, 255, 255, 255)
    if Upgrade == True:
      print("Upgrade is found!")
      pyautogui.click(x=700, y=664)
      pyautogui.moveTo(683, 683, MouseSpeed)
      with pyautogui.hold('ctrl'):
        pyautogui.click(x=683, y=683)
      SleepDelayF()
      pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
      SleepDelayF()
    else:
        print("Upgrade: Not Found")
        pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
        SleepDelayF()
MouseSpeed = 0.2
SleepDelay = 2
LoopTimesM = 5
EVUL2 = "1"
#MergeBP = pixel_loop(1130, 807, 255, 255, 255)
#if MergeBP == True:
#  print("MergeBP is found!")
#  pyautogui.click(x=1130, y=807)
UpgradeBPS()

