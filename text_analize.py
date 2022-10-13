# We import the necessary packages
#import the needed packages
import cv2 as cv
import os
import pytesseract
from PIL import Image
from settings import Settings

config = Settings()

image = cv.imread(config.misja_koniec)

#convert to grayscale image
gray=cv.cvtColor(image, cv.COLOR_BGR2GRAY)
	
#memory usage with image i.e. adding image to memory
filename = "{}.jpg".format(os.getpid())
cv.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# DBEUG show the output images
# cv.imshow("Output In Grayscale", gray)
# cv.waitKey(0)
