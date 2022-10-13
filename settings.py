import os
import pyautogui


class Settings:
    def __init__(self):
        self.img_dir = "img/"
        self.width, self.height = pyautogui.size()
        self.monitor = {"top": 0, "left": 0, "width": self.width, "height": self.height}

        # templates
        self.login_needle = f"{self.img_dir}login.png"
        self.karczma_needle = f"{self.img_dir}karczma.png"
        self.karczma_check = f"{self.img_dir}karczma_check.png"
        self.quest_check = f"{self.img_dir}na_misji.png"
        self.misja_koniec = f"{self.img_dir}misja_koniec.png"
        self.lvl_up = f"{self.img_dir}nowy_poziom.png"
        self.lvl_up_continue = f"{self.img_dir}nowy_poziom_continue.png"
        self.logowanie_codzienne = f"{self.img_dir}odbierz.png"

        # static positions for mouse click
        # middle npc
        self.karczma_questnpc1_x = self.width / 1.91
        self.karczma_questnpc1_y = self.height / 1.5
        # right npc
        self.karczma_questnpc2_x = self.width / 1.35
        self.karczma_questnpc2_y = self.height / 1.35
        # left npc
        self.karczma_questnpc3_x = self.width / 2.36
        self.karczma_questnpc3_y = self.height / 1.42
        # mission confirm
        self.karczma_quest_x = self.width / 1.66
        self.karczma_quest_y = self.height / 1.44
        
