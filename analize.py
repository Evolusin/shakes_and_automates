from vision import Vision
from settings import Settings
from windowcapture import get_screenshot, get_screenshot_grab
from PIL import Image
import cv2 as cv
import os
import pyautogui
import time

config = Settings().settings


def needle_position(img_needle):
    """
    Anlizes screen and returns img_needle position
    """
    login_vision = Vision(img_needle)
    screen = get_screenshot(config.monitor)
    points = login_vision.find(screen, debug_mode=False)
    if points:
        x, y, w, h = points
        x = x + (w / 2)
        y = y + (h / 2)
        points = (x, y)
        return points


def needle_position_once(img_needle, sphere=config.monitor):
    """
    Anlizes screen once and returns x,y points position if found
    """
    login_vision = Vision(img_needle)
    screen = get_screenshot(sphere)
    points = login_vision.find(screen, debug_mode=False)
    if points:
        x, y, w, h = points
        x = x + (w / 2)
        y = y + (h / 2)
        points = (x, y)
        return points
    else:
        return None


def click_point(x, y, debug=False):
    x = int(x)
    y = int(y)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y, button="left")
    if debug:
        print(f"Klikam na {x} - {y}")
    time.sleep(1)

def move_to(x,y):
    x = int(x)
    y = int(y)
    pyautogui.moveTo(x, y)
    time.sleep(1)
    
def click_point_right(x, y, debug=False):
    x = int(x)
    y = int(y)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y, button="right")
    if debug:
        print(f"Klikam na {x} - {y}")
    time.sleep(1)
    
def refresh_site():
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(20)
