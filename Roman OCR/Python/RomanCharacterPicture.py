import ImageOps
import cv2
import numpy as np
from PIL import *
from pytesser import *

from RectangleCoordinates import RectangleCoordinates


class RomanCharacterPicture:
    leftRectangle = RectangleCoordinates(0,0)
    rightRectangle = RectangleCoordinates(0,0)
    webcamImage = 0

    def __init__(self, webcamImage, leftRectangle, rightRectangle):
        self.rightRectangle = rightRectangle
        self.leftRectangle = leftRectangle
        self.webcamImage = webcamImage

    def __init__(self, webcamImage, foundRectangles):
        self.webcamImage = webcamImage
        if foundRectangles[0][0] < foundRectangles[1][0]:
            self.leftRectangle = RectangleCoordinates(foundRectangles[0][0] + foundRectangles[0][2], foundRectangles[0][1])
            self.rightRectangle = RectangleCoordinates(foundRectangles[1][0], foundRectangles[1][1] + foundRectangles[1][3])
        else:
            self.leftRectangle = RectangleCoordinates(foundRectangles[1][0] + foundRectangles[1][2], foundRectangles[1][1])
            self.rightRectangle = RectangleCoordinates(foundRectangles[0][0], foundRectangles[0][1] + foundRectangles[0][3])

    def evaluatePicture(self):
        x1 = self.leftRectangle.getXPos()
        y1 = self.leftRectangle.getYPos()
        x2 = self.rightRectangle.getXPos()
        y2 = self.rightRectangle.getYPos()
        print "x1: " + str(x1) + " x2:" + str(x2) + " y1:" + str(y1) + " y2:" + str(y2)
        if x1 < x2:
            subImg = self.webcamImage[y1:y2, x1:x2]
        else:
            subImg = self.webcamImage[y1:y2, x2:x1]

        #cv2.imshow('test', subImg)

        hsv = cv2.cvtColor(subImg, cv2.COLOR_BGR2HSV)

        # lower mask (0-10)
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 255, 30])
        mask0 = cv2.inRange(hsv, lower_black, upper_black)

        # upper mask (170-180)
        lower_black = np.array([0, 0, 20])
        upper_black = np.array([180, 255, 50])
        mask1 = cv2.inRange(hsv, lower_black, upper_black)

        # Combine Masks
        black_hue_image = cv2.addWeighted(mask0, 1.0, mask1, 1.0, 0.0)
        test = cv2.GaussianBlur(black_hue_image, (9,9), 0)

        #print type(test)
        cv2.imwrite('color_img.jpg', test)
        img = Image.open('color_img.jpg')
        #img = ImageOps.invert(img)
        img.save('test.tiff')
        img.load()
        test = image_to_string(Image.open("test.tiff"))
        counterI = 0
        counterV = 0
        print test
        for c in test:
            if c == "I" or c == "l" or c == "1" or c == "i" or c == "L" or c == "j" or c == "J" or c == "[" or c == "]":
                counterI += 1
            if c == "V" or c == "v" or c == "W" or c == "w":
                counterV += 1

        if "\/" in test:
            counterV += 1

        return counterI + (counterV * 5)

