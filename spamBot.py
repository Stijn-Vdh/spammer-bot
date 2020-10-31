import pyautogui
import time

time.sleep(5)
filename = "textToSpam"
file = open(filename, 'r')

for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
