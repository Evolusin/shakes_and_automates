from calendar import c
import cv2 as cv
from settings import Settings
from analize import (
    click_point_right,
    needle_position,
    click_point,
    get_needle_and_text,
    needle_position_once,
    refresh_site,
)
import time
import pyautogui
from functions import Helper


class States:
    gold_ammount = 0

    def __init__(self) -> None:
        self.config = Settings()
        self.help = Helper()
        pass

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
        login_position = needle_position_once(self.config.login_needle)
        if login_position:
            x, y = login_position
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
        quest_check = needle_position_once(self.config.quest_check)
        finish_quest = needle_position_once(self.config.misja_koniec)
        if quest_check:
            print("Postać jest na misji")
            return "exit"
        elif finish_quest:
            print("Wykryłem skończoną misję")
            x, y = finish_quest
            click_point(x, y)
            lvl_up = needle_position(self.config.lvl_up)
            if lvl_up:
                lvl_up_continue = needle_position(self.config.lvl_up_continue)
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
        print("here")
        codzienne_logowanie = needle_position_once(
            self.config.logowanie_codzienne
        )
        if codzienne_logowanie:
            x, y = codzienne_logowanie
            click_point(x, y)
        print("here2")
        karczma_check = needle_position_once(self.config.karczma_check)
        print("Karczma check")
        karczma_position = needle_position_once(self.config.karczma_needle)
        print("Karczma position")
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
        print("Jestem w karczmie")
        energy_left = self.help.energy_left()
        print(f"Energia - {energy_left}")
        print("Przechodzę do klikania npc od questów")
        click_point(
            self.config.karczma_questnpc1["x"],
            self.config.karczma_questnpc1["y"],
        )
        karczma_quest_accept = needle_position_once(
            self.config.karczma_quest_accept
        )
        if not karczma_quest_accept:
            click_point(
                self.config.karczma_questnpc2["x"],
                self.config.karczma_questnpc2["y"],
            )
            karczma_quest_accept = needle_position_once(
                self.config.karczma_quest_accept
            )
            if not karczma_quest_accept:
                click_point(
                    self.config.karczma_questnpc3["x"],
                    self.config.karczma_questnpc3["y"],
                )
        mount = needle_position_once(
            self.config.quest_no_mount, self.config.quest_no_mount_sphere
        )
        if mount:
            print("Brak mounta!")
            self.help.buy_mount()
        best_quest, best_quest_time = self.help.get_quests_info(debug=True)
        print(f"Akceptuję misję nr: {best_quest}")
        print(f"Czas jej wykonania - {best_quest_time} sekund")
        if best_quest == 1:
            click_point(
                self.config.quest1_pos["x"], self.config.quest1_pos["y"]
            )
        elif best_quest == 2:
            click_point(
                self.config.quest2_pos["x"], self.config.quest2_pos["y"]
            )
        else:
            click_point(
                self.config.quest3_pos["x"], self.config.quest3_pos["y"]
            )
        click_point(
            self.config.karczma_quest["x"], self.config.karczma_quest["y"]
        )
        if self.help.full_eq_check():
            return "eq_sell"
        print("Misja zaakceptowana. Przechodzę w tryb uśpienia")
        self.help.mission_sleep(best_quest_time)
        return "quest_check"

    def upgrade(self):
        wallet = self.help.get_gold()
        print(f"Stan golda {wallet}")
        return "exit"

    def eq_sell(self):
        print("Przechodzę do ekwipunku")
        click_point(
            self.config.character_menu["x"], self.config.character_menu["y"]
        )
        print("Zaczynam sprzedawać przedmioty")
        self.help.sell_equipment()
        print("Sprzedałem wszystkie itemy")
        print("Przechodzę do karczmy")
        return "quest_check"

    def energry_status(self):
        energy_left = self.help.energy_left()
        print(f"Pozostała energia - {energy_left}")
        return "exit"
