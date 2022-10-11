from calendar import c
import cv2 as cv
from settings import Settings
from analize import needle_position, click_point
import time
import pyautogui

config = Settings()
state = 0
# DEBUG MOUSE POS
# print(pyautogui.position())
while True:
    # DEBUG MOUSE POS
    print(pyautogui.position()) 
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
        print("Jestem w karczmie. Przechodzę do klikania npc od questów")
        click_point(config.karczma_questnpc1_x,config.karczma_questnpc1_y)
        click_point(config.karczma_questnpc2_x,config.karczma_questnpc2_y)
        print("Akceptuję misję")
        click_point(config.karczma_quest_x,config.karczma_quest_y)
        break
    
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break