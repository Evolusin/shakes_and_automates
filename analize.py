from vision import Vision
from settings import Settings
from windowcapture import get_screenshot
import pyautogui
import time

config = Settings()

def needle_position(img_needle):
    login_vision = Vision(img_needle)
    screen = get_screenshot(config.monitor)
    points = login_vision.find(screen, debug_mode=True)
    if points:
        x,y,w,h = points
        x = x+(w/2)
        y = y+(h/2)
        points = (x,y)
        return points

def click_point(x,y):
    x = int(x)
    y = int(y)
    pyautogui.moveTo(x,y)
    time.sleep(0.5)
    pyautogui.click(x,y,button='left')
    print(f"Clicked at {x} - {y}")
    time.sleep(2)