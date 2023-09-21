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

is_retina = False
MouseSpeed = 0.2
SleepDelay = 2
LoopTimesM = 5
EVUL2 = "1"
Col = 25
Row = 12

def SleepDelayF():
    print("Sleep:", SleepDelay, "Seconds")
    time.sleep(SleepDelay)

def r(num, rand):
    return num + rand * random.random()

def imagesearch_count(image, precision=.95):
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


##def imagesearch(image, precision=.95):
##    with mss.mss() as sct:
##        im = sct.grab(sct.monitors[0])
##        if is_retina:
##            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
##        # im.save('testarea.png') useful for debugging purposes, this will save the captured region as "testarea.png"
##        img_rgb = np.array(im)
##        #img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
##        template = cv2.imread(image, 0)
##        if template is None:
##            raise FileNotFoundError('Image file not found: {}'.format(image))
##        template.shape[::-1]
##
##        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
##        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
##        if max_val < precision:
##            return [-1, -1]
##        return max_loc
def imagesearch(image, precision=0.95):
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
    
def click_image(image, pos, action, Timestamp, offset=5):
    img = cv2.imread(image)
    if img is None:
        raise FileNotFoundError('Image file not found: {}'.format(image))
    height, width, channels = img.shape
    pyautogui.moveTo(pos[0] + r(width / 2, offset), pos[1] + r(height / 2, offset), Timestamp)
    pyautogui.click(button=action)

def UpgradeBPS(image, BPMCMD):
    SleepDelayF()
    Upgrade = pixel_loop(701, 688, 255, 255, 255)
    if Upgrade == True:
      print("Upgrade is found!")
      pyautogui.click(x=600, y=664)
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
##def Main(image, BPMCMD):
##    pos = imagesearch(image)
##    if pos[0] != -1:
##        print(image, "Found at:", pos[0], pos[1])
##        print("Moving Mouse to", pos[0], pos[1])
##        time.sleep(SleepDelay)
##        print("Left Click Mouse at", pos[0], pos[1])
##        click_image(image, pos, "left", MouseSpeed, offset=5)
##        if BPMCMD == "Upgrade":
##            UpgradeBPS()
##        elif BPMCMD == "Merge":
##            MergeBPS()

def EVUL(image): #Caller for main
    EVUL = imagesearch_count(image)
    EVUL.sort(reverse=True) #Reverse the list, start from bottom right. To not messup the XY of other items.
    for x in EVUL:
        pyautogui.moveTo(x)
        SleepDelayF()
        pyautogui.click()
        NBPF = MergeBPS(image)
        if NBPF == "NBP":
            EVUL2(image)

def EVUL2(image):
    NBPF = 1
    EVUL(image)
    
##def FreshBP(image,precision=0.8 ):
##    uloop = imagesearch(image,precision)
##    uloop_count = 0
##    while uloop[0] != -1:
##        Main(image,"Upgrade")
##        uloop = imagesearch(image,precision)
##        uloop_count += 1
##        print("We are on loop", uloop_count)
##def FreshBP(image, precision=.9): #Caller for main
##    EVUL = imagesearch_count(image, precision=.9)
##    EVUL.sort(reverse=True) #Reverse the list, start from bottom right. To not messup the XY of other items.
##    for x in EVUL:
##        pyautogui.click(x)
##        NBPF = UpgradeBPS()
##        if NBPF == "NBP":
##            EVUL2(image)
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
    uloop = pyautogui.locateCenterOnScreen(image, confidence = 0.8)
    if uloop is not None:
        uloop = pyautogui.locateCenterOnScreen(image, confidence = 0.8)
        pyautogui.moveTo(uloop[0], uloop[1], MouseSpeed)
        pyautogui.leftClick()
        if BPMCMD == "Upgrade":
            UpgradeBPS(image, "Upgrade")
        elif BPMCMD == "Merge":
            MergeBPS(image, "Merge")                
#Main Program begins Below this line!

i = 1
while i < LoopTimesM:
    print("Loop",i,"/",LoopTimesM ,"Start")
    Main("10-2.png", "Upgrade")
    Main("1-51.png", "Merge")
    Main("2-51.png", "Merge")
    Main("3-51.png", "Merge")
    Main("4-51.png", "Merge")
    Main("5-51.png", "Merge")
    i += 1
    print("Loop",i,"/",LoopTimesM,"End")


##i = 1
##while i < LoopTimesM:
##    print("Loop", i , "Start")
##    NBPF = 1
##    EVUL("1-51.png")
##    EVUL("2-51.png")
##    EVUL("3-51.png")
##    EVUL("4-51.png")
##    EVUL("5-51.png")
##    i += 1
##    print("Loop", i, "End")

