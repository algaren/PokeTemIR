# main.py
import win32gui
import pyautogui
from library import Library


# Find Temtem and move (0,0), set width-heihgt and focus.
hwnd = win32gui.FindWindow(None, "Temtem")
win32gui.MoveWindow(hwnd, -7, 0, 1280, 720, True)
win32gui.SetForegroundWindow(hwnd)
pepe = True
attackCount = 0
temtemCards = 40
temtemts = 0
isLuma = False
#Library.Shop()
while pepe:
    #Get Map pixels so we know we are idle.
    pixMap1 = pyautogui.screenshot(region=(1171, 52, 1, 1)).getpixel((0, 0))#RGB(60, 232, 234) blue pixMap pixel Arriba
    pixMap2 = pyautogui.screenshot(region=(1088,141, 1, 1)).getpixel((0, 0))#RGB(60, 232, 234) blue pixMap pixel Izquierda
    pixMap3 = pyautogui.screenshot(region=(1165,196, 1, 1)).getpixel((0, 0))#RGB(60, 232, 234) blue pixMap pixel Abajo
    pixMap4 = pyautogui.screenshot(region=(1235,133, 1, 1)).getpixel((0, 0))#RGB(60, 232, 234) blue pixMap pixel Derecha

    if pixMap1 == pixMap2 ==  pixMap3 == pixMap4 == (60, 232, 234):
        while (60, 232, 234) == pyautogui.screenshot(region=(1171,52, 1, 1)).getpixel((0, 0)):
            Library.temtemFarm2()
            attackCount = 0
            if temtemCards < 50:
               temtemCards = Library.Shop(temtemCards)

    else:
        battleSwap = pyautogui.screenshot(region=(548,599, 1, 1)).getpixel((0, 0))#RGB(255, 167, 50) orange swap temtem in battle
        battleBag = pyautogui.screenshot(region=(615,660, 1, 1)).getpixel((0, 0))#RGB(34, 253, 255) blue bag in battle
        if battleBag == (34, 253, 255) and battleSwap == (255, 167, 50):            
            print("battleready")

            if attackCount==0 and pyautogui.locateOnScreen('luma.png', confidence=0.9, region=(754, 41,500,100)) != None:
                attackCount=3
                isLuma = True
            else:
                isLuma = False

            if Library.twoTemtem():
                if attackCount==0: 
                    Library.firstAtackTwoTemtem()
                    attackCount=1
                elif attackCount==1:
                    Library.secondAtackTwoTemtem()
                    attackCount=3
            else:
                if attackCount <3:
                    Library.atackTemtem()
                    attackCount = attackCount+1
            
            if attackCount>=3:
                Library.captureTemTem()
                temtemCards = temtemCards-1
                print(temtemCards)
        
        if Library.isTemtemCaptured():
            if isLuma == False:
                Library.leaveTemtem()
            else:
                Library.saveTemtem()
            temtemts = temtemts+1
            print(temtemts)

                



#bbox = win32gui.GetWindowRect(hwnd)
#img = ImageGrab.grab(bbox)
print(pyautogui.position())
#Point(x=1171, y=52) MAP BORDER
battleSwap = pyautogui.screenshot(region=(548,599, 1, 1)).getpixel((0, 0))#RGB(255, 167, 50) orange swap temtem in battle
battleBag = pyautogui.screenshot(region=(615,660, 1, 1)).getpixel((0, 0))#RGB(34, 253, 255) blue bag in battle
print(battleSwap.getpixel((0, 0)))
print(battleBag.getpixel((0, 0)))