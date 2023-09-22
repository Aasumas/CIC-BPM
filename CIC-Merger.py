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

MouseSpeed = 0
SleepDelay = 2
pyautogui.useImageNotFoundException(False)

def SleepDelayF():
    print("Sleep:", SleepDelay, "Seconds")
    time.sleep(SleepDelay)

def r(num, rand):
    return num + rand * random.random()

def UpgradeBPS(image, BPMCMD):
    SleepDelayF()
    Upgrade = pixel_loop(701, 688, 255, 255, 255)
    if Upgrade == True:
      print("Upgrade is found!")
      pyautogui.click(x=500, y=664)
      with pyautogui.hold('ctrl'):
        pyautogui.click(x=701, y=688)
      SleepDelayF()
      pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
      SleepDelayF()
      Main(image, BPMCMD)
    else:
        print("Upgrade: Not Found")
        pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
        SleepDelayF()
        Main(image, BPMCMD)
def pixel_loop(x, y, r, g, b):
    pos = pyautogui.pixelMatchesColor(x, y, (r, g, b))
    while pos == False:
        print("Pixel not found, waiting")
        time.sleep(SleepDelay)
        pos = pyautogui.pixelMatchesColor(x, y, (r, g, b))
    return True

def MergeBPS(image, BPMCMD):
    Merge = pixel_loop(718, 729, 251, 251, 251)
    if Merge == True:
      print("Merge is found!")
      pyautogui.click(x=718, y=729)  
      SleepDelayF()
      print("Selecting BluePrints")
      NOBP = pyautogui.pixelMatchesColor(1074, 490, (255, 0, 0))
      if NOBP == False:
          #BP = pixel_loop(1023, 486, 18, 139, 19)
          #if BP == True:
        print("BP is found!")
        pyautogui.click(x=1023, y=486)  
        print("Merging BluePrints")
        #MergeBP = pixel_loop(1130, 807, 255, 255, 255)
        MergeBP = True
        if MergeBP == True:
          print("MergeBP is found!")
          pyautogui.click(x=1130, y=807)  
          SleepDelayF()
          UpgradeBPS(image, BPMCMD)
          print("Upgrading New BluePrint")
          Main(image, BPMCMD)
          return "NBP"
      else:
        pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
        pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
        Main(image, BPMCMD)
   
def FreshBP(image):
    uloop = pyautogui.locateCenterOnScreen(image, confidence = 0.8)
    if uloop is not None:
        uloop = pyautogui.locateCenterOnScreen(image, confidence = 0.8)
        pyautogui.moveTo(uloop[0], uloop[1], MouseSpeed)
        pyautogui.leftClick()
        UpgradeBPS(image)

def BP2M(image):
    uloop = pyautogui.locateCenterOnScreen(image, confidence = 0.8)
    if uloop is not None:
        uloop = pyautogui.locateCenterOnScreen(image, confidence = 0.8)
        pyautogui.moveTo(uloop[0], uloop[1], MouseSpeed)
        pyautogui.leftClick()
        MergeBPS(image)

def Main(image, BPMCMD):
    try:
        uloop = pyautogui.locateCenterOnScreen(image, confidence = 0.8)
        if uloop is not None:
            uloop = pyautogui.locateCenterOnScreen(image, confidence = 0.8)
            pyautogui.moveTo(uloop[0], uloop[1], MouseSpeed)
            pyautogui.leftClick()
            if BPMCMD == "Upgrade":
                UpgradeBPS(image, "Upgrade")
            elif BPMCMD == "Merge":
                MergeBPS(image, "Merge")                
    except:
        print(image,"is not found.")
def BPSwitcher():
    DownArrow = pixel_loop(260, 152, 255, 255, 255)
    if DownArrow == True:
      print("DownArrow is found!")
      pyautogui.click(x=260, y=152)
      pyautogui.press('down')
      pyautogui.press('enter')

def BPSReset():
    DownArrow = pixel_loop(260, 152, 255, 255, 255)
    if DownArrow == True:
      print("DownArrow is found!")
      pyautogui.click(x=260, y=152)
      i = 1
      while i < 40:
        pyautogui.press('up')
        i += 1
    pyautogui.press('enter')
#Main Program begins Below this line!

BPSwitcher()
SleepDelayF()
i = 1
while i < 32:
    print("Loop",i,"/ 32 Start")
    Main("10-2.png", "Upgrade")
    Main("1-51.png", "Merge")
    Main("2-51.png", "Merge")
    Main("3-51.png", "Merge")
    Main("4-51.png", "Merge")
    Main("5-51.png", "Merge")
    i += 1
    print("Loop",i,"/ 32 End")
    BPSwitcher()
    SleepDelayF()
BPSReset()
