from calendar import c
import cv2 as cv
from settings import Settings
from analize import needle_position, click_point
import time
import pyautogui

config = Settings()
state = 0
print(pyautogui.size())
while True:
    if state == 0:
        login_position = needle_position(config.login_needle)
        if login_position:
            x, y = login_position
            click_point(x, y)
            state = 1
            
    elif state == 1:
        karczma_position = needle_position(config.karczma_needle)
        if karczma_position:
            x,y = karczma_position
            click_point(x,y)
            state = 2
    elif state == 2:
        x = config.width/1.91
        y = config.height/1.53
        click_point(x,y)
        print("Ok czas na wybór misji")
        break
    
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break