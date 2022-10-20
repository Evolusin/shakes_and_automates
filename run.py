from calendar import c
import cv2 as cv
from settings import Settings
from analize import needle_position, click_point, get_needle_and_text
import time
import pyautogui

config = Settings()


# DEBUG MOUSE POS
# print(pyautogui.position())

print("Launched")

while True:
    if config.state == "mouse_pos":
        print(pyautogui.position())

    elif config.state == "debug":
        get_needle_and_text(
            config.quest_time_top_left_x, config.quest_time_top_left_y,
            config.quest_time_w, config.quest_time_h
        )

    elif config.state == "logowanie":
        login_position = needle_position(config.login_needle)
        if login_position:
            x, y = login_position
            click_point(x, y)
            codzienne_logowanie = needle_position(config.logowanie_codzienne)
            if codzienne_logowanie:
                x, y = codzienne_logowanie
                click_point(x, y)
            print("Przechodzę do quest_check")
            config.state = "quest_check"

    elif config.state == "quest_check":
        print("Sprawdzam czy na misji")
        quest_check = needle_position(config.quest_check)
        finish_quest = needle_position(config.misja_koniec)
        if quest_check:
            print("Postać jest na misji")
            break
        elif finish_quest:
            print("Wykryłem skończoną misję")
            x, y = finish_quest
            click_point(x, y)
            lvl_up = needle_position(config.lvl_up)
            if lvl_up:
                lvl_up_continue = needle_position(config.lvl_up_continue)
                x, y = lvl_up_continue
                click_point(x, y)
                config.state = "do_karczmy"
            else:
                config.state = "do_karczmy"
        else:
            print("Nie wykryto misji")
            config.state = "do_karczmy"

    elif config.state == "do_karczmy":
        karczma_check = needle_position(config.karczma_check)
        karczma_position = needle_position(config.karczma_needle)
        if karczma_check:
            config.state = "karczma"
        else:
            if karczma_position:
                x, y = karczma_position
                click_point(x, y)
                config.state = "karczma"

    elif config.state == "karczma":
        print("Jestem w karczmie. Przechodzę do klikania npc od questów")
        click_point(config.karczma_questnpc1_x, config.karczma_questnpc1_y)
        click_point(config.karczma_questnpc2_x, config.karczma_questnpc2_y)
        click_point(config.karczma_questnpc3_x, config.karczma_questnpc3_y)
        print("Akceptuję misję")
        click_point(config.karczma_quest_x, config.karczma_quest_y)
        print("Misja zaakceptowana. Wychodzę z programu")
        break

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
