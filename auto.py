import pyautogui
import time

# for x in range(0,5):
#     print(pyautogui.position())


while True:

    t_end = time.time() + 14
    while time.time() < t_end:
        frToast = pyautogui.locateOnScreen('frToast.JPG', confidence=0.53)
        later = pyautogui.locateOnScreen('later.JPG', confidence=0.65)
        x = pyautogui.locateOnScreen('x.JPG', confidence=0.70)
        later2 = pyautogui.locateOnScreen('later2.JPG', confidence=0.5)
        # accept = pyautogui.locateOnScreen('accept.JPG', confidence=0.7)
        # Ok = pyautogui.locateOnScreen('Ok.JPG', confidence=0.6)
        if frToast is not None:
            pyautogui.click(frToast[0] + 10, frToast[1] + 10)
        elif later is not None or later2 is not None:
            if later is not None:
                pyautogui.click(later[0], later[1])
            else:
                pyautogui.click(later2[0], later2[1])
        elif x is not None:
            pyautogui.click(x[0], x[1])
        pyautogui.click(x=1524, y=785)
        time.sleep(1)

    t_end = time.time() + 14
    while time.time() < t_end:
        frToast = pyautogui.locateOnScreen('frToast.JPG', confidence=0.53)
        later = pyautogui.locateOnScreen('later.JPG', confidence=0.65)
        x = pyautogui.locateOnScreen('x.JPG', confidence=0.70)
        later2 = pyautogui.locateOnScreen('later2.JPG', confidence=0.5)
        # accept = pyautogui.locateOnScreen('accept.JPG', confidence=0.7)
        # Ok = pyautogui.locateOnScreen('Ok.JPG', confidence=0.6)
        if frToast is not None:
            pyautogui.click(frToast[0] + 10, frToast[1] + 10)
            time.sleep(1.5)
        elif later is not None or later2 is not None:
            if later is not None:
                pyautogui.click(later[0], later[1])
            else:
                pyautogui.click(later2[0], later2[1])
        elif x is not None:
            pyautogui.click(x[0], x[1])

        pyautogui.click(x=1542, y=600)
        time.sleep(1)

    t_end = time.time() + 14
    while time.time() < t_end:
        frToast = pyautogui.locateOnScreen('frToast.JPG', confidence=0.53)
        later = pyautogui.locateOnScreen('later.JPG', confidence=0.65)
        x = pyautogui.locateOnScreen('x.JPG', confidence=0.70)
        later2 = pyautogui.locateOnScreen('later2.JPG', confidence=0.5)
        # accept = pyautogui.locateOnScreen('accept.JPG', confidence=0.7)
        # Ok = pyautogui.locateOnScreen('Ok.JPG', confidence=0.6)
        if frToast is not None:
            pyautogui.click(frToast[0] + 10, frToast[1] + 10)
        elif later is not None or later2 is not None:
            if later is not None:
                pyautogui.click(later[0], later[1])
            else:
                pyautogui.click(later2[0], later2[1])
        elif x is not None:
            pyautogui.click(x[0], x[1])
        pyautogui.click(x=1650, y=650)
        time.sleep(1)

    t_end = time.time() + 14
    while time.time() < t_end:
        frToast = pyautogui.locateOnScreen('frToast.JPG', confidence=0.53)
        later = pyautogui.locateOnScreen('later.JPG', confidence=0.65)
        x = pyautogui.locateOnScreen('x.JPG', confidence=0.70)
        later2 = pyautogui.locateOnScreen('later2.JPG', confidence=0.5)
        # accept = pyautogui.locateOnScreen('accept.JPG', confidence=0.7)
        # Ok = pyautogui.locateOnScreen('Ok.JPG', confidence=0.6)
        if frToast is not None:
            pyautogui.click(frToast[0] + 10, frToast[1] + 10)
        elif later is not None or later2 is not None:
            if later is not None:
                pyautogui.click(later[0], later[1])
            else:
                pyautogui.click(later2[0], later2[1])
        elif x is not None:
            pyautogui.click(x[0], x[1])
        pyautogui.click(x=1770, y=749)
        time.sleep(1)

    t_end = time.time() + 14
    while time.time() < t_end:
        frToast = pyautogui.locateOnScreen('frToast.JPG', confidence=0.53)
        later = pyautogui.locateOnScreen('later.JPG', confidence=0.65)
        x = pyautogui.locateOnScreen('x.JPG', confidence=0.70)
        later2 = pyautogui.locateOnScreen('later2.JPG', confidence=0.5)
        # accept = pyautogui.locateOnScreen('accept.JPG', confidence=0.7)
        # Ok = pyautogui.locateOnScreen('Ok.JPG', confidence=0.6)
        if frToast is not None:
            pyautogui.click(frToast[0] + 10, frToast[1] + 10)
        elif later is not None or later2 is not None:
            if later is not None:
                pyautogui.click(later[0], later[1])
            else:
                pyautogui.click(later2[0], later2[1])
        elif x is not None:
            pyautogui.click(x[0], x[1])
        pyautogui.click(x=1651, y=962)
        time.sleep(1)