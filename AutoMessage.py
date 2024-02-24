import pyautogui
import time
time.sleep(5)
#Enter how many times you want to send a message
a=10
while a>=1:
    #Enter your message
    pyautogui.typewrite("Hello Friend")
    time.sleep(0)
    pyautogui.press("enter")
    a -=1
