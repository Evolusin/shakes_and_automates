import os
import pyautogui


class Settings:
    def __init__(self):
        self.img_dir = "img/"
        self.width, self.height = pyautogui.size()
        self.monitor = {"top": 0, "left": 0, "width": self.width, "height": self.height}
        self.state = "logowanie"
        self.quest_mode = "gold"
        # for mac it's 1.7778 / Full HD - 1
        # https://www.omnicalculator.com/other/resolution-scale
        self.scale = 1
        # wolf / raptor / dragon
        self.mount = 'wolf'

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
        self.full_eq = f"{self.img_dir}full_eq.png"
        self.character_menu = f"{self.img_dir}character_menu.png"
        self.quest_no_mount = f"{self.img_dir}quest_no_mount.png"
        # variable for x/y positions
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
        self.quest_time_right_down = {x:int(self.width / 1.444),y:int(self.height / 1.574)}
        self.quest_time_top_left = {x:int(self.width / 1.515), y:int(self.height / 1.655)}
        # quest gold expected position and lenght
        self.quest_gold_right_down = {x:970,y:691}
        self.quest_gold_top_left = {x:884,y:651}
        # quests 1/2/3 button position
        self.quest1_pos = {x:922,y:400}
        self.quest2_pos = {x:1097,y:386}
        self.quest3_pos = {x:1397,y:403}
        # full eq cancel button position
        self.full_eq_cancel_pos = {x:1243,y:700}
        # character menu
        self.character_menu = {x:175, y:148}
        # stables 
        self.stables = {x:286, y:521}
        # stables - wolf
        self.stables_wolf = {x:1039, y:763}
        self.stables_raptor = {x:1274, y:763}
        self.stables_dragon = {x:1521, y:763}
        # stables - rent button
        self.stables_rent = {x:1475, y:912}

        # items in backpack
        self.item1_pos = {x:1220, y:165}
        self.item1_sell_pos = {x:1220, y:265}
        self.item2_pos = {x:1343, y:165}
        self.item2_sell_pos = {x:1343, y:265}
        self.item3_pos = {x:1470, y:165}
        self.item3_sell_pos = {x:1470, y:265}
        self.item4_pos = {x:1600, y:165}
        self.item4_sell_pos = {x:1600, y:265}
        self.item5_pos = {x:1730, y:165}
        self.item5_sell_pos = {x:1730, y:265}

        # energy bar in quest hub
        self.energy_top_left = {x:1205,y:918}
        self.energy_bottom_right = {x:1289,y:945}

        # gold in wallet
        self.wallet_top_left = {x:300, y:96}
        self.wallet_bottom_right= {x:399, y:136}

        # sphere positions for screenshots
        self.quest_no_mount_sphere = {"top": 600, "left": 500, "width": 500, "height": 450}
