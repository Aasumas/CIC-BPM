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
        time.sleep(1)
        pos = pyautogui.pixelMatchesColor(x, y, (r, g, b))
    return True
def BPSwitcher():
    DownArrow = pixel_loop(260, 152, 255, 255, 255)
    if DownArrow == True:
      print("DownArrow is found!")
      pyautogui.click(x=260, y=152)
      pyautogui.press('down')
      pyautogui.press('enter')
def BPSOpener():
    NoToken = pyautogui.pixelMatchesColor(1265, 368, (0, 34, 34))
    NoRoom = pyautogui.pixelMatchesColor(1773, 691, (101, 155, 0))
    if NoToken == True:
      print("No Token is found!")
      pyautogui.click(x=1300, y=370)
    while NoToken == False and NoRoom == False:
        GetANewPack = pixel_loop(815, 741, 245, 245, 245)
        if GetANewPack == True:
            pyautogui.click(x=830, y=730)
        RevealALL = pixel_loop(698, 735, 255, 255, 255)
        if RevealALL == True:
            pyautogui.click(x=698, y=735)
        time.sleep(10)
        NoToken = pyautogui.pixelMatchesColor(1265, 368, (0, 34, 34))
        NoRoom = pyautogui.pixelMatchesColor(1773, 691, (101, 155, 0))
#Main Code
#BPOpener
#BPSSelecter
BPSOpener()
