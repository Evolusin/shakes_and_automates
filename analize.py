import cv2 as cv
import numpy as np
from vision import Vision
from settings import Settings
from windowcapture import get_screenshot

config = Settings()

def login_position():
    login_vision = Vision(config.login_needle)
    screen = get_screenshot(config.monitor)
    points = login_vision.find(screen, debug_mode=True)
    if points:
        print(f"Found at {points}")
