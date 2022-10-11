import os
import pyautogui

class Settings:
    def __init__(self):
            self.img_dir = 'img/'
            self.width, self.height = pyautogui.size()
            self.monitor = {"top": 0, "left": 0, "width": self.width, "height": self.height}
            self.login_needle = f'{self.img_dir}login.png'
            self.karczma_needle = f'{self.img_dir}karczma.png'

