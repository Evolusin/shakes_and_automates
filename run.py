import cv2 as cv
import numpy as np
from settings import Settings
from analize import login_position

from windowcapture import get_screenshot


config = Settings()
monitor = {"top": 0, "left": 0, "width": 600, "height": 600,}


while True:
    x = login_position()

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break