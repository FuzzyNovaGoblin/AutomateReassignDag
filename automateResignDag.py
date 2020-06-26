import pyautogui
import time
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

NEEDED_COUNT = 50
assignCount = 0


for lap in range(10):
    # pyautogui.click(x=2597, y=1450)
    pyautogui.click(x=2597-1920, y=1450-1080)
    time.sleep(2)
    butt = pyautogui.locateOnScreen('fileButt.png')
    if butt != None:
        buttPoint = pyautogui.center(butt)
        pyautogui.rightClick(x=buttPoint.x, y=buttPoint.y)

    butt = pyautogui.locateOnScreen('rFromWorkFlow.png')
    if butt != None:
        print("removed")
        buttPoint = pyautogui.center(butt)
        pyautogui.click(x=buttPoint.x, y=buttPoint.y)
        # time.sleep(0.4)
        pyautogui.click(x=2735-1920, y=1728-1080)
    # time.sleep(0.2)
    pyautogui.rightClick(x=2597-1920, y=1450-1080)
    # time.sleep(0.4)
    pyautogui.rightClick(x=2597-1920, y=1450-1080)
    # time.sleep(0.4)
    pyautogui.moveRel(15, 15)
    pyautogui.click()
    time.sleep(1)
    print("lookint for aaprover")
    butt = pyautogui.locateOnScreen('aAprover1.png')
    if butt != None:
        buttPoint = pyautogui.center(butt)
        pyautogui.click(x=buttPoint.x, y=buttPoint.y)
        pyautogui.click(x=2640 - 1920, y=1994 - 1080)
        assignCount += 1
    else:
        butt = pyautogui.locateOnScreen('aAprover1.png')
        if butt != None:
            buttPoint = pyautogui.center(butt)
            pyautogui.click(x=buttPoint.x, y=buttPoint.y)
            pyautogui.click(x=2640 - 1920, y=1994 - 1080)
            assignCount += 1
        else:
            pyautogui.click(x=795, y=911)
            # raise(Exception)
    if assignCount >= NEEDED_COUNT:
        break
    time.sleep(2)

pyautogui.hotkey('alt', 'w')
