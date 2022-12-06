from settings import Settings
from analize import (
    needle_position,
    click_point,
    needle_position_once,
    refresh_site,
)
import time
from functions import Helper


class States:
    def __init__(self) -> None:
        self.config = Settings().settings
        self.help = Helper()
        pass

    def s_debug(self):
        """Enters debug mode in infinte loop

        Returns:
            string: debug
        """
        print("Debug mode")
        return "debug"

    def logowanie(self):
        """Checks if user is already logged in the game

        Returns:
            string: next state
        """
        print(self.config.login_needle)
        login_position = needle_position_once(self.config.login_needle)
        if login_position:
            click_point(self.config.login["x"], self.config.login["y"])
            print("Przechodze do quest_check")
            return "quest_check"
        else:
            print("Jestes juz zalogowany. Przechodze do quest_check")
            return "quest_check"

    def quest_check(self):
        """Checks if char is on the mission. If yes then returns sleep state.
        Otherwise returns do_karczmy state

        Returns:
            string: next state
        """
        print("Sprawdzam czy na misji")
        quest_check = needle_position_once(self.config.quest_check)
        finish_quest = needle_position_once(self.config.misja_koniec)
        if quest_check:
            print("Postac jest na misji")
            return "sleep"
        elif finish_quest:
            print("Wykrylem skonczona misje")
            x, y = finish_quest
            click_point(x, y)
            time.sleep(4)
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
            time.sleep(3)
            lvl_up = needle_position(self.config.lvl_up)
            if lvl_up:
                print("Wykrylem level up")
                lvl_up_continue = needle_position(self.config.lvl_up_continue)
                x, y = lvl_up_continue
                click_point(x, y)
            return "do_karczmy"

    def do_karczmy(self):
        """Check's if its already in quest hub. If yes then returns
        karczma state. Otherwise click's quest hub locations

        Returns:
            string: next state
        """
        print("Przechodze do karczmy")
        codzienne_logowanie = needle_position_once(
            self.config.logowanie_codzienne
        )
        if codzienne_logowanie:
            x, y = codzienne_logowanie
            click_point(x, y)
        karczma_check = needle_position_once(self.config.karczma_check)
        karczma_position = needle_position_once(self.config.karczma_needle)
        if karczma_check:
            return "karczma"
        else:
            if karczma_position:
                x, y = karczma_position
                click_point(x, y)
                return "karczma"
            else:
                print("Zbugowalem sie. Odswiezam strone")
                return "refresh"

    def karczma(self):
        """Clickes in order on NPC localistions. If NPC is found then
        accepts quest and returns sleep state

        Returns:
            string: next state
        """
        print("Jestem w karczmie")
        print("Przechodze do klikania npc od questów")
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
        mount = needle_position_once(self.config.quest_no_mount)
        if mount:
            print("Brak mounta!")
            self.help.buy_mount()
        energy_check = needle_position_once(self.config.no_eneregy)
        if energy_check:
            print("No energy left")
            return "upgrade"

        click_point(
            self.config.karczma_quest["x"], self.config.karczma_quest["y"]
        )
        if self.help.full_eq_check():
            return "eq_sell"
        print("Misja zaakceptowana. Przechodze w tryb uspienia")
        return "quest_check"

    def refresh(self):
        refresh_site()
        return "logowanie"

    def upgrade(self):
        print("Upgrade statystyk")
        click_point(
            self.config.character_menu["x"], self.config.character_menu["y"]
        )
        self.help.upgrade_stats()
        return "exiting"

    def exiting(self):
        print("Wylaczam bota")
        return None

    def eq_sell(self):
        print("Przechodze do ekwipunku")
        click_point(
            self.config.character_menu["x"], self.config.character_menu["y"]
        )
        print("Zaczynam sprzedawac przedmioty")
        self.help.sell_equipment()
        print("Sprzedalem wszystkie itemy")
        print("Przechodze do karczmy")
        return "quest_check"
