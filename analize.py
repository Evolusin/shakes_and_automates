from enum import Flag
from vision import Vision
from settings import Settings
from windowcapture import get_screenshot, get_screenshot_grab
from PIL import Image
import cv2 as cv
import pytesseract
import os
import pyautogui
import time

config = Settings()

def needle_position(img_needle):
    """
    Anlizes screen and returns img_needle position
    """
    login_vision = Vision(img_needle)
    screen = get_screenshot(config.monitor)
    points = login_vision.find(screen, debug_mode=False)
    if points:
        x,y,w,h = points
        x = x+(w/2)
        y = y+(h/2)
        points = (x,y)
        return points

def needle_position_once(img_needle, sphere = config.monitor):
    """
    Anlizes screen once and returns x,y points position if found
    """
    login_vision = Vision(img_needle)
    screen = get_screenshot(sphere)
    points = login_vision.find(screen, debug_mode=False)
    if points:
        x,y,w,h = points
        x = x+(w/2)
        y = y+(h/2)
        points = (x,y)
        return points
    else:
        return None

def click_point(x,y, debug=False):
    x = int(x)
    y = int(y)
    pyautogui.moveTo(x,y)
    time.sleep(0.5)
    pyautogui.click(x,y,button='left')
    if debug:
        print(f"Klikam na {x} - {y}")
    time.sleep(1)

def refresh_site():
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(3)

def click_point_right(x,y, debug=False):
    x = int(x)
    y = int(y)
    pyautogui.moveTo(x,y)
    time.sleep(0.5)
    pyautogui.click(x,y,button='right')
    if debug:
        print(f"Klikam na {x} - {y}")
    time.sleep(1)


def get_needle_and_text(top,left,bottom,right, debug=False, numbers_only = False):
    """
    Get's needle position and screenshots then returns text
    readed from it
    """
    screen = get_screenshot_grab(top,left,bottom,right)
    if debug:
        # time.sleep(1)
        # cv.imshow('test',screen)
        print("start")
    text = needle_text(screen,debug=debug,numbers_only=numbers_only)
    if text == "" or text == ")\n" or text == "(\n" or len(text)>8:
        screen = get_screenshot_grab(top-5,left-5,bottom+5,right+5)
        text = needle_text(screen,debug=debug,numbers_only=numbers_only)
        if text == "" or text == ")\n" or text == "(\n" or len(text)>8:
            screen = get_screenshot_grab(top-10,left-10,bottom+10,right+10)
            text = needle_text(screen,debug=debug,numbers_only=numbers_only)
            if text == ")\n" or text == "(\n" or len(text)>8:
                text = ""
                return text
    return text

def needle_text(img_needle, debug=False, numbers_only=False):
    """
    Returns text readed from image
    """
    #convert to grayscale image
    gray=cv.cvtColor(img_needle, cv.COLOR_BGR2GRAY)
    #memory usage with image i.e. adding image to memory
    filename = "temp/{}.jpg".format('temporary')
    cv.imwrite(filename, gray)
    if numbers_only:
        text = pytesseract.image_to_string(Image.open(filename),config="digits")
    else:
        text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    if debug:
        print(f"Text from image - {text}")
    return text