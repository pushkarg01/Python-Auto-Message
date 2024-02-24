import pyautogui
import time
time.sleep(5)
a=10
while a>=1:
    pyautogui.typewrite("Hello Friend")
    time.sleep(0)
    pyautogui.press("enter")
    a -=1