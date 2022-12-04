from calendar import c
from os import stat
import cv2 as cv
from settings import Settings
from analize import needle_position, click_point, get_needle_and_text, needle_position_once
from states import States
import time
import pyautogui


config = Settings()
states = States()
faze = config.state
quest_done = 0
# DEBUG MOUSE POS
# print(pyautogui.position())

time.sleep(2)
print("Launched")

while True:
    if faze == "mouse_pos":
        faze = states.s_mouse_pos

    elif faze == "debug":
        print(config.karczma_questnpc1['x'])
        print(config.karczma_questnpc1['y'])
        
    elif faze == "sleep":
        print("Zasypiam na 150 sekund")
        time.sleep(150)
        faze = "logowanie"

    elif faze == "logowanie":
        print(f"Ilosc zrobionych na ten moment questow {quest_done}")
        faze = states.logowanie()

    elif faze == "quest_check":
        faze = states.quest_check()

    elif faze == "do_karczmy":
        faze = states.do_karczmy()

    elif faze == "karczma":
        quest_done=quest_done+1
        faze = states.karczma()

    elif faze == "upgrade":
        faze = states.upgrade()
    
    elif faze == "eq_sell":
        faze = states.eq_sell()

    elif faze == "energry_status":
        faze = states.energry_status()

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
