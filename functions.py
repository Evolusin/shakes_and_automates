from calendar import c
import cv2 as cv
import itertools
from settings import Settings, logger
from analize import (
    click_point_right,
    needle_position,
    click_point,
    needle_position_once,
    move_to,
)
import time
import pyautogui


class Helper:
    def __init__(self) -> None:
        self.config = Settings().settings
        pass

    def buy_mount(self):
        mount = self.config.mount
        logger.info(f"Przechodze do kupywania - {mount}")
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
        logger.info("Mount kupiony!")
        return "do_karczmy"

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
            logger.info("Wykrylem pelen ekwipunek!")
            click_point(
                self.config.full_eq_cancel_pos["x"],
                self.config.full_eq_cancel_pos["y"],
            )
            return True

    def upgrade_stats(self):
        stats_to_upgrade = [
            self.config.strength,
            self.config.agility,
            self.config.inteligence,
            self.config.constitution,
        ]
        upgrades = 0
        # 788,674 72,85,44 #48552C
        still_have_gold = True
        while still_have_gold:
            for stat in itertools.cycle(stats_to_upgrade):
                click_point(stat["x"], stat["y"])
                upgrades = upgrades + 1
                move_to(self.config.safe_pos["x"], self.config.safe_pos["y"])
                r, g, b = pyautogui.pixel(
                    self.config.upgrade_gold_check["x"],
                    self.config.upgrade_gold_check["y"],
                )
                if r != self.config.upgrade_gold_check["r"]:
                    still_have_gold = False
                    break
        logger.info(f"Zrobilem upgrade {upgrades} razy")
        return None
