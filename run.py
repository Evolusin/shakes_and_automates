from calendar import c
import cv2 as cv
from settings import Settings
from analize import needle_position, click_point, get_needle_and_text
import time
import mss
import pyautogui

config = Settings()
state = "debug"

# DEBUG MOUSE POS
# print(pyautogui.position())

print("Launched")

while True:
    if state == "mouse_pos":
        print(pyautogui.position())

    elif state == "debug":
        # get_needle_and_text(
        #     config.quest_time_top_left_x, config.quest_time_top_left_y,
        #     config.quest_time_w, config.quest_time_h
        # )
        with mss.mss() as sct:
            img_needle_position = {"top":config.quest_time_top_left_x, "left":config.quest_time_top_left_y,"width":config.quest_time_w, "height":config.quest_time_h}
            output = "sct-{top}x{left}_{width}x{height}.png".format(**img_needle_position)
            sctgas=sct.grab(img_needle_position)
            mss.tools.to_png(sctgas.rgb, sctgas.size, output=output)
            print(output)

    if state == "logowanie":
        login_position = needle_position(config.login_needle)
        if login_position:
            x, y = login_position
            click_point(x, y)
            codzienne_logowanie = needle_position(config.logowanie_codzienne)
            if codzienne_logowanie:
                x, y = codzienne_logowanie
                click_point(x, y)
            print("Przechodzę do quest_check")
            state = "quest_check"

    elif state == "quest_check":
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
                state = "do_karczmy"
            else:
                state = "do_karczmy"
        else:
            print("Nie wykryto misji")
            state = "do_karczmy"

    elif state == "do_karczmy":
        karczma_check = needle_position(config.karczma_check)
        karczma_position = needle_position(config.karczma_needle)
        if karczma_check:
            state = "karczma"
        else:
            if karczma_position:
                x, y = karczma_position
                click_point(x, y)
                state = "karczma"

    elif state == "karczma":
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
