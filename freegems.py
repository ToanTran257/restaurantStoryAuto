import pyautogui
import time

while True:
    x = pyautogui.locateOnScreen('x.JPG', confidence=0.70)
    accept = pyautogui.locateOnScreen('accept.JPG', confidence=0.7)
    later = pyautogui.locateOnScreen('later.JPG', confidence=0.7)
    Ok = pyautogui.locateOnScreen('Ok.JPG', confidence=0.6)

    if x is None and accept is None and later is None and Ok is None:

    else:
        if x is not None:
            pyautogui.click(x[0], x[1])
        elif accept is not None:
            pyautogui.click(accept[0] + 10, accept[1] + 5)
        elif Ok is not None:
            pyautogui.click(Ok[0] + 5, Ok[1] + 5)
        else:
            pyautogui.click(later[0], later[1])