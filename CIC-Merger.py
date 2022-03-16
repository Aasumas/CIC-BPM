#AutoBluePrintMerger for Crafting Idle Click by Aasum.
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
is_retina = False
def r(num, rand):
    return num + rand * random.random()

def imagesearch_count(image, precision=0.8):
    img_rgb = pyautogui.screenshot()
    filename = "Result-"  + image 
    if is_retina:
        img_rgb.thumbnail((round(img_rgb.size[0] * 0.5), round(img_rgb.size[1] * 0.5)))
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= precision)
    offset = 5
    count = []
    for pt in zip(*loc[::-1]):  # Swap columns and rows
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        #count .append((pt[0], pt[1])) # Orignal top left of image
        count .append((pt[0] + r(w / 2, offset), pt[1] + r(h / 2, offset))) # Modified for center of image with a tad of random
        cv2.imwrite(filename , img_rgb) # Uncomment to write output image with boxes drawn around occurrences
    return count

def imagesearch(image, precision=0.9):
    with mss.mss() as sct:
        im = sct.grab(sct.monitors[0])
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
        # im.save('testarea.png') useful for debugging purposes, this will save the captured region as "testarea.png"
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        if template is None:
            raise FileNotFoundError('Image file not found: {}'.format(image))
        template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val < precision:
            return [-1, -1]
        return max_loc
    
def click_image(image, pos, action, timestamp, offset=5):
    img = cv2.imread(image)
    if img is None:
        raise FileNotFoundError('Image file not found: {}'.format(image))
    height, width, channels = img.shape
    pyautogui.moveTo(pos[0] + r(width / 2, offset), pos[1] + r(height / 2, offset),
                     timestamp)
    pyautogui.click(button=action)

def UpgradeBPS():
    pos1 = imagesearch("Upgrade.png")
    if pos1[0] != -1:
        print("Upgrade Found", pos1[0], pos1[1])
        posy = pos1[1] - 100
        pyautogui.moveTo(pos1[0], posy) #Activate the window
        pyautogui.click()  # click the mouse
        pyautogui.keyDown('ctrl')  # hold down the control key
        click_image("Upgrade.png", pos1, "left", 0.1) #change this to add more clicks if you don't want to do flat 51. Each Click is +50        
        print("Clicking Upgrade ", pos1[0], pos1[1])
        pyautogui.keyUp('ctrl') #release control key
        pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
        time.sleep(1)
    else:
        print("Upgrade: Not Found")
        pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
        time.sleep(1)

def MergeBPS():
##    Lock = imagesearch("Lock.png")
##    if Lock[0] != -1:
##        print("Lock Found: Exiting")
##        pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
##    else:
    pos1 = imagesearch("Merge.png")
    if pos1[0] != -1:
        print("Merge Button", pos1[0], pos1[1])
        posy = pos1[1] - 100
        pyautogui.moveTo(pos1[0], posy) #Activate the window
        pyautogui.click()  # click the mouse
        click_image("Merge.png", pos1, "left", 0.1)
        time.sleep(2)
    NoBPS = imagesearch("NoBluePrints.png")
    if NoBPS[0] != -1:
        print("No BluePrints to Merge, Exiting")
        pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
        pyautogui.press('esc')     # press the ESC keyescape, back to main BluePrint Screen
        time.sleep(1)
    else:     
        time.sleep(1)
        print("Selecting BluePrints", pos1[0], pos1[1])
        pyautogui.moveTo(1004, 491) # change this to the pixel area the blueprints are for blueprint B
        time.sleep(1)
        pyautogui.click()  # click the mouse
        print("Merging BluePrints")
        pos2 = imagesearch("MergeBluePrints.png")
        if pos2[0] != -1:
            click_image("MergeBluePrints.png", pos2, "left", 0.1)       
            time.sleep(5)
            UpgradeBPS()
            print("Upgrading New BluePrint")


#Main Program begins Below this line!

EVUL = imagesearch_count("E1U01.png") # Evolution 1, Upgrade 1 = Fresh BP
EVUL.reverse() #Reverse the list, start from bottom right. To not messup the XY of other items.
for x in EVUL:
    pyautogui.moveTo(x)
    time.sleep(1)
    pyautogui.click()
    UpgradeBPS()

EVUL2 = imagesearch_count("E1U51.png") # Evolution 1, Upgrade 51 BP to Merge,Upgrade
EVUL2.reverse() #Reverse the list, start from bottom right. To not messup the XY of other items.
for x in EVUL2:
    pyautogui.moveTo(x)
    time.sleep(1)
    pyautogui.click()
    MergeBPS()

EVUL3 = imagesearch_count("E2U51-N.png") # Evolution 2, Upgrade 51 BP to Merge,Upgrade
EVUL3.reverse() #Reverse the list, start from bottom right. To not messup the XY of other items.
for x in EVUL3:
    pyautogui.moveTo(x)
    time.sleep(1)
    pyautogui.click()
    MergeBPS()

EVUL4 = imagesearch_count("E3U51.png") # Evolution 3, Upgrade 51 BP to Merge,Upgrade
EVUL4.reverse() #Reverse the list, start from bottom right. To not messup the XY of other items.
for x in EVUL4:
    pyautogui.moveTo(x)
    time.sleep(1)
    pyautogui.click()
    MergeBPS()

EVUL5 = imagesearch_count("E4U51.png") # Evolution 3, Upgrade 51 BP to Merge,Upgrade
EVUL5.reverse() #Reverse the list, start from bottom right. To not messup the XY of other items.
for x in EVUL5:
    pyautogui.moveTo(x)
    time.sleep(1)
    pyautogui.click()
    MergeBPS()
