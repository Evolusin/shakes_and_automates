import os
import pyautogui


class Settings:
    def __init__(self):
        self.img_dir = "img/"
        self.width, self.height = pyautogui.size()
        self.monitor = {"top": 0, "left": 0, "width": self.width, "height": self.height}
        self.state = "logowanie"
        self.quest_mode = "gold"

        # templates
        self.login_needle = f"{self.img_dir}login.png"
        self.karczma_needle = f"{self.img_dir}karczma.png"
        self.karczma_check = f"{self.img_dir}karczma_check.png"
        self.karczma_quest_accept = f"{self.img_dir}karczma_quest_accept.png"
        self.quest_check = f"{self.img_dir}na_misji.png"
        self.misja_koniec = f"{self.img_dir}misja_koniec.png"
        self.lvl_up = f"{self.img_dir}nowy_poziom.png"
        self.lvl_up_continue = f"{self.img_dir}nowy_poziom_continue.png"
        self.logowanie_codzienne = f"{self.img_dir}odbierz.png"

        #variable for x/y
        x = "x"
        y = "y"

        # static positions for mouse click
        # middle npc
        self.karczma_questnpc1 = {x:self.width / 1.91,y:self.height / 1.5}
        # right npc
        self.karczma_questnpc2 = {x:self.width / 1.35,y:self.height / 1.35}
        # left npc
        self.karczma_questnpc3 = {x:self.width / 2.36,y:self.height / 1.42}
        # mission confirm
        self.karczma_quest = {x:self.width / 1.66,y:self.height / 1.44}
        # quest time expected position and lenght
        self.quest_time_w = int(self.width / 1.444)
        self.quest_time_h = int(self.height / 1.574)
        self.quest_time_top_left = {x:int(self.width / 1.515), y:int(self.height / 1.655)}
        # quest gold expected position and lenght
        self.quest_gold_w = 950
        self.quest_gold_h = 687
        self.quest_gold_top_left = {x:885,y:655}
        #quest 2 and 3 button position
        self.quest2_pos = {x:1097,y:386}
        self.quest3_pos = {x:1397,y:403}


