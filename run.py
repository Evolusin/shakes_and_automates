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

# DEBUG MOUSE POS
# print(pyautogui.position())

print("Launched")

while True:
    if faze == "mouse_pos":
        faze = states.s_mouse_pos

    elif faze == "debug":
        # get_needle_and_text(
        #     config.quest_time_top_left_x,
        #     config.quest_time_top_left_y,
        #     config.quest_time_w,
        #     config.quest_time_h,
        # )
        print(config.karczma_questnpc1['x'])
        print(config.karczma_questnpc1['y'])
        
    elif faze == "exit":
        break

    elif faze == "logowanie":
        faze = states.logowanie()

    elif faze == "quest_check":
        faze = states.quest_check()

    elif faze == "do_karczmy":
        faze = states.do_karczmy()

    elif faze == "karczma":
        faze = states.karczma()

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
