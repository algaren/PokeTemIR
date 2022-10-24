# library.py
import win32gui
import pyautogui
from random import uniform
from time import sleep

class Library:

    def holdKey(key, seconds=1.00):
        pyautogui.FAILSAFE = False        
        pyautogui.keyDown(key)
        sleep(seconds)
        pyautogui.keyUp(key)
        pyautogui.FAILSAFE = True 

    def temtemFarm():
        seconds = uniform(0.5,1.45)
        miliseconds = uniform(0.1,0.3)
        pyautogui.FAILSAFE = False
        pyautogui.keyDown("D")
        sleep(seconds)        
        pyautogui.keyUp("D")
        pyautogui.keyDown("A")
        sleep(seconds)
        pyautogui.keyUp("A")

    def temtemFarm2():       
        Library.holdKey("A",uniform(0.1,0.3))
        Library.holdKey("D",uniform(0.09,0.25))

    def temtemLeft():
        #TemTem IZQUIERDA Point(x=789, y=86) COLOR: (30, 30, 30)
        return pyautogui.screenshot(region=(789, 86, 1, 1)).getpixel((0, 0)) == (30, 30, 30)

    def temtemRight():
        #TemTem DERECHA Point(x=1038, y=121) COLOR: (30, 30, 30)
        return pyautogui.screenshot(region=(1038,121,1, 1)).getpixel((0, 0)) == (30, 30, 30)

    def twoTemtem():
        return Library.temtemLeft() and Library.temtemRight()

    def atackTemtemUP():
        Library.holdKey("1",uniform(0.1,0.2))
        sleep(uniform(0.1,1)) 
        Library.holdKey("W",uniform(0.05,0.07))
        sleep(uniform(0.1,1)) 
        Library.holdKey("F",uniform(0.1,0.2))

    def atackTemtemDown():
        Library.holdKey("1",uniform(0.1,0.2))
        sleep(uniform(0.1,1)) 
        Library.holdKey("W",uniform(0.05,0.07))
        sleep(uniform(0.1,1)) 
        Library.holdKey("F",uniform(0.1,0.2))

    def atackTemtem():
        Library.holdKey("1",uniform(0.1,0.2))
        sleep(uniform(0.1,1)) 
        Library.holdKey("F",uniform(0.1,0.2))

    def firstAtackTwoTemtem():
        Library.atackTemtemUP()
        sleep(uniform(0.1,0.5)) 
        Library.atackTemtem()

    def secondAtackTwoTemtem():
        Library.atackTemtem()
        sleep(uniform(0.2,1)) 
        Library.atackTemtemDown()

    def captureTemTem():
        if Library.twoTemtem():
            Library.holdKey("7",uniform(0.1,0.5))
            sleep(uniform(0.1,1.2)) 
            Library.holdKey("F",uniform(0.1,0.6))
            sleep(uniform(0.1,1.2)) 
            Library.holdKey("F",uniform(0.1,0.6))
        else:
            Library.holdKey("7",uniform(0.1,0.5))
            sleep(uniform(0.1,1.2)) 
            Library.holdKey("F",uniform(0.1,0.6))

    def isTemtemCaptured():
        return pyautogui.screenshot(region=(491,325,1, 1)).getpixel((0, 0)) == (27, 209, 211) and pyautogui.screenshot(region=(613,434,1, 1)).getpixel((0, 0)) == (255, 255, 255)

    def leaveTemtem():
        Library.holdKey("D",uniform(0.02,0.06))
        sleep(uniform(0.1,1.2)) 
        Library.holdKey("F",uniform(0.1,0.2))
        sleep(uniform(0.1,1.2)) 
        Library.holdKey("F",uniform(0.1,0.2))

    def saveTemtem():
        Library.holdKey("F",uniform(0.1,0.2))
        sleep(uniform(0.1,1.2)) 
        Library.holdKey("F",uniform(0.1,0.2))

    def Shop(cards):
        Library.holdKey("A",uniform(1,2))
        sleep(uniform(0.1,0.5))
        Library.holdKey("F",uniform(0.05,0.09))
        sleep(uniform(0.1,0.5))
        if pyautogui.screenshot(region=(937,393,1, 1)).getpixel((0, 0)) == (42, 42, 42) and pyautogui.screenshot(region=(869,602,1, 1)).getpixel((0, 0)) == (255, 255, 255):
            Library.holdKey("F",uniform(0.05,0.09))
            sleep(uniform(0.1,0.5))
            Library.holdKey("S",uniform(0.02,0.07))
            sleep(uniform(0.01,0.1))
            Library.holdKey("S",uniform(0.02,0.07))
            sleep(uniform(0.01,0.1))
            Library.holdKey("S",uniform(0.02,0.07))
            sleep(uniform(0.01,0.1))
            Library.holdKey("F",uniform(0.05,0.09))
            sleep(uniform(0.1,0.2))
            Library.holdKey("S",uniform(0.02,0.07))
            sleep(uniform(0.01,0.1))
            Library.holdKey("S",uniform(0.02,0.07))
            sleep(uniform(0.01,0.1))
            Library.holdKey("F",uniform(0.05,0.09))
            sleep(uniform(0.1,0.5))
            pyautogui.press("esc")
            return 100
        return cards