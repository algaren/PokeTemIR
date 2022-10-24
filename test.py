# main.py
import win32gui
import pyautogui
from library import Library


# Find Temtem and move (0,0), set width-heihgt and focus.
hwnd = win32gui.FindWindow(None, "Temtem")
win32gui.MoveWindow(hwnd, -7, 0, 1280, 720, True)
#win32gui.SetForegroundWindow(hwnd)

print(pyautogui.position())
#pyautogui.screenshot("test.png",region=(pyautogui.position().x,pyautogui.position().y,500,100))
pyautogui.screenshot("test.png",region=(754, 41,500,100))

if pyautogui.locateOnScreen('luma.png', confidence=0.9, region=(754, 41,500,100)) != None:
    print("pepe")
#battleSwap = pyautogui.screenshot(region=(548,599, 1, 1)).getpixel((0, 0))#RGB(255, 167, 50) orange swap temtem in battle

#TemTem IZQUIERDA Point(x=789, y=86) COLOR: (30, 30, 30)
#TemTem DERECHA Point(x=1038, y=121) COLOR: (30, 30, 30)




#print(pyautogui.screenshot(region=(1097,109,1,1)).getpixel((0, 0))) #DERECHA (245, 147, 56)
#RIGHT
#Point(x=1131, y=109)
#(134, 194, 73)VERDE
#(245, 147, 56) NARANJA
#(144, 79, 22) ShadowNarnaja

#print(pyautogui.screenshot(region=(851,73,1,1)).getpixel((0, 0))) #IZQ (241, 144, 55)
#LEFT
#Point(x=851, y=73)
#(132, 191, 72) VERDE
#(241, 144, 55) Naranja
