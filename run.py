import cv2 as cv
from settings import Settings, logger
from states import States
import time
import random


config = Settings().settings
states = States()
faze = config.state
quest_done = 0


time.sleep(10)
logger.info("Launched")

while True:

    if faze == "debug":
        logger.info(config.karczma_questnpc1["x"])
        logger.info(config.karczma_questnpc1["y"])

    elif faze == "sleep":
        x = random.randrange(50, 150)
        logger.info(f"Zasypiam na {x} sekund")
        time.sleep(x)
        faze = "quest_check"

    elif faze == "logowanie":
        logger.info(f"Ilosc zrobionych na ten moment questow {quest_done}")
        faze = states.logowanie()

    elif faze == "quest_check":
        faze = states.quest_check()
    
    elif faze == "refresh":
        faze = states.refresh()

    elif faze == "do_karczmy":
        faze = states.do_karczmy()

    elif faze == "karczma":
        quest_done = quest_done + 1
        faze = states.karczma()

    elif faze == "upgrade":
        faze = states.upgrade()

    elif faze == "eq_sell":
        faze = states.eq_sell()

    elif faze == "exiting":
        faze = states.exiting()
        break
