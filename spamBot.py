import pyautogui
import time

time.sleep(5)
filename = "textToSpam"
file = open(filename, 'r')

for line in file:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
