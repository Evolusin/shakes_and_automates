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


class Helper:
    def __init__(self) -> None:
        self.config = Settings()
        pass

    def mission_sleep(self, sleeptime):
        ptime1 = time.perf_counter()
        print(f"Usypiam na {sleeptime} sekund")
        check = False
        while not check:
            check = self.mission_sleep_check(ptime1, sleeptime)
            time.sleep(5)
        return True

    def mission_sleep_check(self, remaining_time, sleeptime):
        ptime2 = time.perf_counter()
        count_time = ptime2 - remaining_time
        if sleeptime > count_time:
            return False
        else:
            return True

    def buy_mount(self):
        mount = self.config.mount
        print(f"Przechodzę do kupywania - {mount}")
        click_point(self.config.stables["x"], self.config.stables["y"])
        # TODO - Check gold before buying
        if mount == "wolf":
            click_point(
                self.config.stables_wolf["x"], self.config.stables_wolf["y"]
            )
        elif mount == "raptor":
            click_point(
                self.config.stables_raptor["x"],
                self.config.stables_raptor["y"],
            )
        elif mount == "dragon":
            click_point(
                self.config.stables_dragon["x"],
                self.config.stables_dragon["y"],
            )
        click_point(
            self.config.stables_rent["x"], self.config.stables_rent["y"]
        )
        print("Mount kupiony!")
        return "do_karczmy"

    def energy_left(self):
        energy_left = get_needle_and_text(
            self.config.energy_top_left["x"],
            self.config.energy_top_left["y"],
            self.config.quest_time_right_down["x"],
            self.config.energy_bottom_right["y"],
            debug=False,
            numbers_only=True,
        )
        if energy_left == "":
            energy_left = get_needle_and_text(
                self.config.energy_top_left["x"] - 3,
                self.config.energy_top_left["y"] - 3,
                self.config.quest_time_right_down["x"] + 3,
                self.config.energy_bottom_right["y"] + 3,
                debug=False,
                numbers_only=True,
            )
            if energy_left == "":
                print("Nie udało mi się odczytać pozostałej energi")
                return None
        if energy_left[0] == ";":
            energy_left = energy_left[1:]
        energy_left = energy_left.replace(";", ".")
        energy_left = energy_left.replace(",", ".")
        energy_left = energy_left.replace(")", "")
        if len(energy_left) > 2:
            energy_left = energy_left[:2]
        return energy_left

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
        if debug:
            print(f"Gold misji po wyczyszczeniu: {questes_gold}")
            print(f"Czas misji po wyczyszczeniu: {questes_time}")
        print(f"Opłacalność misji {questes_ratio}")
        best_quest = min(questes_ratio, key=questes_ratio.get)
        best_quest_time = questes_time[best_quest - 1]
        return best_quest, best_quest_time

    def get_gold(self):
        print("Getting gold")
        wallet = get_needle_and_text(
            self.config.wallet_top_left["x"],
            self.config.wallet_top_left["y"],
            self.config.wallet_bottom_right["x"],
            self.config.wallet_bottom_right["y"],
        )
        wallet = str(wallet)
        wallet = wallet.replace(",", ".")
        wallet = wallet.replace("\n", "")

        return float(wallet)

    def values_from_quests(self):
        q1time = get_needle_and_text(
            self.config.quest_time_top_left["x"],
            self.config.quest_time_top_left["y"],
            self.config.quest_time_right_down["x"],
            self.config.quest_time_right_down["y"],
        )
        if q1time == "":
            q1time = get_needle_and_text(
                self.config.quest_time_top_left["x"] - 5,
                self.config.quest_time_top_left["y"] - 5,
                self.config.quest_time_right_down["x"] + 5,
                self.config.quest_time_right_down["y"] + 5,
            )
            if q1time == "":
                print("Nie mogłem znaleść czasu dla 1 misji. Pomijam quest")
                q1time = "100000"
        q1gold = get_needle_and_text(
            self.config.quest_gold_top_left["x"],
            self.config.quest_gold_top_left["y"],
            self.config.quest_gold_right_down["x"],
            self.config.quest_gold_right_down["y"],
        )
        if q1gold == "":
            q1gold = get_needle_and_text(
                self.config.quest_gold_top_left["x"] - 5,
                self.config.quest_gold_top_left["y"] - 5,
                self.config.quest_gold_right_down["x"] + 5,
                self.config.quest_gold_right_down["y"] + 5,
            )
            if q1gold == "":
                print("Nie mogłem znaleść golda dla 1 misji. Pomijam quest")
                q1gold = "1"
        click_point(self.config.quest2_pos["x"], self.config.quest2_pos["y"])

        q2time = get_needle_and_text(
            self.config.quest_time_top_left["x"],
            self.config.quest_time_top_left["y"],
            self.config.quest_time_right_down["x"],
            self.config.quest_time_right_down["y"],
        )
        if q2time == "":
            q2time = get_needle_and_text(
                self.config.quest_time_top_left["x"] - 5,
                self.config.quest_time_top_left["y"] - 5,
                self.config.quest_time_right_down["x"] + 5,
                self.config.quest_time_right_down["y"] + 5,
            )
            if q2time == "":
                print("Nie mogłem znaleść czasu dla 2 misji. Pomijam quest")
                q2time = "100000"
        q2gold = get_needle_and_text(
            self.config.quest_gold_top_left["x"],
            self.config.quest_gold_top_left["y"],
            self.config.quest_gold_right_down["x"],
            self.config.quest_gold_right_down["y"],
        )
        if q2gold == "":
            q2gold = get_needle_and_text(
                self.config.quest_gold_top_left["x"] - 5,
                self.config.quest_gold_top_left["y"] - 5,
                self.config.quest_gold_right_down["x"] + 5,
                self.config.quest_gold_right_down["y"] + 5,
            )
            if q2gold == "":
                print("Nie mogłem znaleść golda dla 2 misji. Pomijam quest")
                q2gold = "1"
        click_point(self.config.quest3_pos["x"], self.config.quest3_pos["y"])
        q3time = get_needle_and_text(
            self.config.quest_time_top_left["x"],
            self.config.quest_time_top_left["y"],
            self.config.quest_time_right_down["x"],
            self.config.quest_time_right_down["y"],
        )
        if q3time == "":
            q3time = get_needle_and_text(
                self.config.quest_time_top_left["x"] - 5,
                self.config.quest_time_top_left["y"] - 5,
                self.config.quest_time_right_down["x"] + 5,
                self.config.quest_time_right_down["y"] + 5,
            )
            if q3time == "":
                print("Nie mogłem znaleść czasu dla 3 misji. Pomijam quest")
                q3time = "100000"
        q3gold = get_needle_and_text(
            self.config.quest_gold_top_left["x"],
            self.config.quest_gold_top_left["y"],
            self.config.quest_gold_right_down["x"],
            self.config.quest_gold_right_down["y"],
        )
        if q3gold == "":
            q3gold = get_needle_and_text(
                self.config.quest_gold_top_left["x"] - 5,
                self.config.quest_gold_top_left["y"] - 5,
                self.config.quest_gold_right_down["x"] + 5,
                self.config.quest_gold_right_down["y"] + 5,
            )
            if q3gold == "":
                print("Nie mogłem znaleść golda dla 3 misji. Pomijam quest")
                q3gold = "1"
        return q1time, q1gold, q2time, q2gold, q3time, q3gold

    def sell_equipment(self):
        item_list = [
            self.config.item1_pos,
            self.config.item2_pos,
            self.config.item3_pos,
            self.config.item4_pos,
            self.config.item5_pos,
        ]
        item_sell_list = [
            self.config.item1_sell_pos,
            self.config.item2_sell_pos,
            self.config.item3_sell_pos,
            self.config.item4_sell_pos,
            self.config.item5_sell_pos,
        ]
        for key, value in zip(item_list, item_sell_list):
            click_point_right(key["x"], key["y"])
            # clickicking two times to confirm sell
            click_point(value["x"], value["y"])
            click_point(value["x"], value["y"])

    def full_eq_check(self):
        full_eq_check = needle_position_once(self.config.full_eq)
        if full_eq_check:
            print("Wykryłem pełen ekwipunek!")
            click_point(
                self.config.full_eq_cancel_pos["x"],
                self.config.full_eq_cancel_pos["y"],
            )
            return True
