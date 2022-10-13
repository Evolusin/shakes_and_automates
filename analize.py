from vision import Vision
from settings import Settings
from windowcapture import get_screenshot
from PIL import Image
import cv2 as cv
import pytesseract
import os
import pyautogui
import time

config = Settings()

def needle_position(img_needle):
    """
    Anlizes screen and returns img_needle position if found
    """
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

def needle_text(img_needle):
    """
    Returns text readed from image
    """
    image = cv.imread(img_needle)
    #convert to grayscale image
    gray=cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #memory usage with image i.e. adding image to memory
    filename = "{}.jpg".format(os.getpid())
    cv.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(f"Text from image {img_needle} - {text}")
    return text