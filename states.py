from calendar import c
import cv2 as cv
from settings import Settings
from analize import (
    needle_position,
    click_point,
    get_needle_and_text,
    needle_position_once,
)
import time
import pyautogui

config = Settings()


class States:
    def s_debug(self):
        """Enters debug mode in infinte loop

        Returns:
            string: debug
        """
        print("Debug mode")
        return "debug"

    def s_mouse_pos(self):
        """Gives mouse location in infnite loop

        Returns:
            string: mouse_pos
        """
        print(pyautogui.position())
        return "mouse_pos"

    def logowanie(self):
        """Checks if user is already logged in the game

        Returns:
            string: next state
        """
        login_position = needle_position_once(config.login_needle)
        if login_position:
            x, y = login_position
            click_point(x, y)
            codzienne_logowanie = needle_position_once(
                config.logowanie_codzienne
            )
            if codzienne_logowanie:
                x, y = codzienne_logowanie
                click_point(x, y)
            print("Przechodzę do quest_check")
            return "quest_check"
        else:
            print("Jesteś już zalogowany. Przechodzę do quest_check")
            return "quest_check"

    def quest_check(self):
        """Checks if char is on the mission. If yes then returns exit state.
        Otherwise returns do_karczmy state

        Returns:
            string: next state
        """
        print("Sprawdzam czy na misji")
        quest_check = needle_position_once(config.quest_check)
        finish_quest = needle_position_once(config.misja_koniec)
        if quest_check:
            print("Postać jest na misji")
            return "exit"
        elif finish_quest:
            print("Wykryłem skończoną misję")
            x, y = finish_quest
            click_point(x, y)
            lvl_up = needle_position(config.lvl_up)
            if lvl_up:
                lvl_up_continue = needle_position(config.lvl_up_continue)
                x, y = lvl_up_continue
                click_point(x, y)
                return "do_karczmy"
            else:
                return "do_karczmy"
        else:
            print("Nie wykryto misji")
            return "do_karczmy"

    def do_karczmy(self):
        """Check's if its already in quest hub. If yes then returns
        karczma state. Otherwise click's quest hub locations

        Returns:
            string: next state
        """
        karczma_check = needle_position_once(config.karczma_check)
        karczma_position = needle_position_once(config.karczma_needle)
        if karczma_check:
            return "karczma"
        else:
            if karczma_position:
                x, y = karczma_position
                click_point(x, y)
                return "karczma"

    def karczma(self):
        """Clickes in order on NPC localistions. If NPC is found then 
        accepts quest and returns exit state

        Returns:
            string: next state
        """
        print("Jestem w karczmie. Przechodzę do klikania npc od questów")
        click_point(
            config.karczma_questnpc1["x"], config.karczma_questnpc1["y"]
        )
        karczma_quest_accept = needle_position_once(
            config.karczma_quest_accept
        )
        if not karczma_quest_accept:
            click_point(
                config.karczma_questnpc2["x"], config.karczma_questnpc2["y"]
            )
            karczma_quest_accept = needle_position_once(
                config.karczma_quest_accept
            )
            if not karczma_quest_accept:
                click_point(
                    config.karczma_questnpc3["x"],
                    config.karczma_questnpc3["y"],
                )
        print("Akceptuję misję")
        click_point(config.karczma_quest["x"], config.karczma_quest["y"])
        print("Misja zaakceptowana. Wychodzę z programu")
        return "exit"
