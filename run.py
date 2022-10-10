import cv2 as cv
import numpy as np
from settings import Settings
from vision import Vision
from windowcapture import get_screenshot
import time

config = Settings()

test = cv.imshow('test',get_screenshot(config.monitor))
time.sleep(5)
