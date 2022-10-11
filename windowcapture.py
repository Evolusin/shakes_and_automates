import numpy as np
import mss
import cv2 as cv


def get_screenshot(monitor):
    with mss.mss() as sct:
        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        return img


def convert_tuple2dict(tuple):
    left = int(tuple[0])
    top = int(tuple[1])
    width = int(tuple[2])
    height = int(tuple[3])
    created_dict = {"top": top, "left": left, "width": width, "height": height}
    return created_dict

def convert_tuple2dict_position(tuple):
    x = int(tuple[0]) 
    y = int(tuple[1])
    width = int(tuple[2])
    height = int(tuple[3])
    x = x + (width/2)
    y = y + (height/2)
    return x,y

