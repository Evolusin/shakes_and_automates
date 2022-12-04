import pyautogui
from stats_upgrade import StatsUpgrade

stats = StatsUpgrade()


class Settings:
    def __init__(self):
        self.img_dir = "img/"
        self.linux = False
        self.width, self.height = pyautogui.size()
        self.monitor = {
            "top": 0,
            "left": 0,
            "width": self.width,
            "height": self.height,
        }
        self.state = "logowanie"
        # wolf / raptor / dragon
        self.mount = "wolf"

        # templates
        if not self.linux:
            self.login_needle = f"{self.img_dir}login.png"
            self.karczma_needle = f"{self.img_dir}karczma.png"
            self.karczma_check = f"{self.img_dir}karczma_check.png"
            self.karczma_quest_accept = (
                f"{self.img_dir}karczma_quest_accept.png"
            )
            self.quest_check = f"{self.img_dir}na_misji.png"
            self.misja_koniec = f"{self.img_dir}misja_koniec.png"
            self.lvl_up = f"{self.img_dir}nowy_poziom.png"
            self.lvl_up_continue = f"{self.img_dir}nowy_poziom_continue.png"
            self.logowanie_codzienne = f"{self.img_dir}odbierz.png"
            self.full_eq = f"{self.img_dir}full_eq.png"
            self.quest_no_mount = f"{self.img_dir}quest_no_mount.png"
            self.no_eneregy = f"{self.img_dir}no_energy.png"

        # variable for x/y positions
        x = "x"
        y = "y"

        # static positions for mouse click
        # middle npc
        self.karczma_questnpc1 = {x: self.width / 1.91, y: self.height / 1.5}
        # right npc
        self.karczma_questnpc2 = {x: self.width / 1.35, y: self.height / 1.35}
        # left npc
        self.karczma_questnpc3 = {x: self.width / 2.36, y: self.height / 1.42}
        # mission confirm
        self.karczma_quest = {x: self.width / 1.66, y: self.height / 1.44}
        # full eq cancel button position
        self.full_eq_cancel_pos = {x: 1243, y: 700}
        # character menu
        self.character_menu = {x: 230, y: 160}
        # login main screen position
        self.login = {x: 1150, y: 510}
        # stables
        self.stables = {x: 323, y: 525}
        # stables - wolf
        self.stables_wolf = {x: 725, y: 523}
        self.stables_raptor = {x: 1274, y: 763}
        self.stables_dragon = {x: 1521, y: 763}
        # stables - rent button
        self.stables_rent = {x: 1451, y: 887}

        # items in backpack
        self.item1_pos = {x: 1204, y: 204}
        self.item1_sell_pos = {x: 1204, y: 298}
        self.item2_pos = {x: 1317, y: 204}
        self.item2_sell_pos = {x: 1317, y: 298}
        self.item3_pos = {x: 1431, y: 204}
        self.item3_sell_pos = {x: 1431, y: 298}
        self.item4_pos = {x: 1565, y: 204}
        self.item4_sell_pos = {x: 1565, y: 298}
        self.item5_pos = {x: 1669, y: 204}
        self.item5_sell_pos = {x: 1669, y: 298}

        # upgrade stats positions
        self.strength = {x: 788, y: 669}
        self.agility = {x: 788, y: 746}
        self.inteligence = {x: 788, y: 809}
        self.constitution = {x: 1081, y: 669}
