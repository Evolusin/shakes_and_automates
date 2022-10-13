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
        self.misja_koniec = f"{self.img_dir}misja_koniec.png"
        self.logowanie_codzienne = f"{self.img_dir}odbierz.png"

        # static positions for mouse click
        self.karczma_questnpc1_x = self.width / 1.91
        self.karczma_questnpc1_y = self.height / 1.5
        self.karczma_questnpc2_x = self.width / 1.35
        self.karczma_questnpc2_y = self.height / 1.35
        self.karczma_questnpc3_x = self.width / 1.35
        self.karczma_questnpc3_y = self.height / 1.35
        self.karczma_quest_x = self.width / 1.66
        self.karczma_quest_y = self.height / 1.44
        
