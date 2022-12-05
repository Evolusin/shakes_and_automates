import pyautogui
import os

class Settings:
    def __init__(self) -> None:
        # Determine if it's linux prod or dev Mac
        if os.getenv("SHAKES") == "LINUX":
            self.settings = SettingsLinux()
        else:
            self.settings = SettingsMain()

class SettingsMain:
    def __init__(self):
        self.img_dir = "img/"
        self.width, self.height = pyautogui.size()
        self.monitor = {
            "top": 0,
            "left": 0,
            "width": self.width,
            "height": self.height,
        }
        self.state = "logowanie"
        # wolf / raptor / dragon mount
        self.mount = "wolf"

        # templates
        self.login_needle = self.load("login")
        self.karczma_needle = self.load("karczma")
        self.karczma_check = self.load("karczma_check")
        self.karczma_quest_accept = self.load("karczma_quest_accept")
        self.quest_check = self.load("na_misji")
        self.misja_koniec = self.load("misja_koniec")
        self.lvl_up = self.load("nowy_poziom")
        self.lvl_up_continue = self.load("nowy_poziom_continue")
        self.logowanie_codzienne = self.load("odbierz")
        self.full_eq = self.load("full_eq")
        self.quest_no_mount = self.load("quest_no_mount")
        self.no_eneregy = self.load("no_energy")

        # variables for x/y positions and r - red (from RGB)
        x = "x"
        y = "y"
        r = "r"

        # static positions for mouse click
        # safe pos for mouse
        self.safe_pos = {x: 100, y: 100}
        # middle npc
        self.karczma_questnpc1 = {x: 1005, y: 720}
        # right npc
        self.karczma_questnpc2 = {x: 1422, y: 800}
        # left npc
        self.karczma_questnpc3 = {x: 813, y: 760}
        # mission confirm
        self.karczma_quest = {x: 1156, y: 750}
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

        # upgrade check gold pos and color for empty pocket
        self.upgrade_gold_check = {x: 788, y: 674, r: 255}

    def load(self, template):
        print(f"{self.img_dir}{template}.png")
        return f"{self.img_dir}{template}.png"


class SettingsLinux(SettingsMain):
    def __init__(self):
        super().__init__()
        print("Wczytuje config dla Linuxa")
        # variables for x/y positions and r - red (from RGB)
        x = "x"
        y = "y"
        r = "r"

        # static positions for mouse click
        # middle npc
        self.karczma_questnpc1 = {x: 1005, y: 720}
        # right npc
        self.karczma_questnpc2 = {x: 1422, y: 800}
        # left npc
        self.karczma_questnpc3 = {x: 813, y: 760}
        # mission confirm
        self.karczma_quest = {x: 1156, y: 750}
        # full eq cancel button position
        self.full_eq_cancel_pos = {x: 1243, y: 700} 
        # character menu
        self.character_menu = {x: 170, y: 150}
        # login main screen position
        self.login = {x: 1150, y: 510}
        # stables
        self.stables = {x: 260, y: 525}
        # stables - wolf
        self.stables_wolf = {x: 725, y: 523}
        self.stables_raptor = {x: 1274, y: 763}
        self.stables_dragon = {x: 1521, y: 763}
        # stables - rent button
        self.stables_rent = {x: 1451, y: 923    }

        # items in backpack
        self.item1_pos = {x: 1204, y: 204}
        self.item1_sell_pos = {x: 1204, y: 298}
        self.item2_pos = {x: 1317, y: 204}
        self.item2_sell_pos = {x: 1317, y: 298}
        self.item3_pos = {x: 1431, y: 204}
        self.item3_sell_pos = {x: 1431, y: 298}
        self.item4_pos = {x: 1565, y: 204}
        self.item4_sell_pos = {x: 1565, y: 298}
        self.item5_pos = {x: 1700, y: 204}
        self.item5_sell_pos = {x: 1700, y: 298}

        # upgrade stats positions
        self.strength = {x: 767, y: 693}
        self.agility = {x: 767, y: 774}
        self.inteligence = {x: 767, y: 843}
        self.constitution = {x: 1081, y: 693}
        # upgrade check gold pos and color for empty pocket
        self.upgrade_gold_check = {x: 770, y: 689, r: 255}

    def load(self, template):
        print(f"{self.img_dir}{template}_linux.png")
        return f"{self.img_dir}{template}_linux.png"
