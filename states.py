from calendar import c
import cv2 as cv
from settings import Settings
from analize import (
    click_point_right,
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
        energy = self.energry_status()
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
        # click_point(config.karczma_quest["x"], config.karczma_quest["y"])
        best_quest = self.get_quests_info(debug=True)
        print(f"Akceptuję misję nr: {best_quest}")
        if best_quest == 1:
            click_point(config.quest1_pos["x"], config.quest1_pos["y"])
        elif best_quest == 2:
            click_point(config.quest2_pos["x"], config.quest2_pos["y"])
        else:
            click_point(config.quest3_pos["x"], config.quest3_pos["y"])
        click_point(config.karczma_quest["x"], config.karczma_quest["y"])
        full_eq_check = needle_position_once(config.full_eq)
        if full_eq_check:
            print("Wykryłem pełen ekwipunek!")
            click_point(
                config.full_eq_cancel_pos["x"], config.full_eq_cancel_pos["y"]
            )
            return "eq_sell"
        print("Misja zaakceptowana. Wychodzę z programu")
        return "exit"

    def values_from_quests(self):
        q1time = get_needle_and_text(
            config.quest_time_top_left["x"],
            config.quest_time_top_left["y"],
            config.quest_time_right_down["x"],
            config.quest_time_right_down["y"],
        )
        if q1time == "":
            q1time = get_needle_and_text(
                config.quest_time_top_left["x"] - 5,
                config.quest_time_top_left["y"] + 5,
                config.quest_time_right_down["x"] + 5,
                config.quest_time_right_down["y"] + 5,
            )
            if q1time == "":
                print("Nie mogłem znaleść czasu dla 1 misji. Pomijam quest")
                q1time = "100000"
        q1gold = get_needle_and_text(
            config.quest_gold_top_left["x"],
            config.quest_gold_top_left["y"],
            config.quest_gold_right_down["x"],
            config.quest_gold_right_down["y"],
        )
        if q1gold == "":
            q1gold = get_needle_and_text(
                config.quest_gold_top_left["x"] - 5,
                config.quest_gold_top_left["y"] + 5,
                config.quest_gold_right_down["x"] + 5,
                config.quest_gold_right_down["y"] + 5,
            )
            if q1gold == "":
                print("Nie mogłem znaleść golda dla 1 misji. Pomijam quest")
                q1gold = "0"
        click_point(config.quest2_pos["x"], config.quest2_pos["y"])

        q2time = get_needle_and_text(
            config.quest_time_top_left["x"],
            config.quest_time_top_left["y"],
            config.quest_time_right_down["x"],
            config.quest_time_right_down["y"],
        )
        if q2time == "":
            q2time = get_needle_and_text(
                config.quest_time_top_left["x"] - 5,
                config.quest_time_top_left["y"] + 5,
                config.quest_time_right_down["x"] + 5,
                config.quest_time_right_down["y"] + 5,
            )
            if q2time == "":
                print("Nie mogłem znaleść czasu dla 2 misji. Pomijam quest")
                q2time = "100000"
        q2gold = get_needle_and_text(
            config.quest_gold_top_left["x"],
            config.quest_gold_top_left["y"],
            config.quest_gold_right_down["x"],
            config.quest_gold_right_down["y"],
        )
        if q2gold == "":
            q2gold = get_needle_and_text(
                config.quest_gold_top_left["x"] - 5,
                config.quest_gold_top_left["y"] + 5,
                config.quest_gold_right_down["x"] + 5,
                config.quest_gold_right_down["y"] + 5,
            )
            if q2gold == "":
                print("Nie mogłem znaleść golda dla 2 misji. Pomijam quest")
                q2gold = "0"
        click_point(config.quest3_pos["x"], config.quest3_pos["y"])
        q3time = get_needle_and_text(
            config.quest_time_top_left["x"],
            config.quest_time_top_left["y"],
            config.quest_time_right_down["x"],
            config.quest_time_right_down["y"],
        )
        if q3time == "":
            q3time = get_needle_and_text(
                config.quest_time_top_left["x"] - 5,
                config.quest_time_top_left["y"] + 5,
                config.quest_time_right_down["x"] + 5,
                config.quest_time_right_down["y"] + 5,
            )
            if q3time == "":
                print("Nie mogłem znaleść czasu dla 3 misji. Pomijam quest")
                q3time = "100000"
        q3gold = get_needle_and_text(
            config.quest_gold_top_left["x"],
            config.quest_gold_top_left["y"],
            config.quest_gold_right_down["x"],
            config.quest_gold_right_down["y"],
        )
        if q3gold == "":
            q3gold = get_needle_and_text(
                config.quest_gold_top_left["x"] - 5,
                config.quest_gold_top_left["y"] + 5,
                config.quest_gold_right_down["x"] + 5,
                config.quest_gold_right_down["y"] + 5,
            )
            if q3gold == "":
                print("Nie mogłem znaleść golda dla 3 misji. Pomijam quest")
                q3gold = "0"
        return q1time, q1gold, q2time, q2gold, q3time, q3gold

    def get_quests_info(self, debug=False):
        (
            q1time,
            q1gold,
            q2time,
            q2gold,
            q3time,
            q3gold,
        ) = self.values_from_quests()
        questes_time_str = [q1time, q2time, q3time]
        questes_gold_str = [q1gold, q2gold, q3gold]
        if debug:
            print(f"Gold misji przed wyczyszczeniem: {questes_gold_str}")
            print(f"Czas misji przed wyczyszczeniem: {questes_time_str}")
        questes_time = []
        questes_gold = []
        questes_ratio = {1: None, 2: None, 3: None}

        i = 1
        for obj in questes_time_str:
            value = sum(x * int(t) for x, t in zip([60, 1], obj.split(":")))
            questes_time.append(value)
        for obj in questes_gold_str:
            obj = str(obj)
            value = obj.replace(",", ".")
            value = value.replace("\n", "")
            questes_gold.append(float(value))
        for qtime, gold in zip(questes_time, questes_gold):
            questes_ratio[i] = round(float(qtime / gold), 2)
            i = i + 1
        print(f"Opłacalność misji {questes_ratio}")
        best_quest = min(questes_ratio, key=questes_ratio.get)
        return best_quest

    def eq_sell(self):
        print("Przechodzę do ekwipunku")
        click_point(config.character_menu["x"], config.character_menu["y"])
        print("Zaczynam sprzedawać przedmioty")
        item_list = [
            config.item1_pos,
            config.item2_pos,
            config.item3_pos,
            config.item4_pos,
            config.item5_pos,
        ]
        item_sell_list = [
            config.item1_sell_pos,
            config.item2_sell_pos,
            config.item3_sell_pos,
            config.item4_sell_pos,
            config.item5_sell_pos,
        ]
        for key, value in zip(item_list, item_sell_list):
            click_point_right(key["x"], key["y"])
            # clickicking two times to confirm sell
            click_point(value["x"], value["y"])
            click_point(value["x"], value["y"])

        print("Sprzedałem wszystkie itemy")
        print("Przecohdzę do karczmy")
        return "do_karczmy"

    def energry_status(self):
        energy_left = get_needle_and_text(
            config.energy_top_left["x"],
            config.energy_top_left["y"],
            config.quest_time_right_down["x"],
            config.energy_bottom_right["y"],
            debug=False,
        )
        if energy_left == "":
            energy_left = get_needle_and_text(
                config.energy_top_left["x"] - 3,
                config.energy_top_left["y"] + 3,
                config.quest_time_right_down["x"] + 3,
                config.energy_bottom_right["y"] + 3,
                debug=False,
            )
            if energy_left == "":
                print("Nie udało mi się odczytać pozostałej energi")
                return "exit"
        if energy_left[0] == ";":
            energy_left = energy_left[1:]
        energy_left = energy_left.replace(";", ".")
        energy_left = energy_left.replace(",", ".")
        energy_left = energy_left.replace(")", "")
        print(f"Pozostała energia - {energy_left}")
        return "exit"
